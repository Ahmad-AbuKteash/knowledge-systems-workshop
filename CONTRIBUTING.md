# Submit your source to the workshop demo

Each participant works on one assigned source in their own clone of this repository.
You do not need the private application repository, Java, Node, or Docker.

1. Clone the workshop repository using the URL and workshop branch supplied by the trainer:
   `git clone --branch <workshop-branch> <workshop-repository-url>`.
2. Open the cloned folder and follow PREPARATION.md. Stay on the shared workshop
   branch; everyone contributes directly to that branch.
3. Complete the eleven manual steps for your assigned source. Inspect the outputs
   and retrieval review with the trainer. Do not run later steps automatically.
4. Export the completed result. This validates existing artifacts; it does not
   perform missing steps or call the embedding API.

   Windows: `.\.venv\Scripts\python.exe tools/export_submission.py source-01`

   macOS: `./.venv/bin/python tools/export_submission.py source-01`

5. Review `submissions/source-01/bundle.json` and `review.md`. They contain your
   prepared text, provenance, vectors, and evaluation review. Confirm the files
   contain only approved workshop data and no credentials or personal information.
6. Stage only your submission:

   ```sh
   git add submissions/source-01
   git diff --cached --stat
   git commit -m "Submit source-01 knowledge"
   git pull --rebase
   git push
   ```

7. Tell the trainer your source is pushed. There is no pull request or PR review.
   A local commit alone does not transfer it to the instructor's computer.

Replace source-01 and the branch placeholders with your own assignment. Each
participant owns a different source folder to avoid overlapping edits. If another
participant pushes first and Git rejects your push, run `git pull --rebase` and
`git push` again. Never force-push. If a conflict occurs, ask the trainer to resolve
the source assignment rather than overwriting someone else's work.
Keep `.env`, `.venv`, and `workspace/` local. Do not force-add them.

## Instructor collection

Before the workshop, give participants repository write access and use a dedicated
workshop branch that permits direct pushes without requiring PRs. Keep normal
protections on other branches. Assign a unique source folder to each participant.

On the demo computer, check out that same workshop branch in
`knowledge-systems-workshop/`, then run `git pull --ff-only`. The app mounts
`submissions/` read-only and reloads it for each tool call. Refresh the source list
in the chat. No merged SQLite database or re-embedding is needed: the MCP service
searches the exported vectors across submitted bundles and preserves source IDs.

The workflow is: **participant commit + push → instructor pull → Studio Refresh**.
The retrieval review file is a learning artifact from the lab, not a GitHub approval.

The app accepts schema version 1, text-embedding-3-small at 512 dimensions, up to
500 chunks per source and 100 sources. Historical documents remain searchable;
version/applicability must be checked when selecting evidence. This is a teaching
demo, not a production access-control or document-lifecycle system.
