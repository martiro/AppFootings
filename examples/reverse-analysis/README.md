# Worked example: reverse analysis of a project already under way

**FitSlot** is a fictional web app for booking classes at a small gym. It was built quickly: there is working code, a short README and a few tickets, but no organised analysis. The team wants to adopt AppFootings without starting over.

This example shows how the skill starts from what already exists.

## Starting point

```text
fitslot/
├── README.md                 # 20 lines: setup + "users can book classes"
├── docs/tickets.md           # 14 open tickets
├── app/                      # Next.js pages: /classes, /classes/[id], /my-bookings, /admin
├── lib/booking.ts            # booking rules
├── lib/stripe.ts             # memberships
├── supabase/migrations/      # 9 migrations (users, classes, bookings, waitlist, memberships)
└── tests/                    # 6 tests, booking only
```

## How the session starts

The reverse analysis needs read access to the repository, so it runs in a coding agent such as Claude Code, with the skill installed:

```text
This project is already under way but we never did a proper analysis.
Use AppFootings in reverse mode: analyse the code and the docs first.
```

## What AppFootings does

1. **Reconnaissance.** It reads the README, the tickets, the routes, the data migrations, the booking rules, the Stripe integration and the tests. It does not change any code.
2. **As-is model.** It reconstructs the features, roles, entities and states, rules and candidate parameters. Every item is tagged with its provenance (`[code]`, `[docs]`, `[code+docs]`, `[user]`) and a confidence level.
3. **Discrepancies and gaps.** It lists where the code and the documents disagree and what is missing, as findings AS-01 to AS-08.
4. **As-is report.** See [00-as-is-report.md](00-as-is-report.md).
5. **Phases with pre-filled drafts.** The user tells the story, which covers what the code cannot say: why the product exists, who it is for, the goals. Then the Brief comes out pre-filled. See [01-brief-prefilled.md](01-brief-prefilled.md). The other phases follow the same pattern.

## What changes at the end: change prompts

In reverse mode the implementation prompts describe **changes** to existing code. An excerpt:

```markdown
# PR-04 · Cancellation window (F-04, R-07, AS-01)

Current behaviour (as-is): cancellation is free until 12 h before the class,
hard-coded as CANCEL_WINDOW_HOURS = 12 in lib/booking.ts.
Target behaviour: free cancellation until PAR-03 hours before the class
(default 6 h, set by the gym admin). Later cancellations count as a no-show (R-08).
Areas likely affected: lib/booking.ts, app/my-bookings, settings table (new).
Regression tests that must keep passing: tests/booking.test.ts (all 6).
New tests: T-041 boundary at PAR-03, T-042 late cancellation counted as no-show.
```
