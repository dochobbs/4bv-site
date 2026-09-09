# Session Summary - 2026-09-09 (work performed 2026-09-05)

## Project
4bv.ai site — /Users/dochobbs/consult/4BV (public repo dochobbs/4bv-site). Session was opened from
/Users/dochobbs/consult/random/bias (the AOM eval repo), which supplied the content.

## Branch
main

## Accomplishments
- New findings page `aom/` for the pediatric AOM evaluation (~2,500 words): headline table, per-model
  invention counts, seven error modes, identity results, second turn, one-sentence mitigation, grader
  failures, eight-tool CDS battery, OpenEvidence tiers vs ChatGPT for Clinicians, limitations, links to
  both LinkedIn articles, three posts, and the open packet. OG card via make-og.py.
- Home page: AOM card (ear mark, chips) in the Research lane; CDS card rewritten with a line-drawn mark
  ("two answers") and current copy; benchmark card rewritten to method-level facts + locked counts,
  dropping the "first pediatric benchmark" claim the design doc forbids; new Featured writing section
  (nine articles, two-column flow, measured reading times) above the contribution grid.
- Decon page refreshed against the clinician-decon repo: Aug 22 stale-artifact incident, Sep 2
  residual-fragment red team, PPLX head-to-head section, corpus 3,587 cases / 10,761 outputs, unsigned Mac build.
- Type system replaced after a four-round specimen review (14 schemes → 13 superfamilies → 13 owned
  superfamilies → final five → mono options): Fago Office Serif (display), FagoNo (body/UI), Fedra Mono
  (numerals), self-hosted woff2 converted from Michael's OTFs (web licenses confirmed). Near-white paper,
  upright ledes, lining figures. Caecilia/Frutiger no longer referenced.
- Favicon redrawn as the four brand rings on transparent (SVG + 16/32/48/180/512).
- Theme toggle moved to bottom right.
- Impeccable plugin updated 4.0.4 → 4.2.1 (applies next session).

## Work State
- All of the above: committed, pushed, Pages deploy succeeded, verified live at 4bv.ai (200s on /aom/,
  font files, favicon, OG image; served CSS references Fago).
- Local checkout level with origin at 4b533b0; nothing staged.

## Uncommitted / At-Risk
- None from this session. Pre-existing untracked files in the repo (preview.html, ui-kit/, design-system
  docs, stray PNGs) are intentionally unpublished and untouched.
- PEARL repo (~/Downloads/Consult/pearl): 9 commits on `feat/pearl-p2-authoring` unpushed since 2026-08-22 — not this session's work, flagged to Michael.

## Commits Made
- a1c789e FEATURE: AOM findings page, featured writing, new type system, decon refresh
- 36a5558 CHORE: CDS card mark — two overlapping answers
- 23e48e3 DOCS: Benchmark card — what the benchmark is, without the name
- 4b533b0 CHORE: Theme toggle to bottom right

## Issues Encountered
- Local main was 27 nightly contribution-graph commits behind origin; rebased with autostash before committing.
- LinkedIn activity feed exposes only the five most recent posts; the seven-platforms post URL was never found.
- Chrome and Playwright MCP both block file:// URLs; used a throwaway python http.server plus node Playwright for renders.
- `lsof` port check hung and silently prevented the first server start.

## Decisions Made
- Type: Fago + Fedra Mono over Officina+Meta+Operator (runner-up), Plex, Fago, House. Michael's brief: flourish and cohesion, not provenance.
- AOM: hub page, not a republish; articles-only in Featured writing; posts allowed on the subpage.
- PEARL: unnamed card only, no subpage until the medRxiv preprint.
- Featured writing: column flow (not row grid) to avoid ragged rows and orphans; reading times at 230 wpm.

## Next Steps
- Paste the seven-platforms LinkedIn post URL into `aom/index.html` (currently `#tools`).
- On preprint day, build `/pearl/` in the `/aom/` pattern.
- Consider a mark for the AOM card that isn't an ear if it wears thin; CDS mark is "two answers" by Michael's pick.
