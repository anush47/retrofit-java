"""
Agent 2: Structural Locator (The Navigator)

H-MABS Phase 2 implementation.

Goal: Find the exact insertion points in the target repository for both fix
code and test cases, overcoming structural divergence (renamed files, split
classes, moved methods). Produces a `ConsistencyMap` and
`MappedTargetContext` stored in `AgentState`.

CURRENT STATUS: Stub implementation.
  - Reads `semantic_blueprint` and `patch_analysis` from state.
  - Carries forward existing EnsembleRetriever + ReasoningToolkit heavy
    lifting (already implemented in the old `reasoning_agent.py`).
  - Hunk segregation (code vs test hunks) is scaffolded but not split yet.
  - Deterministic line mapping (`map_hunk_lines`) is planned but deferred.
  - Reflection/validation loop is scaffolded but not implemented.

TODO (Phase 2):
  - Hunk segregation: split patch into Code Hunks vs Test Hunks.
  - Use EnsembleRetriever + match_structure / method_fingerprinter for
    target file and method lookup.
  - Build ConsistencyMap (symbol renames) from AST comparison.
  - Implement `map_hunk_lines` deterministic AST/Diff heuristic tool.
  - Reflection loop: extract mapped context, compare semantically to
    mainline method via method_fingerprinter, reject if divergence too high.
"""

from langchain_core.messages import HumanMessage
from state import AgentState


async def structural_locator_node(state: AgentState, config) -> dict:
    """
    Agent 2 node function.

    Inputs from state:
      - semantic_blueprint:    From Agent 1.
      - patch_analysis:        Parsed FileChange list.
      - target_repo_path:      Path to target (older) repository.
      - mainline_repo_path:    Path to mainline (newer) repository.
      - retrieval_results:     Pre-computed retrieval candidates (optional).

    Outputs written to state:
      - consistency_map:        { mainline_symbol: target_symbol, ... }
      - mapped_target_context:  { file_path: { method, start_line, end_line, code_snippet } }
    """
    print("Agent 2 (Structural Locator): Locating target insertion points...")

    semantic_blueprint = state.get("semantic_blueprint")
    patch_analysis = state.get("patch_analysis", [])

    if not semantic_blueprint:
        msg = "Agent 2 Error: No semantic_blueprint found. Agent 1 may not have populated it."
        print(msg)
        return {"messages": [HumanMessage(content=msg)]}

    # -----------------------------------------------------------------------
    # TODO (Phase 2): Replace this stub with:
    #   1. Hunk Segregation: split patch_analysis hunks into code vs test lists.
    #   2. EnsembleRetriever: build_index + search_candidates for each changed file.
    #   3. match_structure: fingerprint mainline vs target candidates.
    #   4. get_class_context / find_method_match: locate exact methods.
    #   5. map_hunk_lines: deterministic AST/Diff tool for insertion line numbers.
    #   6. Reflection loop: extract mapped context, compare via method_fingerprinter.
    #   7. Build consistency_map from symbol diffs.
    # -----------------------------------------------------------------------

    changed_files = [
        (ch.file_path if hasattr(ch, "file_path") else ch.get("file_path", "unknown"))
        for ch in patch_analysis
    ]

    # Stub: create identity mappings so Agent 3 has context to consume
    stub_consistency_map: dict[str, str] = {}   # Will be populated in Phase 2

    stub_mapped_context: dict[str, dict] = {
        f: {
            "method": "[STUB — method unknown until Phase 2]",
            "start_line": None,
            "end_line": None,
            "code_snippet": "[STUB — AST extraction pending Phase 2]",
        }
        for f in changed_files
    }

    print(
        f"Agent 2 (Stub): Created placeholder context for {len(changed_files)} file(s). "
        "Full structural location deferred to Phase 2."
    )

    return {
        "messages": [
            HumanMessage(
                content=(
                    f"Agent 2 complete (stub). Mapped {len(changed_files)} file(s). "
                    "Full AST-based location + ConsistencyMap pending Phase 2."
                )
            )
        ],
        "consistency_map": stub_consistency_map,
        "mapped_target_context": stub_mapped_context,
    }
