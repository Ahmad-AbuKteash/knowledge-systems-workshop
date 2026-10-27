# Submit one completed source

Use for `$submit-source source-01` (Codex) or `/submit-source source-01`
(Claude Code / Copilot). The explicit invocation authorizes exporting this source,
committing its submission, and pushing to the current shared workshop branch.
No PR or approval workflow. Keep explaining what happens: this is a workshop.

1. Resolve the assigned source as in WORKSHOP_MODE.md. Read CONTRIBUTING.md and
   the repository instructions. Check Git status, current branch, and origin.
   Require a branch starting `workshop/`, with an upstream on origin for that same
   branch. Never submit to main, switch branches automatically, or create a session
   branch from a participant's working tree. If opened on main, explain the correct
   workshop clone/branch and stop without discarding or moving work.
2. Fetch origin. Check that local unpushed commits change only
   `submissions/<assigned-source>/`. Check staged and tracked working changes too;
   unrelated staged changes or tracked modifications must be resolved by the user
   first. Ignore untracked/local workspace outputs. Do not stash or reset anything.
3. Confirm all eleven steps are complete and their artifacts are current. Run
   `tools/export_submission.py <source>` with the workshop virtual environment.
   If prerequisites fail, explain and stop; do not run missing steps. If the bundle
   already exists, inspect it against the current chunk records and embedding file
   (including IDs, metadata, text, model, dimensions, and vector values). Reuse it
   only if it matches and evaluation/review.md matches the submitted review; otherwise
   stop and explain the need for a deliberate replacement. Do not silently overwrite.
4. Inspect only the source's exported bundle and review. Show a short summary of
   passage/document counts, embedding settings, and paths. Keep credentials and
   local environments out of Git. Do not read .env. Check submitted files for obvious
   accidental secrets without echoing any secret content.
5. Stage only `submissions/<source>/`; inspect staged paths. Commit if there is a
   change, with a message such as `Submit source-01 knowledge`. If nothing changed,
   do not create an empty commit. Never stage the whole repository.
6. Run `git pull --rebase`, then `git push origin HEAD:<current-workshop-branch>`.
   If the pull starts a rebase and conflicts, abort that rebase and report the
   conflicting paths; preserve the participant's commit. Never choose theirs/ours,
   force-push, or overwrite another source. For a push rejected solely because
   another participant pushed first, fetch/rebase and retry up to two times, then stop.
   Authentication failures are not concurrency failures: explain access is required.
7. Fetch the branch and verify the local submission commit is contained in the
   remote branch. Report branch, commit ID, source folder, and verified pushed status.
   Tell the participant the instructor can now run update-studio. Do not run that
   instructor operation from the participant repository.

If the same source folder changes remotely, treat it as a source-assignment conflict
even if Git could auto-merge it. Stop for the trainer to resolve ownership.
