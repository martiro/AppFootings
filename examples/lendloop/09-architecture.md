# LendLoop: Architecture

| Version | Date | Status | Purpose |
|---|---|---|---|
| 1.0 | 2026-11-25 | validated | Technical architecture and decisions |

## 1. Drivers
NFR-01 to NFR-04, LEG-02 (location privacy), EU data residency (GDPR), a two-person team, low running costs.

## 2. Stack
| Layer | Choice | Why |
|---|---|---|
| Mobile app | React Native (Expo), TypeScript | One code base for iOS and Android; small team |
| Backend | Node.js (TypeScript), REST + WebSocket | Shared language with the app |
| Database | PostgreSQL with PostGIS | Relational states plus distance queries |
| Files | S3-compatible object storage, EU region | Item photos |
| Push | Pluggable provider (INT-01), default FCM/APNs | ARC-03 |
| Hosting | Managed containers, EU region | Low ops effort |

## 3–4. Modules and interactions

```mermaid
flowchart LR
    App[Mobile app] -->|REST| API[API gateway]
    App <-->|WebSocket| RT[Realtime service]
    API --> ID[Identity & groups]
    API --> CAT[Catalogue]
    API --> LOAN[Borrowing & loans]
    API --> CHAT[Chat]
    LOAN --> EV[(Event bus)]
    EV --> NOTIF[Notifications]
    EV --> AUDIT[Audit log]
    EV --> RT
    NOTIF --> PUSH[Push provider INT-01]
    CAT --> FILES[(Object storage)]
    ID & CAT & LOAN & CHAT --> DB[(PostgreSQL + PostGIS)]
    CFG[Parameters & flags] --> LOAN & CAT & NOTIF
```

### Key sequence: P-03 Borrow an item

```mermaid
sequenceDiagram
    participant B as Borrower app
    participant L as Borrowing & loans
    participant N as Notifications
    participant O as Owner app
    B->>L: POST /requests (item, dates)
    L->>L: check R-05, R-06, R-08, R-09
    L-->>B: 201 Pending
    L->>N: RequestCreated
    N->>O: push N-03
    O->>L: POST /requests/{id}/accept
    L->>L: create Loan (Approved), decline overlaps
    L->>N: RequestAccepted
    N->>B: chat message + push N-04
    Note over L: scheduler expires Pending after PAR-03 (R-07)
```

## 7. Parameters and flags
A configuration table with per-group overrides, cached for 60 s. Every change is written to the audit log.

## 8. Deployment
Staging and production in an EU region. CI runs the test plan on every pull request. Mobile releases go through EAS builds, with over-the-air updates for non-native changes.

## 12. Decisions
| ID | Decision | Consequence |
|---|---|---|
| ARC-01 | Monolith with modules, not microservices | Simple to run; modules can be split later |
| ARC-02 | Request expiry handled by a scheduler, not by client timers | R-07 is enforced even when no app is open |
| ARC-03 | Push behind an interface | Provider can change without touching business logic |
