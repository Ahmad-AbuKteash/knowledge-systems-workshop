# Validate: check prepared knowledge

## Prerequisite
enrich complete.

## Concept
Validate the prepared information before retrieval indexing. Formatting checks
and factual review answer different questions; perform both.

## Procedure
Follow WORKSHOP_MODE.md. Check unique document IDs, correct source_id, valid
source paths/hashes, nonempty text, metadata fields, and justified exclusions.
Trace samples back to original files: numbers, conditions, dates, tables, and
version conflicts. Check redaction only where the source exercise requires it.
For each known policy relationship, verify the referenced document exists.
Do not silently repair upstream content in this step. Report where a fix belongs.
Write knowledge/validation.json with `passed` (true only if all required checks
pass), `documents_sha256` (hash of knowledge/documents.json), and checks with
actual results and limitations. The API helper uses this hash to detect changes.
Mark progress complete or failed accordingly. Stop before chunking.

## Output
knowledge/validation.json; a human-readable review report.

## Participant checkpoint
Show evidence for the pass/fail decision. Has the participant checked at least
one original against prepared knowledge? Any unresolved failure blocks Stage 2.
