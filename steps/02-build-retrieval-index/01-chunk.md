# Chunk: define retrievable passages

## Prerequisite
validate complete and passed; knowledge hash matches validation.json.

## Concept
Chunks are retrieval units. Keep enough context for meaning without dragging in
unrelated sections. Small documents can remain one chunk.

## Procedure
Follow WORKSHOP_MODE.md. Read max_chunk_characters from workshop.json. Split by
headings/paragraphs where possible, with a hard cap of 2000 Unicode characters.
If a section is too long, split at sentence boundaries; use a hard split only
as a documented fallback. Small overlap (up to 200 characters) may preserve
continuity. Ensure the loop always advances. Character counts are not tokens.
Create chunks/chunks.json as a list with chunk_id, document_id, source_id, section,
start, end, text. Offsets are zero-based Python character offsets into the exact
knowledge record text; end is exclusive. text must equal document.text[start:end].
Use deterministic unique IDs including document identity and offsets/content hash.
Check nonempty chunks, coverage of substantive text, offsets, and size limits.
Do not embed or attach document metadata yet. Explain two chunk boundaries and
record progress. Do not alter prepared knowledge to fit the chunker.

## Output
chunks/chunks.json; chunking report and repeatable participant script.

## Participant checkpoint
Does a chunk preserve definitions and exceptions needed to interpret it?
Are chunk boundaries and overlap visible and justified?
