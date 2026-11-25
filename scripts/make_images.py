"""Generate the example images for the AppFootings README (fictional app: LendLoop).

Usage: python3 scripts/make_images.py [output_dir]
Writes SVG sources and, if rsvg-convert is installed, PNGs at 1.5x into docs/images.
Also builds examples/lendloop/prototype/index.html (navigable prototype) and, with ImageMagick,
docs/images/prototype-walkthrough.gif and docs/images/analysis-loop.gif (+ PNG poster).
Keep IDs, values and wording consistent with examples/lendloop/.
"""
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "images")
os.makedirs(OUT, exist_ok=True)

NAVY = "#0F2A44"
TEAL = "#0E8C8C"
TEAL_L = "#E3F3F3"
BG = "#F5F7FA"
TEXT = "#1B2430"
MUTED = "#6B7785"
BORDER = "#DDE3EA"
AMBER = "#E8A33D"
AMBER_L = "#FDF3E2"
GREEN = "#2E9E6A"
GREEN_L = "#E4F4EC"
RED = "#D64545"
WHITE = "#FFFFFF"
FONT = "Inter, 'DejaVu Sans', sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def t(x, y, s, size=14, fill=TEXT, weight=400, anchor="start", extra="", font=FONT):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'fill="{fill}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def rect(x, y, w, h, fill=WHITE, stroke="none", r=8, sw=1, extra=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')


def svg(w, h, body, bg=WHITE):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">{rect(0, 0, w, h, bg, r=0)}'
            '<defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{NAVY}"/></marker>'
            '<marker id="arrT" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{TEAL}"/></marker>'
            '<marker id="arrA" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">'
            f'<path d="M0,0 L10,5 L0,10 z" fill="{AMBER}"/></marker></defs>'
            f'{body}</svg>')


# ---------------------------------------------------------------- phone screens
# Each screen is drawn in a 360 x 740 coordinate space.

def phone_frame(content, title, back=True):
    s = rect(0, 0, 360, 740, WHITE, "#C9D1DA", r=36, sw=2)
    s += rect(8, 8, 344, 724, BG, r=30)
    s += t(28, 38, "9:41", 13, TEXT, 600)
    s += t(332, 38, "100%", 12, TEXT, 500, "end")
    s += rect(130, 18, 100, 24, "#1B2430", r=12)
    # app bar
    s += rect(8, 52, 344, 56, WHITE, r=0)
    if back:
        s += t(26, 88, "‹", 30, NAVY, 400)
    s += t(180, 87, title, 17, TEXT, 600, "middle")
    s += f'<line x1="8" y1="108" x2="352" y2="108" stroke="{BORDER}"/>'
    s += content
    return s


def btn(x, y, w, label, primary=True, h=48):
    if primary:
        return rect(x, y, w, h, TEAL, r=12) + t(x + w / 2, y + h / 2 + 5, label, 15, WHITE, 600, "middle")
    return rect(x, y, w, h, WHITE, TEAL, r=12, sw=1.5) + t(x + w / 2, y + h / 2 + 5, label, 15, TEAL, 600, "middle")


def chip(x, y, label, fg, bg):
    w = 8 * len(label) + 20
    return rect(x, y, w, 24, bg, r=12) + t(x + w / 2, y + 16, label, 12, fg, 600, "middle")


def card(x, y, w, h):
    return rect(x, y, w, h, WHITE, BORDER, r=14)


def screen_item_detail():
    c = ""
    # photo placeholder
    c += rect(24, 124, 312, 170, "#DCE6EE", r=16)
    c += f'<g transform="translate(150,170)" fill="none" stroke="{MUTED}" stroke-width="4">' \
         '<rect x="0" y="20" width="60" height="26" rx="6"/><rect x="58" y="26" width="22" height="14" rx="3"/>' \
         '<path d="M10 46 L4 80 L22 80 L26 46"/></g>'
    c += t(24, 326, "Cordless drill", 22, TEXT, 700)
    c += t(24, 350, "Giulia R. · 0.4 km · Via Roma", 13, MUTED)
    c += chip(24, 364, "Available", GREEN, GREEN_L)
    c += chip(124, 364, "Max 3 days", NAVY, "#E6ECF2")
    # availability strip
    c += card(24, 404, 312, 118)
    c += t(40, 430, "Availability · next 7 days", 13, TEXT, 600)
    days = ["M", "T", "W", "T", "F", "S", "S"]
    busy = {2, 3}
    for i, d in enumerate(days):
        x = 40 + i * 41
        col = "#F4D9D9" if i in busy else GREEN_L
        fg = RED if i in busy else GREEN
        c += rect(x, 446, 34, 50, col, r=8)
        c += t(x + 17, 466, d, 12, fg, 600, "middle")
        c += t(x + 17, 486, str(10 + i), 13, fg, 700, "middle")
    c += t(40, 512, "Red = already on loan", 11, MUTED)
    # rules
    c += card(24, 534, 312, 76)
    c += t(40, 560, "Lending rules", 13, TEXT, 600)
    c += t(40, 580, "Pick-up at owner's home · no deposit", 12, MUTED)
    c += t(40, 598, "Owner answers within 48 h", 12, MUTED)
    c += btn(24, 636, 312, "Request to borrow")
    c += t(180, 708, "Ask Giulia a question", 13, TEAL, 600, "middle")
    return phone_frame(c, "Item")


def screen_request():
    c = ""
    c += t(24, 144, "Cordless drill · Giulia R.", 14, MUTED)
    c += card(24, 160, 312, 150)
    c += t(40, 188, "From", 12, MUTED)
    c += rect(40, 196, 132, 44, BG, BORDER, r=10) + t(56, 224, "Fri 14", 15, TEXT, 600)
    c += t(188, 188, "To", 12, MUTED)
    c += rect(188, 196, 132, 44, BG, TEAL, r=10, sw=2) + t(204, 224, "Sun 16", 15, TEXT, 600)
    c += t(40, 266, "3 days · maximum allowed by this group", 12, MUTED)
    c += t(40, 290, "Change limit: group settings", 11, TEAL)
    c += card(24, 324, 312, 130)
    c += t(40, 352, "Message to the owner (optional)", 12, MUTED)
    c += t(40, 378, "Hi Giulia! I need it to hang", 14, TEXT)
    c += t(40, 398, "some shelves this weekend.", 14, TEXT)
    c += rect(24, 470, 312, 84, AMBER_L, r=14)
    c += t(40, 498, "What happens next", 13, "#8A5A12", 700)
    c += t(40, 518, "Giulia has 48 h to answer.", 12, "#8A5A12")
    c += t(40, 536, "No answer = request expires, no penalty.", 12, "#8A5A12")
    c += btn(24, 636, 312, "Send request")
    c += t(180, 708, "Cancel", 13, MUTED, 600, "middle")
    return phone_frame(c, "Request")


def screen_owner():
    c = ""
    c += t(24, 144, "Requests for your items", 14, MUTED)
    c += card(24, 160, 312, 236)
    c += f'<circle cx="62" cy="200" r="20" fill="{TEAL_L}"/>' + t(62, 206, "M", 16, TEAL, 700, "middle")
    c += t(94, 196, "Marco B.", 15, TEXT, 700)
    c += t(94, 214, "0.6 km · 12 loans returned on time", 12, MUTED)
    c += t(40, 252, "Cordless drill", 15, TEXT, 600)
    c += t(40, 272, "Fri 14 → Sun 16 · 3 days", 13, MUTED)
    c += t(40, 300, "“I need it to hang some shelves", 12, MUTED)
    c += t(40, 316, "this weekend.”", 12, MUTED)
    c += btn(40, 334, 134, "Decline", False, 44)
    c += btn(186, 334, 134, "Accept", True, 44)
    c += t(180, 420, "Suggest other dates", 13, TEAL, 600, "middle")
    c += rect(24, 446, 312, 56, "#E6ECF2", r=14)
    c += t(40, 470, "Expires in 41 h", 13, NAVY, 700)
    c += t(40, 488, "After that the request closes by itself.", 12, MUTED)
    return phone_frame(c, "Requests")


def screen_confirmed():
    c = ""
    c += f'<circle cx="180" cy="190" r="44" fill="{GREEN_L}"/>'
    c += f'<path d="M160 190 L175 205 L202 176" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
    c += t(180, 268, "Loan confirmed", 22, TEXT, 700, "middle")
    c += t(180, 292, "Giulia accepted your request", 13, MUTED, 400, "middle")
    c += card(24, 316, 312, 150)
    rows = [("Item", "Cordless drill"), ("Dates", "Fri 14 → Sun 16"), ("Pick-up", "Via Roma 12, from 18:00"),
            ("Return by", "Sun 16, 20:00")]
    for i, (k, v) in enumerate(rows):
        y = 348 + i * 32
        c += t(40, y, k, 12, MUTED) + t(320, y, v, 13, TEXT, 600, "end")
    c += rect(24, 482, 312, 56, TEAL_L, r=14)
    c += t(40, 506, "A private chat with Giulia is open", 13, TEAL, 700)
    c += t(40, 524, "The confirmation was posted there.", 12, TEAL)
    c += btn(24, 576, 312, "Open chat")
    c += btn(24, 636, 312, "Mark as picked up", False)
    return phone_frame(c, "Loan", back=False)


def bottom_nav(active):
    items = ["Nearby", "My loans", "Add", "Chat", "Profile"]
    s = rect(8, 668, 344, 64, WHITE, r=0) + f'<line x1="8" y1="668" x2="352" y2="668" stroke="{BORDER}"/>'
    for i, it in enumerate(items):
        x = 42 + i * 69
        col = TEAL if it == active else MUTED
        s += f'<circle cx="{x}" cy="690" r="9" fill="none" stroke="{col}" stroke-width="2"/>'
        s += t(x, 716, it, 11, col, 700 if it == active else 500, "middle")
    return s


NEARBY_ITEMS = [
    ("Cordless drill", "Giulia R. · 0.4 km", "Available", GREEN, GREEN_L),
    ("Ladder 3 m", "Paolo T. · 0.7 km", "Available", GREEN, GREEN_L),
    ("Pressure washer", "Anna M. · 1.1 km", "On loan until Sat", RED, "#F4D9D9"),
    ("Camping tent", "Luca B. · 1.8 km", "Available", GREEN, GREEN_L),
]
NEARBY_CARD_Y0, NEARBY_CARD_H, NEARBY_CARD_GAP = 252, 86, 12


def screen_nearby():
    c = ""
    c += rect(24, 122, 200, 30, "#E6ECF2", r=15) + t(40, 142, "Via Roma neighbours  ▾", 13, NAVY, 600)
    c += rect(24, 164, 312, 44, WHITE, BORDER, r=12) + t(46, 191, "Search drill, ladder, tent…", 14, MUTED)
    for i, (lab, active) in enumerate([("All", True), ("Tools", False), ("Garden", False), ("Within 2 km", False)]):
        x = [24, 72, 134, 206][i]
        w = 8 * len(lab) + 22
        c += rect(x, 218, w, 26, TEAL if active else WHITE, "none" if active else BORDER, r=13)
        c += t(x + w / 2, 236, lab, 12, WHITE if active else TEXT, 600, "middle")
    for i, (name, who, status, fg, bg) in enumerate(NEARBY_ITEMS):
        y = NEARBY_CARD_Y0 + i * (NEARBY_CARD_H + NEARBY_CARD_GAP)
        c += card(24, y, 312, NEARBY_CARD_H)
        c += rect(36, y + 12, 62, 62, "#DCE6EE", r=10)
        c += t(112, y + 32, name, 16, TEXT, 700)
        c += t(112, y + 52, who, 12, MUTED)
        c += chip(112, y + 58, status, fg, bg)
    c += bottom_nav("Nearby")
    return phone_frame(c, "Nearby", back=False)


def screen_my_loans(drill_state="Approved"):
    states = {"Approved": (GREEN, GREEN_L), "Declined": (RED, "#F4D9D9"), "Pending": ("#8A5A12", AMBER_L)}
    c = ""
    c += rect(24, 122, 312, 40, "#E6ECF2", r=20)
    c += rect(28, 126, 152, 32, WHITE, r=16) + t(104, 147, "Borrowing", 13, TEXT, 700, "middle")
    c += t(256, 147, "Lending", 13, MUTED, 600, "middle")
    c += t(24, 194, "REQUESTS", 11, MUTED, 700, extra='letter-spacing="1"')
    rows = [("Cordless drill", "Giulia R. · Fri 14 → Sun 16", drill_state, None),
            ("Ladder 3 m", "Paolo T. · expires in 41 h", "Pending", None)]
    y = 206
    for name, sub, st, _ in rows:
        fg, bg = states[st]
        hl = drill_state == "Declined" and name == "Cordless drill"
        c += rect(24, y, 312, 70, WHITE, RED if hl else BORDER, r=14, sw=2 if hl else 1)
        c += t(40, y + 30, name, 15, TEXT, 700) + t(40, y + 52, sub, 12, MUTED)
        w = 8 * len(st) + 20
        c += chip(320 - w, y + 16, st, fg, bg)
        y += 82
    if drill_state == "Declined":
        c += t(40, y + 2, "Giulia can't lend it these days. Try other dates.", 12, RED)
        y += 20
    c += t(24, y + 26, "LOANS", 11, MUTED, 700, extra='letter-spacing="1"')
    y += 38
    c += card(24, y, 312, 92)
    c += t(40, y + 30, "Pressure washer", 15, TEXT, 700) + t(40, y + 52, "Anna M. · Picked up", 12, MUTED)
    c += chip(40, y + 60, "Return by Sat 15 · tomorrow", "#8A5A12", AMBER_L)
    y += 104
    c += card(24, y, 312, 70)
    c += t(40, y + 30, "Hedge trimmer", 15, TEXT, 700) + t(40, y + 52, "Paolo T. · Returned on time", 12, MUTED)
    c += bottom_nav("My loans")
    return phone_frame(c, "My loans", back=False)


SCREENS = {
    "S-02": ("Nearby items", screen_nearby),
    "S-04": ("Item detail", screen_item_detail),
    "S-05": ("Borrow request", screen_request),
    "S-07": ("Owner requests", screen_owner),
    "S-08": ("Loan confirmed", screen_confirmed),
    "S-06": ("My loans", screen_my_loans),
}


def place(svg_body, x, y, scale):
    return f'<g transform="translate({x},{y}) scale({scale})">{svg_body}</g>'


def wrap_lines(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines


def id_chip(x, y, label):
    w = 7.6 * len(label) + 14
    return rect(x, y, w, 22, "#E6ECF2", r=6) + t(x + w / 2, y + 15, label, 12, NAVY, 700, "middle",
                                                  font="DejaVu Sans Mono, monospace"), w


# ---------------------------------------------------------------- image 1: mock-up section
def mockup_section():
    W, H = 1280, 890
    b = t(48, 62, "Mock-ups › Borrowing", 14, MUTED, 500)
    b += t(48, 100, "S-04 · Item detail", 30, TEXT, 700)
    b += t(48, 128, "Example section from the Mock-ups document of a fictional app (LendLoop, neighbours lending tools).",
           14, MUTED)
    b += place(screen_item_detail(), 48, 160, 0.9)
    x0 = 430
    # What it covers
    b += rect(x0, 160, 802, 330, WHITE, BORDER, r=16)
    b += t(x0 + 28, 200, "What it covers", 20, NAVY, 700)
    covers = [
        ("F-03", "Borrow an item: entry point of the request"),
        ("R-05", "A loan lasts at most the group's maximum (shown as a chip)"),
        ("R-06", "Days already on loan cannot be selected"),
        ("R-09", "Requests blocked while the member has an overdue loan"),
        ("PAR-02", "Max loan duration · default 3 days · set by group admin"),
        ("PAR-03", "Owner answer time · default 48 h · platform parameter"),
        ("P-03", "Process “Borrow an item”, step 1"),
    ]
    y = 236
    for code, text in covers:
        chipsvg, w = id_chip(x0 + 28, y - 16, code)
        b += chipsvg + t(x0 + 118, y, text, 15, TEXT)
        y += 36
    # How it works
    b += rect(x0, 510, 802, 340, WHITE, BORDER, r=16)
    b += t(x0 + 28, 550, "How it works", 20, NAVY, 700)
    how = [
        "Opened from the nearby list (S-02) or from a shared link.",
        "The availability strip shows the next 7 days: green free, red already on loan. Tapping a free day pre-fills the request dates.",
        "“Request to borrow” opens S-05. It is disabled, with the reason shown, if the item is unavailable for the whole week or the user has an overdue loan (R-09).",
        "“Ask Giulia a question” opens a chat invitation; the owner must accept it before messages arrive.",
        "Empty state: no photo → category icon. Error state: item withdrawn → banner and back to the list.",
    ]
    y = 586
    for i, h in enumerate(how):
        b += f'<circle cx="{x0 + 40}" cy="{y - 5}" r="11" fill="{TEAL_L}"/>' + t(x0 + 40, y, str(i + 1), 12, TEAL, 700, "middle")
        for j, line in enumerate(wrap_lines(h, 92)):
            b += t(x0 + 62, y + j * 20, line, 14, TEXT)
        y += 20 * len(wrap_lines(h, 92)) + 14
    return svg(W, H, b, BG)


# ---------------------------------------------------------------- image 2: process
def process_section():
    W, H = 1440, 1100
    b = t(48, 62, "Processes › Borrowing", 14, MUTED, 500)
    b += t(48, 100, "P-03 · Borrow an item", 30, TEXT, 700)
    b += t(48, 128, "Example section from the Processes document of a fictional app (LendLoop).", 14, MUTED)
    # header card: actors etc.
    b += rect(48, 152, 1344, 96, WHITE, BORDER, r=16)
    meta = [("Actors", "Borrower, Owner"), ("Trigger", "Borrower needs an item"),
            ("Preconditions", "Same group, no overdue loan"), ("Rules", "R-05 to R-09"),
            ("Notifications", "N-03, N-04, N-05")]
    for i, (k, v) in enumerate(meta):
        x = 76 + i * 266
        b += t(x, 188, k.upper(), 11, MUTED, 700, extra='letter-spacing="1"')
        b += t(x, 214, v, 15, TEXT, 600)
    # steps + variants
    b += rect(48, 268, 860, 250, WHITE, BORDER, r=16)
    b += t(76, 304, "Steps", 18, NAVY, 700)
    steps = [
        "Borrower finds the item nearby, opens it and checks availability.",
        "Borrower chooses dates (max PAR-02) and sends the request.",
        "Owner is notified (N-03) and accepts, declines or suggests other dates.",
        "Both see the confirmed loan; a private chat opens with the confirmation (N-04).",
    ]
    y = 340
    for i, s in enumerate(steps):
        b += f'<circle cx="88" cy="{y - 5}" r="12" fill="{NAVY}"/>' + t(88, y, str(i + 1), 12, WHITE, 700, "middle")
        b += t(112, y, s, 15, TEXT)
        y += 40
    b += t(76, 500, "Outcome: loan in state Approved → Picked up → Returned (see domain model E-04).", 13, MUTED)
    b += rect(928, 268, 464, 250, AMBER_L, r=16)
    b += t(956, 304, "Variants", 18, "#8A5A12", 700)
    var = [("2a", "Borrower cancels before the answer → Cancelled."),
           ("3a", "Owner declines → Declined, borrower notified."),
           ("3b", "No answer within PAR-03 (48 h) → Expired, no penalty."),
           ("3c", "Owner suggests dates → borrower accepts or cancels.")]
    y = 336
    for code, s in var:
        b += t(956, y, code, 14, "#8A5A12", 700)
        for j, line in enumerate(wrap_lines(s, 44)):
            b += t(992, y + j * 20, line, 14, "#5C3C0C")
        y += 20 * len(wrap_lines(s, 44)) + 10
    # screen sequence
    b += t(48, 572, "Screen sequence", 22, TEXT, 700)
    order = ["S-02", "S-04", "S-05", "S-07", "S-08"]
    actions = ["Tap the item", "Request to borrow", "Send request", "Accept"]
    covers = ["Step 1", "Step 1", "Step 2", "Step 3 · owner", "Step 4"]
    scale = 0.52
    pw = 360 * scale
    gap = (1344 - 5 * pw) / 4
    for i, sid in enumerate(order):
        x = 48 + i * (pw + gap)
        name, fn = SCREENS[sid]
        b += f'<circle cx="{x + 16}" cy="{606}" r="14" fill="{TEAL}"/>' + t(x + 16, 611, str(i + 1), 13, WHITE, 700, "middle")
        b += t(x + 38, 604, f"{sid} · {name}", 14, TEXT, 700)
        b += t(x + 38, 622, covers[i], 12, MUTED)
        b += place(fn(), x, 640, scale)
        if i < len(order) - 1:
            ax1, ax2 = x + pw + 12, x + pw + gap - 12
            ay = 640 + 740 * scale / 2
            b += f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" stroke="{NAVY}" stroke-width="2.5" marker-end="url(#arr)"/>'
            for j, line in enumerate(wrap_lines(actions[i], 12)):
                b += t((ax1 + ax2) / 2, ay - 14 - 16 * (len(wrap_lines(actions[i], 12)) - 1 - j), line, 12, NAVY, 600, "middle")
    b += t(48, 1070, "Originals: S-02 Nearby items · S-04 Item detail · S-05 Borrow request · S-07 Owner requests · S-08 Loan confirmed (Mock-ups document) · Play it: navigable prototype",
           13, TEAL, 600)
    return svg(W, H, b, BG)


# ---------------------------------------------------------------- image 3: document map
def doc_map():
    W, H = 1280, 980
    b = t(640, 56, "AppFootings document map", 28, TEXT, 700, "middle")
    b += t(640, 84, "Each deliverable derives from the ones above it. Dots show what each complexity level includes.", 14, MUTED, 400, "middle")
    full, half, none = "full", "half", "none"
    rows = [
        [("R", "As-is report", "reverse mode only", [full, full, full]),
         ("1", "Brief", "the problem story", [full, full, full])],
        [("2", "Master", "functional spec · source of truth", [full, full, full])],
        [("3", "Visual guidelines", "style and components", [half, full, full]),
         ("4", "Mock-ups", "screens + clickable prototype", [half, full, full])],
        [("5", "Processes", "flows across screens", [none, full, full]),
         ("6", "Solution design", "states, roles, parameters…", [full, full, full])],
        [("7", "Compliance", "GDPR, AI Act, DSA…", [half, full, full]),
         ("8", "Business & roadmap", "separate track", [none, half, full])],
        [("9", "Architecture", "stack, modules, diagrams", [half, full, full])],
        [("10", "Test plan", "derived from all of the above", [full, full, full])],
        [("11", "Implementation prompts", "one per module / phase", [full, full, full])],
    ]
    bw, bh = 360, 72
    cx = 640
    y = 116
    centers = []
    for row in rows:
        n = len(row)
        xs = [cx - bw / 2] if n == 1 else [cx - bw - 20, cx + 20]
        rc = []
        for (num, name, sub, lv), x in zip(row, xs):
            master = name == "Master"
            dashed = 'stroke-dasharray="6 5"' if name.startswith("Business") or name.startswith("As-is") else ""
            fill = NAVY if master else WHITE
            stroke = NAVY if master else "#B9C4CF"
            b += rect(x, y, bw, bh, fill, stroke, r=14, sw=2 if master else 1.5, extra=dashed)
            fg = WHITE if master else TEXT
            sfg = "#C9D6E3" if master else MUTED
            b += f'<circle cx="{x + 30}" cy="{y + bh / 2}" r="15" fill="{TEAL if not master else WHITE}"/>'
            b += t(x + 30, y + bh / 2 + 5, num, 13, WHITE if not master else NAVY, 700, "middle")
            b += t(x + 56, y + 32, name, 17, fg, 700)
            b += t(x + 56, y + 54, sub, 12, sfg)
            # level dots
            for k, state in enumerate(lv):
                dx = x + bw - 66 + k * 20
                dy = y + 22
                col = WHITE if master else TEAL
                if state == full:
                    b += f'<circle cx="{dx}" cy="{dy}" r="6" fill="{col}"/>'
                elif state == half:
                    b += f'<circle cx="{dx}" cy="{dy}" r="6" fill="none" stroke="{col}" stroke-width="1.5"/>'
                    b += f'<path d="M{dx},{dy - 6} A6,6 0 0,0 {dx},{dy + 6} z" fill="{col}"/>'
                else:
                    b += f'<circle cx="{dx}" cy="{dy}" r="6" fill="none" stroke="{col}" stroke-width="1.5"/>'
                b += t(dx, y + 44, "ESC"[k], 9, sfg, 700, "middle")
            rc.append((x + bw / 2, y, y + bh))
        centers.append(rc)
        y += bh + 34
    # spine connectors between consecutive rows
    for a, c in zip(centers, centers[1:]):
        bottom = max(r[2] for r in a)
        top_c = min(r[1] for r in c)
        b += f'<line x1="{cx}" y1="{bottom + 2}" x2="{cx}" y2="{top_c - 3}" stroke="#8C9BAA" stroke-width="2" marker-end="url(#arr)"/>'
    # cascade arrow left
    top, bot = 160, centers[-1][0][2]
    b += f'<line x1="150" y1="{top}" x2="150" y2="{bot}" stroke="{TEAL}" stroke-width="6" marker-end="url(#arrT)"/>'
    b += t(130, (top + bot) / 2, "Changes cascade down", 16, TEAL, 700, "middle",
           f'transform="rotate(-90 130 {(top + bot) / 2})"')
    b += t(178, (top + bot) / 2, "write in the highest document, then align every dependent one", 12, MUTED, 400, "middle",
           f'transform="rotate(-90 178 {(top + bot) / 2})"')
    # discoveries arrow right
    b += f'<line x1="1130" y1="{bot}" x2="1130" y2="{top + 70}" stroke="{AMBER}" stroke-width="6" marker-end="url(#arrA)"/>'
    b += t(1150, (top + bot) / 2, "Discoveries flow up to the Master", 16, "#B87713", 700, "middle",
           f'transform="rotate(90 1150 {(top + bot) / 2})"')
    b += t(1102, (top + bot) / 2, "a gap found downstream is fixed at the source first", 12, MUTED, 400, "middle",
           f'transform="rotate(90 1102 {(top + bot) / 2})"')
    # legend
    ly = H - 24
    b += t(400, ly, "E / S / C = Essential / Standard / Complete", 12, MUTED, 600, "middle")
    b += f'<circle cx="620" cy="{ly - 4}" r="6" fill="{TEAL}"/>' + t(632, ly, "required", 12, MUTED)
    b += f'<circle cx="720" cy="{ly - 4}" r="6" fill="none" stroke="{TEAL}" stroke-width="1.5"/>' \
         f'<path d="M720,{ly - 10} A6,6 0 0,0 720,{ly + 2} z" fill="{TEAL}"/>' + t(732, ly, "light / recommended", 12, MUTED)
    b += f'<circle cx="880" cy="{ly - 4}" r="6" fill="none" stroke="{TEAL}" stroke-width="1.5"/>' + t(892, ly, "only if a trigger applies", 12, MUTED)
    return svg(W, H, b, WHITE)


# ---------------------------------------------------------------- image 4: alignment report
def alignment_report():
    W, H = 1280, 600
    b = t(48, 60, "Every change ends with an alignment report", 26, TEXT, 700)
    b += t(48, 88, "Example: the group decides the maximum loan duration becomes 5 days and can be extended once by the owner.", 14, MUTED)
    # left: the change
    b += rect(48, 116, 360, 440, NAVY, r=16)
    b += t(76, 156, "Change", 13, "#9FB4C9", 700, extra='letter-spacing="1"')
    for j, line in enumerate(["Max loan 3 → 5 days;", "owner can extend once"]):
        b += t(76, 190 + j * 28, line, 20, WHITE, 700)
    b += t(76, 262, "Written first in", 13, "#9FB4C9")
    b += t(76, 288, "Master › F-03, R-05, new R-11", 16, WHITE, 600)
    b += t(76, 336, "Impacts traced through", 13, "#9FB4C9")
    for j, line in enumerate(["• traceability matrix row F-03", "• copies table (S-04, S-05)", "• parameters PAR-02, new PAR-07"]):
        b += t(76, 362 + j * 26, line, 14, WHITE)
    b += t(76, 470, "New open point", 13, "#9FB4C9")
    b += t(76, 494, "OP-13: who is notified of an extension?", 14, AMBER, 600)
    # right: report
    b += rect(436, 116, 796, 440, WHITE, BORDER, r=16)
    rows = [
        ("ok", "Master", "R-05 updated, R-11 added (OP-12: extension only if days are free)"),
        ("ok", "Mock-ups", "S-04 chip “Max 5 days”, S-05 hint text, S-08 “Extend” button"),
        ("ok", "Processes", "P-03 step 2, new variant 4a “Extension”; screen copies in P-03"),
        ("ok", "Solution design", "PAR-02 default 5, PAR-07 max extensions = 1; loan states"),
        ("ok", "Test plan", "T-031 boundary 5/6 days, new T-048 extension"),
        ("todo", "Business & roadmap", "check whether extensions are a paid feature"),
        ("todo", "Prompts", "PR-05 Borrowing to regenerate after OP-13"),
    ]
    b += t(464, 154, "Alignment report", 18, NAVY, 700)
    y = 196
    for status, doc, what in rows:
        if status == "ok":
            b += f'<circle cx="474" cy="{y - 5}" r="10" fill="{GREEN_L}"/>' \
                 f'<path d="M469 {y - 5} L473 {y - 1} L480 {y - 10}" fill="none" stroke="{GREEN}" stroke-width="2.5"/>'
        else:
            b += f'<circle cx="474" cy="{y - 5}" r="10" fill="{AMBER_L}"/>' + t(474, y, "!", 13, "#B87713", 800, "middle")
        b += t(496, y, doc, 15, TEXT, 700)
        b += t(680, y, what, 14, TEXT if status == "ok" else "#8A5A12")
        y += 44
    b += f'<line x1="464" y1="{y - 18}" x2="1204" y2="{y - 18}" stroke="{BORDER}"/>'
    b += t(464, y + 10, "Not yet aligned items stay “needs alignment” in the Project Register until closed.", 13, MUTED)
    return svg(W, H, b, BG)


# ---------------------------------------------------------------- image 5: two more mock-ups
def screens_gallery():
    W, H = 1280, 860
    b = t(48, 62, "Mock-ups › LendLoop", 14, MUTED, 500)
    b += t(48, 100, "Two more screens from the example", 30, TEXT, 700)
    b += t(48, 128, "Drawn with the Visual guidelines; every screen links back to features, rules and processes by ID.", 14, MUTED)
    cols = [
        ("S-02 · Nearby items", screen_nearby(), [
            ("F-03", "entry point to borrowing"),
            ("PAR-01", "search radius, default 2 km"),
            ("R-06", "status chip: on loan until…"),
            ("P-03", "step 1, find the item"),
        ]),
        ("S-06 · My loans", screen_my_loans("Approved"), [
            ("F-05", "loan lifecycle"),
            ("E-03", "request states as chips"),
            ("E-04", "loan states as chips"),
            ("N-06", "return reminder, shown inline"),
            ("P-03", "outcome of variant 3a"),
        ]),
    ]
    for i, (title, scr, covers) in enumerate(cols):
        x0 = 48 + i * 616
        b += t(x0, 178, title, 20, NAVY, 700)
        b += place(scr, x0, 196, 0.86)
        tx = x0 + 330
        b += t(tx, 236, "What it covers", 14, TEXT, 700)
        y = 270
        for code, text in covers:
            chipsvg, w = id_chip(tx, y - 16, code)
            b += chipsvg
            for j, line in enumerate(wrap_lines(text, 22)):
                b += t(tx, y + 26 + j * 18, line, 13, TEXT)
            y += 26 + 18 * len(wrap_lines(text, 22)) + 18
    return svg(W, H, b, BG)


# ---------------------------------------------------------------- navigable prototype (P-03)
HOT = {
    "item": (24, NEARBY_CARD_Y0, 312, NEARBY_CARD_H),
    "request": (24, 636, 312, 48),
    "send": (24, 636, 312, 48),
    "accept": (186, 334, 134, 44),
    "decline": (40, 334, 134, 44),
}

PROTO_SCREENS = {
    "S-02": ("S-02 · Nearby items", screen_nearby),
    "S-04": ("S-04 · Item detail", screen_item_detail),
    "S-05": ("S-05 · Borrow request", screen_request),
    "S-07": ("S-07 · Owner requests", screen_owner),
    "S-08": ("S-08 · Loan confirmed", screen_confirmed),
    "S-06d": ("S-06 · My loans (after decline)", lambda: screen_my_loans("Declined")),
}

_COMMON = [
    {"screen": "S-02", "actor": "Borrower", "step": "1", "text": "Marco finds a drill in the nearby list and opens it.",
     "hot": [{"r": HOT["item"], "label": "Tap the item", "next": 1}]},
    {"screen": "S-04", "actor": "Borrower", "step": "1", "text": "He checks the availability strip (R-06) and asks to borrow it.",
     "hot": [{"r": HOT["request"], "label": "Request to borrow", "next": 2}]},
    {"screen": "S-05", "actor": "Borrower", "step": "2", "text": "He picks the dates, up to PAR-02 (3 days), and sends the request.",
     "hot": [{"r": HOT["send"], "label": "Send request", "next": 3}]},
]
PATHS = {
    "main": {"title": "P-03 · Borrow an item", "steps": _COMMON + [
        {"screen": "S-07", "actor": "Owner", "step": "3", "text": "Giulia gets the request (N-03) and accepts it.",
         "hot": [{"r": HOT["accept"], "label": "Accept", "next": 4}]},
        {"screen": "S-08", "actor": "Borrower", "step": "4",
         "text": "Loan confirmed. A private chat opens with the confirmation (N-04). End of process.", "hot": []},
    ]},
    "3a": {"title": "P-03 · Variant 3a: owner declines", "steps": _COMMON + [
        {"screen": "S-07", "actor": "Owner", "step": "3a", "text": "Giulia gets the request (N-03) and declines it.",
         "hot": [{"r": HOT["decline"], "label": "Decline", "next": 4}]},
        {"screen": "S-06d", "actor": "Borrower", "step": "3a",
         "text": "The request is Declined and Marco is notified (N-05). End of variant.", "hot": []},
    ]},
}


def build_prototype(path):
    import json
    screens = {k: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 740">{fn()}</svg>'
               for k, (_, fn) in PROTO_SCREENS.items()}
    names = {k: n for k, (n, _) in PROTO_SCREENS.items()}
    data = json.dumps({"screens": screens, "names": names, "paths": PATHS})
    html = PROTO_TEMPLATE.replace("/*DATA*/", data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)


PROTO_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LendLoop · Navigable prototype</title>
<style>
  :root { --navy:#0F2A44; --teal:#0E8C8C; --teal-l:#E3F3F3; --bg:#F5F7FA; --ink:#1B2430; --muted:#6B7785; --border:#DDE3EA; --amber:#E8A33D; }
  * { box-sizing: border-box; }
  body { margin:0; font-family: Inter, system-ui, -apple-system, "Segoe UI", sans-serif; background:var(--bg); color:var(--ink); }
  header { padding:20px 32px; background:#fff; border-bottom:1px solid var(--border); display:flex; flex-wrap:wrap; gap:8px 24px; align-items:baseline; }
  header h1 { margin:0; font-size:20px; }
  header span { color:var(--muted); font-size:13px; }
  main { display:flex; flex-wrap:wrap; gap:32px; padding:28px 32px; align-items:flex-start; justify-content:center; }
  .panel { flex:1 1 340px; max-width:440px; background:#fff; border:1px solid var(--border); border-radius:16px; padding:22px; }
  .panel h2 { font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--muted); margin:18px 0 8px; }
  .panel h2:first-child { margin-top:0; }
  select, button { font:inherit; }
  select { width:100%; padding:10px 12px; border-radius:10px; border:1px solid var(--border); background:#fff; }
  ol { list-style:none; padding:0; margin:0; }
  ol li { display:flex; gap:10px; padding:9px 10px; border-radius:10px; font-size:14px; line-height:1.4; color:var(--muted); cursor:pointer; }
  ol li .n { flex:0 0 34px; height:24px; border-radius:12px; background:var(--bg); color:var(--navy); font-weight:700; font-size:12px; display:flex; align-items:center; justify-content:center; }
  ol li.done { color:var(--ink); }
  ol li.current { background:var(--teal-l); color:var(--ink); font-weight:600; }
  ol li.current .n { background:var(--teal); color:#fff; }
  .actor { display:inline-flex; gap:8px; align-items:center; padding:6px 12px; border-radius:16px; background:var(--navy); color:#fff; font-size:13px; font-weight:600; }
  .controls { display:flex; gap:8px; flex-wrap:wrap; margin-top:14px; }
  .controls button { padding:9px 14px; border-radius:10px; border:1px solid var(--teal); background:#fff; color:var(--teal); font-weight:600; cursor:pointer; }
  .controls button.primary { background:var(--teal); color:#fff; }
  label.toggle { display:flex; gap:8px; align-items:center; font-size:14px; margin-top:12px; cursor:pointer; }
  .stage { position:relative; flex:0 0 auto; }
  .phone { position:relative; width:360px; max-width:86vw; aspect-ratio:360/740; }
  .phone svg { width:100%; height:100%; display:block; }
  .hot { position:absolute; border-radius:12px; border:0; background:transparent; cursor:pointer; padding:0; }
  .hot:focus-visible { outline:3px solid var(--amber); outline-offset:2px; }
  .show .hot, .hint .hot { background:rgba(232,163,61,.28); box-shadow:0 0 0 3px var(--amber) inset; }
  .hint .hot { animation: pulse .9s ease-in-out 2; }
  @keyframes pulse { 50% { background:rgba(232,163,61,.05); } }
  .toast { position:absolute; left:50%; top:16px; transform:translateX(-50%); background:var(--navy); color:#fff; padding:10px 16px; border-radius:12px; font-size:14px; font-weight:600; opacity:0; transition:opacity .3s; pointer-events:none; white-space:nowrap; }
  .toast.on { opacity:1; }
  .caption { text-align:center; font-size:13px; color:var(--muted); margin-top:10px; }
  .map { display:flex; gap:10px; flex-wrap:wrap; }
  .map button { width:64px; padding:0; border:2px solid transparent; border-radius:10px; background:none; cursor:pointer; }
  .map button.on { border-color:var(--teal); }
  .map svg { width:100%; display:block; }
  .note { font-size:12px; color:var(--muted); margin-top:16px; line-height:1.5; }
  .end { margin-top:12px; padding:10px 12px; border-radius:10px; background:var(--teal-l); color:var(--teal); font-size:14px; font-weight:600; display:none; }
</style>
</head>
<body>
<header>
  <h1>LendLoop · Navigable prototype</h1>
  <span>Generated from the Mock-ups and Processes of the AppFootings worked example · fictional app</span>
</header>
<main>
  <section class="panel" aria-label="Process">
    <h2>Process to play</h2>
    <select id="path" aria-label="Process to play"></select>
    <h2>Steps</h2>
    <ol id="steps"></ol>
    <div class="end" id="end">End of the process. Restart or choose another path.</div>
    <h2>Acting now</h2>
    <span class="actor" id="actor"></span>
    <div class="controls">
      <button id="back">Back</button>
      <button id="restart" class="primary">Restart</button>
    </div>
    <label class="toggle"><input type="checkbox" id="show"> Show clickable areas</label>
    <h2>Screen map</h2>
    <div class="map" id="map"></div>
    <p class="note">Tap the highlighted elements on the phone to move through the process. Tapping anywhere else shows where you can tap. The screen map opens any screen outside the process.</p>
  </section>
  <section class="stage" aria-label="Phone">
    <div class="phone" id="phone"></div>
    <div class="toast" id="toast"></div>
    <div class="caption" id="caption"></div>
  </section>
</main>
<script>
const D = /*DATA*/;
const $ = (id) => document.getElementById(id);
let pathKey = "main", idx = 0, hist = [], free = null;

function init() {
  for (const [k, p] of Object.entries(D.paths)) {
    const o = document.createElement("option"); o.value = k; o.textContent = p.title; $("path").appendChild(o);
  }
  for (const k of Object.keys(D.screens)) {
    const b = document.createElement("button"); b.innerHTML = D.screens[k]; b.title = D.names[k]; b.dataset.k = k;
    b.onclick = () => { free = k; render(); }; $("map").appendChild(b);
  }
  $("path").onchange = (e) => { pathKey = e.target.value; restart(); };
  $("back").onclick = () => { if (free) { free = null; } else if (hist.length) { idx = hist.pop(); } render(); };
  $("restart").onclick = restart;
  $("show").onchange = (e) => $("phone").classList.toggle("show", e.target.checked);
  $("phone").addEventListener("click", (e) => {
    if (e.target.classList.contains("hot")) return;
    const ph = $("phone"); ph.classList.remove("hint"); void ph.offsetWidth; ph.classList.add("hint");
  });
  render();
}
function restart() { idx = 0; hist = []; free = null; render(); }
function go(next) {
  const prev = D.paths[pathKey].steps[idx];
  hist.push(idx); idx = next;
  const cur = D.paths[pathKey].steps[idx];
  if (cur.actor !== prev.actor) toast("Now acting: " + cur.actor);
  render();
}
function toast(msg) { const t = $("toast"); t.textContent = msg; t.classList.add("on"); setTimeout(() => t.classList.remove("on"), 1600); }
function render() {
  const path = D.paths[pathKey], st = path.steps[idx];
  const key = free || st.screen;
  const ph = $("phone"); ph.innerHTML = D.screens[key];
  if (!free) {
    for (const h of st.hot) {
      const [x, y, w, hh] = h.r, b = document.createElement("button");
      b.className = "hot"; b.setAttribute("aria-label", h.label); b.title = h.label;
      Object.assign(b.style, { left: x / 3.6 + "%", top: y / 7.4 + "%", width: w / 3.6 + "%", height: hh / 7.4 + "%" });
      b.onclick = () => go(h.next); ph.appendChild(b);
    }
  }
  $("caption").textContent = D.names[key] + (free ? " · free view (Back returns to the process)" : "");
  $("actor").textContent = free ? "—" : st.actor;
  $("end").style.display = !free && st.hot.length === 0 ? "block" : "none";
  const ol = $("steps"); ol.innerHTML = "";
  path.steps.forEach((s, i) => {
    const li = document.createElement("li");
    li.className = i === idx && !free ? "current" : (i < idx ? "done" : "");
    li.innerHTML = '<span class="n">' + s.step + '</span><span>' + s.text + ' <em style="color:var(--muted);font-style:normal">(' + D.names[s.screen].split(" · ")[0] + ', ' + s.actor + ')</em></span>';
    ol.appendChild(li);
  });
  for (const b of $("map").children) b.classList.toggle("on", b.dataset.k === key);
}
init();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- walkthrough GIF frames (P-03 main path)
def walkthrough_frames():
    frames = []
    steps = PATHS["main"]["steps"]
    for i, st in enumerate(steps):
        W, H = 960, 680
        b = t(40, 52, "Navigable prototype · P-03 Borrow an item", 22, TEXT, 700)
        b += t(40, 78, "LendLoop example: mock-ups linked by the process, playable before anything is built", 13, MUTED)
        sc = 0.78
        b += place(PROTO_SCREENS[st["screen"]][1](), 40, 100, sc)
        for h in st["hot"]:
            x, y, w, hh = h["r"]
            b += rect(40 + x * sc - 4, 100 + y * sc - 4, w * sc + 8, hh * sc + 8, "rgba(232,163,61,0.25)", AMBER, r=12, sw=3)
            b += f'<circle cx="{40 + (x + w * 0.7) * sc}" cy="{100 + (y + hh / 2) * sc}" r="14" fill="{AMBER}" opacity="0.9"/>'
        px = 380
        b += rect(px, 100, 540, 540, WHITE, BORDER, r=16)
        b += t(px + 24, 138, "ACTING NOW", 11, MUTED, 700, extra='letter-spacing="1"')
        b += rect(px + 24, 150, 16 + 9 * len(st["actor"]), 30, NAVY, r=15) + t(px + 32, 170, st["actor"], 13, WHITE, 700)
        if i > 0 and steps[i - 1]["actor"] != st["actor"]:
            b += t(px + 40 + 9 * len(st["actor"]) + 16, 170, "← role switch", 13, "#B87713", 700)
        b += t(px + 24, 214, "STEPS", 11, MUTED, 700, extra='letter-spacing="1"')
        y = 244
        for j, s2 in enumerate(steps):
            cur = j == i
            lines = wrap_lines(s2["text"], 52)
            hgt = 16 + 20 * len(lines)
            if cur:
                b += rect(px + 16, y - 20, 508, hgt + 6, TEAL_L, r=10)
            b += rect(px + 26, y - 14, 30, 22, TEAL if cur else BG, r=11) + t(px + 41, y + 2, s2["step"], 12, WHITE if cur else NAVY, 700, "middle")
            for k, line in enumerate(lines):
                b += t(px + 68, y + 2 + k * 20, line, 14, TEXT if j <= i else MUTED, 600 if cur else 400)
            y += hgt + 14
        if st["hot"]:
            b += t(px + 24, 620, "Next tap: " + st["hot"][0]["label"], 14, "#B87713", 700)
        else:
            b += t(px + 24, 620, "End of process", 14, TEAL, 700)
        frames.append(svg(W, H, b, BG))
    return frames


# ---------------------------------------------------------------- analysis loop animation
LOOP_DOCS = ["Brief", "Master", "Mock-ups", "Processes", "Prototype", "Solution design", "Test plan", "Prompts"]
ST_COL = {  # status -> (fill, stroke, text, badge)
    "ok": (WHITE, "#B9C4CF", TEXT, ("aligned", GREEN, GREEN_L)),
    "check": (AMBER_L, AMBER, TEXT, ("checking", "#8A5A12", AMBER_L)),
    "conflict": ("#FBE3E3", RED, TEXT, ("conflict", RED, "#F4D9D9")),
    "update": (TEAL_L, TEAL, TEXT, ("updating", TEAL, WHITE)),
    "done": (GREEN_L, GREEN, TEXT, ("updated", GREEN, WHITE)),
    "wait": (WHITE, "#B9C4CF", MUTED, ("to align", "#8A5A12", AMBER_L)),
}

LOOP_STEPS = [
    {"t": "A change arrives",
     "x": ["“Max loan 5 days, and the owner can extend it once.”",
           "Every change starts from the highest document it touches: the Master."],
     "st": {}, "arrow": ("in", "Master")},
    {"t": "Check coherence first",
     "x": ["Before writing anything, the change is checked against everything",
           "already documented: rules, states, parameters, screens, processes."],
     "st": {"Master": "check"}},
    {"t": "Conflict found: raise it",
     "x": ["An extension can clash with R-06: the next days may already be",
           "reserved by someone else. Logged as OP-12 and brought to you",
           "with a recommendation. Nothing is written yet."],
     "st": {"Master": "conflict"}, "bubble": "OP-12 · Extend into reserved days?"},
    {"t": "You decide, the Master is updated",
     "x": ["Decision: extension only if the next days are free.",
           "R-05 updated, R-11 added. The Master is coherent again."],
     "st": {"Master": "done"}, "bubble_user": "Only if the days are free."},
    {"t": "Cascade down",
     "x": ["Impacts are traced by ID and every dependent document is",
           "updated in order. Mock-ups: S-04 chip, new “Extend” on S-08."],
     "st": {"Master": "done", "Mock-ups": "update", "Processes": "wait", "Prototype": "wait",
            "Solution design": "wait", "Test plan": "wait", "Prompts": "wait"}, "arrow": ("down", "Mock-ups")},
    {"t": "A discovery flows up",
     "x": ["Updating P-03, a new step needs to notify the borrower about",
           "the extension, but the Master never says who is notified.",
           "The cascade pauses; the gap goes up as OP-13."],
     "st": {"Master": "conflict", "Mock-ups": "done", "Processes": "conflict", "Prototype": "wait",
            "Solution design": "wait", "Test plan": "wait", "Prompts": "wait"}, "arrow": ("up", "Processes"),
     "bubble": "OP-13 · Who is notified of an extension?"},
    {"t": "Decided at the source",
     "x": ["Decision: the borrower gets a push and a chat message (N-08).",
           "Written in the Master first, then the cascade resumes."],
     "st": {"Master": "done", "Mock-ups": "done", "Processes": "update", "Prototype": "wait",
            "Solution design": "wait", "Test plan": "wait", "Prompts": "wait"}, "bubble_user": "Push + chat message.",
     "arrow": ("down", "Processes")},
    {"t": "Cascade resumes",
     "x": ["P-03 gets variant 4a, the prototype is regenerated,",
           "PAR-02 becomes 5, PAR-07 and N-08 are added."],
     "st": {"Master": "done", "Mock-ups": "done", "Processes": "done", "Prototype": "done",
            "Solution design": "update", "Test plan": "wait", "Prompts": "wait"}, "arrow": ("down", "Solution design")},
    {"t": "Tests and prompts follow",
     "x": ["T-031 now tests 5/6 days, T-048 covers the extension.",
           "PR-05 Borrowing is regenerated with the new rules."],
     "st": {"Master": "done", "Mock-ups": "done", "Processes": "done", "Prototype": "done",
            "Solution design": "done", "Test plan": "done", "Prompts": "update"}, "arrow": ("down", "Prompts")},
    {"t": "Consistent again",
     "x": ["A last pass finds nothing new. The alignment report lists what",
           "changed in each document. Every change runs this loop."],
     "st": {d: "done" for d in LOOP_DOCS if d != "Brief"}, "final": True},
]


def loop_frame(i):
    W, H = 1200, 720
    step = LOOP_STEPS[i]
    b = t(40, 52, "How AppFootings keeps the analysis coherent", 24, TEXT, 700)
    b += t(40, 80, "Example from LendLoop: one change, one conflict, one discovery, and everything aligned again", 14, MUTED)
    bx, bw, bh, gap, y0 = 120, 300, 54, 14, 104
    pos = {}
    for k, d in enumerate(LOOP_DOCS):
        y = y0 + k * (bh + gap)
        pos[d] = y
        stt = step["st"].get(d, "ok")
        fill, stroke, fg, (lab, bfg, bbg) = ST_COL[stt]
        master = d == "Master"
        b += rect(bx, y, bw, bh, fill, stroke, r=12, sw=3 if stt != "ok" else 1.5)
        b += t(bx + 18, y + 33, d, 16, fg, 700 if master else 600)
        if master:
            b += t(bx + 18 + 9.5 * len(d) + 8, y + 33, "source of truth", 11, MUTED, 600)
        w = 7.2 * len(lab) + 18
        b += rect(bx + bw - w - 12, y + 15, w, 24, bbg, bfg, r=12, sw=1) + t(bx + bw - 12 - w / 2, y + 31, lab, 11, bfg, 700, "middle")
    # spine
    for k in range(len(LOOP_DOCS) - 1):
        ya = pos[LOOP_DOCS[k]] + bh
        b += f'<line x1="{bx + bw / 2}" y1="{ya + 1}" x2="{bx + bw / 2}" y2="{ya + gap - 1}" stroke="#C9D1DA" stroke-width="2"/>'
    # arrows
    arr = step.get("arrow")
    mid = lambda d: pos[d] + bh / 2
    if arr:
        kind, target = arr
        if kind == "in":
            b += f'<line x1="40" y1="{mid("Master")}" x2="{bx - 8}" y2="{mid("Master")}" stroke="{NAVY}" stroke-width="4" marker-end="url(#lN)"/>'
            b += t(36, mid("Master") - 12, "change", 12, NAVY, 700)
        elif kind == "down":
            x = bx - 40
            b += f'<line x1="{x}" y1="{mid("Master")}" x2="{x}" y2="{mid(target)}" stroke="{TEAL}" stroke-width="5" marker-end="url(#lT)"/>'
            b += f'<line x1="{x}" y1="{mid("Master")}" x2="{bx - 4}" y2="{mid("Master")}" stroke="{TEAL}" stroke-width="3"/>'
            b += t(x - 16, (mid("Master") + mid(target)) / 2, "cascade", 12, TEAL, 700, "middle",
                   f'transform="rotate(-90 {x - 16} {(mid("Master") + mid(target)) / 2})"')
        elif kind == "up":
            x = bx + bw + 40
            b += f'<line x1="{x}" y1="{mid(target)}" x2="{x}" y2="{mid("Master") + 4}" stroke="{RED}" stroke-width="5" marker-end="url(#lR)"/>'
            b += f'<line x1="{bx + bw + 4}" y1="{mid(target)}" x2="{x}" y2="{mid(target)}" stroke="{RED}" stroke-width="3"/>'
            b += t(x + 20, (mid("Master") + mid(target)) / 2, "discovery goes up", 12, RED, 700, "middle",
                   f'transform="rotate(90 {x + 20} {(mid("Master") + mid(target)) / 2})"')
    # right panel
    px, py, pw, ph = 520, 104, 640, 530
    b += rect(px, py, pw, ph, WHITE, BORDER, r=16)
    b += t(px + 28, py + 40, f"STEP {i + 1} OF {len(LOOP_STEPS)}", 12, MUTED, 700, extra='letter-spacing="1"')
    b += t(px + 28, py + 80, step["t"], 26, TEXT, 700)
    for j, line in enumerate(step["x"]):
        b += t(px + 28, py + 122 + j * 26, line, 16, TEXT)
    yb = py + 122 + len(step["x"]) * 26 + 30
    if step.get("bubble"):
        txt = step["bubble"]
        w = 9 * len(txt) + 60
        b += rect(px + 28, yb, w, 54, "#FBE3E3", RED, r=14, sw=1.5)
        b += t(px + 50, yb + 22, "AppFootings asks you", 11, RED, 700)
        b += t(px + 50, yb + 42, txt, 15, TEXT, 600)
        yb += 74
    if step.get("bubble_user"):
        txt = step["bubble_user"]
        w = 9 * len(txt) + 60
        b += rect(px + pw - 28 - w, yb, w, 54, NAVY, r=14)
        b += t(px + pw - 28 - w + 22, yb + 22, "You decide", 11, "#9FB4C9", 700)
        b += t(px + pw - 28 - w + 22, yb + 42, txt, 15, WHITE, 600)
        yb += 74
    if step.get("final"):
        rows = [("Master", "R-05, R-11, N-08"), ("Mock-ups", "S-04, S-08"), ("Processes", "P-03 variant 4a"),
                ("Prototype", "regenerated"), ("Solution design", "PAR-02, PAR-07, N-08"), ("Test plan", "T-031, T-048"),
                ("Prompts", "PR-05")]
        b += t(px + 28, yb, "Alignment report", 15, NAVY, 700)
        for j, (d, w_) in enumerate(rows):
            yy = yb + 28 + j * 24
            b += f'<circle cx="{px + 38}" cy="{yy - 5}" r="7" fill="{GREEN}"/>' + t(px + 56, yy, d, 14, TEXT, 700) + t(px + 220, yy, w_, 14, MUTED)
    # progress dots
    for k in range(len(LOOP_STEPS)):
        b += f'<circle cx="{px + 28 + k * 22}" cy="{py + ph - 28}" r="6" fill="{TEAL if k <= i else BORDER}"/>'
    # legend
    ly = 690
    items = [("aligned / updated", GREEN), ("checking", AMBER), ("conflict", RED), ("updating", TEAL), ("to align", None)]
    x = 120
    for lab, col in items:
        if col:
            b += f'<circle cx="{x}" cy="{ly - 5}" r="7" fill="{col}"/>'
        else:
            b += f'<circle cx="{x}" cy="{ly - 5}" r="6" fill="{AMBER_L}" stroke="#8A5A12" stroke-width="1.5"/>'
        b += t(x + 14, ly, lab, 13, MUTED)
        x += 40 + 7.5 * len(lab)
    out = svg(W, H, b, BG)
    mk = "".join(f'<marker id="{i}" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" refX="13" refY="8" orient="auto">'
                 f'<path d="M0,0 L16,8 L0,16 z" fill="{c}"/></marker>' for i, c in (("lT", TEAL), ("lR", RED), ("lN", NAVY)))
    return out.replace('</defs>', mk + '</defs>')


# ---------------------------------------------------------------- hero: the name explained (also the GitHub social preview)
EARTH, EARTH_D, STONE, STONE_D = "#E9E1D3", "#CDBFA6", "#D9DFE6", "#B9C4CF"


def mini_phone(x, y, sc):
    g = f'<g transform="translate({x},{y}) scale({sc})">'
    g += rect(0, 0, 120, 236, WHITE, NAVY, r=20, sw=4) + rect(44, 10, 32, 8, NAVY, r=4)
    g += rect(14, 34, 92, 22, TEAL_L, r=6)
    for yy in (64, 110, 156):
        g += rect(14, yy, 92, 40, WHITE, BORDER, r=6)
    return g + rect(14, 206, 92, 18, TEAL, r=6) + '</g>'


def mini_browser(x, y, sc):
    g = f'<g transform="translate({x},{y}) scale({sc})">'
    g += rect(0, 0, 300, 190, WHITE, NAVY, r=12, sw=4) + f'<line x1="0" y1="30" x2="300" y2="30" stroke="{NAVY}" stroke-width="3"/>'
    for i, c in enumerate([RED, AMBER, GREEN]):
        g += f'<circle cx="{18 + i * 16}" cy="15" r="5" fill="{c}"/>'
    g += rect(16, 44, 70, 130, TEAL_L, r=6) + rect(98, 44, 186, 40, WHITE, BORDER, r=6)
    g += rect(98, 92, 90, 82, WHITE, BORDER, r=6) + rect(196, 92, 88, 82, WHITE, BORDER, r=6)
    return g + '</g>'


def hero():
    G = 300
    b = rect(0, G, 1280, 340, EARTH, r=0)
    for i in range(-400, 1280, 34):
        b += f'<line x1="{i}" y1="640" x2="{i + 340}" y2="{G}" stroke="{EARTH_D}" stroke-width="1" opacity="0.6"/>'
    b += f'<line x1="0" y1="{G}" x2="1280" y2="{G}" stroke="#8C7A5B" stroke-width="3"/>'
    b += t(60, 70, "AppFootings", 40, TEXT, 800) + t(60, 100, "Users see the app. It stands on what you can't see.", 17, MUTED, 500)
    b += t(60, 128, "A Claude skill that analyses your app before you build it.", 14, MUTED)
    b += t(60, G - 16, "WHAT USERS SEE", 12, MUTED, 700, extra='letter-spacing="2"')
    b += t(60, G + 30, "WHAT IT STANDS ON", 12, "#6B5A3C", 700, extra='letter-spacing="2"')
    b += rect(410, G - 14, 560, 14, NAVY, r=2)
    b += mini_browser(450, G - 14 - 160, 0.82) + mini_phone(760, G - 14 - 196, 0.82)
    b += t(872, 196, "Your app", 15, NAVY, 700) + t(872, 214, "web and mobile", 12, MUTED)
    piers = [("Visual", "guidelines"), ("Mock-ups", "& prototype"), ("Processes", ""), ("Solution", "design"),
             ("Compliance", ""), ("Architec-", "ture"), ("Test plan", "")]
    for k, (a, c) in enumerate(piers):
        x = 450 + k * 80
        b += rect(x - 13, G, 26, 150, STONE, STONE_D, r=2)
        b += f'<path d="M{x - 36},{G + 190} L{x - 24},{G + 150} L{x + 24},{G + 150} L{x + 36},{G + 190} z" fill="{STONE}" stroke="{STONE_D}"/>'
        b += t(x, G + 212, a, 12, "#3D3220", 700, "middle")
        if c:
            b += t(x, G + 228, c, 12, "#3D3220", 700, "middle")
    b += rect(400, G + 248, 580, 40, TEAL, r=4) + t(690, G + 274, "Master · source of truth", 16, WHITE, 700, "middle")
    b += rect(360, G + 288, 660, 30, "#C2B190", r=2) + t(690, G + 309, "Brief · the problem story", 13, "#3D3220", 700, "middle")
    b += t(1000, G + 70, "Implementation prompts", 13, NAVY, 700) + t(1000, G + 88, "carry it all into the build", 12, MUTED)
    b += f'<path d="M995,{G + 64} C975,{G + 40} 975,{G + 10} 972,{G - 6}" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>'
    return svg(1280, 640, b, "#EEF3F8")


images = {
    "document-map": doc_map(),
    "example-mockup": mockup_section(),
    "example-process": process_section(),
    "example-alignment-report": alignment_report(),
    "example-screens": screens_gallery(),
    "hero": hero(),
}
import shutil
import subprocess

converter = shutil.which("rsvg-convert")
for name, content in images.items():
    svg_path = os.path.join(OUT, name + ".svg")
    with open(svg_path, "w") as f:
        f.write(content)
    if converter:
        subprocess.run([converter, "-z", "1.5", svg_path, "-o", os.path.join(OUT, name + ".png")], check=True)
if converter:  # GitHub social preview: exactly 1280x640
    subprocess.run([converter, os.path.join(OUT, "hero.svg"), "-o", os.path.join(OUT, "social-preview.png")], check=True)
if not converter:
    print("rsvg-convert not found: SVGs written, PNGs not regenerated (install librsvg).")

# navigable prototype of the worked example
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
build_prototype(os.path.join(ROOT, "examples", "lendloop", "prototype", "index.html"))

# walkthrough GIF (needs rsvg-convert and ImageMagick)
magick = shutil.which("magick") or shutil.which("convert")
if converter and magick:
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        pngs = []
        for i, fr in enumerate(walkthrough_frames()):
            sp, pp = os.path.join(tmp, f"f{i}.svg"), os.path.join(tmp, f"f{i}.png")
            open(sp, "w").write(fr)
            subprocess.run([converter, sp, "-o", pp], check=True)
            pngs.append(pp)
        cmd = [magick, "-delay", "220", "-loop", "0"] + pngs + ["+dither", "-colors", "160",
                                                                  os.path.join(OUT, "prototype-walkthrough.gif")]
        subprocess.run(cmd, check=True)
    with tempfile.TemporaryDirectory() as tmp:
        args = [magick, "-loop", "0"]
        for i in range(len(LOOP_STEPS)):
            sp, pp = os.path.join(tmp, f"l{i}.svg"), os.path.join(tmp, f"l{i}.png")
            open(sp, "w").write(loop_frame(i))
            subprocess.run([converter, sp, "-o", pp], check=True)
            delay = "500" if i == len(LOOP_STEPS) - 1 else "300"
            args += ["-delay", delay, pp]
        args += ["+dither", "-colors", "160", os.path.join(OUT, "analysis-loop.gif")]
        subprocess.run(args, check=True)
        # static poster of the discovery step for places where GIFs do not play
        subprocess.run([converter, "-z", "1.5", os.path.join(tmp, "l5.svg"), "-o", os.path.join(OUT, "analysis-loop.png")], check=True)
else:
    print("GIFs not regenerated (needs rsvg-convert and ImageMagick).")
print("ok", list(images))
