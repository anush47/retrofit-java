# Transition Summary

- Source: phase_outputs
- Valid backport signal: True
- Reason: Valid: Observed fail-to-pass and/or newly passing relevant tests with no regressions.
- fail->pass (4): ['org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testDenseVector {p0=false}', 'org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testDenseVector {p0=true}', 'org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testSparseVector {p0=false}', 'org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testSparseVector {p0=true}']
- newly passing (0): []
- pass->fail (0): []

## Touched Test States
- Touched tests (from patch): ['org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests']
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testDenseVector {p0=false}: baseline=failed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testDenseVector {p0=true}: baseline=failed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testFieldHasValue {p0=false}: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testFieldHasValue {p0=true}: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testFieldHasValueWithEmptyFieldInfos {p0=false}: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testFieldHasValueWithEmptyFieldInfos {p0=true}: baseline=passed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testSparseVector {p0=false}: baseline=failed, patched=passed
  - org.elasticsearch.xpack.inference.highlight.SemanticTextHighlighterTests#testSparseVector {p0=true}: baseline=failed, patched=passed
