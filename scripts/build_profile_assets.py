"""Build deterministic editorial SVGs for the three selected portfolio studies."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
FONT = 'Arial, DejaVu Sans, sans-serif'
MONO = 'DejaVu Sans Mono, monospace'
SERIF = 'Georgia, DejaVu Serif, serif'
PAPER, INK, GREEN, MUTED = '#f5f1e8', '#172d24', '#1d634b', '#5c6d62'


def text(x, y, value, size=22, color=INK, weight=400, family=FONT, spacing=0):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>')


def svg(width, height, title, content):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img"><title>{escape(title)}</title>{content}</svg>\n')


def hero():
    parts = [
        f'<rect width="1280" height="360" rx="12" fill="{PAPER}"/>',
        '<path d="M44 76H1236M44 314H1236M862 105V284" stroke="#ccd4c7"/>',
        text(44, 47, 'FINANCIAL RESEARCH / BUILT WITH CODE', 15, GREEN, 600, MONO, 1),
        text(1065, 47, 'dev-belly', 21, INK, 700),
        text(39, 177, 'Follow the', 87, INK, 400, SERIF, -3),
        text(39, 274, 'numbers.', 105, GREEN, 700, SERIF, -4),
        text(912, 145, '01 / READ THE BUSINESS', 16, INK, 600, MONO),
        text(912, 200, '02 / TEST THE IDEA', 16, INK, 600, MONO),
        text(912, 255, '03 / SHOW THE WORK', 16, INK, 600, MONO),
        text(44, 343, 'SOURCE / METHOD / RESULT / REPLAY', 14, MUTED, 500, MONO, .4),
        text(942, 343, 'PYTHON + SQL + STATISTICS', 14, GREEN, 600, MONO),
    ]
    return svg(1280, 360, 'dev-belly — Follow the numbers. Financial research built with code.', ''.join(parts))


PROJECTS = [
    ('statementtrace-v4', '01', 'StatementTrace', 'PUBLIC FILINGS / CORPORATE CASH FLOW', GREEN,
     'Profit grows. Does cash follow?', 'Apple / Microsoft / Alphabet — FY2023–FY2024',
     '24 SOURCE FACTS / 6 ISSUER-YEARS / PYTHON + SQL', 'REAL FILINGS. EXPLICIT FISCAL WINDOWS.'),
    ('creditvintage-v4', '02', 'CreditVintage', 'MODEL VALIDATION / DECISION CAPACITY', '#c7e3ae',
     'Better probabilities. Better decisions?', 'Compare calibration, ranking and a fixed review budget.',
     '35,000 OBSERVED SBA LOANS / LATER FUNDING COHORTS', 'RETROSPECTIVE RESEARCH.'),
    ('pitbridge-v4', '03', 'PITBridge', 'TEMPORAL DATA / RESEARCH INPUTS', GREEN,
     'What was known at the decision?', 'Change an arrival time. Inspect the selected record.',
     'BROWSER INPUT / SQL SNAPSHOT / PYTHON REPLAY', 'SYNTHETIC EVENT EXAMPLES.'),
]


def card(project):
    slug, index, name, category, accent, question, detail, proof, scope = project
    dark = index == '02'
    bg, fg, muted, line = (INK, PAPER, '#bfccbf', '#3a5145') if dark else (PAPER, INK, MUTED, '#ccd4c7')
    parts = [
        f'<rect x="1" y="1" width="1278" height="258" rx="12" fill="{bg}" stroke="{line}"/>',
        text(34, 39, index+' / '+category, 13, accent, 600, MONO, .4),
        text(31, 100, name, 48, fg, 700, spacing=-1.8),
        text(34, 145, question, 25, fg, 600),
        text(34, 181, detail, 18, muted),
        f'<path d="M34 205H1246M874 35V185" stroke="{line}"/>',
        text(34, 237, proof, 14, accent, 600, MONO),
        text(890, 237, scope, 10, muted, 500, MONO),
    ]
    if index == '01':
        parts += [
            text(917, 85, 'OPERATING CASH FLOW', 16, accent, 600, MONO),
            text(917, 127, '− CASH CAPEX', 22, fg, 600, MONO),
            text(917, 170, '= FREE CASH FLOW', 22, accent, 600, MONO),
        ]
    elif index == '02':
        parts += [
            text(919, 84, 'TRAIN → CALIBRATE', 18, accent, 600, MONO),
            text(919, 127, '→ LATER COHORTS', 18, accent, 600, MONO),
            text(919, 170, 'SAME REVIEW CAPACITY', 15, muted, 500, MONO),
        ]
    else:
        parts += [
            text(919, 83, 'EVENT TIME', 18, fg, 600, MONO),
            text(919, 126, 'KNOWLEDGE TIME', 18, accent, 600, MONO),
            text(919, 169, 'DECISION TIME', 18, fg, 600, MONO),
        ]
    return svg(1280, 260, f'{name}: {question} {detail}', ''.join(parts))


def stack():
    return svg(1280, 88, 'Python, SQL and statistics; Polars, Parquet, DuckDB and dbt; FastAPI and Pydantic.',
               f'<rect width="1280" height="88" fill="{PAPER}"/>'
               + '<path d="M0 1H1280M0 87H1280" stroke="#ccd4c7"/>' + text(20, 34,
               'PYTHON  /  SQL  /  STATISTICS  /  SCIKIT-LEARN  /  C++20', 19, GREEN, 500, MONO)
               + text(20, 66, 'FINANCIAL DATA  /  POLARS  /  PARQUET  /  DUCKDB  /  DBT  /  FASTAPI  /  PYDANTIC',
                      17, MUTED, 500, MONO))


def outputs():
    return {'profile-signal-v4.svg': hero(), 'stack-v4.svg': stack(),
            **{f'{project[0]}.svg': card(project) for project in PROJECTS}}


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    expected = outputs()
    for path in ASSETS.glob('*.svg'):
        if path.name not in expected:
            path.unlink()
    for name, content in expected.items():
        (ASSETS/name).write_text(content, encoding='utf-8')
    print(f'Built {len(expected)} profile SVGs')
