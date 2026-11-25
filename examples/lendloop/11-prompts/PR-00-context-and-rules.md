# PR-00 · Context and rules

> Save this as the permanent rules file of the repository (`CLAUDE.md` or `AGENTS.md`).

## Product
LendLoop is a mobile app where neighbours lend tools and household items to each other inside neighbourhood groups. No payments, no deposits: trust between neighbours. Users are adults.

## Source documents and hierarchy
The analysis lives in `docs/analysis/`. When documents disagree, the higher one wins:
1. Brief → 2. **Master (source of truth)** → 3. Visual guidelines, Mock-ups → 4. Processes, Solution design → 5. Compliance → 6. Architecture → 7. Test plan.

## Glossary
Group, Item, Request, Loan, Owner, Borrower: see Master § 2. Owner and borrower are positions in a loan, not roles.

## IDs
Requirements use stable IDs: F (feature), R (rule), S (screen), P (process), E (entity), PAR (parameter), N (notification), NFR, LEG, ARC, T (test). Reference them in commit messages, code comments on business rules, and test names (`T-031 rejects loans longer than PAR-02`).

## Working rules
- **Do not invent business rules.** If something is missing or ambiguous, stop and list the question with the related IDs.
- Every value listed in Solution design § 3 is a **parameter** read from configuration, never hard-coded.
- Nothing is hard-deleted: use cancelled states and write every state change to the audit log.
- Respect the Visual guidelines tokens and components; do not add new colours or fonts.
- Disabled actions always show their reason.
- Personal data: never expose an exact address before a loan is accepted (LEG-02).

## Definition of done
- Acceptance criteria of the prompt met.
- Listed tests (T-) implemented and passing.
- No new lint or type errors; accessibility checks pass on new screens.
- Short report: what was done, IDs covered, deviations or open questions.
