"""
Agent 1: Context & Intent Analyzer (The Strategist)

H-MABS Phase 2 implementation.

Goal: Replace the need for a Vulnerability Knowledge Base (VKB) by extracting
the "Why" and "How" directly from the mainline patch via on-the-fly semantic
analysis. Produces a `SemanticBlueprint` stored in `AgentState`.

CURRENT STATUS: Stub implementation.
  - Reads `patch_diff` and `patch_analysis` from state.
  - Placeholder for the LLM-based blueprint extraction.
  - Self-reflection loop (verifying blueprint against pre-patch AST) is
    scaffolded but not yet implemented.

TODO (Phase 2):
  - Integrate Tree-sitter AST pulls of pre-patch mainline methods.
  - LLM call to produce SemanticBlueprint (root_cause, fix_logic, dependent_apis).
  - Self-reflection verification prompt to reject hallucinated blueprints.
"""

from langchain_core.messages import HumanMessage
from state import AgentState


async def context_analyzer_node(state: AgentState, config) -> dict:
    """
    Agent 1 node function.

    Inputs from state:
      - patch_diff:          Raw unified diff of the mainline patch.
      - patch_analysis:      Parsed list of FileChange objects.
      - mainline_repo_path:  Path to the mainline (newer) repository.
      - original_commit:     Commit hash in the mainline repo for AST pulls.

    Outputs written to state:
      - semantic_blueprint:  SemanticBlueprint dict (root_cause, fix_logic, dependent_apis).
    """
    print("Agent 1 (Context Analyzer): Analyzing mainline patch intent...")

    patch_diff = state.get("patch_diff", "")
    patch_analysis = state.get("patch_analysis", [])

    if not patch_diff:
        msg = "Agent 1 Error: No patch_diff found in state. Phase 0 may not have run."
        print(msg)
        return {"messages": [HumanMessage(content=msg)]}

    # -----------------------------------------------------------------------
    # TODO (Phase 2): Replace this stub with:
    #   1. Pull pre-patch function bodies from mainline via Tree-sitter.
    #   2. LLM analysis of the unified diff to extract SemanticBlueprint.
    #   3. Self-reflection loop: apply blueprint backward against pre-patch
    #      mainline code to verify correctness.
    # -----------------------------------------------------------------------

    # Stub: derive minimal blueprint from patch metadata so downstream agents
    # have something to work with during Phase 1 integration testing.
    changed_files = [
        (ch.file_path if hasattr(ch, "file_path") else ch.get("file_path", "unknown"))
        for ch in patch_analysis
    ]

    stub_blueprint = {
        "root_cause_hypothesis": (
            f"[STUB] Patch modifies {len(changed_files)} file(s): "
            + ", ".join(changed_files)
        ),
        "fix_logic": "[STUB] Exact fix logic will be extracted by LLM in Phase 2.",
        "dependent_apis": [],  # Will be populated by AST analysis in Phase 2
    }

    print(f"Agent 1 (Stub): Generated semantic blueprint for {len(changed_files)} files.")
    print(f"  root_cause: {stub_blueprint['root_cause_hypothesis']}")

    return {
        "messages": [
            HumanMessage(
                content=(
                    f"Agent 1 complete (stub). Blueprint covers {len(changed_files)} changed file(s). "
                    "Full LLM-based intent extraction pending Phase 2."
                )
            )
        ],
        "semantic_blueprint": stub_blueprint,
    }
