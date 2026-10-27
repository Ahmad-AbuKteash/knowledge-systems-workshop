# Embed: create numerical representations

## Prerequisite
carry-metadata complete; prepared knowledge passed validation; API key configured.

## Concept
An embedding model maps text to vectors. Similarity can identify related content
but does not establish factual correctness or policy authority.

## Procedure
Follow WORKSHOP_MODE.md. Read workshop.json: text-embedding-3-small, 512 dimensions.
Explain that chunk text will be sent to OpenAI using the trainer-provided key and
that API usage incurs charges. Do not read or print .env; the helper loads it.
Invoke tools/retrieval.py embed <source> with the project's .venv Python. This
validates records, batches requests, records actual API token usage, and writes
embeddings/embeddings.json only after successful responses. No fake fallback.
On failure, explain the error and stop. Some completed requests may still have
been billed even when output was not saved. Avoid repeated automatic retries.
Inspect record count, vector dimensions, model identity, and a SHORT vector sample.
Explain that the numbers are learned features, not readable categories.
Update progress after checks pass. Do not build the index yet.

## Output
embeddings/embeddings.json, including input hash, model, dimensions, and real usage.

## Participant checkpoint
Does each chunk have one vector? Are all vector lengths equal? Did the API actually
run? Never treat offline test fixtures as real embeddings.

Reference: https://developers.openai.com/api/reference/python/resources/embeddings/methods/create
