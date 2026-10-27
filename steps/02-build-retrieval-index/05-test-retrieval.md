# Test retrieval: inspect the evidence returned

## Prerequisite
index complete; the stored index and upstream artifacts are current.

## Concept
Retrieval quality and answer quality are distinct. Similarity always returns the
closest candidates, even when none supports an answer.

## Procedure
Follow WORKSHOP_MODE.md. Read collected/questions.json. For each question invoke
tools/retrieval.py search <source> "<question>" with .venv Python. Quote shell
arguments safely; do not interpolate untrusted source text into shell code.
The helper embeds the query with the same model/dimensions as the store, computes
cosine scores, and saves ranked results under evaluation/search-<unique-id>.json.
Explain one ranking, the source/version, and what each passage does or does not
support. Scores are similarities, not confidence probabilities.
Write evaluation/review.md with actual evidence, relevance, support, and missing
information for each question. Do not read full sources to secretly supplement
the retrieved evidence during answer generation. For a final RAG demonstration,
answer one question using only returned passages, with chunk/source citations;
abstain if unsupported. Verify citations against returned text. The participant's
existing agent generates this answer; no extra chat-model API is required.
Mark test-retrieval complete only after real searches and review. A correct
abstention on the unsupported question is a successful outcome. Stop.

## Output
evaluation/search-*.json; evaluation/review.md with a cited answer demonstration.

## Participant checkpoint
Did retrieval find useful evidence? Did the answer stay within that evidence?
Could outdated but similar content have caused an incorrect answer?
