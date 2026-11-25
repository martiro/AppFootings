# Worked example: LendLoop

**LendLoop** is a fictional app where neighbours lend tools and household items to each other. It shows what an AppFootings analysis looks like at the **Standard** level.

The documents are deliberately shortened: each one shows its full structure, with one or two sections complete and the rest summarised. All IDs are consistent across documents, so you can follow a single feature, **F-03 Borrow an item**, from the Brief down to the implementation prompt.

## Documents

| # | Document | What to look at |
|---|---|---|
| 0 | [Project register](00-project-register.md) | Level, triggers, document status, copies table |
| 1 | [Brief](01-brief.md) | How the problem story becomes a structured brief |
| 2 | [Master](02-master.md) | Feature list, the full F-03 section, open points, traceability row |
| 3 | [Visual guidelines](03-visual-guidelines.md) | Base system, tokens, components |
| 4 | [Mock-ups](04-mockups.md) | Screen index and the full S-02, S-04 and S-06 sections |
| 5 | [Processes](05-processes.md) | Process index and the full P-03 section with screen sequence |
| 5b | [Navigable prototype](prototype/index.html) | P-03 playable as a clickable preview of the app (download and open in a browser) |
| 6 | [Solution design](06-solution-design.md) | States, permissions, parameters, notifications, NFRs |
| 7 | [Compliance](07-compliance.md) | GDPR, DSA, minors, app stores |
| 8 | [Roadmap](08-roadmap.md) | Light roadmap (Standard level: no business model) |
| 9 | [Architecture](09-architecture.md) | Stack, modules, diagrams |
| 10 | [Test plan](10-test-plan.md) | Tests derived from P-03 and its rules |
| 11 | [Implementation prompts](11-prompts/) | PR-00 context and rules, PR-05 Borrowing |

## Follow one feature end to end

| Step | Where F-03 appears |
|---|---|
| Scenario | Brief › scenario 1 |
| Rules | Master › F-03 › R-05, R-06, R-07, R-08, R-09 |
| Screens | Mock-ups › S-02, S-04, S-05, S-07, S-08 |
| Preview | Navigable prototype › P-03 |
| Process | Processes › P-03 |
| States | Solution design › E-03 Request, E-04 Loan |
| Parameters | Solution design › PAR-02, PAR-03 |
| Notifications | Solution design › N-03, N-04, N-05 |
| Tests | Test plan › T-030 to T-039 |
| Build | Prompts › PR-05 Borrowing |

## A change, end to end

The [analysis loop animation](../../docs/images/analysis-loop.gif) and the [alignment report image](../../docs/images/example-alignment-report.png) show a hypothetical **future** change: the maximum loan becomes 5 days and can be extended once. In the animation, the coherence check finds a conflict with R-06 (OP-12), and updating P-03 reveals a missing notification (OP-13). Both are decided in the Master before the cascade completes. The change is not applied to these documents.
