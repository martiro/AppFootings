# LendLoop: Test plan

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | validated | Tests derived from the analysis |

> *Example excerpt: the tests derived for F-03 / P-03.*

## Strategy
Unit tests for rules and state transitions, integration tests on the API, end-to-end tests on the main processes, load tests against NFR-04, and accessibility checks against WCAG 2.1 AA.

## Test cases (F-03)
| ID | Source | Derived by rule | Steps | Expected |
|---|---|---|---|---|
| T-030 | P-03 | process → happy path | Borrower requests free dates; owner accepts | Request *Approved*, Loan *Approved*, N-03 to owner, N-04 in chat |
| T-031 | R-05, PAR-02 | parameter → boundary | Request 3 days, then 4 days (default 3) | 3 accepted; 4 rejected with message |
| T-032 | R-06 | rule → negative | Select a day already on loan | Day not selectable |
| T-033 | R-09 | rule → negative | Member with an overdue loan opens S-04 | Button disabled, reason shown; API rejects the request |
| T-034 | P-03 › 3a | variant | Owner declines | Request *Declined*, N-05 to borrower |
| T-035 | P-03 › 3b, R-07, PAR-03 | variant + parameter | No answer for 48 h | Request *Expired*, N-05, no penalty |
| T-036 | P-03 › 3c | variant | Owner suggests dates, borrower accepts | Request *Proposed* → *Approved*, loan created |
| T-037 | Permissions | matrix → denied | Non-member calls POST /requests | 403 |
| T-038 | N-03 | notification | New request | Only the owner is notified; cannot be disabled |
| T-039 | Audit | audit | Each transition in T-030 | Audit record with actor, time, before/after |

## Coverage (F-03)
| Requirement | Tests |
|---|---|
| R-05 | T-031 |
| R-06 | T-032 |
| R-07 | T-035 |
| R-08 | covered in the F-03 extended set (not shown) |
| R-09 | T-033 |
| P-03 | T-030, T-034, T-035, T-036 |
| N-03 / N-04 / N-05 | T-038, T-030, T-034 |
