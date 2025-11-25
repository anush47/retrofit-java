import asyncio
import sys
import os
from graph import app

# Add src to path if needed
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

async def main():
    # sse_url = os.getenv("MCP_SERVER_URL", "http://localhost:8080/mcp/sse")
    # print(f"Connecting to Analysis Engine at {sse_url}...")


    try:
        print("Running Orchestrator Graph...")
        
        # Get patch file path from user
        patch_path = input("Enter the absolute path to the patch file: ").strip()
        
        # Get target repo path
        target_repo_path = input("Enter the absolute path to the target repo: ").strip()
        
        # Get mainline repo path
        mainline_repo_path = input("Enter the absolute path to the mainline repo: ").strip()
        
        # Experiment mode
        experiment_input = input("Is this an experiment? (y/n): ").strip().lower()
        experiment_mode = experiment_input == 'y'
        
        backport_commit = ""
        original_commit = "HEAD"
        if experiment_mode:
            backport_commit = input("Enter the backport commit hash: ").strip()
            original_commit = input("Enter the original commit hash (from mainline): ").strip()
        
        inputs = {
            "messages": ["Start"],
            "patch_path": patch_path,
            "target_repo_path": target_repo_path,
            "mainline_repo_path": mainline_repo_path,
            "experiment_mode": experiment_mode,
            "backport_commit": backport_commit,
            "original_commit": original_commit
        }
        
        async for output in app.astream(inputs):
            for key, value in output.items():
                print(f"Output from {key}:")
                # Pretty print messages
                if "messages" in value:
                    for msg in value["messages"]:
                        print(f"  {msg.content}")
                print("----")
    except Exception as e:
        print(f"Error running Orchestrator: {e}")

if __name__ == "__main__":
    asyncio.run(main())
