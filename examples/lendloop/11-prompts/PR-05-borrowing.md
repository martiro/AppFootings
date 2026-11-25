# PR-05 · Borrowing (F-03)

## 1. Objective
Let a member request an item from their groups, and let the owner accept, decline or suggest other dates, up to the creation of the loan.

## 2. Scope
- **In:** F-03, the request part of P-03, and the creation of the Loan in state *Approved*.
- **Out:** pick-up and return (PR-06, P-04); the chat itself (PR-06). This prompt only posts the confirmation message through the chat module's interface.

## 3. Entities and states
- **E-03 Request**: Pending, Proposed, Approved, Declined, Expired, Cancelled.
- **E-04 Loan**: creation in *Approved* only.

Transitions are listed in Solution design § 1. Reject any other transition.

## 4. Rules (quoted from the Master)
- **R-05** A loan lasts at most the group's maximum duration (PAR-02, default 3 days). If owner and borrower share several groups, the highest maximum applies.
- **R-06** Days on which the item is already on loan or reserved cannot be selected.
- **R-07** The owner has PAR-03 (default 48 h) to answer. After that the request expires automatically, with no penalty.
- **R-08** At most one pending request per item per borrower; the borrower can cancel it until the owner answers.
- **R-09** A member with an overdue loan cannot send new requests; the reason is shown.
- Edge cases: an item withdrawn while requests are pending → those requests are cancelled and N-05 is sent. Accepting one request automatically declines overlapping ones ("dates no longer available").

## 5. Screens
Build S-04 (request part), S-05 and S-07, plus the confirmation state of S-08, as drawn in `docs/analysis/04-mockups.md` and the P-03 screen sequence. Use only Visual guidelines components: status chips, availability strip, warning info box.

## 6. Process
P-03 steps 1–4 and variants 2a, 3a, 3b, 3c.

## 7. Permissions, notifications, parameters, audit
- Permissions: Solution design § 2. The requester must share a group with the owner and must not have an overdue loan.
- Notifications: N-03 (owner, cannot be disabled), N-04 (posted in the private chat + push), N-05 (borrower).
- Parameters: PAR-02, PAR-03, read from configuration.
- Audit: log every Request transition and the Loan creation.

## 8. Integrations
Push through the notifications module (INT-01 behind its interface). Expiry runs in a server-side scheduler (ARC-02).

## 9. Compliance
LEG-02: S-04, S-05 and S-07 show distance only; the exact address appears only on S-08.

## 10. NFRs
NFR-02: N-03 is delivered in under 30 s (p95).

## 11. Acceptance criteria
- A member can request free dates up to PAR-02, and the owner receives N-03.
- Accept, decline, suggest dates and expiry produce the states and notifications above.
- R-06, R-08 and R-09 are enforced both in the UI and in the API.
- Changing PAR-02 or PAR-03 in configuration changes the behaviour without a release.

## 12. Tests to pass
T-030 to T-039 (`docs/analysis/10-test-plan.md`).

## 13. Constraints
- Do not implement payments, deposits or ratings.
- Do not add states or rules that are not in the Master; raise a question instead.

## 14. Report back
List what was built, the IDs covered, any deviation, and any open question with its related IDs.
