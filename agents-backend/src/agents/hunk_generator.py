"""
Agent 3: Hunk Generator (The Surgeon)

H-MABS Phase 3 implementation.

Goal: Rewrite the mainline patch hunks surgically, hunk-by-hunk, to fit the
target repository's structure and naming conventions. Uses `ConsistencyMap`
for symbol translation and `SemanticBlueprint` to preserve fix intent.
Outputs `adapted_code_hunks` and `adapted_test_hunks`.

CURRENT STATUS: Stub implementation.
  - Reads `consistency_map`, `mapped_target_context`, `semantic_blueprint`.
  - Placeholder for the LLM hunk-by-hunk rewrite loop.
  - Output format (Unified Diff or line-replacement commands) is scaffolded
    but not generated.
  - Active blueprint validation (counter-checking generated hunks against
    the blueprint intent) is planned but deferred.

TODO (Phase 3):
  - Iterate over each code hunk and test hunk from `patch_analysis`.
  - LLM prompt: inject mapped_target_context + consistency_map + blueprint.
  - Translate variable/method names using consistency_map.
  - Counter-check generated hunk against semantic_blueprint (intent check).
  - Format output as strict Unified Diff or line-replacement commands.
  - Apply dry-run validation via `apply_hunk_dry_run` before finalizing.
"""

from langchain_core.messages import HumanMessage
from state import AgentState


async def hunk_generator_node(state: AgentState, config) -> dict:
    """
    Agent 3 node function.

    Inputs from state:
      - mapped_target_context:  From Agent 2. Exact target insertion points.
      - consistency_map:        From Agent 2. Symbol rename mapping.
      - semantic_blueprint:     From Agent 1. Fix intent and root cause.
      - patch_analysis:         Raw FileChange list (contains original hunks).
      - validation_attempts:    How many retry iterations have occurred.
      - validation_error_context: Error logs from Agent 4 (on retry only).

    Outputs written to state:
      - adapted_code_hunks:  List of adapted fix patch hunks.
      - adapted_test_hunks:  List of adapted test patch hunks.
    """
    print("Agent 3 (Hunk Generator): Generating adapted patch hunks...")

    consistency_map = state.get("consistency_map", {})
    mapped_target_context = state.get("mapped_target_context", {})
    semantic_blueprint = state.get("semantic_blueprint")
    patch_analysis = state.get("patch_analysis", [])
    validation_attempts = state.get("validation_attempts", 0)
    error_context = state.get("validation_error_context", "")

    if not semantic_blueprint:
        msg = "Agent 3 Error: No semantic_blueprint in state. Cannot generate hunks."
        print(msg)
        return {"messages": [HumanMessage(content=msg)]}

    if validation_attempts > 0:
        print(
            f"Agent 3: Retry attempt #{validation_attempts}. "
            f"Error context from Agent 4:\n  {error_context[:200]}"
        )

    # -----------------------------------------------------------------------
    # TODO (Phase 3): Replace this stub with:
    #   1. Separate patch_analysis hunks into code_hunks vs test_hunks.
    #   2. For each hunk: LLM prompt with mapped_target_context + consistency_map
    #      + semantic_blueprint + (optionally) validation_error_context on retry.
    #   3. Translate symbols using consistency_map.
    #   4. Active blueprint validation: verify generated hunk preserves intent.
    #   5. apply_hunk_dry_run: validate format before finalizing.
    #   6. Format as Unified Diff strings or line-replacement commands.
    # -----------------------------------------------------------------------

    changed_files = [
        (ch.file_path if hasattr(ch, "file_path") else ch.get("file_path", "unknown"))
        for ch in patch_analysis
    ]

    # Stub: yield placeholder hunk placeholders so Agent 4 has inputs
    stub_code_hunks = [
        {
            "file": f,
            "hunk": "[STUB — LLM-generated adapted hunk pending Phase 3]",
        }
        for f in changed_files
    ]
    stub_test_hunks = []  # Will be filled when test hunk segregation is implemented

    print(
        f"Agent 3 (Stub): Generated {len(stub_code_hunks)} placeholder code hunk(s), "
        f"{len(stub_test_hunks)} test hunk(s). Full generation deferred to Phase 3."
    )

    return {
        "messages": [
            HumanMessage(
                content=(
                    f"Agent 3 complete (stub). {len(stub_code_hunks)} code hunk(s) generated. "
                    "Full LLM-based surgical rewrite pending Phase 3."
                )
            )
        ],
        "adapted_code_hunks": stub_code_hunks,
        "adapted_test_hunks": stub_test_hunks,
    }
