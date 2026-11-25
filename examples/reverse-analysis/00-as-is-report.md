# FitSlot: As-is report

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | draft, to be confirmed | Reconstruct what the existing code and documents say, as the starting point of the analysis |

Provenance: `[code]` found in code · `[docs]` found in README or tickets · `[code+docs]` both agree · `[user]` confirmed by the user.
Confidence: H high · M medium · L low. Nothing tagged `[code]` or `[docs]` is decided until the user confirms it.

## 1. Summary
FitSlot lets gym members see the weekly class timetable, book a place, cancel a booking and pay a monthly membership. A staff area manages classes. Booking works end to end. The waiting list was started but never finished. Several rules exist only in the code, and two of them contradict the tickets.

## 2. Sources analysed
README.md, docs/tickets.md (14 tickets), 4 route groups in `app/`, `lib/booking.ts`, `lib/stripe.ts`, 9 migrations, 6 tests. The app was run locally and screenshots were taken of 7 screens.

## 3. Stack
Next.js (web, responsive), Supabase (Postgres + auth), Stripe Checkout for memberships, transactional email via a third-party SMTP service. Hosting not documented.

## 4. Inventory

### Features
| ID (proposed) | Feature | Provenance | Conf. |
|---|---|---|---|
| F-01 | Sign-up and login (email + magic link) | `[code]` | H |
| F-02 | Weekly timetable | `[code+docs]` | H |
| F-03 | Book a class | `[code+docs]` | H |
| F-04 | Cancel a booking | `[code+docs]` | H |
| F-05 | Membership payment | `[code]` | H |
| F-06 | Waiting list | `[code]` (table only) · `[docs]` ticket #9 | L |
| F-07 | Staff: manage classes | `[code]` | M |

### Roles
| Role | Provenance | Note |
|---|---|---|
| Member | `[code]` | default role |
| Staff | `[code]` | `is_staff` flag; checks only in the UI (AS-05) |

### Entities and states
| Entity | States found | Provenance |
|---|---|---|
| Booking | booked → cancelled · booked → attended | `[code]` |
| Membership | active → past_due → cancelled | `[code]`, from Stripe events |
| Waitlist entry | (no states, table only) | `[code]` |

### Rules
| Rule | Provenance | Conf. |
|---|---|---|
| A member needs an active membership to book | `[code]` | H |
| Max 1 booking per class per member | `[code]` | H |
| Free cancellation until 12 h before the class | `[code]` (ticket #4 says 2 h) | M (AS-01) |
| Max 3 future bookings per member | `[code]` | H |

### Candidate parameters (hard-coded values)
| Value | Where | Proposed |
|---|---|---|
| `CANCEL_WINDOW_HOURS = 12` | lib/booking.ts | PAR-03, set by gym admin |
| `MAX_FUTURE_BOOKINGS = 3` | lib/booking.ts | PAR-04, set by gym admin |
| `DEFAULT_CAPACITY = 20` | migration 004 | PAR-05, per class |

### Screens
`/classes` (timetable), `/classes/[id]` (class detail + book), `/my-bookings`, `/login`, `/membership`, `/admin/classes`, `/admin/classes/[id]`. Navigation map in the screenshots appendix.

### Integrations
Stripe Checkout and webhooks `[code]`; SMTP email `[code]`.

## 5. Screen map
Timetable → Class detail → Book → My bookings → Cancel. Login and Membership are reached from a banner when a member without a membership tries to book. Admin is a separate area.

## 6. Discrepancies and gaps
| ID | Finding | Type | Proposed handling |
|---|---|---|---|
| AS-01 | Tickets say free cancellation until 2 h before; the code allows it until 12 h | code vs docs | Open point: which value? Make it a parameter |
| AS-02 | Waiting list table exists, no UI and no logic | unfinished feature | Decide: finish, defer or remove |
| AS-03 | Class capacity hard-coded at 20 by default | hard-coded value | Parameter per class |
| AS-04 | Staff cancellations of member bookings are not logged | missing audit | Add audit (who, when, why) |
| AS-05 | Staff permissions checked only in the UI, not in the API | security | High priority: enforce server-side |
| AS-06 | Personal data sent to an SMTP provider; no processor listed in the privacy notice | compliance | GDPR: list processor, check DPA |
| AS-07 | Ticket #11 mentions a no-show penalty; nothing in code | missing rule | Open point |
| AS-08 | Dates shown in three different formats across screens | UX consistency | Visual guidelines |

## 7. Risks
AS-05 (privilege escalation through the API) and AS-06 (GDPR) should be addressed before any new feature.

## 8. Proposed level and triggers
**Standard.** Triggers: personal data → full GDPR; payments → audit and security tests (Stripe holds the money); several roles → permissions matrix and Processes.

## 9. Questions for the user
1. Why was FitSlot built, and for which gyms? One gym or many?
2. Which cancellation window is right: 2 h, 12 h, or something configurable (AS-01)?
3. Is the waiting list still wanted (AS-02)?
4. Should no-shows have consequences (AS-07)?
5. Is a mobile app expected, or is the responsive web app enough?
