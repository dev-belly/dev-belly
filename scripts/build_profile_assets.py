"""Build the profile's self-contained SVGs using only the Python standard library."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT = "Arial, DejaVu Sans, sans-serif"
MONO = "DejaVu Sans Mono, monospace"


def text(x, y, value, size=22, color="#c2ccda", weight=400, family=FONT, spacing=0):
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">'
        f"{escape(value)}</text>"
    )


def svg(width, height, title, content):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img">'
        f"<title>{escape(title)}</title>{content}</svg>\n"
    )


def hero():
    parts = [
        '<defs><linearGradient id="bg" x2="1" y2="1">'
        '<stop stop-color="#0b1421"/><stop offset="1" stop-color="#081018"/>'
        '</linearGradient><linearGradient id="accent">'
        '<stop stop-color="#64e7cf"/><stop offset="1" stop-color="#61b8ff"/>'
        '</linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">'
        '<path d="M32 0H0V32" fill="none" stroke="#678ba5" stroke-opacity=".10"/>'
        '</pattern></defs>',
        '<rect x="1" y="1" width="1278" height="418" rx="22" fill="url(#bg)" '
        'stroke="#244153" stroke-width="2"/>',
        '<rect x="744" y="24" width="510" height="372" fill="url(#grid)"/>',
        '<rect x="48" y="44" width="42" height="4" rx="2" fill="#69e2cc"/>',
        text(102, 51, "FINANCIAL DATA / RESEARCH SYSTEMS", 15, "#8cabbf", 600, MONO, 1.8),
        text(48, 161, "dev-belly", 88, "#f2f7fc", 700, spacing=-3),
        '<rect x="507" y="111" width="13" height="57" rx="2" fill="#69e2cc"/>',
        text(50, 215, "Build the system.", 34, "#e3edf7", 600),
        text(50, 259, "Make the result inspectable.", 34, "#69e2cc", 600),
        text(50, 318, "CREDIT RISK    /    QUANT RESEARCH    /    AUDIT ANALYTICS", 15, "#9cb3c5", 400, MONO),
        '<path d="M48 354H695" stroke="#263d4f"/>',
        text(50, 383, "CUFE · Data Science & Big Data Technology", 18, "#819daf"),
        '<path d="M782 141H818M1054 141H1103V208H1054M818 270H781V141" '
        'stroke="url(#accent)" stroke-width="2" fill="none" opacity=".60"/>',
    ]
    stages = [
        (818, 92, "01 / DATA", "Point-in-time inputs"),
        (872, 181, "02 / MODEL", "Measured assumptions"),
        (818, 270, "03 / EVIDENCE", "Replayable outputs"),
    ]
    for x, y, label, detail in stages:
        parts += [
            f'<rect x="{x}" y="{y}" width="294" height="76" rx="12" fill="#101e2b" '
            'stroke="#335063"/>',
            f'<rect x="{x}" y="{y+18}" width="3" height="39" rx="1" fill="#69e2cc"/>',
            text(x + 22, y + 28, label, 14, "#6ddccb", 600, MONO, 1),
            text(x + 22, y + 54, detail, 20, "#dbe7f3", 500),
        ]
    parts.append(text(818, 382, "CODE  ·  BASELINES  ·  VERIFICATION", 13, "#66879f", 400, MONO))
    return svg(1280, 420, "dev-belly — financial data and research systems", "".join(parts))


PROJECTS = [
    ("creditvintage", "01", "CreditVintage", "CREDIT RISK", "#6be6cc",
     "Application-time data.", "Prospective cohort evaluation.", "PIT FEATURES + MATURE LABELS", "Python · scikit-learn · report verification"),
    ("pitbridge", "02", "PITBridge", "FINANCIAL DATA ENGINEERING", "#64e5c4",
     "Only what the decision could know.", "Late data, revisions and tombstones.", "SQL SNAPSHOTS + INDEPENDENT REPLAY", "Python · SQLite · source-record lineage"),
    ("stressatlas", "03", "StressAtlas", "PORTFOLIO RISK", "#f4b76a",
     "Marginal risk and clustered defaults.", "Paired scenarios with additive tail risk.", "160 LOANS / 20,000 SHARED PATHS", "Python · NumPy · SciPy · discrete ES"),
    ("alphaforge", "04", "AlphaForge", "QUANT RESEARCH", "#7eb7ff",
     "Factor research to portfolios.", "Walk-forward models and backtests.", "FACTORS → PORTFOLIOS → REPORTS", "Python · LightGBM · CVXPY · FastAPI"),
    ("tradeforge", "05", "TradeForge", "EXECUTION SYSTEMS", "#a6a2ff",
     "Event-driven execution research.", "C++ core, Python reference model.", "CAUSALITY + EVENT-BY-EVENT PARITY", "C++20 · pybind11 · transaction costs"),
    ("auditlens", "06", "AuditLens", "AUDIT ANALYTICS", "#efc47b",
     "Explainable financial anomaly triage.", "From source ledger to review queue.", "30,128 VOUCHERS / 9 PROCEDURES", "Python · SQL · Isolation Forest · Streamlit"),
    ("controltrace", "07", "ControlTrace", "EVIDENCE ENGINEERING", "#6fcbeb",
     "Access and change-control evidence.", "Human review with replayable exports.", "5 CONTROL TESTS / SOURCE LINEAGE", "Python · DuckDB · append-only reviews"),
    ("ledgerx", "08", "LedgerX", "ACCOUNTING SYSTEMS", "#d2a6e3",
     "Double-entry accounting for fills.", "Independent point-in-time valuation.", "DECIMAL LEDGER / QUOTE-BASED MARKS", "Python · Decimal · journal verification"),
]


def card(project):
    slug, index, name, category, accent, first, second, proof, stack = project
    parts = [
        '<rect x="1" y="1" width="598" height="276" rx="18" fill="#0d1723" '
        'stroke="#284252" stroke-width="2"/>',
        f'<path d="M24 1H140" stroke="{accent}" stroke-width="3"/>',
        text(28, 40, category, 14, accent, 600, MONO, 1.5),
        text(547, 40, index, 16, "#526d82", 500, MONO),
        text(27, 89, name, 37, "#f1f6fc", 700, spacing=-.7),
        text(28, 129, first, 22, "#b8c9d8"),
        text(28, 158, second, 22, "#b8c9d8"),
        f'<rect x="27" y="182" width="546" height="34" rx="7" fill="{accent}" fill-opacity=".07"/>',
        text(40, 205, proof, 15, accent, 600, MONO, .5),
        text(28, 251, stack, 17, "#7993a9"),
    ]
    return svg(600, 278, f"{name} — {category.lower()}", "".join(parts))


def stack():
    labels = [("PYTHON", 126), ("SQL / DUCKDB", 184), ("C++20", 122),
              ("SCIKIT-LEARN", 184), ("LIGHTGBM", 150), ("FASTAPI", 134), ("PYTORCH", 148)]
    x = 0
    parts = []
    for label, width in labels:
        parts.append(f'<rect x="{x}" y="1" width="{width}" height="40" rx="8" '
                     'fill="#101f2d" stroke="#2a4758"/>')
        parts.append(text(x+18, 27, label, 14, "#aacbdb", 600, MONO, .6))
        x += width + 12
    return svg(x-12, 43, "Python, SQL, C++20, scikit-learn, LightGBM, FastAPI and PyTorch", "".join(parts))


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "profile-hero.svg").write_text(hero(), encoding="utf-8")
    (ASSETS / "stack.svg").write_text(stack(), encoding="utf-8")
    for project in PROJECTS:
        (ASSETS / f"{project[0]}.svg").write_text(card(project), encoding="utf-8")
    print(f"Built {len(PROJECTS)+2} profile SVGs")
