# Submit your source to the workshop demo

Each participant works on one assigned source in their own clone of this repository.
You do not need the private application repository, Java, Node, or Docker.

1. Clone the workshop repository using the URL and workshop branch supplied by the trainer:
   `git clone --branch <workshop-branch> <workshop-repository-url>`.
2. Open the cloned folder, follow PREPARATION.md, and create your branch:
   `git switch -c participant/<your-name>-source-01`.
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
   git push -u origin HEAD
   ```

7. Open a pull request against the trainer's workshop branch. If you have no push
   access, agree on a fork or patch handoff with the trainer. A local commit alone
   does not transfer your contribution to the instructor's computer.

Replace source-01 and the branch placeholders with your own assignment. Work in
separate participant branches; do not push everyone's changes directly to one branch.
Keep `.env`, `.venv`, and `workspace/` local. Do not force-add them.

## Instructor collection

Review and merge each participant PR into the workshop branch, then pull that
branch into `knowledge-systems-workshop/` on the demo computer. The app mounts
`submissions/` read-only and reloads it for each tool call. Refresh the source list
in the chat. No merged SQLite database or re-embedding is needed: the MCP service
searches the exported vectors across reviewed bundles and preserves source IDs.

The app accepts schema version 1, text-embedding-3-small at 512 dimensions, up to
500 chunks per source and 100 sources. Historical documents remain searchable;
version/applicability must be checked when selecting evidence. This is a teaching
demo, not a production access-control or document-lifecycle system.
