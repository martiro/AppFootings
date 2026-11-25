# FitSlot: Brief (pre-filled from the As-is report)

| Version | Date | Status | Purpose |
|---|---|---|---|
| 0.9 | 2026-11-25 | draft | Shared understanding of the problem, users and goals |

> Sections marked `[user]` come from the user's story. The others come from the [As-is report](00-as-is-report.md) and were confirmed by the user, unless marked *to confirm*.

## 1. Problem statement `[user]`
Small gyms take class bookings through phone calls and chat messages. Classes overflow or run half empty, and staff spend hours a week managing bookings by hand.

## 2. Users and primary target
- Members: book and cancel classes `[code+docs]`.
- Staff: manage classes and attendance `[code]`.
- **Primary target:** owners of single-location gyms with 100–500 members `[user]`.

## 3. Usage scenarios
1. A member books tomorrow's spinning class from the phone in under 30 seconds `[code+docs]`.
2. A member cancels in time and the place goes to the waiting list `[user]`. **Change vs as-is:** the waiting list is not implemented (AS-02).
3. Staff create next month's timetable in one go `[user]`. **Change vs as-is:** classes are created one by one today.

## 4. Current alternatives and gaps
General booking platforms charge per booking and are designed for chains `[user]`, with comparable products listed from domain research. Paper and chat do not scale `[user]`.

## 5. Goals and success criteria `[user]`
- Average class fill rate above 80%.
- Staff time on bookings under 1 hour a week.

## 6. Constraints and assumptions
Responsive web app, no native app for now `[user]`. Existing stack kept (Next.js, Supabase, Stripe) `[code]`, confirmed.

## 7. Business intent `[user]`
Sold to gyms as a monthly subscription. *To confirm:* one gym per installation or a multi-gym platform (multi-tenancy trigger).

## 8. Out of scope
Personal training sessions, nutrition plans `[user]`.

## 9. Level
**Standard**, confirmed. Triggers: personal data, payments, several roles; multi-tenancy *to confirm*.
