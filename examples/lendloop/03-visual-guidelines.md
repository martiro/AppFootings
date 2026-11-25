# LendLoop: Visual guidelines

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | validated | Visual language for mock-ups and product |

## 1. Principles and tone
- **Neighbourly**: warm, plain words; "Ask Giulia", not "Contact owner".
- **Calm**: one primary action per screen.
- **Honest**: always say why something is disabled.
- Tone of voice: friendly, short, no exclamation marks in errors.

## 2. References and base
References chosen by the team: a neighbourhood social app (lists), a booking app (date picking), a messaging app (chat). Base system: **Material Design 3**, customised with the tokens below.

## 3. Colour
| Token | Value | Use |
|---|---|---|
| `primary` | `#0E8C8C` | Primary buttons, links |
| `ink` | `#1B2430` | Text |
| `muted` | `#6B7785` | Secondary text |
| `surface` | `#F5F7FA` | Background |
| `success` | `#2E9E6A` | Available, confirmed |
| `danger` | `#D64545` | Unavailable, overdue |
| `warning` | `#E8A33D` | Time limits, pending |

All text and background pairs meet WCAG 2.1 AA contrast.

## 4–6. Typography, spacing, iconography
Inter: 22/700 titles, 15/600 buttons, 13–14/400 body. 8-pt spacing grid, 12–16 px radius. Line icons; when an item has no photo, its category icon is shown.

## 7. Core components and states
Primary button, secondary button, status chips (Available, Max *n* days, Pending, Overdue), item card, availability strip, date pickers, info box (warning tone for "what happens next"), empty state with illustration.

## 8. Motion and feedback
A short highlight on values that changed in real time, such as a new request or a status change.

## 9. Copy
Disabled buttons show the reason underneath. Confirmations say what happens next.

## 10. Accessibility
Touch targets of at least 44 px, Dynamic Type support, and colour never used alone (chips always carry text).
