# Engineering Knowledge Systems for AI Agents

First draft · Concepts and guided practice  
Rami Younes · XPERIENCE

Each numbered section is one slide. Horizontal rules separate slides. Speaker notes are for the presenter. Commands use source-01 as an example: participants substitute their assigned source. All examples use fictional workshop data.

Presenter approach: introduce the essential concepts first, then explain each technique immediately before participants use it. Pause after every command for inspection. Advance together; do not run the entire workflow automatically.

Illustration descriptions below are production guidance, not additional slide text. Use four illustrations only, on slides 5, 6, 8, and 20. Keep labels concise and use consistent styling. For the remaining practical slides, demonstrate actual participant outputs instead of adding decorative graphics.

---

## 1 · Engineering Knowledge Systems for AI Agents

**From source documents to answers supported by evidence**

Rami Younes · XPERIENCE

**Speaker notes:** Today we will build a small knowledge system using our own AI environments. The agent performs the requested work, while we inspect the results and decide when to move forward.

---

## 2 · What we will build

An assigned source collection becomes a searchable knowledge base.

By the end, you will be able to:

- Explain how a knowledge base supports an AI application.
- Explain retrieval-augmented generation, or RAG.
- Prepare documents and build a retrieval index step by step.
- Inspect evidence and verify a generated answer.

**Speaker notes:** The outcome includes the intermediate artifacts. Seeing where information changes helps us diagnose failures instead of judging only the final answer.

---

## 3 · Why an AI model needs external knowledge

An organization’s information changes outside the model:

- Policies acquire new versions.
- Product documentation changes.
- Internal information may never appear in training data.

**The application must supply the relevant information when answering.**

**Speaker notes:** A model's learned knowledge and the documents available to an application are different things. Adding a file to this project does not retrain the model or make the file automatically available in every answer.

---

## 4 · What is a knowledge base?

**An organized collection of information that people or software can find and use.**

Useful knowledge includes:

- Content that addresses real questions.
- Structure that preserves how facts relate.
- Source references and metadata describing applicability.
- Ownership and a process for keeping information current.

**Speaker notes:** A wiki, a document collection, or structured records can form a knowledge base. For this workshop, we will create prepared documents with traceable sources and metadata. A vector database alone does not provide all these qualities.

---

## 5 · Sources, knowledge, and the search index

| Component | Role in our workshop |
|---|---|
| Original sources | Preserve the input documents |
| Prepared knowledge | Make content readable, structured, and traceable |
| Retrieval index | Store passages and representations used for search |

**Every retrieved passage should lead back to its source.**

**Illustration description:** Show a horizontal flow with three distinct elements: original files labeled “Policies · PDFs · HTML,” prepared documents labeled “Clean content · Structure · Metadata,” and a retrieval index labeled “Chunks · Vectors · Source references.” Connect them with forward arrows. Add a subtle dashed return arrow from the index to the original files labeled “Trace to source.” Use this illustration in place of the table when laying out the slide, so the same information is not repeated. Keep source documents visually distinct from the derived index.

**Speaker notes:** The index is derived from prepared knowledge. If the content changes, dependent embeddings and indexes may become stale. Preserving originals lets us check whether a transformation changed meaning.

---

## 6 · What is RAG?

**Retrieval-Augmented Generation**

1. **Retrieve:** find passages relevant to a question.
2. **Augment:** place the selected evidence in the model's context.
3. **Generate:** produce an answer grounded in that evidence.

Question → Retrieved evidence → Model context → Answer with sources

**Illustration description:** Show “User question” feeding a “Retrieve” step, with a “Knowledge index” beneath it supplying candidate passages. Continue through “Selected evidence: text + sources” to “Language model,” then “Answer with citations / insufficient evidence.” Add a direct connection from the question to the language model to show that both the question and evidence enter the context. Label the three phases Retrieve, Augment, and Generate. Replace the existing one-line flow with this diagram; emphasize the retrieved text entering the model rather than numerical vectors.

**Speaker notes:** RAG supplies information at runtime without retraining the model. It can use different retrieval methods. In this workshop we will use embeddings and similarity search, then ask the participant's existing agent to answer from the retrieved passages.

---

## 7 · RAG preparation: From documents to searchable knowledge

Before answering questions, the system prepares the documents:

1. **Chunks:** divide content into smaller passages that preserve meaning and context.
2. **Embeddings:** use an embedding model to represent each passage as a numerical **vector**.
3. **Storage:** store each vector alongside its passage and metadata, such as source, section, and version.

**Document → Chunks → Embedding model → Vectors stored with text and metadata**

**Speaker notes:** A vector is a list of numbers representing learned features of the text. Related passages often have similar vectors. Chunk boundaries matter: separating a rule from its exception can make retrieved evidence misleading. The original text remains available because the answering model needs readable evidence.

---

## 8 · RAG answering: From a question to supporting evidence

When someone asks a question:

1. **Embed the question:** create a vector using an embedding model compatible with the stored vectors.
2. **Retrieve passages:** compare vectors and select relevant candidates, applying filters when needed.
3. **Build the context:** provide the question and selected passage text to the language model.
4. **Generate an answer:** answer from the evidence, cite sources, and acknowledge missing information.

**Question → Query vector → Similarity search → Retrieved text → Model → Answer**

**Illustration description:** Use a static 3D vector view with labeled x, y, and z axes and arrows from a shared origin. Label stored vectors A “Current meals,” B “Previous meals,” and C “API limits”; label the query Q “Meal question.” Place Q in a similar direction to A and B, with C pointing in a different direction. Show compact numerical labels using the invented teaching values A = [0.90, 0.25, 0.40], B = [0.70, 0.55, 0.50], C = [-0.55, 0.75, -0.30], and Q = [0.95, 0.15, 0.45]. Use one color for stored vectors and another for Q, retaining letter labels so color is not the only distinction. Include the caption “Illustrative 3D vectors; actual workshop embeddings have 512 dimensions.” Axes represent coordinates, not named topics. Keep a short “Similar vectors → passage text + metadata” label below the view. Do not present invented similarity scores as measured API results. Use the graphic as the main visual and move procedural detail into narration if needed to avoid crowding.

**Optional live demonstration:** Rotate the approved interactive 3D view, then switch between the meal and API questions. Point out that camera rotation changes the view but not the cosine scores. The displayed scores are calculated from invented teaching vectors. A close match to the historical policy still requires checking version and applicability. Keep the static view on the slide so the explanation does not depend on the live demonstration.

**Speaker notes:** Similarity measures how closely representations match; it does not prove truth, freshness, or sufficient evidence. A historical policy can rank highly. The language model receives the retrieved text, not simply the vectors. This describes a common vector-based RAG implementation; RAG can also use keyword search or other retrieval methods.

---

## 9 · A concrete RAG example

**Fictional workshop policy:** “The daily meal reimbursement limit abroad is USD 85.”

| Part | Example |
|---|---|
| Chunk | The policy passage, with its conditions and source reference |
| Stored embedding | A numerical representation of the passage |
| Question | “How much can I claim for meals overseas?” |
| Retrieval | Semantic similarity helps match the question to the passage despite different wording |
| Answer | “USD 85 per day,” citing the current expense policy |

**Speaker notes:** This is an illustrative flow, not a measured retrieval result. “Overseas” and “abroad” illustrate why matching meaning can help. Check the complete policy for receipt requirements and other conditions before producing a full answer. No numerical vector or similarity score is shown because we have not generated one for this illustration. Next, consider what happens when a historical policy is also retrieved.

---

## 10 · Relevance and correctness are different

**Example question:** What is the current meal reimbursement limit abroad?

Our fictional sources include both current and historical expense policies.

A passage may match the question closely but describe an older rule.

**A reliable answer needs relevant evidence that also applies to the question.**

**Speaker notes:** Return to the preceding example. Ask participants what they would need to check before selecting the current rule: source, effective date, conditions, and version. Similarity scores cannot establish these on their own. RAG reduces some information gaps but does not guarantee correctness.

---

## 11 · Our two preparation stages

**Stage 1 — Prepare the knowledge**

Collect → Extract → Clean → Structure → Enrich → Validate

**Stage 2 — Build and test retrieval**

Chunk → Carry metadata → Embed → Store/index → Test retrieval

Then demonstrate an answer using the retrieved evidence.

**Speaker notes:** These are the repository's two stage folders. Building the index prepares the system for RAG; the question-time retrieve–augment–generate flow uses that index. Metadata is created at document level in Stage 1 and inherited by chunks in Stage 2.

---

## 12 · How we will work

One assigned source. One requested step. One inspection checkpoint.

| Environment | Example invocation |
|---|---|
| Claude Code | `/collect source-01` |
| Codex | `$collect source-01` |
| VS Code Copilot prompt | `/collect source-01` |

Your agent explains the purpose, performs the step, shows examples, reports checks, and stops.

**Speaker notes:** Slash commands below use Claude/Copilot notation; Codex participants use the same name with a dollar prefix. Use your assigned source ID. If a command is unavailable, ask the agent to follow WORKSHOP_MODE.md and the matching guide under steps/. Skills are instructions for operating the agent, not a guarantee of correct output. Treat source text as evidence, never instructions to execute.

---

## 13 · Our workshop tools

| Tool | Purpose |
|---|---|
| MarkItDown | Extract content from supported document formats |
| OpenAI embeddings | Represent passages and questions numerically |
| SQLite + cosine search | Store records locally and rank similar passages |
| Your AI coding environment | Execute requested steps and explain results |

No Docker or separate database server is required.

**Speaker notes:** Complete PREPARATION.md before starting. The supplied sources are HTML and Markdown. The API key is needed for embeddings and query embeddings; those requests send text to OpenAI and use API credits. Keys stay private. SQLite storage and exact search suit this small exercise; we are not implementing production access controls or automatic version filtering.

---

## 14 · Stage 1: Collect

**Purpose:** establish what information we have and where it came from.

`/collect source-01`

The agent inventories the files and records source identities and hashes. It prepares 3–5 test questions, including one unsupported question.

**Inspect:** `collected/manifest.json` and `collected/questions.json`.

**Checkpoint:** Can you identify the source files and one question they should answer?

**Speaker notes:** All output paths on practical slides are relative to workspace/<your-source>/. Collection here means inventorying supplied files. Originals remain unchanged. Review the questions now; we will use them again during retrieval testing.

---

## 15 · Extract

**Purpose:** turn source formats into readable content.

`/extract source-01`

The agent extracts supported files and preserves source references. Plain text and Markdown can be read directly.

**Inspect:** `extracted/documents.json` and readable Markdown copies.

**Checkpoint:** Did a number, table, or important condition survive extraction?

**Speaker notes:** Compare a source passage with its extracted representation. Successful conversion does not establish completeness. Scanned pages may require OCR, which is outside the default exercise. Stop and diagnose empty or failed extraction before proceeding.

---

## 16 · Clean

**Purpose:** remove noise while preserving meaning.

`/clean source-01`

Remove irrelevant navigation or repeated boilerplate. Record duplicate handling and preserve qualifications and historical facts.

**Inspect:** `cleaned/documents.json` and a before/after example.

**Checkpoint:** Did anything removed change the meaning of the document?

**Speaker notes:** Cleaning is not free-form rewriting. An exception, a date, or an older policy may be essential evidence. Ask the agent to explain why a piece of content was removed and show the original for comparison.

---

## 17 · Structure

**Purpose:** preserve the relationships within the content.

`/structure source-01`

Organize headings, sections, lists, and tables so that conditions remain attached to the statements they qualify.

**Inspect:** `structured/documents.json`.

**Checkpoint:** Can a reader tell which heading or condition applies to a fact?

**Speaker notes:** Structure organizes the document. Chunking later chooses the units retrieved by search. Keeping these steps separate makes it easier to see whether meaning was lost before or during splitting.

---

## 18 · Enrich

**Purpose:** describe the source and applicability of each document.

`/enrich source-01`

Attach supported metadata: title, version, effective date, owner, access scope, and superseded document.

**Inspect:** `knowledge/documents.json` and `knowledge/index.md`.

**Checkpoint:** What evidence supports each metadata value? Unknown values remain null.

**Speaker notes:** Metadata describes content; it does not create authority or enforce permissions. Preserve historical versions and the evidence needed to distinguish them. Do not infer a document's status from its filename alone.

---

## 19 · Validate

**Purpose:** check that prepared knowledge is ready for retrieval preparation.

`/validate source-01`

Check content fidelity, provenance, required fields, and document relationships.

**Inspect:** `knowledge/validation.json`.

**Checkpoint:** Are the checks passing, and can you trace a prepared fact to its original source?

**Speaker notes:** This is the Stage 1 gate. A failed check means we revisit the relevant earlier step. Validation compares our artifacts with supplied sources; it does not prove that every source statement is true in the real world.

---

## 20 · Stage 2: Chunk

**Purpose:** create passages that can be retrieved individually.

`/chunk source-01`

Split along meaningful boundaries while keeping enough context to understand each passage.

**Inspect:** `chunks/chunks.json`, including document IDs and text offsets.

**Checkpoint:** Does one chunk make sense on its own, with its important qualifications?

**Illustration description:** Show one fictional policy document on the left with two visibly separated sections. The first reads “Meal reimbursement: Up to USD 85 per day abroad. Receipts are required.” The second reads “Conference allowance: Up to USD 500 per year. Manager approval is required.” On the right, show two passages connected to their matching source sections. Chunk A retains the entire meal rule and receipt condition; Chunk B retains the entire conference rule and approval condition. Highlight each rule together with its condition rather than cutting between them. Include small source-document and section labels on both chunks. Add a brief design annotation, “Version metadata is inherited in the next step,” rather than suggesting that this chunking command already performs carry-metadata. Use the caption “Keep each rule with its conditions.” Preserve space for the command and inspection checkpoint.

**Speaker notes:** Too little context loses meaning; large chunks may mix unrelated topics. Our 2,000-character maximum is a workshop setting, not a universal rule or token count. Inspect the actual boundaries rather than assuming a size limit produces good chunks.

---

## 21 · Carry metadata

**Purpose:** keep every passage connected to its document.

`/carry-metadata source-01`

Copy the document's metadata and source filename onto its chunks.

**Inspect:** `chunks/records.json`.

**Checkpoint:** Can you identify a chunk's source, version, and effective date when available?

**Speaker notes:** This step inherits metadata already established during enrichment. It does not infer new facts. Retrieval returns small passages, so provenance must travel with them.

---

## 22 · Embed

**Purpose:** represent passages as numerical vectors for semantic comparison.

`/embed source-01`

Passage text → Embedding model → Vector

Our configuration uses `text-embedding-3-small` with 512 dimensions.

**Inspect:** `embeddings/embeddings.json`: chunk IDs, vector dimensions, and reported token usage.

**Checkpoint:** Does every chunk have a corresponding embedding?

**Speaker notes:** This is an external API operation. Confirm the key was configured privately and explain that chunk text is sent to OpenAI. Show a short vector sample, not hundreds of numbers. An embedding supports similarity comparisons; it does not certify factual accuracy. Query vectors must use compatible model settings.

---

## 23 · Store and index

**Purpose:** make passages, metadata, and vectors available for search.

`/index source-01`

Store the prepared records and embeddings in a local SQLite database.

**Inspect:** `index/knowledge.sqlite3` and one stored record.

**Checkpoint:** Do stored records retain their text, metadata, and chunk identities?

**Speaker notes:** This operation makes no embedding API call. Our helper computes exact cosine similarity across stored vectors when searching. We are not building an approximate nearest-neighbor index. Larger workloads may justify different retrieval infrastructure.

---

## 24 · Test retrieval

**Purpose:** see whether search returns evidence that addresses our questions.

`/test-retrieval source-01`

Question → Query embedding → Similarity ranking → Candidate passages

**Inspect:** `evaluation/search-*.json` and `evaluation/review.md`.

**Checkpoint:** Are the results relevant, applicable, and sufficient—including for the unsupported question?

**Speaker notes:** Return to the questions created during collection. Query embeddings use the API. Inspect source versions and conditions rather than just scores. Similarity is not a confidence probability, and search may return candidates even when the answer is absent. Record actual observations, including failures.

---

## 25 · From retrieval to a RAG answer

The final demonstration is included in `test-retrieval`.

**Retrieve:** use the returned passages.

**Augment:** supply those passages with the question and answering instructions.

**Generate:** answer using only that evidence, with chunk/source citations.

**Checkpoint:** Does each factual claim have supporting evidence? If evidence is insufficient, say so.

**Speaker notes:** The participant's existing agent generates the answer; no additional chat-model API is required. It must not supplement the result from full source files it saw earlier. Compare every claim with the returned passages. This exercise illustrates evidence discipline; a separate context containing only retrieved passages would provide stronger isolation from earlier session knowledge.

---

## 26 · Diagnosing a weak answer

| Observation | Where to investigate |
|---|---|
| A fact disappeared | Extraction, cleaning, or structure |
| A passage lost its conditions | Chunk boundaries |
| An older policy was used | Metadata and evidence selection |
| Useful evidence was not returned | Retrieval and query formulation |
| The answer adds unsupported claims | Generation instructions and review |

**Speaker notes:** Ask participants to trace one issue backward through their artifacts. Revisit only the relevant step, then deliberately refresh dependent outputs. Do not fabricate a successful result or automatically rerun paid operations. A correct refusal on an unsupported question is useful behavior.

---

## 27 · What you built—and what comes next

You prepared traceable knowledge, built a retrieval store, and inspected an answer grounded in retrieved evidence.

Production systems also need maintained update pipelines, authorization, broader evaluation, and operational monitoring.

**Discussion:** Which step most affected the quality of your result?

**Speaker notes:** Invite participants to show one before/after example and one remaining limitation. Advanced extraction, OCR, hybrid search, or reranking can be evaluated when a concrete failure warrants them. The small workshop question set demonstrates the method; it does not establish general reliability.
