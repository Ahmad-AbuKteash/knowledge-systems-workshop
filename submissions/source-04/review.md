# source-04 retrieval review

Agent-reviewed real retrieval tests; participant inspection remains separate. All answers below were generated solely from each question’s saved returned passages. No full originals or cross-source notes were consulted to supplement answers. Queries used text-embedding-3-small at 512 dimensions; actual query token usage: 19, 30, 15 (64 total). No extra chat-model API call. Configured top_k=5, but this corpus contains only 3 passages, so each search returns all 3. Scores are cosine similarities, not confidence probabilities.

## Question 1

On an overseas work trip, is the food allowance for each meal or for the entire day?

Saved evidence: search-2294457211ca.json

| Rank | Chunk | Version | Effective | Cosine | Relevance and support |
| --- | --- | --- | --- | --- | --- |
| 1 | source-04/operational-notice.png:0-626 | 1.0 | 2026-09-01 | 0.54643894 | Supports USD 85 combined daily cap, not per meal; exception does not increase cap. |
| 2 | source-04/previous-policy.html:0-590 | 2025.1 | 2025-01-01 | 0.47115785 | Historical 2025.1; does not govern transactions after 2026-09-01. |
| 3 | source-04/current-policy.pdf:0-1143 | 2026.2 | 2026-09-01 | 0.45724204 | Supports current table, signed-declaration receipt exception and exclusions. |

Planned paraphrase target: source-04/operational-notice.png:0-626. Actual result: rank 1, cosine 0.5464389387012049. Target found. Different wording matched the intended meaning. This is a single planned test, not a measured improvement over a baseline.

Retrieved evidence:

> Effective 2026-09-01. Finance Operations confirms that the international USD 85 meal cap in current-policy.pdf covers all eligible meals combined in one calendar day. It is not a per-meal cap. The USD 20 lost-receipt exception does not increase the daily cap.

Answer: Effective 2026-09-01, the international USD 85 cap covers all eligible meals combined in one calendar day, not each meal. The USD 20 lost-receipt exception does not add to that cap. [`source-04/operational-notice.png:0-626` — `sources/source-04/operational-notice.png`, version 1.0, effective 2026-09-01]

Citation/claim check: amount USD 85, combined-calendar-day unit, per-meal negative, effective date and no-increase condition all appear in the quoted returned notice. Notice is supplemental, not a replacement for the full policy.
## Question 2

For travel on 2026-10-10, what is the international daily meal cap, and what can I do if I lose a receipt?

Saved evidence: search-231421762f1d.json

| Rank | Chunk | Version | Effective | Cosine | Relevance and support |
| --- | --- | --- | --- | --- | --- |
| 1 | source-04/previous-policy.html:0-590 | 2025.1 | 2025-01-01 | 0.59033473 | Historical 2025.1; does not govern transactions after 2026-09-01. |
| 2 | source-04/operational-notice.png:0-626 | 1.0 | 2026-09-01 | 0.56180222 | Supports USD 85 combined daily cap, not per meal; exception does not increase cap. |
| 3 | source-04/current-policy.pdf:0-1143 | 2026.2 | 2026-09-01 | 0.52307651 | Supports current table, signed-declaration receipt exception and exclusions. |

Retrieved excerpts:

> Version: 2026.2. Effective: 2026-09-01. Supersedes previous-policy.html.
> | Meals | USD 45 | USD 85 |
> Meals require itemized receipts. Exception: a lost receipt may be replaced by a signed declaration for one meal costing no more than USD 20 per trip. Alcohol is excluded in all cases.

The table headers in the returned policy are Category, Domestic / day, International / day.

Answer: For 2026-10-10 travel, the international meal cap is USD 85 per day. Itemized receipts are required, but a signed declaration can replace a lost receipt for one meal costing no more than USD 20 per trip. Alcohol is excluded. [`source-04/current-policy.pdf:0-1143` — `sources/source-04/current-policy.pdf`, version 2026.2, effective 2026-09-01] The cap covers all eligible meals combined in one calendar day; the receipt exception does not increase it. [`source-04/operational-notice.png:0-626` — `sources/source-04/operational-notice.png`, version 1.0, effective 2026-09-01] The historical USD 60 rule does not apply after 2026-09-01. [`source-04/previous-policy.html:0-590` — `sources/source-04/previous-policy.html`, version 2025.1, effective 2025-01-01]

Claim/citation mapping: USD 85 and daily/international labels → current policy table; signed declaration, one meal, USD 20, per trip and alcohol exclusion → current policy Rule and exception; applicable 2026-10-10 → current effective date plus historical supersession; combined daily cap and no increase → notice main paragraph; exclusion of USD 60 → historical applicability. All cited IDs exist in this question’s results and quotations match returned text.

Observed ranking limitation: the inapplicable historical policy ranked first (0.5903347295608331), above notice and current policy. Retrieval succeeded in returning useful evidence, but rank 1 alone would be unsafe for applicability. The answer checks dates/scope instead of using the most similar amount.
## Question 3

What mileage reimbursement rate per kilometer applies when I drive my personal car?

Saved evidence: search-82e7f9d6c5ec.json

| Rank | Chunk | Version | Effective | Cosine | Relevance and support |
| --- | --- | --- | --- | --- | --- |
| 1 | source-04/current-policy.pdf:0-1143 | 2026.2 | 2026-09-01 | 0.36670541 | Daily ground-transport caps, no per-kilometer rate. |
| 2 | source-04/previous-policy.html:0-590 | 2025.1 | 2025-01-01 | 0.32775601 | Historical meals/hotel terms, no mileage rate. |
| 3 | source-04/operational-notice.png:0-626 | 1.0 | 2026-09-01 | 0.27873657 | Meal clarification only; no mileage rate. |

Returned candidate evidence: current-policy.pdf gives Ground transport USD 35 domestic / day and USD 55 international / day; previous-policy.html discusses historical meals/hotels; operational-notice.png discusses meals. None contains a personal-car distance rate.

Answer: Insufficient evidence. The retrieved passages do not state a personal-car mileage reimbursement rate per kilometer. The daily ground-transport caps do not establish that rate. No numerical mileage rate can be answered from this result set.

Abstention check: all three complete returned passages were inspected; no distance-rate rule is present. Correct abstention is a successful unsupported-case outcome. No citation is fabricated to support a rate.

## Quality decision and remaining limits

Did we retrieve the right evidence, and did the answer stay within it? The paraphrase target was rank 1. Applicable evidence was returned for the dated question, but historical content outranked it. All demonstrated factual claims map to the same query’s returned text and retain dates, units, exceptions and scope. The unsupported question correctly abstains.

Retrieval success: useful passages present for both supported questions. Answer faithfulness: supported claims checked and unsupported rate withheld. Observed failure/limitation: historical passage rank 1 for a current-date query. No automatic date filtering is implemented. With 3 documents and top_k 5, these tests do not assess recall in a larger corpus, production robustness or general accuracy. No baseline or performance improvement was measured.

Participant inspection: compare a cited answer to its returned text; verify 2026.2/2026-09-01 applicability rather than rank 1 historical terms; inspect the mileage result and insufficient-evidence response.
