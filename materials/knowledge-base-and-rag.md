# Engineering Knowledge Systems for AI Agents

## Knowledge bases and retrieval-augmented generation

Rami Younes · XPERIENCE  
[xperience.works](https://xperience.works/)

Presentation content: each numbered section is a slide; horizontal rules separate slides. Speaker notes provide optional narration. Nimbus examples are fictional.

---

## 1 · Knowledge Bases and RAG

**How AI applications find and use your organization's knowledge**

Engineering Knowledge Systems for AI Agents  
Rami Younes · XPERIENCE

**Speaker notes:** Introduce the goal: understand how external information becomes evidence for an AI answer. Focus on the architecture and engineering decisions rather than a particular product.

---

## 2 · The organizational knowledge problem

Your information lives across:

- Documents and shared folders.
- Wikis and internal portals.
- Product documentation and support articles.
- Databases and business systems.

**Finding a document is only useful if it contains relevant, current information.**

**Speaker notes:** Information may be scattered, duplicated, outdated, or inaccessible to the person asking. Connecting AI to sources introduces those same challenges into the answering process.

---

## 3 · Model knowledge and external knowledge

**Model knowledge**  
Patterns and information learned during training, represented in model parameters.

**External knowledge**  
Information supplied through context, retrieval, and tools at runtime.

**An AI application needs a way to access relevant private or changing information.**

**Speaker notes:** Training does not automatically give a model access to a company's current policies. Supplying documents at runtime does not update the model's underlying weights. The information is available within the context provided for that interaction.

---

## 4 · What is a knowledge base?

**An organized collection of information maintained so people or software can find and use it.**

For an AI application, useful knowledge includes:

- Content that answers real questions.
- Structure that makes relevant sections discoverable.
- Metadata that identifies source, scope, and version.
- Rules for access, ownership, and updates.

**Speaker notes:** A knowledge base can include documents, structured records, or both. It is broader than a folder of Markdown and broader than a vector database. An existing wiki may already serve as a knowledge base.

---

## 5 · Sources, knowledge bases, and indexes

| Component | Purpose |
|---|---|
| Source system | Maintains original information |
| Knowledge base | Organizes information for discovery and use |
| Search index | Helps locate relevant content efficiently |

**These roles may be implemented within the same system or across several systems.**

**Speaker notes:** A database can store knowledge, metadata, or indexes. A vector store is one indexing/storage option. Keep the original source identifiable even when content is transformed and copied elsewhere.

---

## 6 · What is RAG?

**Retrieval-Augmented Generation**

1. **Retrieve:** find evidence relevant to the question.
2. **Augment:** include that evidence in the model's context.
3. **Generate:** produce an answer using the available evidence.

**The knowledge base holds information. RAG connects retrieved information to an answer.**

**Speaker notes:** RAG is a runtime pattern. It does not require retraining the model, a specific framework, or a vector database. Retrieval may use text search, semantic search, structured queries, or file-reading tools.

---

## 7 · RAG architecture

```text
Preparation
Sources → Extract → Prepare → Store / Index

Answering
Question → Retrieve → Select evidence → Model → Answer + Sources
```

**Preparation determines what can be found. Retrieval determines what the model receives.**

**Speaker notes:** Separate the preparation path from the answering path. Preparation may happen on a schedule, on source changes, or on demand. Simple systems can search prepared files directly without building a separate index.

---

## 8 · A question through the system

**Question:** “What is our current meal reimbursement limit abroad?”

**Retrieved evidence:**

> Expense Policy 2026: The daily meal reimbursement limit abroad is USD 85.

**Answer:**

> The current limit is USD 85 per day, according to Expense Policy 2026.

**Speaker notes:** This is a fictional example. A complete system must verify applicability, effective date, access rights, and the supporting passage. Retrieving the historical policy could lead to a different answer.

---

## 9 · Ingestion: preparing sources for retrieval

**Collect → Extract → Clean → Structure → Enrich → Validate**

- Extract text and relationships from source formats.
- Remove irrelevant boilerplate without changing meaning.
- Preserve headings, lists, tables, and source references.
- Identify duplicates and conflicting versions.

**Speaker notes:** Conversion is one step within ingestion. A successful extraction command does not prove that a table, qualification, or exception was preserved. Scans may need OCR; some content needs human review.

---

## 10 · Structure and metadata

**Structure explains how content fits together.**

Sections · Headings · Tables · Relationships

**Metadata explains where and when it applies.**

Source · Version · Effective date · Owner · Access scope

**Speaker notes:** Plain text or Markdown is often convenient, but complex layouts and relationships may need a richer representation. Metadata can guide filtering and source selection; it needs explicit, trustworthy values and rules for using them.

---

## 11 · Chunking: choosing retrieval units

Divide long content into passages that remain meaningful on their own.

- Respect section and topic boundaries.
- Keep necessary definitions and qualifications together.
- Attach document identity and section context.
- Use overlap when it preserves useful continuity.

**Too little context loses meaning. Too much context adds irrelevant material.**

**Speaker notes:** Chunking is useful for many indexed retrieval systems, but every document does not need splitting. There is no universal chunk size. Evaluate using the actual question types, document structure, and model context budget.

---

## 12 · Keyword and semantic retrieval

| Method | What it looks for | Useful example |
|---|---|---|
| Keyword search | Matching terms and their relevance | Exact API names or error codes |
| Semantic search | Similarity between learned representations | Different wording about a related concept |
| Hybrid search | Combined lexical and semantic signals | Queries needing both exact terms and conceptual matches |

**Speaker notes:** BM25 is a common lexical ranking method. Semantic search can help with paraphrases, but does not guarantee relevance. Hybrid systems need a way to combine rankings, and their benefit must be evaluated rather than assumed.

---

## 13 · Embeddings and vector indexes

**An embedding represents text as a numerical vector.**

```text
Passages → Embedding model → Stored vectors
Question → Embedding model → Similarity search → Candidate passages
```

**Similarity identifies candidates; it does not prove correctness or authority.**

**Speaker notes:** Query and document representations must be compatible. Similarity is learned from the embedding model, so it can miss important distinctions. A highly similar policy can still be outdated or irrelevant to the user's location.

---

## 14 · Filtering and reranking

**Filter**  
Restrict eligible content by access, scope, date, or document type.

**Retrieve**  
Find candidate passages.

**Rerank**  
Optionally score candidates again for relevance to the question.

**Select**  
Choose evidence that fits the context budget.

**Speaker notes:** Implementation order varies, but authorization must prevent unauthorized evidence from reaching the model. Reranking may improve candidate ordering while adding cost and latency. Selecting more passages is not automatically better.

---

## 15 · Generation and supporting citations

The model receives the question, instructions, and selected evidence.

A useful answer should:

- Respond directly to the question.
- Identify the supporting source and version.
- Cite passages that support its factual claims.
- Explain missing evidence or unresolved conflicts.

**Speaker notes:** Citations make verification easier but do not guarantee truth. Check whether a passage exists, whether it supports the claim, and whether the source applies. The assistant should abstain when evidence is insufficient.

---

## 16 · Agent-driven retrieval

An agent can decide to:

1. Search the available sources.
2. Open promising documents.
3. Refine the query or follow references.
4. Answer when it has enough evidence.

**Search can be a tool within a broader reasoning workflow.**

**Speaker notes:** A fixed RAG pipeline follows predefined retrieval steps. Agent-driven retrieval can choose or repeat steps. That flexibility can introduce additional latency, cost, and variability. File search, database queries, and vector search can all be tools; an agent does not need to use all of them.

---

## 17 · RAG and fine-tuning

| Approach | Primary mechanism | Example use |
|---|---|---|
| RAG | Supplies retrieved information at runtime | Answering from current internal policies |
| Fine-tuning | Updates model parameters using training examples | Adapting behavior or performance for a task |

**They can be used together.**

**Speaker notes:** This is a mechanism distinction, not a strict division of capabilities. Fine-tuning can affect factual behavior, but changing documents still need a maintained update process. Neither approach guarantees accurate or current answers.

---

## 18 · Where RAG fails

- **Source failure:** the information is absent, wrong, or outdated.
- **Ingestion failure:** useful information is lost or distorted.
- **Retrieval failure:** the relevant evidence is not selected.
- **Generation failure:** the answer misuses or invents evidence.

**Trace the evidence through the system before choosing a fix.**

**Speaker notes:** Use an outdated policy as an example spanning several stages. Rewriting the final prompt cannot restore a table lost during extraction. Better retrieval cannot fix a wrong source fact by itself.

---

## 19 · Evaluating a knowledge system

**Retrieval quality**  
Did the relevant evidence appear among the retrieved results?

**Answer quality**  
Is the answer correct, supported, and appropriately complete?

**Operational quality**  
Is the system current, responsive, affordable, and enforcing access rules?

**Speaker notes:** Build a reviewed question set with expected evidence, historical/current cases, ambiguous requests, and questions that should not be answered. Evaluate retrieval and generation separately. Measure latency and cost with real traces, and add examples when failures occur. Do not equate a small demo set with general reliability.

---

## 20 · Freshness, access, and untrusted content

- Update searchable knowledge when authoritative sources change.
- Remove obsolete indexed content when sources are deleted or replaced.
- Enforce access before evidence reaches the model.
- Treat retrieved instructions as untrusted document content.
- Track which content is sent to external services.

**Speaker notes:** Production knowledge is a maintained system. Access rules must apply during retrieval, not only at the final answer. Documents can contain prompt-injection attempts. Local extraction does not imply local model inference or prevent disclosure through an agent's other tools.

---

## 21 · Choosing the simplest useful architecture

Start with the workload:

- What questions must the system answer?
- How large and complex are the sources?
- How often do they change?
- Who may access each part?
- What do the measured failures tell you?

**Add extraction, indexing, and agent complexity where it solves a demonstrated problem.**

**Speaker notes:** A small, clear collection may work with direct search. Complex documents may justify advanced extraction; difficult retrieval may justify hybrid search or reranking. Document count alone is not a sufficient architecture rule.

---

## 22 · Key takeaways

1. A knowledge base organizes information for discovery and use.
2. RAG brings retrieved evidence into answer generation.
3. Source quality, metadata, and freshness affect reliability.
4. Embeddings and vector stores are implementation choices.
5. Verify evidence, evaluate outcomes, and maintain access controls.

**Questions?**

Rami Younes · XPERIENCE  
[xperience.works](https://xperience.works/)

**Speaker notes:** Return to the distinction between the knowledge collection and the answering workflow. Invite questions about the architecture and its tradeoffs.
