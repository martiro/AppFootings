# LendLoop: Master (functional specification)

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | validated | Functional specification and source of truth |

> Source of truth. Every decision is written here first and then cascaded to the other documents.
> *Example excerpt: F-03 is complete; the other features are summarised.*

## 1. Purpose and scope
See [Brief](01-brief.md). The first release covers neighbourhood groups, item catalogue, borrowing, loan lifecycle, chat and notifications.

## 2. Glossary
| Term | Meaning |
|---|---|
| Group | A neighbourhood community. Members only see items of their own groups |
| Item | Something a member makes available for lending |
| Request | A borrower's proposal to borrow an item for given dates |
| Loan | An accepted request, from pick-up to return |
| Owner / Borrower | Positions of a member in a loan. They are not separate roles |

## 3. Roles
| ID | Role | Summary |
|---|---|---|
| ROLE-MB | Member | Lends and borrows inside their groups |
| ROLE-GA | Group admin | Member who also manages invitations, group rules and reported content |
| ROLE-PA | Platform admin | Handles platform parameters and escalated reports |

Full matrix in [Solution design › Permissions](06-solution-design.md#2-roles-and-permissions).

## 4. Feature list
| ID | Feature | Screens | Processes |
|---|---|---|---|
| F-01 | Account and profile | S-01, S-11 | — |
| F-02 | Neighbourhood groups | S-10 | P-01 |
| F-03 | **Borrow an item** | S-02, S-04, S-05, S-07, S-08 | P-03 |
| F-04 | Lend an item (catalogue) | S-03, S-04 | P-02 |
| F-05 | Loan lifecycle | S-06, S-08 | P-04, P-05 |
| F-06 | Chat | S-09 | P-03 (step 4) |
| F-07 | Notifications | — | all |
| F-08 | Group rules | S-10 | P-06 |
| F-09 | Reliability record | S-07, S-11 | P-04 |

## 5. Features

### F-01 Account and profile (summary)
Sign-up by email or phone, name, photo, approximate address used only to compute distances. Account deletion blocked while the user has an active loan (R-02).

### F-02 Neighbourhood groups (summary)
A member can belong to several groups. Joining is by invitation from any member, confirmed by a group admin (R-03).

### F-03 Borrow an item

**Description.** A member finds an available item in their groups, chooses the dates and sends a request to the owner. The owner accepts, declines or suggests other dates. When a request is accepted, a loan is created and a private chat between the two opens with the confirmation.

**Rules**
- **R-05** A loan lasts at most the group's maximum duration (PAR-02, default 3 days). If the item's owner belongs to several shared groups, the highest maximum applies.
- **R-06** Days on which the item is already on loan or reserved cannot be selected.
- **R-07** The owner has PAR-03 (default 48 h) to answer. After that the request expires automatically, with no penalty for anyone.
- **R-08** A borrower can have at most one pending request per item. They can cancel it until the owner answers.
- **R-09** A member with an overdue loan cannot send new requests until the item is returned. The reason is shown on the button.

**Edge cases**
- The owner withdraws the item while a request is pending → the request is cancelled and the borrower is notified (N-05).
- Two requests for overlapping dates → both stay pending; accepting one automatically declines the other with the message "dates no longer available".
- The owner suggests other dates → the borrower accepts, which creates the loan, or cancels.

**Defaults:** PAR-02 = 3 days, PAR-03 = 48 h.

**Links:** S-02, S-04, S-05, S-07, S-08 · P-03 · E-03, E-04 · N-03, N-04, N-05

### F-04 to F-09 (summary)
- **F-04** Items have photo (optional, category icon if missing), category, description and lending notes.
- **F-05** Loan states and reminders: see E-04. The owner confirms the return.
- **F-06** Private chat between two members. Writing to a member you have no loan with requires an accepted chat invitation.
- **F-07** Notifications: see N-01 to N-07.
- **F-08** Group rules: maximum loan duration, who can invite. Every rule has a default.
- **F-09** Reliability record: number of loans returned on time, visible to group members. No star ratings.

## 6. Cross-cutting rules
- **History:** nothing is deleted. Requests and loans are cancelled and stay in the history, with who did what and when.
- **Privacy:** only the approximate distance is shown, never the address, until a loan is accepted.

## 7. Future evolutions
- Loan extension (placeholder).
- Waiting list for busy items (placeholder).

## 8. Open points
| ID | Question | Status |
|---|---|---|
| OP-03 | Can a group admin remove an item? | Resolved → F-08, R-12 |
| OP-05 | What happens to requests from members with overdue loans? | Resolved → R-09 |
| OP-08 | Should borrowers see the owner's reliability record before requesting? | Open, not blocking |
| OP-11 | Pick-up reminders: one or two? | Open, not blocking |

## Appendix: traceability (row for F-03)
| Feature | Rules | Screens | Processes | Parameters | Phase | Tests | Prompt |
|---|---|---|---|---|---|---|---|
| F-03 | R-05 to R-09 | S-02, S-04, S-05, S-07, S-08 | P-03 | PAR-02, PAR-03 | 1 | T-030 to T-039 | PR-05 |
