# OSINT Implementation Guidelines

**Source:** [https://incyber.org/en/article/osint-put-to-the-test-of-ai-exploring-measuring-verifying/](https://incyber.org/en/article/osint-put-to-the-test-of-ai-exploring-measuring-verifying/)

**Last Updated:** 2026-09-30T15:17:39.312703+00:00

## OSINT Best Practices for AI Projects

### Metrics to Track
Per OSINT-AI benchmark (INCYBER 2024):
- **NER Precision/Recall**: Entity extraction accuracy on project metadata
- **Metadata Completeness**: commit hash, licence, slug, tracked files, languages, source lines
- **Hallucination Rate**: False facts in AI-generated summaries
- **Collection Accuracy**: Verified against ground truth

### Implementation Strategy
1. Ensure all 6 metadata fields are populated in `project_facts.json`
2. Run NER (Named Entity Recognition) quarterly on project descriptions
3. Validate slug → GitHub URL → commit hash chain
4. Use `upstream_provenance.json` as ground truth source

### Tools Referenced
- spaCy NER pipeline for entity extraction
- HuggingFace `dslim/bert-base-NER` for token classification
- DISARM framework for disinformation/threat entity taxonomy
- MITRE ATT&CK entity vocabulary for security project OSINT

### Red Flags
- `"commit": ""` = no provenance = OSINT gap
- `"licence": "UNKNOWN"` = legal risk = investigate immediately
- `"tracked_files": 0` = broken git index = run `git restore --staged .`
