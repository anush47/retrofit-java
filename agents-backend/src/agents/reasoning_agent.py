from langchain_core.messages import HumanMessage
from state import AgentState
from utils.patch_analyzer import PatchAnalyzer
from utils.retrieval.ensemble_retriever import EnsembleRetriever
import os

async def reasoning_agent(state: AgentState, config):
    """
    The Architect. Analyzes, plans, and directs the other agents.
    """
    print("Reasoning Agent: Analyzing patch and planning...")
    
    # 1. Patch Analysis
    patch_path = state.get("patch_path")
    if not patch_path or not os.path.exists(patch_path):
        print(f"Error: Patch file not found at {patch_path}")
        return {"messages": [HumanMessage(content="Error: Patch file not found")]}

    try:
        with open(patch_path, "r", encoding="utf-8") as f:
            diff_text = f.read()
        
        analyzer = PatchAnalyzer()
        changes = analyzer.analyze(diff_text)
        
        print(f"\n--- Patch Analysis Results ({len(changes)} files) ---")
        for change in changes:
            print(f"File: {change.file_path} [{change.change_type}]")
        print("---------------------------------------------------\n")
        
        # 2. Retrieval
        target_repo_path = state.get("target_repo_path")
        mainline_repo_path = state.get("mainline_repo_path")
        experiment_mode = state.get("experiment_mode", False)
        backport_commit = state.get("backport_commit")
        original_commit = state.get("original_commit", "HEAD") # Default to HEAD if not provided
        
        if not target_repo_path or not os.path.exists(target_repo_path):
             print(f"Error: Target repo not found at {target_repo_path}")
             return {"messages": [HumanMessage(content="Error: Target repo not found")]}
        
        if not mainline_repo_path or not os.path.exists(mainline_repo_path):
             print(f"Error: Mainline repo not found at {mainline_repo_path}")
             return {"messages": [HumanMessage(content="Error: Mainline repo not found")]}

        retriever = EnsembleRetriever(mainline_repo_path, target_repo_path)
        
        # Handle Experiment Mode
        commit_to_index = "HEAD"
        if experiment_mode and backport_commit:
            print(f"Experiment Mode: Checking out parent of {backport_commit}...")
            try:
                # Checkout parent of backport commit to simulate state before backport
                retriever.target_repo.git.checkout(f"{backport_commit}^")
                commit_to_index = "HEAD" # Now HEAD is the parent
            except Exception as e:
                print(f"Error checking out commit: {e}")
                return {"messages": [HumanMessage(content=f"Error checking out commit: {e}")]}
        
        # Build Index
        retriever.build_index(commit_to_index)
        
        retrieval_results = {}
        
        print("\n--- Retrieval Results ---")
        for change in changes:
            if change.change_type == "MODIFIED":
                # Use find_candidates with original_commit
                candidates = retriever.find_candidates(change.file_path, original_commit)
                
                retrieval_results[change.file_path] = candidates
                
                print(f"Source: {change.file_path}")
                for c in candidates:
                    print(f"  -> {c['file']} (via {c['reason']})")
            else:
                print(f"Skipping retrieval for {change.change_type} file: {change.file_path}")
        print("-------------------------\n")
        
        # Restore Repo if Experiment Mode
        if experiment_mode:
            print("Restoring target repo to main branch...")
            try:
                retriever.target_repo.git.checkout("-") # Checkout previous branch
            except:
                pass

        return {
            "messages": [HumanMessage(content="Patch Analyzed and Candidates Retrieved")],
            "patch_analysis": changes,
            "retrieval_results": retrieval_results
        }
        
    except Exception as e:
        print(f"Error in Reasoning Agent: {e}")
        import traceback
        traceback.print_exc()
        return {"messages": [HumanMessage(content=f"Error: {e}")]}
