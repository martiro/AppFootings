# LendLoop: Compliance

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | draft | Preliminary legal risk analysis |

> Preliminary risk analysis. **Not legal advice**: have it validated by a qualified professional before launch.

## Applicability
| Area | Applies | Why |
|---|---|---|
| GDPR | yes | Personal data, approximate location, messages |
| AI Act | no | No AI features in the first release |
| ePrivacy | yes | Push notifications, analytics |
| DSA | yes, light | Users publish item photos and descriptions (hosting) |
| Accessibility Act | check | Depends on the service classification; WCAG 2.1 AA adopted anyway |
| Consumer protection | no | Free, no transactions |
| Payments | no | No money moves between users |
| App stores | yes | Account deletion inside the app is required |
| Minors | yes | Service restricted to 18+ |

## Requirements
| ID | Requirement | Impact |
|---|---|---|
| LEG-01 | Legal basis and privacy notice for profile, location, chat | S-01 consent screen |
| LEG-02 | Location stored as approximate area; exact address only shared with a counterpart after a loan is accepted | Master › Cross-cutting rules, E-01 |
| LEG-03 | Data export and deletion on request | F-01, S-11 |
| LEG-04 | Notice and action: report an item or message; group admin then platform admin | F-08, S-04 menu |
| LEG-05 | Age confirmation (18+) at sign-up | S-01 |
| LEG-06 | Account deletion available inside the app | S-11 (R-02: blocked during active loans, with explanation) |
| LEG-07 | Liability for damaged items: disclaimer in the terms | Open question for legal review |

## Open questions for a professional
- LEG-07 liability wording.
- Whether the Accessibility Act applies to a free community service.
