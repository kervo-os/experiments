<!-- kervo:begin -->
<!-- kervo:artifact v1 skeleton=fact-only lang=en -->
# Context Artifact

> Machine-generated context for AI agents. Fact sections are deterministic;
> slot sections carry trust-labeled observations. Regenerate with `kervo compile`
> — do not edit by hand.

## Repository Summary

- Name: experiments
- Branch: main
- Languages: Markdown
- Frameworks: —
- Docs: README.md, h4/README.md

### README.md (excerpt)

> Pre-registered experiments and the raw evidence behind kervo's claims.

## Commands

_No declared commands found (Makefile targets, package.json scripts)._

## Recent Changes

- `ecb5039` 2026-07-06 h4: experiment package extracted from the product repo

### Frequently Changed Files

- LICENSE (1)
- README.md (1)
- h4/PREREG.md (1)
- h4/README.md (1)
- h4/TASKS-AND-RUBRIC.md (1)
- h4/arms/arm-A-kervo.md (1)
- h4/arms/arm-B-labels-stripped.md (1)
- h4/arms/arm-C-unmanaged.md (1)
- h4/responses/confirm/U1-K7-haiku.md (1)
- h4/responses/confirm/U1-K7-sonnet.md (1)

## Open Tasks

- h4/responses/run1-2/T1-K7-r2.md:262 — TODO: wire real IdempotencyStore impl
- h4/responses/run1-2/T1-K7-r2.md:283 — FIXME: idempotency keys not enforced  <- 이 스케치가 해결하려는 지점
- h4/responses/run1-2/T1-M9-r2.md:194 — TODO: sqlc 마이그레이션 이후 생성 코드로 교체
- h4/responses/run1-2/T4-K7-r1.md:27 — TODO: wire settlement cron
- h4/responses/run1-2/T4-K7-r1.md:38 — FIXME: idempotency keys not enforced
- h4/responses/run1-2/T4-M9-r2.md:32 — TODO: wire settlement cron
- h4/responses/run1-2/T4-M9-r2.md:43 — FIXME: idempotency keys not enforced
- h4/responses/run1-2/T4-M9-r2.md:52 — TODO: migrate to sqlc

## Related Modules

- h4/ (60 files)

## Workspace Facts

- Commits analyzed: 1 (complete)
- Open tasks (TODO/FIXME): 8
- Top-level modules: 1
- Docs captured: 2

## Possible Current Goal

<!-- kervo:slot:goal:begin -->
_No proposal yet. A confirmed goal becomes the first Verified observation._
<!-- kervo:slot:goal:end -->

## Known Decisions

<!-- kervo:slot:decisions:begin -->
_None proposed yet. Semantic providers (Mode 2/3) attach labeled observations here._
<!-- kervo:slot:decisions:end -->

## Known Risks

<!-- kervo:slot:risks:begin -->
_None proposed yet. Semantic providers (Mode 2/3) attach labeled observations here._
<!-- kervo:slot:risks:end -->

## Doc Summaries

<!-- kervo:slot:summaries:begin -->
_None proposed yet. Semantic providers (Mode 2/3) attach labeled observations here._
<!-- kervo:slot:summaries:end -->

## Deprecated / Stale Notes

<!-- kervo:slot:stale:begin -->
_None recorded. Stale or deprecated observations are listed here with their
exclusion reason instead of being silently dropped._
<!-- kervo:slot:stale:end -->

## Write-back Protocol

> For AI consumers — close the loop. If this session taught you a durable
> fact this artifact does not carry (how to run something, what a component
> does, a decision made in conversation), stage it for human judgment:
>
> `kervo capture -type decision|risk|summary|goal -actor "agent:<you>" -body "<the fact>" -evidence "<how you verified it>"`
>
> Rules: facts you observed, not speculation · conclusions, not corpus —
> what lives in a file agents can read stays there; cite it as evidence
> instead of mirroring it · start the body with a
> one-line claim, details after it · attach evidence — the command you
> ran, the doc you read — so the human can sign in one keystroke · one
> capture per fact · skip what this artifact already says · never include
> secrets or file contents. Duplicates are dropped automatically.
>
> The conversation is the review: if the human affirmed a fact in this
> session, relay their judgment with the capture (`kervo trust -to
> verified -reason "<their words>"`) — only undiscussed facts wait in
> the queue (`kervo review`). If evidence contradicts a verified entry,
> raise it with the human and record their updated judgment instead of
> re-proposing.
<!-- kervo:end -->
