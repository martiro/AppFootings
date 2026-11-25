# LendLoop: Brief

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | validated | Shared understanding of the problem, users and goals |

## 1. Problem statement
Most households own tools they use a few times a year: a drill, a ladder, a pressure washer. Neighbours buy the same items again, or borrow them through chat groups where requests get lost, nobody knows who has what, and nobody remembers who still has the ladder.

## 2. Users and primary target
- **Members**: neighbours who lend and borrow. The same person is a lender for some items and a borrower for others.
- **Group admins**: the people who start a neighbourhood group and set its rules.
- **Primary target**: neighbours who already lend informally through chat groups. They feel the problem today and bring their neighbours with them.

## 3. Usage scenarios
1. **Borrow**: Marco needs a drill for the weekend, finds one 400 m away, requests it, picks it up and returns it.
2. **Lend**: Giulia adds her drill and ladder, accepts or declines requests, and always knows where her items are.
3. **Run a group**: an admin creates the group for their building, invites neighbours and sets the maximum loan duration.

## 4. Current alternatives and gaps
| Alternative | Gap |
|---|---|
| Neighbourhood chat groups | No catalogue, requests lost in the flow, no record of who has what |
| General sharing apps | Built for strangers and rentals, with payments and deposits; too heavy for neighbours |
| Spreadsheets | Nobody updates them |

## 5. Goals and success criteria
- A borrower finds an available item and sends a request in under a minute.
- Owners always know where their items are and when they come back.
- 80% of loans are returned on time.
- A group is set up in under 5 minutes, with every rule already at a sensible default.

## 6. Constraints and assumptions
- Mobile first; built by a team of two developers.
- Trust between neighbours: no deposits, no payments.
- Users are adults (18+).

## 7. Business intent
Free for the first release. Possible later: sponsored local shops, paid features for large residential complexes. Not designed yet (see [Roadmap](08-roadmap.md)).

## 8. Out of scope
Payments and deposits, rentals between strangers, delivery, insurance.

## 9. Proposed level
**Standard**. Rationale and triggers in the [Project register](00-project-register.md).
