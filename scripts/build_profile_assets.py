"""Generate portable profile SVGs: typography and schematic method illustrations."""
from html import escape
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
FONT = 'Arial, DejaVu Sans, sans-serif'
MONO = 'DejaVu Sans Mono, monospace'
PAPER, INK, LIME = '#f1f0e9', '#111319', '#d7fa73'

def text(x, y, value, size=22, color=PAPER, weight=400, family=FONT, spacing=0):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" letter-spacing="{spacing}">{escape(value)}</text>')

def svg(width, height, title, content):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img"><title>{escape(title)}</title>{content}</svg>\n')

def hero():
    p = ['<defs><linearGradient id="surface" x2="1" y2="1"><stop stop-color="#151920"/>'
         '<stop offset="1" stop-color="#090b0f"/></linearGradient><clipPath id="frame">'
         '<rect width="1280" height="570" rx="20"/></clipPath></defs><g clip-path="url(#frame)">',
         '<rect width="1280" height="570" fill="url(#surface)"/>',
         '<path d="M836 0V570M0 500H1280" stroke="#343a40"/>',
         '<circle cx="1220" cy="58" r="7" fill="#d7fa73"/>',
         text(44, 63, 'dev-belly', 25, weight=700),
         text(880, 63, 'FINANCIAL RESEARCH / CODE', 13, LIME, 500, MONO, .4),
         text(39, 174, 'FINANCE.', 107, weight=800, spacing=-5),
         text(39, 286, 'DATA.', 107, weight=800, spacing=-5),
         text(39, 398, 'EVIDENCE.', 107, LIME, 800, spacing=-5),
         text(44, 455, 'I turn financial questions into inspectable systems.', 23, '#b9c0c9'),
         text(44, 539, 'CUFE / DATA SCIENCE & BIG DATA TECHNOLOGY', 16, '#b9c0c9', 500, MONO),
         text(880, 539, 'BUILT TO BE QUESTIONED.', 15, LIME, 500, MONO),
         '<circle cx="1048" cy="265" r="137" fill="none" stroke="#2a313a"/>',
         '<circle cx="1048" cy="265" r="104" fill="none" stroke="#434e44"/>',
         '<path d="M880 265H1224M1048 100V430" stroke="#36402e" stroke-dasharray="3 9"/>',
         text(949, 315, 'db', 134, weight=700, spacing=-10),
         '<circle cx="1166" cy="329" r="13" fill="#d7fa73"/>',
         '<path d="M909 393L954 363M1151 154L1181 121" stroke="#d7fa73" stroke-width="3"/>',
         text(879, 467, 'CREDIT / TEMPORAL DATA / RISK', 14, '#909daa', family=MONO), '</g>']
    return svg(1280, 570, 'dev-belly: finance, data, evidence. CUFE data science student.', ''.join(p))

PROJECTS = [
    ('creditvintage-v3', '01', 'CreditVintage', 'CREDIT MODEL VALIDATION', LIME,
     'When does a credit score deserve trust?', 'Chronological cohorts. Mature outcomes. Source lineage.',
     'PITBRIDGE → FEATURES → PROSPECTIVE EVALUATION', 'Python / scikit-learn / reproducible reports'),
    ('pitbridge-v3', '02', 'PITBridge', 'TEMPORAL DATA ENGINEERING', '#365ad9',
     'Know what was known.', 'Publication, ingestion, revisions and rolling windows.',
     'SQL SNAPSHOTS = INDEPENDENT PYTHON REPLAY', 'Python / SQLite / record-level provenance'),
    ('stressatlas-v3', '03', 'StressAtlas', 'PORTFOLIO TAIL RISK', '#ffb994',
     'Measure the tail. Then measure uncertainty.', 'Correlated defaults, exact tail attribution and paired paths.',
     '20,000 PATHS / 300 PAIRED RESAMPLES', 'Python / NumPy / SciPy / Monte Carlo'),
]

def card(project):
    slug, index, name, category, accent, first, second, proof, technology = project
    bg, fg, muted, border = (PAPER, INK, '#535c69', '#ced1cd') if index == '02' else (INK, PAPER, '#acb6c1', '#353c45')
    p = [f'<rect x="1" y="1" width="1278" height="338" rx="16" fill="{bg}" stroke="{border}"/>',
         text(38, 46, index+' / '+category, 15, accent, 600, MONO, .8),
         text(34, 119, name, 65, fg, 700, spacing=-2),
         text(38, 169, first, 26, fg, 600), text(38, 207, second, 21, muted),
         f'<path d="M38 242H771M814 32V308" stroke="{border}"/>',
         text(38, 272, proof, 16, accent, 600, MONO), text(38, 309, technology, 17, muted)]
    if index == '01':
        for y, label, dates in [(67, 'TRAIN', '2022'), (131, 'CALIBRATE', '2023 H2'), (195, 'HOLD OUT', '2024 H2')]:
            p += [f'<rect x="851" y="{y}" width="345" height="47" rx="4" fill="#222b20" stroke="#4f6337"/>',
                  text(866, y+29, label, 15, LIME, 600, MONO), text(1092, y+29, dates, 15, family=MONO)]
        p.append(text(853, 293, 'SEPARATE TIME. SAVE THE PROOF.', 13, muted, 500, MONO))
    elif index == '02':
        p += ['<path d="M853 191H1230" stroke="#8d98ba" stroke-width="2"/>',
              '<path d="M1105 79V248" stroke="#365ad9" stroke-width="2" stroke-dasharray="5 6"/>',
              text(864, 112, 'AVAILABLE', 16, accent, 700, MONO), text(864, 141, 'AT THE DECISION', 16, accent, 700, MONO)]
        for x, label, fill in [(879, 'v1', accent), (1000, 'v2', accent), (1188, 'LATE', '#c5c8ca')]:
            p += [f'<circle cx="{x}" cy="191" r="8" fill="{fill}"/>', text(x-17, 224, label, 14, muted, family=MONO)]
        p.append(text(853, 293, 'EVENT TIME + KNOWLEDGE TIME', 13, muted, 500, MONO))
    else:
        p.append(text(853, 84, 'SAME PATHS. TWO SCENARIOS.', 14, accent, 600, MONO))
        for i in range(7):
            y = 125+i*18
            p.append(f'<path d="M852 {y}C938 {y+20} 939 {y-18} 1028 {y+4}S1146 {y+38} 1224 {y+6}" fill="none" stroke="{accent}" stroke-opacity="{.22+i*.09:.2f}" stroke-width="2"/>')
        p += [text(853, 276, 'VaR / ES / INDUSTRY CONTRIBUTIONS', 13, muted, family=MONO),
              text(853, 300, 'METHOD ILLUSTRATION', 11, '#76818d', family=MONO)]
    return svg(1280, 340, f'{name}: {first} {second}', ''.join(p))

def stack():
    return svg(1280, 60, 'Python, SQL, C++20, scikit-learn, LightGBM and NumPy.',
               '<rect width="1280" height="60" rx="8" fill="#1a1d23"/>'+text(28, 38,
               'PYTHON  /  SQL  /  C++20  /  SCIKIT-LEARN  /  LIGHTGBM  /  NUMPY', 21, '#b9c0c9', 500, MONO))

def outputs():
    return {'profile-signal-v3.svg': hero(), 'stack-v3.svg': stack(),
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
