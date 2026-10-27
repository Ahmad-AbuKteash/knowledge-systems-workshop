# Carry metadata: preserve source context in every chunk

## Prerequisite
chunk complete; validated knowledge unchanged.

## Concept
Document metadata is inherited by chunks. We do not invent a second metadata set.

## Procedure
Follow WORKSHOP_MODE.md. Join chunks to knowledge records by document_id. Preserve
chunk_id, source_id, text, section, start, and end. Add source_file and a copy of
the document metadata object. Preserve nulls; do not infer missing values.
Write chunks/records.json as a JSON list. Validate every chunk belongs to exactly
one known document, source_id matches the assigned source, offsets/text match,
metadata equals its document metadata, and chunk IDs are unique.
Show one document-to-chunk mapping. Update progress and stop before API calls.

## Output
chunks/records.json, ready for embedding with traceable sources.

## Participant checkpoint
Can a retrieved chunk identify its original document and relevant version?
Does it retain scope information without pretending metadata enforces access?
