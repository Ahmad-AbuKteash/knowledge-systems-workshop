# Retrieval review: source-05

Index: `workspace/source-05/index/knowledge.sqlite3` (11 chunks, text-embedding-3-small, 512 dimensions, exact cosine, top_k 5).
Searches: 5 real queries embedded by OpenAI (query tokens: 22, 30, 27, 23, 12). The q02 query was first interrupted by an `APIConnectionError`; it was re-run once by participant request and only q02–q05 were sent again.

Scores are cosine similarities between query and passage vectors. They are not confidence probabilities: the unsupported pricing question (q05) scored 0.62 at rank 1, higher than the best passage for q02 (0.59).

Evidence below comes only from the returned passages and their carried metadata.

## source-05-q01 — standard key read-order limit (current policy)

Search file: `evaluation/search-4ee6fb50da0a.json`

| Rank | Score | Chunk | Version / status | Relevance | Support |
|---|---|---|---|---|---|
| 1 | 0.7257 | `source-05-current-policy:312-607:2c3670a0` (Limits and eligibility) | 2026.2 current | high | Supports: table row `Read orders \| 120 \| 300` under `Standard key / minute`, plus "Limits are per API key and operation". |
| 2 | 0.6736 | `source-05-current-policy:450-815:c367e14d` (Rule and exception) | 2026.2 current | high | Same table; adds the sandbox exception. |
| 3 | 0.6612 | `source-05-current-policy:294-421:d2f2ebc5` (Applicability) | 2026.2 current | medium | Scope only, no number. |
| 4 | 0.6439 | `source-05-previous-policy:454-667:43404dbd` (Previous terms) | 2025.1 historical | misleading | Contains the superseded value 60. |
| 5 | 0.6417 | `source-05-previous-policy:0-452:3a21c828` | 2025.1 historical | low | States it was superseded on 2026-09-01. |

Assessment: answerable (expected). The correct value (120) is at rank 1. Risk: the outdated value 60 appears at rank 4 with a close score; `metadata.status` must be used to reject it.
Missing information: none.

## source-05-q02 — backoff calculation and Retry-After

Search file: `evaluation/search-14738d0dd7c1.json`

| Rank | Score | Chunk | Version / status | Relevance | Support |
|---|---|---|---|---|---|
| 1 | 0.5909 | `source-05-current-policy:843-1554:9302f889` (Idempotency) | 2026.2 current | high | Supports: its overlap paragraph "Backoff delay in seconds = min(2^attempt, 32), with attempt starting at 0. If Retry-After is present, wait at least its stated duration instead." |
| 2 | 0.5092 | `source-05-current-policy:632-987:72a76c8a` (Calculation or timing) | 2026.2 current | high | Same backoff sentence in its own section; adds HTTP 429 context. |
| 3–5 | 0.29–0.27 | previous-policy limits; current limits table | mixed | low | No retry information. |

Assessment: answerable (expected). Note: rank 1 is labeled "Idempotency", but the supporting text comes from its overlap with "Calculation or timing"; a citation should name the section where the sentence originates.
Missing information: none for the formula; the passages do not define a maximum number of attempts.

## source-05-q03 — export jobs during the 2026-10-30 maintenance window

Search file: `evaluation/search-851a0cf2b7e1.json`

| Rank | Score | Chunk | Version / status | Relevance | Support |
|---|---|---|---|---|---|
| 1 | 0.6965 | `source-05-operational-notice:0-411:36535ad7` (Maintenance window notice) | 1.0 supplemental | high | Supports: "Effective 2026-10-30 only, from 01:00 to 02:00 UTC. New export jobs will return HTTP 503. Existing exports remain downloadable." and "Retry exports after 02:00 UTC". |
| 2–5 | 0.36–0.30 | current/previous policy passages | mixed | low | Mention the notice or retries generally; no window details. |

Assessment: answerable (expected), with a clear score gap (0.70 vs 0.36).
Limitation: the notice text is a manual transcript of an image (`participant_verified: false`); verify it against `sources/source-05/operational-notice.png` before relying on it.

## source-05-q04 — sandbox limit before 2026-09-01 and now

Search file: `evaluation/search-64ca215645bc.json`

| Rank | Score | Chunk | Version / status | Relevance | Support |
|---|---|---|---|---|---|
| 1 | 0.6743 | `source-05-previous-policy:473-800:a8367def` (Applicability) | 2025.1 historical | high (old value) | "Sandbox keys were limited to 5 requests per minute." and "rules in force before 2026-09-01". |
| 2 | 0.6528 | `source-05-previous-policy:454-667:43404dbd` (Previous terms) | 2025.1 historical | high (old value) | Same old limit. |
| 3 | 0.6101 | `source-05-current-policy:632-987:72a76c8a` (Calculation or timing, overlap from Rule and exception) | 2026.2 current | high (current value) | "sandbox keys may make only 10 requests per minute for any operation, regardless of plan." |
| 4 | 0.5989 | `source-05-current-policy:312-607:2c3670a0` | 2026.2 current | medium | General limits table (no sandbox row). |
| 5 | 0.5672 | `source-05-current-policy:450-815:c367e14d` (Rule and exception) | 2026.2 current | high | Table plus the sandbox exception. |

Assessment: answerable (expected). The two top passages are historical: a system using only rank 1 would report the outdated limit (5) as current. Version metadata (`status`, `effective_date`) is what separates the answers.

## source-05-q05 — monthly price of a partner API key (unsupported)

Search file: `evaluation/search-2db2fa83d1b8.json`

| Rank | Score | Chunk | Version / status | Relevance | Support |
|---|---|---|---|---|---|
| 1 | 0.6212 | `source-05-current-policy:312-607:2c3670a0` | 2026.2 current | related topic | Mentions "Partner key / minute" limits; no price. |
| 2–5 | 0.54–0.43 | applicability, preambles, table | mixed | related topic | No price, cost, or billing information. |

Assessment: not answerable (expected). Similar-sounding passages were returned with moderately high scores, but none supports a price. Correct outcome: abstain.

## Cited answer demonstration (source-05-q04)

Answer generated in the participant's agent session from the returned passages only:

Before 2026-09-01, sandbox keys were limited to 5 requests per minute [1][3]. Under the current policy (version 2026.2), sandbox keys may make only 10 requests per minute for any operation, regardless of plan, and excess traffic returns HTTP 429 [2].

1. `source-05-previous-policy:454-667:43404dbd` — `sources/source-05/previous-policy.html`, version 2025.1 (historical): "Sandbox keys were limited to 5 requests per minute."
2. `source-05-current-policy:632-987:72a76c8a` — `sources/source-05/current-policy.pdf`, version 2026.2 (current): "Exception: sandbox keys may make only 10 requests per minute for any operation, regardless of plan. Excess traffic returns HTTP 429."
3. `source-05-previous-policy:473-800:a8367def` — `sources/source-05/previous-policy.html`, version 2025.1 (historical): "This archived document records rules in force before 2026-09-01. It does not govern transactions after that date."

Citation check: each quote is verified verbatim against the returned chunk text by `scripts/test_retrieval.py finalize` (see `evaluation/answer-citations.json`).

Abstention demonstration (source-05-q05): the returned passages contain no pricing information, so the answer is "The retrieved sources do not state a price for a partner API key."

## Overall

- Useful evidence was found at rank 1 or 2 for every answerable question.
- Outdated but similar content ranked high for q01 (rank 4) and q04 (ranks 1–2); answers must check `metadata.status` and `effective_date`.
- The unsupported question returned related but non-supporting passages; abstaining was correct.
- Open item: participant verification of the operational-notice transcript.
