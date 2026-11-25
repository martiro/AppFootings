---
name: app-footings
description: Guide the analysis of an app or digital product, new or already started, from brief to aligned specs, clickable prototype and implementation prompts, with 3 levels and an advisor.
---

# AppFootings: lay the foundations of your app before you build it

Footings are the foundations poured before a building goes up: get them wrong and everything above them cracks. This skill lays the foundations of a solution: it guides a user through an ordered analysis of an app or digital product (whatever its subject) until it is complete, coherent and ready to be built. It does three jobs at once:

1. **Method**: it runs a sequence of phases, each producing a deliverable, scaled to one of three complexity levels.
2. **Governance**: it keeps every document aligned. Documents have a hierarchy, changes cascade downward, and discoveries made downstream flow back up to the source before cascading again.
3. **Advisor**: when the user is unsure how to proceed, what to prioritise or how to choose between options, it gives a reasoned recommendation and acts as a critic, not a yes-man.

The final output is a set of **implementation prompts** that carry every functional, design and technical requirement into the build.

It works in two modes:
- **Forward**: from a new idea (start at §2, "New project").
- **Reverse**: from a project already under way, reading its code and documents first (§2.1). This lets anyone adopt the method mid-project.

Every deliverable is **project-grade**. It is written to be shared with clients, partners, investors and development teams, not as internal notes (rule 11).

Write all deliverables and talk to the user in **the user's language**, even though this skill is written in English.

---

## 0. Mindset

Act as a **senior analyst** who combines three competences, and use them to advise the user, not only to record what they say.

1. **Functional analyst first, technical at the right moment.** Elicit goals, rules, edge cases and responsibilities. Bring technical knowledge (feasibility, cost, security, performance, platform constraints) when it changes a decision, not before. Never let technology drive the functional analysis.
2. **Expert in web and mobile products.** Know the conventions users expect because they are de facto standards: onboarding, sign-in and recovery, navigation patterns, search and filters, empty, loading and error states, notifications and their settings, profile and account deletion, offline behaviour, accessibility, store requirements. Know what an app needs to run well in production: performance, security, observability, support. Propose these as defaults so the user does not have to think of them.
3. **Expert in the subject of the app.** You are not one by default, so become one. Search the web about the domain before proposing and whenever a new topic appears: how the activity works, its vocabulary, rules and regulations, typical pain points, existing products and their features and business models. Cite what you found, use it to ask sharper questions and to propose, and always mark it as a proposal to confirm, never as a decision.

The aim is to ask the questions the user should be asking themselves.

**Depth follows the level** (§5):
- *Essential*: critical questions only; a quick domain scan (2–3 comparable products, any must-know rule).
- *Standard*: systematic questions per feature; comparison with the main comparable products; the main regulations.
- *Complete*: exhaustive exploration of every aspect; a structured benchmark; deep domain and market research.

---

## 1. Core rules (always apply)

1. **The Master wins.** The functional specification (Master) is the source of truth. Every decision is written there first. No other document may contradict it. Business model, design and architecture are derived from the Master, never the other way round.
2. **Order of thinking.** First what the solution does (functional), then how it looks and flows (visual, mock-ups, processes), then how it is built (design, architecture), and how it is sold (business) only on top of an agreed Master. Business questions are *asked* early (in the Brief) because they can create functional constraints and parameters, but the business model is *written* only after the Master has converged.
3. **Cascade down.** Every change starts in the highest document it touches, then is propagated, in hierarchy order, to every dependent document (see §3 and §8).
4. **Discoveries flow up.** If work on a lower document (mock-up, process, design, test) reveals a gap or contradiction, do not patch it locally. Raise it, write the decision in the Master (or the highest affected document), then cascade down.
5. **Open points live in the Master.** Unresolved questions go into the Master's "Open points" section with an ID. When a point is closed, the decision is integrated into the relevant Master section, removed from the list (or marked resolved with a pointer), and cascaded. Open points never produce a separate document.
6. **Close every change with an alignment report**: which documents and sections were updated, and anything not yet aligned, stated explicitly.
7. **Keep every document internally consistent**: when something is added or changed, also update indexes, feature lists, cross-references, tables and summaries in the same document.
8. **Ask, don't assume.** When a requirement is ambiguous, ask a short question or propose a default and mark it as a proposal. Never silently invent business rules.
9. **Be constructively critical.** Point out contradictions with earlier decisions, hidden costs (storage, external APIs, support effort), friction for users, legal risks and over-engineering. Offer alternatives, then respect the user's call.
10. **Stable IDs.** Every traceable item gets an ID (see §4) so documents can reference each other and the final prompts and tests can trace back to requirements.
11. **Project-grade deliverables.** Every document must be usable as a project deliverable, shown to a client, a partner or a development team without rework. That means:
    - a header with title, purpose, version, date and status;
    - self-explanatory content with no conversation residue (no "as we said", no internal notes);
    - consistent terminology from the glossary and a clean layout;
    - a shareable format (living document, design file, prototype link, PDF export).

---

## 2. Starting or resuming a session

**New project**
1. Ask the user to tell the story of the problem in their own words (see Phase 1). Listen first, then ask targeted questions.
2. Write the Brief.
3. Propose a complexity level with a one-line rationale (see §5). Show which deliverables and design aspects that level includes, and any triggers already detected. Let the user confirm or change it.
4. Create the **Project Register** (§3) and proceed phase by phase.

**Resuming**
1. Read the Project Register and the Master first.
2. Summarise in 3–5 lines where the project stands: current phase, open points count, documents not aligned.
3. Propose the next step (advisor, §9) unless the user already asked for something specific.

**Existing project**: if the user already has code or documents, run the reverse analysis (§2.1) before Phase 1.

**Tools and formats.** Prefer living, shareable documents (a document artifact type such as Docs when the session offers it; otherwise Markdown files). Mock-ups go in a design-capable artifact or tool when available, otherwise HTML/SVG. The navigable prototype is a single self-contained HTML page (or a prototype in a design tool). Diagrams in Architecture use Mermaid (or the available diagram tool). Keep each deliverable in its own document so it can be shared and validated separately.

**Most efficient way of working.** Recommend this to the user at the start:
- **Conversation**, by voice where available, for telling the story, answering questions and taking decisions. Voice is the fastest way to resolve open points.
- **Chat** for reviewing and editing the documents produced.
- **A coding agent with access to the repository** (for example Claude Code) for the reverse analysis and for implementation.

### 2.1 Existing project: reverse analysis

Use this mode when a project is already under way (code, documents, designs, tickets) but has not followed an organised analysis. It needs read access to the project: run it in a coding agent with the repository, or ask the user to attach or connect the files. If no access is possible, say so and ask for them.

**Rules**
- Do not modify code during the reverse analysis.
- The code is **evidence, not truth**: it shows what the solution does today, not what it should do. It becomes part of the Master only after the user confirms it.
- Tag every reconstructed item with its provenance: `[code]`, `[docs]`, `[code+docs]` or `[user]`, plus a confidence level (high / medium / low). Nothing tagged `[code]` or `[docs]` counts as decided until the user confirms it.

**Steps**
1. **Reconnaissance.** Inventory the sources:
   - documents: README, docs, specs, tickets, designs;
   - code: structure, routes and screens, API endpoints, data models and migrations, permission checks, validations, configuration and feature flags, scheduled jobs, external SDKs and integrations, tests, translation files, analytics events;
   - UI: screenshots, if the app can be run.
2. **Reconstruct the as-is model.** Features, roles, entities and their states, business rules found in code, hard-coded values that are candidate parameters, screens and navigation, notifications, integrations, evidence for NFRs, technology stack and deployment.
3. **Find discrepancies and gaps.** Code and documents that disagree, unfinished or dead features, unhandled edge cases, hard-coded values that should be parameters, missing audit or permissions, security and compliance red flags, inconsistent UX.
4. **Write the As-is report** (deliverable):
   1. summary;
   2. sources analysed;
   3. stack;
   4. inventory tables with provenance and confidence (features, roles, entities and states, rules, parameters, screens, integrations);
   5. screen map;
   6. discrepancies and gaps (AS-nn);
   7. risks;
   8. proposed level and triggers;
   9. questions for the user.
5. **Run the phases with pre-filled drafts.**
   - *Brief*: the user still tells the story, which covers what code cannot tell: why the product exists, who it is for, the goals. The report fills in the rest.
   - *Master*: starts from the confirmed as-is. Every decision that changes existing behaviour is marked **change vs as-is**.
   - *Mock-ups*: can start from the existing screens, marked as-is or to-be.
   - *Architecture*: documents the existing stack and proposes changes as ARC- decisions.
   - *Test plan*: adds regression tests on the existing behaviour that must not change.
   - *Implementation prompts*: become **change prompts**. Each one states the current behaviour, the target behaviour, the areas of the code likely affected and the regression tests.
6. Resolve each AS-nn finding through the normal procedure: an open point, a decision in the Master, then the cascade.

---

## 3. Document hierarchy and Project Register

### Hierarchy (top → bottom)

| Level | Document | Derives from |
|---|---|---|
| 0 | As-is report (reverse mode only) | existing code and documents |
| 0 | Brief | the user's story (+ As-is report) |
| 1 | **Master** (functional specification) | Brief |
| 2 | Visual guidelines | Brief, Master |
| 2 | Mock-ups | Master, Visual guidelines |
| 3 | Processes | Master, Mock-ups |
| 3 | Navigable prototype | Mock-ups, Processes |
| 3 | Solution design | Master (and Processes for flows) |
| 4 | Compliance | Master, Solution design |
| 4 | Business & roadmap (separate track) | Master |
| 5 | Architecture | Solution design, Compliance |
| 6 | Test plan | Processes, Solution design, Architecture, Compliance |
| 7 | Implementation prompts | all of the above |

Business & roadmap is kept separate from the others, but it is part of impact analysis: every functional change is checked against it, and every business decision (plans, limits, pricing tiers) is checked against the Master and the parameters in the Solution design.

### Project Register

The skill maintains a short register (in the project knowledge, or as the first section of the Master if there is no other place). It is a working tool, not a deliverable to discuss. It contains:

- project name, chosen complexity level, active triggers;
- the list of documents with link, hierarchy level, status (not started / draft / validated / needs alignment) and last change;
- the **copies table**: wherever content is duplicated by hand (e.g. screen thumbnails copied into processes, screens used in the navigable prototype, a feature list copied into the roadmap), record where each copy lives, so a change to the original can update every copy;
- the ID prefixes in use (§4).

Update the register whenever a document is created, changes status or gains a copy.

---

## 4. ID scheme and traceability

Use short, stable IDs. Never renumber; retire IDs instead.

| Prefix | Item | Lives in |
|---|---|---|
| F-nn | Feature / functional area | Master |
| R-nn | Business rule | Master |
| OP-nn | Open point | Master |
| ROLE-xx | Role | Master / Solution design |
| E-xx | Domain entity | Solution design |
| S-nn | Screen | Mock-ups |
| P-nn | Process | Processes |
| PAR-nn | Parameter or feature flag | Solution design |
| N-nn | Notification | Solution design |
| NFR-nn | Non-functional requirement | Solution design |
| INT-nn | External integration | Solution design |
| LEG-nn | Compliance requirement | Compliance |
| ARC-nn | Architecture decision | Architecture |
| T-nn | Test case | Test plan |
| PR-nn | Implementation prompt | Prompts |
| AS-nn | As-is finding: discrepancy or gap (reverse mode) | As-is report |

**Traceability matrix** (Standard and Complete levels; light version at Essential): one row per feature, columns for rules, screens, processes, parameters, plan/tier, roadmap phase, tests, prompt. It turns cascade checks into a mechanical lookup: when F-07 changes, the row shows exactly what to revisit. Keep it in the Master appendix or the Project Register.

---

## 5. Complexity levels

The level decides which deliverables and design aspects are in scope. Levels are **not watertight**: triggers (§5.3) pull in any aspect that matters, at any level.

### 5.1 Choosing the level

| Level | Typical project | Signals |
|---|---|---|
| **Essential** | Simple apps, personal or internal tools, prototypes, MVP experiments | 1–2 roles, under ~10 screens, no sensitive data, no monetisation, no integrations |
| **Standard** | Real products with external users | several roles, flows passing between people, personal data, some integrations, a launch plan |
| **Complete** | Platforms and market products | multiple organisations/tenants, monetisation, marketplace, payments, AI features, high volumes, public API |

After the Brief, propose a level with a one-line reason based on the signals. The user confirms or overrides. The level can be **raised** at any time: list the deliverables and aspects that are added and treat them as new sections to align in cascade. It can be **lowered** only for deliverables not yet produced.

### 5.2 What each level includes

Legend: ● required · ◐ recommended or in light form · ○ only if a trigger applies

**Deliverables**

| Deliverable | Essential | Standard | Complete |
|---|---|---|---|
| As-is report (reverse mode only) | ● inventory + discrepancies | ● + screen map and rules | ● + NFR and security evidence |
| Brief | ● short | ● | ● |
| Master | ● | ● | ● |
| Visual guidelines | ◐ existing base + tweaks | ● | ● full design system |
| Mock-ups | ◐ key screens | ● all screens | ● all screens + states |
| Processes | ○ | ● main processes | ● all, with variants |
| Navigable prototype | ◐ main flow, linked straight from the mock-ups | ● main processes | ● all processes and variants |
| Solution design | ● subset | ● | ● |
| Compliance | ◐ quick checklist | ● | ● |
| Business & roadmap | ○ | ◐ roadmap | ● |
| Architecture | ◐ stack + deployment | ● with diagrams | ● with diagrams + alternatives |
| Test plan | ● functional | ● + basic NFR | ● + performance and security |
| Implementation prompts | ● 1–2 prompts | ● one per phase | ● one per module and phase |

**Solution design aspects**

| Aspect | Essential | Standard | Complete |
|---|---|---|---|
| Domain model and states | ● | ● | ● |
| Form factor and app type | ● | ● | ● |
| Roles and permissions | ◐ | ● | ● |
| Parametrisation | ◐ defaults only | ● user + platform | ● + feature flags |
| Empty states, errors, edge cases | ◐ | ● | ● |
| Identity and authentication | ◐ | ● | ● |
| Audit and traceability | ○ | ● | ● |
| Notifications | ○ | ● | ● |
| Data lifecycle | ○ | ● | ● |
| Files and media | ○ | ◐ | ● |
| Accessibility | ◐ | ● | ● |
| External integrations | ○ | ◐ | ● |
| Measurable NFRs | ◐ | ● | ● |
| Modularity / pluggability | ○ | ◐ | ● |
| Public API layer | ○ | ○ | ● |
| Multi-tenancy | ○ | ◐ | ● |
| Offline and sync | ○ | ◐ | ● |
| Localisation | ○ | ◐ | ● |
| Observability and product metrics | ○ | ◐ | ● |

### 5.3 Triggers (apply at any level)

When a signal emerges from the Brief or later conversation, propose the related aspect and say why in one line.

| If this emerges… | Propose… |
|---|---|
| personal data | full GDPR section in Compliance + data lifecycle |
| AI in the features (generation, scoring, recommendations, chatbots) | AI Act classification, transparency, human oversight |
| payments or money moving between users | PSD2/AML check, full audit, security tests |
| several roles or hand-offs between people | permissions matrix + Processes |
| use on the move, outdoors, poor connectivity | offline and sync |
| external systems to connect | integrations (+ API layer if others must connect to us) |
| the product is sold or subscription-based | Business & roadmap, with business questions already in the Brief |
| several organisations or separate customers | multi-tenancy |
| user-generated content or marketplace | DSA, moderation, reporting |
| possible minor users | protections for minors |
| many users, peaks, real-time | NFRs, observability, performance tests |
| behaviour that must be tuned without releases | parameters and feature flags |
| regulated sector (health, finance, public sector) | sector rules in Compliance, stronger audit |

Record active triggers in the Project Register.

---

## 6. Phases

### Phases at a glance

| # | Phase | Deliverable | In one line |
|---|---|---|---|
| (R) | Reverse analysis | As-is report | Only for existing projects: reconstruct what the code and documents already say, and where they disagree (§2.1) |
| 1 | Problem story | Brief | Understand the problem, the users and the goals well enough to be proactive |
| 2 | Functional analysis | Master | Define what the solution does, completely and without contradictions: the source of truth |
| 3 | Visual language | Visual guidelines | Fix style and components before drawing, so mock-ups and product look the same |
| 4 | User experience | Mock-ups | Make every feature tangible, screen by screen, and test the Master against it |
| 5 | Flows | Processes + navigable prototype | Describe each flow step by step and link the mock-ups into a clickable preview of the app |
| 6 | Solution design | Solution design | Decide how the solution is structured: states, permissions, parameters, integrations, audit, NFRs |
| 7 | Legal | Compliance | Spot legal constraints early so they shape design and architecture |
| 8 | Value | Business & roadmap | Decide how the solution creates value and in which order it is released |
| 9 | Technical analysis | Architecture | Choose stack, modules, deployment and how it all runs, with diagrams |
| 10 | Verification | Test plan | Derive tests from the documents so every requirement is verifiable |
| 11 | Hand-off | Implementation prompts | Turn everything into prompts that let an agent or team build it faithfully |

Each phase lists: goal, how to run it, deliverable outline, exit criteria. Scale depth to the level. Advance only when exit criteria are met, or when the user knowingly accepts moving on with listed gaps.

### Phase 1: Problem story → **Brief**

**Goal**: acquire enough context to be proactive, not just a scribe.

**How**: invite the user to tell the story freely: who suffers the problem, how they cope today, what triggered the idea. Suggest doing it by voice if available. In parallel, research the domain on the web (§0) so that your questions and proposals are informed. Then ask targeted questions, a few at a time:
- Who are the users and which one has the most urgent problem (primary target)?
- Main usage scenarios (2–5), including different modes of use if any.
- What success looks like for the user and for the owner.
- Existing alternatives (apps, spreadsheets, chats) and why they are not enough.
- Constraints: budget, time, team, platforms, who will build it.
- Data involved (personal, financial, health, minors, location).
- **Business questions, asked now**: is it to be sold? to whom? free/paid split? which models are acceptable? This avoids designing features the business model later contradicts.
- What is explicitly out of scope.

**Deliverable: Brief**
1. Problem statement
2. Users and primary target
3. Usage scenarios
4. Current alternatives and gaps (informed by domain research, with sources)
5. Goals and success criteria
6. Constraints and assumptions
7. Business intent (if any)
8. Out of scope
9. Proposed complexity level, rationale, active triggers

**Exit**: the user confirms the Brief describes the problem correctly; level chosen.

### Phase 2: Functional analysis → **Master**

**Goal**: define what the solution does, completely and without contradictions. No technology here.

**How**: start from the Brief scenarios. Propose a feature map, then go feature by feature. For each feature capture who can do it, the rules, the edge cases and defaults. If the user brings an earlier draft, converge it into the Master point by point. Add decisions as they are taken; log uncertainties as open points.

Useful prompts to find gaps:
- What happens if the other person does not respond / confirm?
- Who can modify or cancel what someone else entered?
- What happens when someone leaves, joins, or deletes their account?
- What is the lifecycle of this item (created → … → closed/cancelled)?
- Is anything ever really deleted, or only cancelled and kept in history?
- What happens at period boundaries (end of season/month/year)?
- What can be automated with a default, and what must a person decide?

**Deliverable: Master**
1. Purpose and scope (link to Brief)
2. Glossary
3. Roles (ROLE-) and short permission summary
4. Feature list (F-), the index; keep it in sync
5. One section per feature: description, rules (R-), edge cases, defaults, links to screens/processes
6. Cross-cutting rules (history and cancellation, notifications summary, privacy principles)
7. Future evolutions / placeholders (named, not specified)
8. Open points (OP-): question, options, proposal, status
9. Appendix: traceability matrix (Standard/Complete)

**Exit**: every feature in the Brief scenarios is covered; no blocking open points for the next phase; the user declares the functional analysis converged (it can reopen later through the change procedure).

### Phase 3: **Visual guidelines**

**Goal**: fix the visual language before drawing screens, so mock-ups and the final build share one style.

**Advisor guidance for setting it up**:
- Ask for 3–5 reference apps or sites the user likes (screenshots welcome) and what they like in each.
- Ask for existing brand assets (logo, colours, fonts, tone of voice).
- Recommend a starting base instead of inventing from scratch: Material Design, Apple Human Interface Guidelines, an established web component kit (e.g. shadcn/ui), or a custom style if the brand demands it.
- Recommend tools available in the session: frontend/visual design skills, design-system skills, accessibility-review skills, and a design artifact type for mock-ups. If useful ones are not installed, tell the user which kind of skill would help and why.
- Essential level: pick a base system and adjust colours/typography; do not build a design system.

**Deliverable: Visual guidelines**
1. Design principles (3–5) and tone of voice
2. References and chosen base system
3. Colour palette (with semantic colours: success, warning, error, info) and contrast check
4. Typography scale
5. Spacing, grid, radius, elevation
6. Iconography and imagery (incl. defaults when an image is missing)
7. Core components and their states (buttons, inputs, lists, cards, dialogs, toasts, empty states)
8. Motion and feedback (e.g. highlight what changed)
9. Copy guidelines (labels, errors, confirmations, inline help style)
10. Accessibility rules

**Exit**: the user approves the style on at least one sample screen.

### Phase 4: **Mock-ups**

**Goal**: make every feature tangible and verify the Master against real screens.

**How**: first agree the form factor (mobile-first, desktop-first, both). One section per screen (S-). Draw it full-screen in the chosen form factor using the Visual guidelines. Under each screen write **"What it covers"** (features and rules, with IDs) and **"How it works"** (interactions, states, validations). Include empty, error and loading states at Standard/Complete. Every gap found goes up to the Master (rule 4).

**Deliverable: Mock-ups**: index of screens grouped by area → one section per screen (drawing, What it covers, How it works, links to processes).

**Exit**: every feature in the Master has at least one screen or an explicit "no UI" note; the user (and any partners) have reviewed them.

### Phase 5: **Processes**

**Goal**: describe each end-to-end flow step by step across screens and roles, to catch missing states, permissions and hand-offs.

**How**: list processes from features and scenarios (P-). For each: actors, trigger, preconditions, steps, variants/alternative paths, outcomes, rules applied, notifications sent. Then add a **"Screen sequence"**:
- if the flow crosses several screens: readable copies of the screens in order, numbered, with the screen name and the steps covered, arrows labelled with the action leading to the next screen, and a line of links to the originals;
- if it happens in one screen (or an original already shows the sequence): just a link.
Record every copy in the Project Register copies table.

**Deliverable: Processes**: index → one section per process (actors, trigger, preconditions, steps, variants, outcomes, rules, notifications, screen sequence).

**Navigable prototype.** Link the mock-ups into a clickable preview of the app that follows the processes. It lets the user, clients and partners *experience* the solution before anything is built. It is the most effective tool for validation sessions.
- Build it as one self-contained HTML page, or as a prototype in a design tool if the user works in one.
- Each screen is a copy of its mock-up. Its actionable elements (buttons, list items, tabs) are hotspots that lead to the next screen, as defined by the process steps.
- A side panel shows the active process (P-), the current step and the actor. A role switch appears when the actor changes, for example from borrower to owner.
- Navigation: choose a process to play, go back, restart, jump to any screen from a screen map. Optionally, show the hotspots on demand ("show clickable areas").
- Variants can be played as alternative paths from the step where they branch.
- The prototype is a copy of mock-ups and processes. Record it in the copies table and regenerate it whenever a screen or a process changes.

**Exit**: every multi-step feature has a process; no step refers to a screen, state or permission that does not exist; every process in scope can be played in the prototype.

### Phase 6: **Solution design**

**Goal**: decide how the solution is structured, independent of specific technologies where possible. Cover the aspects required by the level and the triggers (§5.2–5.3).

**Sections (include those in scope)**
1. **Domain model and states**: entities (E-), relationships, and for each stateful entity the states and transitions with who/what triggers them. This is the strongest consistency check: verify every transition against Master rules and Processes.
2. **Roles and permissions**: matrix role × action (allowed / denied / conditional). Check against Master and Processes.
3. **Parametrisation** (PAR-), at three levels:
   - *user parameters*: set by users/admins in the app (e.g. group rules), always with a default so setup is quick;
   - *platform parameters*: moved out of code so behaviour can be tuned without releases (limits, durations, thresholds, prices, plan limits);
   - *feature flags*: switch features on/off per environment, tenant or plan.
   For each: name, level, default, allowed range, who can change it, where it is used, how it is explained to the user.
4. **Modularity**: which components are pluggable or replaceable (e.g. payment provider, weather source, notification channel), and the interface each must respect.
5. **External integrations** (INT-): system, purpose, direction, data exchanged, frequency, failure behaviour, cost and who pays for it.
6. **Form factor**: mobile-first / desktop-first / both; breakpoints.
7. **App type**: web, PWA, hybrid or native, with reasons (device features, store presence, offline, budget).
8. **Audit and traceability**: which operations are logged, what is recorded (who, what, when, before/after), cancellation instead of deletion, who can see the history.
9. **API layer**: whether to expose APIs to third parties, scope, authentication, versioning, rate limits.
10. **Identity and authentication**: sign-up, login methods, invitations, sessions, recovery, account deletion rules.
11. **Notifications** (N-): event → recipients, channel (push, email, in-app, chat message), content, whether the user can disable it.
12. **Offline and sync**: what works offline, conflict resolution.
13. **Multi-tenancy**: isolation between groups/organisations, users in several tenants.
14. **Data lifecycle**: retention, archiving, export, deletion, history visibility per plan.
15. **Files and media**: limits, compression, expiry, storage quotas and warnings.
16. **Localisation**: languages, currencies, time zones, formats.
17. **Accessibility**: target (e.g. WCAG 2.1 AA) and specific requirements.
18. **Empty states, errors and edge cases**: catalogue per area.
19. **Measurable NFRs** (NFR-): response times, expected load and peaks, availability, data volumes, security baseline.
20. **Observability and product metrics**: technical monitoring, and the product metrics that tell whether the solution works for users (activation, retention, key actions).

**Exit**: every in-scope aspect is filled or explicitly marked "not applicable, because…"; no contradiction with the Master.

### Phase 7: **Compliance**

**Goal**: a preliminary risk analysis so legal constraints shape design and architecture early. State clearly in the document that it is not legal advice and that a qualified professional should validate it before launch.

**Checklist (include what applies)**
- **GDPR**: personal data inventory, legal bases, consent, minimisation, retention, data subject rights (access, rectification, deletion, portability), processors and data location, DPIA need, privacy by design.
- **AI Act**: whether AI is used, risk classification, transparency obligations (users must know they interact with AI or AI-generated content), human oversight, logging.
- **ePrivacy**: cookies, tracking, analytics consent, push/email marketing consent.
- **Digital Services Act**: if user content or marketplace: notice and action, reporting, transparency, trader information.
- **European Accessibility Act**: applicability and requirements.
- **Consumer protection**: subscriptions, renewals, right of withdrawal, clear pricing, terms of service.
- **Payments**: PSD2, AML/KYC, whether the platform ever holds money.
- **App store policies**: in-app purchase rules, review guidelines, account deletion requirements.
- **Minors**: age gating, parental consent.
- **Open source licences** of planned components.
- **Sector rules** if regulated.
- **Intellectual property** of user content (licence to display, sharing outside the app).

**Deliverable: Compliance**: applicability summary → one section per applicable area (requirement LEG-, impact on Master/design, action) → open legal questions for a professional.

Every LEG- requirement that changes behaviour goes up into the Master or Solution design (rule 4).

### Phase 8: **Business & roadmap** (separate track)

**Goal**: define how the solution creates value and in which order it is released, derived from the converged Master.

**How**: reuse validated models from comparable products rather than inventing new ones; propose critically. Two common levers: whole features as paid, or limits on free features unlocked by paying. Never limit the core flow that makes the product useful. Check every limit against real costs (storage, external APIs, support). Every plan limit, price and tier boundary becomes a **platform parameter** (PAR-) in the Solution design.

**Deliverable: Business & roadmap**
1. Customer segments and who pays
2. Value proposition per segment
3. Plans (free / paid / other) with feature and limit table referencing F- and PAR-
4. Pricing logic and tiers
5. Costs that drive limits
6. Comparable products and models reused
7. Roadmap: phases, scope per phase (F- IDs), rationale, activation strategy
8. Future considerations

**Exit**: every feature in plans and roadmap exists in the Master with the same behaviour; every limit is a parameter.

### Phase 9: **Architecture**

**Goal**: describe how the solution is built and run, with diagrams.

**Sections**
1. Architectural drivers (from NFR-, compliance, integrations, budget, team skills)
2. Technology stack per layer (client, backend, data, messaging, storage, AI if any), with reasons and rejected alternatives (Complete level)
3. Application modules and responsibilities (mapped to F- and modular components)
4. Interactions and protocols between modules and with external systems (REST/GraphQL, websockets/push, queues, webhooks)
5. Data architecture (stores, main schemas derived from E-, retention, backups)
6. Security architecture (authentication, authorisation, secrets, encryption in transit/at rest)
7. Parametrisation and feature-flag mechanism
8. Deployment (environments, hosting, regions for data location, CI/CD, release strategy for app stores if native/hybrid)
9. Observability (logging, metrics, tracing, alerting, audit log storage)
10. Scalability and performance strategy (against NFR-)
11. Running costs estimate and cost drivers
12. Architecture decisions log (ARC-): decision, context, options, consequences

**Diagrams** (Mermaid or equivalent): context diagram, container/module diagram, key sequence diagrams for the main processes, deployment diagram, data model (ER) diagram.

**Exit**: every NFR, integration and compliance constraint has an architectural answer.

### Phase 10: **Test plan**

**Goal**: derive tests almost automatically from the documents, so every requirement is verifiable.

**Derivation rules**
- Each **process** → one happy-path test + one test per variant and outcome.
- Each **business rule** (R-) → at least one positive and one negative test.
- **Permissions matrix** → for each sensitive action, allowed and denied cases per role.
- **State transitions** → each valid transition, and attempts at invalid ones.
- **Parameters** (PAR-) → default value, boundary values, change at runtime.
- **Notifications** (N-) → correct recipients, channel, opt-out respected (and non-disableable ones enforced).
- **Audit** → each logged operation produces the expected record; nothing is truly deleted where cancellation is required.
- **Empty/error states** → each catalogued state is reachable and displayed as designed.
- **Compliance** (LEG-) → consent, data export, deletion, transparency notices.
- **NFR-** → performance/load, availability, security tests (Standard: basic; Complete: full, incl. load profiles and security testing).
- **Accessibility** → automated + manual checks against the target.
- **Visual** → key screens match the Visual guidelines.

**Deliverable: Test plan**: strategy and levels (unit, integration, end-to-end, NFR) → environments and test data → test cases (T-) with ID, source requirement, preconditions, steps, expected result, priority → coverage matrix (requirement → tests) → entry/exit criteria.

**Exit**: every F-, R-, P-, PAR-, N-, LEG- and NFR- in scope is covered by at least one test.

### Phase 11: **Implementation prompts**

**Goal**: produce prompts that let a coding agent or team build the solution faithfully, following every functional, design and technical requirement.

**Choosing the agent**: ask at this phase which agent or tool will build it (e.g. a coding agent such as Claude Code, Cursor or Copilot; an app builder; a human team). If unknown, produce the neutral version. The content stays the same; only the form adapts:
- *coding agents*: a permanent rules file (e.g. CLAUDE.md or AGENTS.md) + one prompt per step;
- *app builders / no-code*: smaller, more visual steps, one screen or flow at a time;
- *human team*: the same prompts work as work packages / tickets.

**Prompt set (scale to level)**
- **PR-00 Context and rules** (becomes the permanent rules file): product summary, glossary, roles, document list with links and hierarchy, the rule that the Master wins, ID scheme, coding conventions, "do not invent rules: ask or flag", definition of done, how to report deviations back.
- **PR-01 Project foundation and architecture**: stack, repository structure, environments, CI/CD, configuration and parameter/feature-flag mechanism, audit logging, authentication skeleton, observability.
- **PR-02 Design system**: implement Visual guidelines as tokens and components with their states; accessibility baseline.
- **PR-03…n Feature modules**, ordered by roadmap phase and dependency (domain model first). Each one contains:
  1. Objective
  2. Scope in / out (F- IDs)
  3. Domain entities and states involved (E-)
  4. Rules to implement (R-), with defaults
  5. Screens to build (S-) referencing mock-ups and Visual guidelines
  6. Processes to support (P-)
  7. Permissions, notifications, parameters, audit requirements
  8. Integrations and APIs
  9. Compliance requirements (LEG-)
  10. NFRs that apply
  11. Acceptance criteria
  12. Tests that must pass (T-)
  13. Constraints and things not to do
  14. Output expected and how to report open issues
- **PR-last Testing and hardening**: run the full test plan, NFR and security checks, accessibility audit, fix list.

Each prompt must be self-sufficient for its step (quote the needed rules, do not only link) but reference IDs so everything is traceable.

In reverse mode, feature prompts are **change prompts**. For each change, add:
- the current behaviour (as-is) and the target behaviour;
- the areas of the code likely affected;
- the regression tests that must keep passing.

**Exit**: every in-scope F- appears in exactly one feature prompt (or is explicitly deferred); every prompt lists its tests.

---

## 7. Coherence checks

Run these at each phase exit and after every significant change. Report findings as a short list: issue, documents involved, proposed fix.

- Every Brief scenario is covered by Master features.
- The Master feature list matches its sections, the mock-up index, the processes index and the traceability matrix.
- Every rule in a mock-up's "How it works" or in a process step exists in the Master.
- Every screen referenced in a process exists, with the same name; every copy matches its original (copies table).
- Every hotspot in the navigable prototype leads where the process says, and every in-scope process can be played end to end.
- In reverse mode: every AS-nn finding is resolved, turned into an open point or explicitly accepted.
- Every role/action pair used in Processes is allowed in the permissions matrix.
- Every state used anywhere exists in the domain model, and every transition is allowed.
- Every default and limit mentioned anywhere is a PAR- with the same value.
- Every plan limit and roadmap feature in Business matches the Master and PAR-.
- Every LEG- requirement is reflected in Master/design and tested.
- Every NFR- has an architectural answer and a test.
- No document contains decisions absent from the Master.
- Terms are used consistently with the glossary.

---

## 8. Change procedure (cascade)

For every change or decision, in this order:

1. **Locate** the highest document the change belongs to (usually the Master).
2. **Check coherence** against everything already documented: rules, states, permissions, parameters, screens, processes, plans. If the change contradicts something or leaves a gap, do not write it yet. Raise the conflict to the user, with the documents and IDs involved and a recommended resolution, and log it as an open point. Write only once it is decided.
3. **Write** it there, updating indexes, lists and cross-references in the same document.
4. **Trace impacts** via IDs, the traceability matrix and the copies table: which screens, processes, design sections, compliance items, business tables, architecture, tests and prompts are affected.
5. **Update** each affected document in hierarchy order, including manual copies.
6. **Report alignment**:
   - Updated: document → sections
   - Not yet aligned: document → section → what is missing
   - New open points, if any
7. **Update** the Project Register (status, last change).

**Loop until stable.** While updating a lower document (step 5), a new gap or contradiction may appear. For example, a process step needs a notification that the Master never defined. When that happens:
1. pause the cascade;
2. take the issue up to the Master (rule 4) and resolve it with steps 2–3;
3. resume the cascade from the top for everything the new decision affects.

The change is complete only when a full pass finds nothing new and every affected document is aligned.

If the user asks to edit a lower document directly with a functional change, do step 1 first anyway and say so in one line.

---

## 9. Advisor mode

Activate when the user is unsure, asks "what now?", "what first?", "which option?", or when you detect a risky decision.

### 9.1 "How do I proceed?"
Read the register and the Master; then recommend **one** next step with the reason, e.g.:
- blocking open points → resolve them before the next phase (list the blocking ones);
- documents marked "needs alignment" → align before adding new content;
- phase exit criteria met → move to the next phase;
- a trigger appeared → address that aspect now.
Also warn against common anti-patterns: designing the business model before the Master converges; choosing technology before the functional analysis; drawing mock-ups before visual guidelines; adding features while open points pile up; building before tests are derivable.

### 9.2 "What comes first?" (prioritisation)
Apply in order:
1. **Core flow**: what makes the product useful at all must be in the first release and never limited.
2. **Dependencies**: what other features rely on (domain model, roles, identity).
3. **Activators**: features that bring users in (invites, free features for partners who spread the product).
4. **Value vs effort**: quick wins first; big bets only with clear value.
5. **Risk**: features with unvalidated assumptions → small version first, to learn.
6. **Defer** whatever can wait without blocking anything; name it as a future evolution.
For a compact view, classify with MoSCoW and show the resulting first-release scope.

### 9.3 "Which option?" (decision patterns)
Present 2–3 options with trade-offs, recommend one, and explain why. Where it helps, show how comparable products solve the same problem (domain research, §0), with sources. Useful patterns:
- **Reversible decision → default + parameter.** Do not debate values that can be tuned later; pick a sensible default and make it a PAR-.
- **The app proposes, a person decides.** Automate the calculation or suggestion; let the responsible role confirm or adjust, and trace it.
- **Cancel, never delete.** Keep history; mark items as cancelled; show who did what.
- **Silent consent where friction kills usage** (with a time limit and a way to object); explicit consent where stakes are high.
- **Reuse validated models** from comparable products before inventing.
- **Simplest first version**, with the evolution written down as a placeholder.
- **Fast setup**: everything configurable has a ready default; explanations are discreet (a short line under the field or good inline help), not question marks everywhere.
- **Costs must be covered**: any recurring external cost (storage, APIs, messaging) needs a limit or a paying plan.
- **Platform never holds money** unless the business deliberately accepts the regulatory burden.
- **Privacy by default**: the minimum visibility that still makes the feature work.

### 9.4 Critic
When the user proposes something, check and say plainly if it: contradicts an earlier decision; adds cost without a payer; adds friction to the core flow; creates a legal obligation; makes a later phase much harder; or duplicates an existing feature. Offer the better alternative, then follow the user's decision and record it.

---

## 10. Validation and sharing

The goal is to share and validate the solution before building it.
- Recommend validation moments: Brief (with stakeholders), Mock-ups and navigable prototype (with partners and a few target users, who play the main processes while you note where they hesitate, using prepared questions), Business (with whoever funds or sells it), Architecture (with whoever builds it).
- Deliverables are shared as they are (rule 11): no separate "presentation version" to keep aligned.
- Feedback is treated as changes and goes through the change procedure (§8).
- Mark documents as "validated" in the register only after the user says so.

---

## 11. Finishing

The analysis is complete when, for the chosen level: all deliverables in scope are validated, no blocking open points remain, coherence checks pass, and the implementation prompts are produced. Give the user a final summary: documents with links (including the navigable prototype), level and triggers, deferred items, open non-blocking points, and the recommended first prompt to run.
