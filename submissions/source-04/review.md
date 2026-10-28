# source-04 retrieval review

Source: Nimbus travel expenses (synthetic). Index: `workspace/source-04/index/knowledge.sqlite3`,
6 chunks, `text-embedding-3-small`, 512 dimensions, exact cosine, top_k = 5.
Each query was embedded by a real OpenAI API call (12–17 tokens per query, 69 total).
Scores are cosine similarities, not confidence probabilities. Similarity always returns
five candidates, even when none answers the question.

Chunk key: `doc-01` = current-policy.pdf v2026.2 (effective 2026-09-01, supersedes doc-03);
`doc-02` = operational-notice.png v1.0 (effective 2026-09-01, supplements doc-01);
`doc-03` = previous-policy.html v2025.1 (historical, superseded_by doc-01).

## q1 — What is the current international daily meal cap for Nimbus employee travel?

Evidence: `search-da9518d0ca10.json` · expected answerable: yes

| Rank | Chunk | Cosine | Version | Relevance / support |
|---|---|---|---|---|
| 1 | `source-04-doc-03:0-500:a83cb033` | 0.7273 | 2025.1 | Relevant topic, **does not support** the current cap: "Historical policy. Superseded on 2026-09-01" — USD 60 is outdated |
| 2 | `source-04-doc-01:0-342:2eefb76a` | 0.7100 | 2026.2 | **Supports**: table row "Meals \| USD 45 \| USD 85" under "International / day", effective 2026-09-01 |
| 3 | `source-04-doc-02:0-534:33cd7151` | 0.5696 | 1.0 | Supports and clarifies: USD 85 covers all meals in one calendar day |
| 4 | `source-04-doc-01:344-550:42a72324` | 0.5327 | 2026.2 | Related (receipts), not about the cap |
| 5 | `source-04-doc-01:552-694:1c2a6a8b` | 0.5270 | 2026.2 | Related (min of expense and cap), not the amount |

**Finding:** the outdated policy ranked first. Similarity cannot tell versions apart (the two
caps chunks are 0.904 similar to each other). A correct answer depends on the version and
supersession text carried inside the chunk and its metadata. Missing information: none.

## q2 — Is the international meal cap applied per meal or per calendar day?

Evidence: `search-819cbf491209.json` · expected answerable: yes

| Rank | Chunk | Cosine | Version | Relevance / support |
|---|---|---|---|---|
| 1 | `source-04-doc-02:0-534:33cd7151` | 0.6169 | 1.0 | **Supports**: "covers all eligible meals combined in one calendar day. It is not a per-meal cap." |
| 2 | `source-04-doc-01:552-694:1c2a6a8b` | 0.5522 | 2026.2 | Partial: "applicable daily cap" implies per day, not explicit |
| 3 | `source-04-doc-03:0-500:a83cb033` | 0.5013 | 2025.1 | Historical; "daily meal cap" wording, not current |
| 4 | `source-04-doc-01:344-550:42a72324` | 0.4978 | 2026.2 | Not relevant to per-meal vs per-day |
| 5 | `source-04-doc-01:0-342:2eefb76a` | 0.4169 | 2026.2 | Partial: column header "International / day" |

**Finding:** the PNG-only clarification ranked first, so the image transcription in extract was
essential. Notice effective 2026-09-01 (published 2026-10-01). Missing information: none.

## q3 — What can an employee do if they lose a meal receipt?

Evidence: `search-a88f0b82824f.json` · expected answerable: yes

| Rank | Chunk | Cosine | Version | Relevance / support |
|---|---|---|---|---|
| 1 | `source-04-doc-01:344-550:42a72324` | 0.5762 | 2026.2 | **Supports**: "a lost receipt may be replaced by a signed declaration for one meal costing no more than USD 20 per trip" |
| 2 | `source-04-doc-02:0-534:33cd7151` | 0.4823 | 1.0 | Supports a limit: "The USD 20 lost-receipt exception does not increase the daily cap" |
| 3 | `source-04-doc-01:552-694:1c2a6a8b` | 0.4349 | 2026.2 | Not relevant |
| 4 | `source-04-doc-03:0-500:a83cb033` | 0.3712 | 2025.1 | Historical: "no lost-receipt exception" — outdated, must not be used |
| 5 | `source-04-doc-01:696-1045:ab28b387` | 0.3578 | 2026.2 | Not relevant |

**Finding:** the rule and its exception stayed in one chunk, so the conditions (one meal,
USD 20, per trip) arrived together. Missing information: none.

## q4 — How many days after a trip ends must an expense claim be submitted?

Evidence: `search-deccf88abbbe.json` · expected answerable: yes

| Rank | Chunk | Cosine | Version | Relevance / support |
|---|---|---|---|---|
| 1 | `source-04-doc-01:696-1045:ab28b387` | 0.6300 | 2026.2 | **Supports**: "Submit within 30 calendar days after the trip ends. Late claims require Finance approval." |
| 2–5 | doc-03, doc-01 (Calculation, Limits, Rule) | 0.41–0.38 | — | Not relevant to the deadline |

**Finding:** clear winner with a large score gap (0.63 vs 0.41). Missing information: none.

## q5 — What is the per-kilometre mileage reimbursement rate for using a personal car? (unsupported)

Evidence: `search-aad5adbb51ce.json` · expected answerable: **no**

| Rank | Chunk | Cosine | Version | Relevance / support |
|---|---|---|---|---|
| 1 | `source-04-doc-01:552-694:1c2a6a8b` | 0.4139 | 2026.2 | Does not support: generic reimbursement formula |
| 2 | `source-04-doc-01:696-1045:ab28b387` | 0.4120 | 2026.2 | Does not support |
| 3 | `source-04-doc-01:0-342:2eefb76a` | 0.3898 | 2026.2 | Does not support: "Ground transport USD 35 / USD 55" is a daily cap, not a per-km rate |
| 4 | `source-04-doc-03:0-500:a83cb033` | 0.3772 | 2025.1 | Does not support |
| 5 | `source-04-doc-01:344-550:42a72324` | 0.3303 | 2026.2 | Does not support |

**Finding:** five passages were still returned, all with low, flat scores (0.33–0.41). None
mentions mileage, kilometres or personal cars. **Correct outcome: abstain.** Risk: the
ground-transport cap is a tempting but wrong substitute. Missing information: a mileage rate.

## Summary

| Question | Expected | Top-1 useful? | Supporting chunk retrieved | Outcome |
|---|---|---|---|---|
| q1 | answerable | No — historical first | Yes, rank 2 (+ rank 3) | Answerable using version metadata |
| q2 | answerable | Yes | Yes, rank 1 | Answerable |
| q3 | answerable | Yes | Yes, rank 1 (+ rank 2) | Answerable |
| q4 | answerable | Yes | Yes, rank 1 | Answerable |
| q5 | unsupported | n/a | No support | Abstain (correct) |

## Cited answer demonstration (q1, using only the passages returned for q1)

**Question:** What is the current international daily meal cap for Nimbus employee travel?

**Answer:** The current international meal cap is **USD 85 per day**
[`source-04-doc-01:0-342:2eefb76a`, current-policy.pdf v2026.2: "| Meals | USD 45 | USD 85 |"
under "International / day"; "Version: 2026.2. Effective: 2026-09-01."]. It covers all
eligible meals combined in one calendar day, not each meal
[`source-04-doc-02:0-534:33cd7151`, operational-notice.png v1.0: "covers all eligible meals
combined in one calendar day. It is not a per-meal cap."]. The USD 60 figure in the top-ranked
passage is outdated and was not used: that document states "Historical policy. Superseded on
2026-09-01 by current-policy.pdf." [`source-04-doc-03:0-500:a83cb033`, previous-policy.html v2025.1].

Citations verified: each quoted string appears in the text of the cited chunk as returned in
`search-da9518d0ca10.json`. No full source file was read to supplement the answer.

**Abstention demonstration (q5):** The retrieved passages do not state a per-kilometre mileage
rate, so no answer is given. The ground-transport daily caps (USD 35 domestic / USD 55
international) are not a mileage rate.
