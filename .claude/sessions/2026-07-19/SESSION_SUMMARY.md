# Session Summary - 2026-07-19

## Project
4BV Site (4bv.ai) — /Users/dochobbs/Downloads/Consult/4BV

## Branch
main

## Accomplishments
- Updated the Wren project card link to https://wren.kids (was beta.4bv.io)
- Updated the AI101 project card link to https://ai101.health (was dochobbs.github.io/ai101)
- Verified both production domains respond with HTTP 200 before shipping
- Committed the pending `.gitignore` addition excluding `invoices/` from this public repo
- Pushed to origin/main — live site updated via GitHub Pages

## Commits Made
- 6a68f07: FIX: Point Wren and AI101 cards at production domains

## Decisions Made
- Scoped the commit to `index.html` + `.gitignore` instead of `git add -A` — the repo is public and the untracked working files (ui-kit/, previews, 4bv-preview.zip, design-system reference) must stay unpublished

## Next Steps
- `preview.html` / `preview_standalone.html` still carry the old Wren/AI101 links — sync if those files stay in use
- Licensing review still open: licensed OTF fonts are publicly served from the repo
- Decide fate of untracked working files (commit selectively, ignore, or remove)
