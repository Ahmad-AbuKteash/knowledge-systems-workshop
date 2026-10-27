# Clean: remove noise while preserving evidence

## Prerequisite
extract complete; extracted records and originals remain traceable.

## Concept
Cleaning removes irrelevant material, not inconvenient facts or historical policy.

## Procedure
Follow WORKSHOP_MODE.md. Inspect the extracted documents and explain proposed
rules. Remove clear navigation, repeated headers/footers, and encoding artifacts.
Do not delete substantive warnings, exceptions, historical versions, or numbers.
For exact duplicates, retain one canonical eligible record and record exclusions
with original IDs, canonical ID, and reason in cleaned/exclusions.json.
If synthetic personal contact details are present, redact them and verify against
the planted values; do not claim that a generic regex guarantees privacy.
Write cleaned/documents.json and Markdown copies, retaining IDs and source hashes.
Show at least two before/after examples, or explain honestly that no cleaning
was needed. Record rules and check results. Mark progress and stop.

## Output
cleaned/documents.json; cleaned/exclusions.json; readable copies and change report.

## Participant checkpoint
Did anything meaningful disappear? Do different policy versions still exist?
Can every exclusion be justified and reversed using untouched inputs?
