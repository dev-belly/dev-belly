# Portfolio review · 2026-10-28

## Timestamp-safe PITBridge release · 2026-10-28

[PITBridge #29](https://github.com/dev-belly/PITBridge/pull/29) publishes
[v0.2.1](https://github.com/dev-belly/PITBridge/releases/tag/v0.2.1), carrying
the previously merged precision fix into the installable wheel. A reproduction
using the public v0.2.0 wheel set a decision at `00:00:00Z` and ingestion at
`00:00:00.0000009Z`; truncation made the later record equal to the cutoff and
selected it. The repaired source rejects that input before selection.

The new wheel's isolated installation verifies scalar and rolling results at the
exact cutoff and one microsecond after it. Four CLI cases cover JSON/CSV for both
commands; a seventh fractional digit returns exit 2 without a report. The
release gate requires the installed precision checks as well as independent
replay and the benchmark. Supported previous scalar and rolling demo bundles
replay under the new source. Existing normalized evidence cannot recover digits
already discarded; revisit original timestamps and upstream conversion rules.

The local suite passes **146 tests**; the prior public wheel reproduced the
counterexample and a clean new wheel passed all boundary and replay checks.
All ten [PR CI jobs](https://github.com/dev-belly/PITBridge/actions/runs/40653383137)
pass, including Linux/Windows installations, optional pandas and Chrome. Merge
[`7a6aee2`](https://github.com/dev-belly/PITBridge/commit/7a6aee228887038e0b2aae7cd40720c5f1ab998f)
retains the tested tree `af1709cce1175d77f2eda0f4faf56898756f53ed` exactly.
[Main CI](https://github.com/dev-belly/PITBridge/actions/runs/40653497143),
[Pages deployment](https://github.com/dev-belly/PITBridge/actions/runs/40653497155)
and the [checked release](https://github.com/dev-belly/PITBridge/actions/runs/40653580180)
all pass. All five public release assets were downloaded and verified against
the merge commit and SHA-256 digests. The published wheel, installed into a
separate environment, rejects the old counterexample, keeps the one-microsecond
late record unavailable, and verifies both committed demo bundles.


## Checked credit patch · 2026-10-28

[CreditVintage #39](https://github.com/dev-belly/CreditVintage/pull/39) delivers
[v0.8.1](https://github.com/dev-belly/CreditVintage/releases/tag/v0.8.1), so a
new installation includes the credit-number bounds and timestamp-safe optional
integration previously available only in current source. The first-run guide,
project brief and profile now use this checked patch wheel. At that checkpoint,
the separate PITBridge v0.2.0 wheel retained its older precision behavior. The subsequent v0.2.1 release is described above.

Two malformed SBA cases reproduced an unhandled exception: a rehashed AUC
claim of `10**400` and a reserved DEFLATE block in the downloaded evidence ZIP.
Both now return exit 2 and a diagnostic. Card ZIP checks also handle compressed
stream/runtime errors and check member sizes before reading. Seven new CLI
cases cover positive/negative oversized claims, broken compressed streams,
unsupported compression and a card member-size mismatch. Failed verification
leaves the input files intact.

The complete local suite passes **464 tests and 28 subtests**: 66 SBA/card cases
and 398 remaining cases, with no overlap between those two runs. Ruff lint,
formatting and strict mypy over 24 source files pass. A pre-change SBA bundle
still refits successfully. Its complete ZIP is byte-identical to the new
installed wheel's output, with SHA-256
`30f4a36268438248f444d42f533530a6f607b01c867fff8307fbca29c3d709ac`.

A clean wheel installation outside both repositories replays public credit,
SBA, score/feature monitoring, coverage/policy checks, SQL analysis, 48 review
cases and the optional 480-application / 1,440-feature lineage. It also rejects
rehashed false/oversized SBA metrics and broken DEFLATE with exit 2.
[PR CI and portable replay](https://github.com/dev-belly/CreditVintage/actions/runs/40640295261) ·
[PR public-report build](https://github.com/dev-belly/CreditVintage/actions/runs/40640295246).
All eight PR CI jobs and the report build pass. Merge
[`8a285c4`](https://github.com/dev-belly/CreditVintage/commit/8a285c424f30a2d6b1c27c2a2d9a1867b6587cc2)
retains the checked tree `93d40c750698c6adf028ff4a2e188c24a32b9b71` exactly.
The [main CI](https://github.com/dev-belly/CreditVintage/actions/runs/40640906678),
[main report deployment](https://github.com/dev-belly/CreditVintage/actions/runs/40640906631)
and [checked release](https://github.com/dev-belly/CreditVintage/actions/runs/40641509614)
all pass. All five public assets were downloaded and checked against the merge
commit and SHA-256 values; the public wheel also replays the original SBA case
and cleanly rejects the oversized and damaged-evidence cases in a separate environment.


The SBA source pins, model protocol, targets and numerical results are unchanged.
This remains retrospective funding-cohort research; historical publication and
revision records, independent use and production lending results are not
established by this repair.

## Hiring and a public first trial · 2026-10-28

The next pass targets two concrete reader tasks: a recruiter finding relevant
work quickly, and a developer trying a useful timing rule before installing a
package. The profile now has a short [role-to-project overview](FOR_RECRUITERS.md),
an explicit internship focus, and direct paths to the live example and source.
The interview card separates the observed SBA study from the synthetic workflow
and removes an unqualified archived AlphaForge return claim.

[PITBridge #28](https://github.com/dev-belly/PITBridge/pull/28) adds the
[no-sign-in invoice lesson](https://dev-belly.github.io/PITBridge/try/).
The two timestamps calculate locally; a URL fragment preserves a shareable
scenario. Three presets, a deliberately unsafe comparator, a visible freshness
rule and the source records make the first task inspectable. The fixed browser
mirror uses integer microseconds. It rejects unsupported precision before
showing or sharing a result; the full importer remains in Python.

The exact shipped inline script agrees with SQLite and the independent Python
enumerator over **71 fixed/seeded cases**. All ten final PR CI jobs pass at
`31f67f8`, including the [real-Chrome job](https://github.com/dev-belly/PITBridge/actions/runs/40632291976):
observed viewport widths are **1280 and 390**, with 18 report/lesson selections
across the existing selector case and both new views. The merge is
[`4a6905b`](https://github.com/dev-belly/PITBridge/commit/4a6905bb2d4b67534154dffbe853dc9259bfcf1a),
with tree `2e8189fce98be1b38ecffef4c163ad4497d89238` exactly matching the checked
head. Both committed evidence bundles verify without regeneration. There is
no new package runtime dependency or analytics script.

The new [main CI](https://github.com/dev-belly/PITBridge/actions/runs/40632456760)
and [Pages deployment](https://github.com/dev-belly/PITBridge/actions/runs/40632456567)
also pass. The public page was opened and visually inspected: the three presets
produce missing / invoice-v1 / invoice-v2; a seventh fractional digit hides the
old output and disables sharing; restoring a preset recovers the comparison;
the copy button confirms the scenario link. The [captured public result](assets/try-preview-20261028.jpg)
shows source availability and the project/author links.

GitHub's visible profile bio now states the internship directions. Pins cover
CreditVintage, PITBridge, StatementTrace, StressAtlas, TradeForge and
ControlTrace. CreditVintage's About text now identifies the 35,000 observed
SBA loans, and its topics include financial-data. These presentation changes
also give PITBridge a direct trial homepage and the relevant data-leakage topic.
These changes
are separate from new stars, followers, independent trials or hiring outcomes;
none of those outcomes is inferred from our own checks.

## Temporal precision and credit input boundaries · 2026-10-28

The previous round's remaining [AlphaForge main CI](https://github.com/dev-belly/alphaforge/actions/runs/40522081304)
and [profile main checks](https://github.com/dev-belly/dev-belly/actions/runs/40524956625)
are complete and successful. This pass fixes two reproducible input failures,
then carries the timestamp repair into the credit integration and browser lesson.

| Change | Failure and resulting behavior | Checked head / merge | PR workflow |
| --- | --- | --- | --- |
| [PITBridge #26](https://github.com/dev-belly/PITBridge/pull/26) | A source arriving at `00:00:00.0000009Z` could normalize to `00:00:00Z` and appear known. Excess fractional digits, fractions on shortened clock forms and fractional-second offsets now fail before normalization or output. Supported microsecond equality remains inclusive. | `39a3177` / `219e58a` | [CI](https://github.com/dev-belly/PITBridge/actions/runs/40629046214) |
| [CreditVintage #37](https://github.com/dev-belly/CreditVintage/pull/37) | Unsupported integer cents could pass readiness and overflow later; enormous integer features/config fractions could raise raw conversion errors. Positive int64 cents are checked before fitting, and numeric overflow becomes a contract error. Supported integer cents remain exact above `2^53`. | `ec067ef` / `a9ca40f` | [CI](https://github.com/dev-belly/CreditVintage/actions/runs/40629093374) · [Pages build](https://github.com/dev-belly/CreditVintage/actions/runs/40629093447) |
| [PITBridge #27](https://github.com/dev-belly/PITBridge/pull/27) | The browser notebook installed an older snapshot. It now pins the repaired source and includes a runnable seventh-digit rejection alongside the original invoice decisions. | `851471e` / `80fe336` | [CI](https://github.com/dev-belly/PITBridge/actions/runs/40629643922) |
| [CreditVintage #38](https://github.com/dev-belly/CreditVintage/pull/38) | The integration retained an old importer. README setup, three CI/Pages source checkouts and new summaries now reference the repaired upstream merge. Previously published synthetic evidence keeps its original reference and complete replay requirements. | `b98824f` / `ba28585` | [CI](https://github.com/dev-belly/CreditVintage/actions/runs/40629769949) · [Pages build](https://github.com/dev-belly/CreditVintage/actions/runs/40629769966) |

All four project pull requests are merged after their workflows complete
successfully. Each merge retains exactly the checked head tree. PITBridge's
final [main CI](https://github.com/dev-belly/PITBridge/actions/runs/40629977240)
and [Pages build](https://github.com/dev-belly/PITBridge/actions/runs/40629977393)
also pass. CreditVintage's push workflows on the new integration merge run
separately from its completed PR checks.

PITBridge passes **145 local tests**, including eight new precision methods
with subcases across JSON, native CSV, optional pandas, scalar and rolling
commands. Both committed evidence bundles verify without regeneration. A
source archive and its wheel build successfully; the wheel installs into a
clean environment and passes the existing scalar/rolling JSON/CSV replay and
small benchmark checks. The notebook separately runs its real pinned source
download/install in a fresh environment without PITBridge: all **five code
cells** finish and the imported package is inside that environment. This is
local notebook execution, not a hosted Colab UI acceptance record.

CreditVintage's numeric pass has **26 new cases**: the prior source fails 19
and passes seven supported-input cases. Its full suite passes 454 tests and
28 subtests. After three integration regressions, the final combination passes
**457 tests and 28 subtests**, Ruff lint/format and strict mypy over **24 source
files**. These are overlapping runs, not quantities to add. A source revision
arriving after the last supported microsecond fails under the new dependency;
the same regression fails against the old dependency because it accepts the
truncated instant.

Before upgrading, the original dependency generates a complete **480-application,
1,440-feature** synthetic lineage bundle. The new engine verifies that saved
bundle without rewriting it. A new-reference bundle also generates and verifies:
**17 of 20 files are byte-identical**, including source features, lineage and
predictions. Only the dependency-reference summary, its root manifest and the
derived ZIP differ. Prediction SHA-256 is
`4ae53321c22a41f5bc075feac5c63b433ccad712231b946aa0d025edf40c12a5`.
An unknown declared reference is rejected even after its summary is rehashed.

The profile synchronization passes local checks for five deterministic SVGs,
three flagship panels, 13 documents and 116 local references. The generated
catalog still covers 19 public projects, and rebuilding the graphics changes
no asset. Its PR workflow is checked separately from the project workflows.

The existing PITBridge v0.2.0 and CreditVintage v0.8.0 release assets predate
these repairs and remain unchanged. Use the updated notebook or current source
installation for the new validation. Original digits already discarded before
an old bundle was saved cannot be recovered from normalized evidence. The
financial study protocols, frozen numerical claims and absence of independent
production/adoption evidence retain their prior scope.

## Repository maintenance and application repairs · 2026-10-27

The earlier financial repair checkpoint is now complete: all final
[AlphaForge main checks](https://github.com/dev-belly/alphaforge/actions/runs/40504965215)
and [profile main checks](https://github.com/dev-belly/dev-belly/actions/runs/40505482743)
pass. This continuation covers reproducible Action source references,
three application failure paths and the remaining dated-source review.

All **21 pre-existing pull requests** in this continuation are merged. The
AuditLens pin update and newly generated Ranxin dependency PR are also merged.
This profile synchronization is recorded separately. All 18 workflow-update PRs completed their workflows
successfully. Each workflow-update merge tree matches its checked head exactly.

### Application and source repairs

| Change | Evidence and scope |
| --- | --- |
| [Digital Craftsman #5](https://github.com/dev-belly/digital-craftsman/pull/5) | Invalid expiration dates become an expired value. The 14 actual protected cloud-function entry points pass 196 offline SDK scenarios, and all 13 local release-readiness checks pass. |
| [Ranxin #52](https://github.com/dev-belly/ranxin-mini-program/pull/52) | Partial seed initialization resumes after failure; fixed seed document IDs converge under concurrent initial loads. Four independently deployed helper copies are exercised. Existing curated records and legacy IDs are retained. |
| [Ranxin #53](https://github.com/dev-belly/ranxin-mini-program/pull/53) | Mock and cloud pagination validate the same safe integers and bounds before records are read. Valid pages stay within the caller's records. Combined with #52 and [maintenance #54](https://github.com/dev-belly/ranxin-mini-program/pull/54), all 30 Node tests and JavaScript syntax checks pass. |
| [Goose-leg case #1](https://github.com/dev-belly/goose-leg-auntie-site/pull/1) | All four dated reports were reopened on 2026-10-27. The HTML and Markdown retain conflicting interview dates, distinguish displayed participation counts from transactions, and scope the regulator notice to its publication date. Four source URLs, 14 matched topics, unique IDs and internal anchors pass one-off structural checks. No CI workflow is configured for this content repository. |

These checks use offline application fixtures and the cited historical reports.
They do not supply new WeChat cloud deployment or real-device acceptance evidence.
The combined Ranxin main tree is `82a1d00fde41333dc09a6f37a98fac13ae4e830a`,
exactly matching its locally tested three-PR combination.

### Workflow source references

Sixteen pre-existing dependency PRs cover **111 Action references**. Their
changed lines were checked to contain only Action version/source replacements.
The **73 floating references in those proposals** were resolved from official
upstream refs and pinned to their commit objects. The annotated setup-uv v7
tag was followed to its commit, rather than treating the tag object's SHA as
the Action source. AuditLens [#10](https://github.com/dev-belly/AuditLens/pull/10)
and the profile add four more fixed references; Ranxin [#55](https://github.com/dev-belly/ranxin-mini-program/pull/55)
adds two: **117 references across 19 repositories** in this pass. Project
Python/Node versions, dependency declarations and scientific study source
retain each repository's existing contracts.

Every refreshed workflow PR starts from its current main source; AlphaForge,
TradeForge, ControlTrace and Digital Craftsman include the preceding code
repairs. Completion below uses the successful workflow records for the exact
head commits; four job-check summaries lagged behind their completed run
records. Direct workflow links and merge checkpoints are retained:

| Change | Checked head | Merged checkpoint | Workflow evidence |
| --- | --- | --- | --- |
| [alphaforge #8](https://github.com/dev-belly/alphaforge/pull/8) | `0bc74ee` | [8145379](https://github.com/dev-belly/alphaforge/commit/814537951ce394cdea546feff43ab184b55980ec) | [run 1](https://github.com/dev-belly/alphaforge/actions/runs/40517476021) · [run 2](https://github.com/dev-belly/alphaforge/actions/runs/40517476250) |
| [CreditVintage #36](https://github.com/dev-belly/CreditVintage/pull/36) | `69d0393` | [152bd74](https://github.com/dev-belly/CreditVintage/commit/152bd74fb1397c29e42399aeed7c7271da3a38cc) | [run 1](https://github.com/dev-belly/CreditVintage/actions/runs/40517483050) · [run 2](https://github.com/dev-belly/CreditVintage/actions/runs/40517477319) · [run 3](https://github.com/dev-belly/CreditVintage/actions/runs/40517482989) |
| [PITBridge #25](https://github.com/dev-belly/PITBridge/pull/25) | `2fd3699` | [a8efe14](https://github.com/dev-belly/PITBridge/commit/a8efe14d47c8d766f6b0748f224e0445cc5502f2) | [run 1](https://github.com/dev-belly/PITBridge/actions/runs/40517492027) · [run 2](https://github.com/dev-belly/PITBridge/actions/runs/40517483901) |
| [TradeForge #22](https://github.com/dev-belly/TradeForge/pull/22) | `13340a5` | [cff14bc](https://github.com/dev-belly/TradeForge/commit/cff14bce85e25051da2deb095dd2abd428fe074f) | [run 1](https://github.com/dev-belly/TradeForge/actions/runs/40517503940) |
| [ControlTrace #9](https://github.com/dev-belly/ControlTrace/pull/9) | `2ec8374` | [dce30df](https://github.com/dev-belly/ControlTrace/commit/dce30df262e109020830c3a32d8bdb20d263188c) | [run 1](https://github.com/dev-belly/ControlTrace/actions/runs/40517512520) · [run 2](https://github.com/dev-belly/ControlTrace/actions/runs/40517505419) |
| [StressAtlas #7](https://github.com/dev-belly/StressAtlas/pull/7) | `7420fc5` | [bc82217](https://github.com/dev-belly/StressAtlas/commit/bc822179ac5e8f6663e62783c44d35c9e4666def) | [run 1](https://github.com/dev-belly/StressAtlas/actions/runs/40517563839) · [run 2](https://github.com/dev-belly/StressAtlas/actions/runs/40517558427) |
| [StatementTrace #7](https://github.com/dev-belly/StatementTrace/pull/7) | `2a8c5d8` | [727353b](https://github.com/dev-belly/StatementTrace/commit/727353b27ccdd67c7ac9958c80630a5f2aa52049) | [run 1](https://github.com/dev-belly/StatementTrace/actions/runs/40517574152) |
| [highdim-causal-allocation-lab #3](https://github.com/dev-belly/highdim-causal-allocation-lab/pull/3) | `8014db5` | [66d0553](https://github.com/dev-belly/highdim-causal-allocation-lab/commit/66d05534cc98cbe6d04d6f30ef4deeabb94d68cf) | [run 1](https://github.com/dev-belly/highdim-causal-allocation-lab/actions/runs/40517580839) |
| [LedgerX #6](https://github.com/dev-belly/LedgerX/pull/6) | `148a6df` | [5bd843f](https://github.com/dev-belly/LedgerX/commit/5bd843f16c9292bd857f0f4ae2d0afd00648af1e) | [run 1](https://github.com/dev-belly/LedgerX/actions/runs/40517589835) · [run 2](https://github.com/dev-belly/LedgerX/actions/runs/40517583432) |
| [interval-financial-risk #3](https://github.com/dev-belly/interval-financial-risk/pull/3) | `880eadb` | [86e3496](https://github.com/dev-belly/interval-financial-risk/commit/86e3496ed059bbb89ce5e3b07ccce63cf3bd81a5) | [run 1](https://github.com/dev-belly/interval-financial-risk/actions/runs/40517598788) |
| [wecom-agent-platform #6](https://github.com/dev-belly/wecom-agent-platform/pull/6) | `b46c287` | [7fac4f2](https://github.com/dev-belly/wecom-agent-platform/commit/7fac4f2eaced785f7b3afa91d531a23d43345ed1) | [run 1](https://github.com/dev-belly/wecom-agent-platform/actions/runs/40517607014) |
| [digital-craftsman #6](https://github.com/dev-belly/digital-craftsman/pull/6) | `61c065f` | [b0ce3de](https://github.com/dev-belly/digital-craftsman/commit/b0ce3decce372ec7722c375b11f41627ebf26887) | [run 1](https://github.com/dev-belly/digital-craftsman/actions/runs/40518976997) |
| [personal-ai-chat #3](https://github.com/dev-belly/personal-ai-chat/pull/3) | `9e8fbce` | [802328c](https://github.com/dev-belly/personal-ai-chat/commit/802328c2469e736ea08003cbbd28c77c9ce9c7c8) | [run 1](https://github.com/dev-belly/personal-ai-chat/actions/runs/40517615910) |
| [investor-network-gnn #3](https://github.com/dev-belly/investor-network-gnn/pull/3) | `2249c3f` | [c9a3731](https://github.com/dev-belly/investor-network-gnn/commit/c9a37316a5aee35709b9a060375c15db6f8633df) | [run 1](https://github.com/dev-belly/investor-network-gnn/actions/runs/40517626403) |
| [NetworkClear #6](https://github.com/dev-belly/NetworkClear/pull/6) | `6f4f697` | [c2b8ec2](https://github.com/dev-belly/NetworkClear/commit/c2b8ec23ad58a2080c73e4d12a47698e685f61c2) | [run 1](https://github.com/dev-belly/NetworkClear/actions/runs/40517634281) |
| [ashare-multifactor-research #3](https://github.com/dev-belly/ashare-multifactor-research/pull/3) | `c422165` | [edf60a9](https://github.com/dev-belly/ashare-multifactor-research/commit/edf60a9b88b03179f6d9882aac6e7f32c0c2fa1d) | [run 1](https://github.com/dev-belly/ashare-multifactor-research/actions/runs/40517643869) |
| [AuditLens #10](https://github.com/dev-belly/AuditLens/pull/10) | `c6a83bc` | [11cebee](https://github.com/dev-belly/AuditLens/commit/11cebee024019be805014e36550dc0657cead834) | [run 1](https://github.com/dev-belly/AuditLens/actions/runs/40519513548) |
| [ranxin-mini-program #55](https://github.com/dev-belly/ranxin-mini-program/pull/55) | `291f1c4` | [67b73be](https://github.com/dev-belly/ranxin-mini-program/commit/67b73be826bf0f01d0d3181e315dc5902d968316) | [run 1](https://github.com/dev-belly/ranxin-mini-program/actions/runs/40523783414) |


The profile's two fixed Action refs accompany this record. Local checks pass
for five deterministic SVGs, three flagship panels, 13 documents and 113
local references; the generated catalog covers 19 public projects. The
profile synchronization has its own PR CI. Push workflows on new merge
commits run separately from the completed PR workflows listed above.

## Financial correctness repairs · 2026-10-27

This pass completes six previously drafted fixes in four financial projects.
Each branch was reviewed and brought onto its latest maintenance baseline.
Two AlphaForge regression files needed formatting to unblock CI; AuditLens
needed its README badge and per-file counts reconciled with actual collection.
The changes address calculation and state invariants, without inventing new
business-performance results.

| Project / repair | Concrete failure and resulting behavior | PR workflow |
| --- | --- | --- |
| [AlphaForge #5](https://github.com/dev-belly/alphaforge/pull/5) | A label spanning trading sessions could cross the test boundary despite a calendar-day purge. Purge and embargo now count the supplied sessions, including closure gaps. | [Python / integration](https://github.com/dev-belly/alphaforge/actions/runs/40501138926) |
| [AlphaForge #6](https://github.com/dev-belly/alphaforge/pull/6) | Differencing post-return NAV omitted the first complete rolling window. Returns now compound exactly the requested observations, including window=1. | [Python / integration](https://github.com/dev-belly/alphaforge/actions/runs/40501145366) |
| [AlphaForge #7](https://github.com/dev-belly/alphaforge/pull/7) | Rectangular asset/factor exposure matrices failed, and covariance-table reordering changed an asset's variance. Residuals are reconstructed in asset space and both factor axes align by label. | [Python / integration](https://github.com/dev-belly/alphaforge/actions/runs/40501151214) |
| [AuditLens #9](https://github.com/dev-belly/AuditLens/pull/9) | An epsilon moved 9,999,999.99 into the 1/10 digit buckets. Decimal text preserves 9/99, exact powers, adjacent floats and reconciled statistical counts. | [Linux / Windows](https://github.com/dev-belly/AuditLens/actions/runs/40501160494) |
| [ControlTrace #8](https://github.com/dev-belly/ControlTrace/pull/8) | A timely emergency approval with a whitespace-only person ID suppressed the missing-approver item. It now remains available for manual review, with the original ID retained in evidence and replayable workpapers. | [Linux / Windows](https://github.com/dev-belly/ControlTrace/actions/runs/40501167525) |
| [TradeForge #21](https://github.com/dev-belly/TradeForge/pull/21) | A rejected fill previously entered the journal and consumed its ID. Order validation now precedes journal, identifier and inventory updates. | [Python / native / distribution](https://github.com/dev-belly/TradeForge/actions/runs/40501172993) |

All six PR workflows pass and the fixes are merged. AlphaForge's final
combined merge is [`8f58e7f`](https://github.com/dev-belly/alphaforge/commit/8f58e7f2481b0082ed7cdd996d5f974940a25617),
with tree `c69e5e8662eca9e8ef3a414db9ddba55ead3a3b7` exactly matching the
locally exercised combination of all three fixes. That combined version
passes **1,357 full-suite tests**, Ruff lint/format and mypy over **65 source
files**. Individual local split, metrics and covariance groups additionally
pass **87 / 85 / 49 cases**. These are test executions on overlapping suites,
not counts to sum into an inflated unique total.

AuditLens runs its ten-stage pipeline and
passes **530 tests**; its three PR matrix jobs also pass. ControlTrace's first
local full run passes 117 tests and hits a three-second Streamlit test timeout
in one UI case; that case passes when rerun in isolation. Its rule/source
change is checked separately from this runner timing issue; both current PR
matrix runs pass. TradeForge passes **180 local OMS, domain, order-book,
matching, queue and documented-command tests**, followed by all eight PR CI
jobs: Python 3.11–3.13, Linux/Windows installed wheels, native differential
tests, sanitizers and deterministic replay. The local broader unit attempt
initially lacked the declared Typer dependency; it was installed before the
180-case focused rerun, rather than treating an incomplete environment as a
source-code regression.

Other merged checkpoints are [AuditLens `594f0d4`](https://github.com/dev-belly/AuditLens/commit/594f0d42e1eaf98a3c5dee6c0bac598f39cff0ab),
[ControlTrace `279cb5b`](https://github.com/dev-belly/ControlTrace/commit/279cb5b41dbc31955b9a4c1d66b2cb55cd38953e)
and [TradeForge `f71d10f`](https://github.com/dev-belly/TradeForge/commit/f71d10fcd627a2be8f12638ac68b0ca30885cd37).
Their post-merge main workflows pass. AlphaForge's final post-merge workflow
was still running at this checkpoint; its combined three-fix content matches
the completed local test tree, alongside each successful
PR workflow above. No default-branch completion is inferred from a PR result.

**Archived performance remains archived.** AlphaForge's old synthetic sample
and historical-price comparison have not been refitted under the corrected
trading-session split. Their original figures are retained as historical
artifacts and do not establish leakage-free out-of-sample performance. The
profile, project directory and project briefs now expose that limitation;
return-arithmetic replay cannot certify a model's original split protocol.

The [interview counterexamples](INTERVIEW_PLAYBOOK.zh-CN.md#用四个修复练习追问)
connect these changes to time units, matrix dimensions, digit buckets and
transactional rejection. Author understanding, external use and production
benefit still require their own evidence.

## Observed SBA funding cohorts · 2026-10-26

[CreditVintage #35](https://github.com/dev-belly/CreditVintage/pull/35) adds
observed, retrospective funding-cohort validation in v0.8.0. Both complete
hash-pinned official CSVs contain 1,236,084 logical records. The converter
counts exclusions, retains one earliest eligible recorded borrower group,
and samples by outcome-independent row hashes into 20,000 train / 5,000
calibration / 10,000 test loans. Source bytes, frozen protocol and audit were
reconstructed exactly from both originals.

Four approval inputs use training-only imputation, missing indicators, scaling
and categories. Each earlier 24-calendar-month outcome horizon matures before
the next funding stage starts. The test has **89 recorded events**. Logistic
AUC is **0.672341** (month-bootstrap 95% interval **0.6246–0.7175**), AP 0.018470,
Brier 0.009011. Isotonic lowers Brier to **0.008819** while lowering AUC to
**0.658399**. At the same 1,000 review slots the methods capture 26/89 and 24/89
events, respectively. Neither capture nor calibrated probability estimates
prevented loss. All methods, both test years and all 900 bootstrap rows remain.

The final PR passes **428 tests and 28 subtests**, including **52 new cases**.
All eight [PR CI jobs](https://github.com/dev-belly/CreditVintage/actions/runs/40272342645)
pass, including clean installed distributions and same-ZIP refitting across
Ubuntu/Windows and Python 3.12/3.13. The [Pages build](https://github.com/dev-belly/CreditVintage/actions/runs/40272342687)
passes; four final Chrome desktop/mobile captures were visually inspected.
The mobile check confirms all nine metric cells fit and the page has no
horizontal overflow. Core merge [`55ad624`](https://github.com/dev-belly/CreditVintage/commit/55ad6249fbee7754a2b1fc687fbff6a1143c3bad)
retains exactly the tested source tree.

Local source and installed-wheel checks refit from the frozen bytes, recompute
all metrics and queues, and reject rehashed false AUC and nonfinite scores.
Malformed manifest inventories have controlled CLI errors. Tests independently
check AUC with Mann–Whitney ranks, plain Brier arithmetic, calendar boundaries,
held-out outcome/feature isolation, paired resampling and one-class replicates.
Ruff lint/format and strict mypy pass. Source/wheel archives include data,
protocol, audit, license notices, converter and the actual-run issue form.
A complete site rebuild/refitting passes; CI retains desktop/mobile Chrome
previews and replays the same Linux-built SBA ZIP on Windows and Python 3.13.

The final snapshot lacks historical first-publication times and feature
revisions. It is **retrospective funding-cohort validation**, not a claim of
historical public availability or a replacement for the synthetic event-time
contract. Recorded 24-month SBA charge-off is distinct from 180-day delinquency
and UCI targets. The initial rate is missing for 15,250 training loans; this
shift is retained. Group keys are an imperfect, linkable recorded-identity
heuristic, not verified firms or anonymous identities. US SBA results do not
establish current Chinese lending performance, fairness, deployment or adoption.

[Run on Windows/Linux](START_HERE.md#creditvintage-validate-observed-loans-across-time) ·
[Public report](https://dev-belly.github.io/CreditVintage/sba-credit/) ·
[Source and method](https://github.com/dev-belly/CreditVintage/blob/main/docs/SBA_CREDIT.md) ·
[Actual-run feedback form](https://github.com/dev-belly/CreditVintage/issues/new?template=sba_reproduction.yml).


## Explicit coverage acceptance · 2026-10-25

[CreditVintage #34](https://github.com/dev-belly/CreditVintage/pull/34) adds
user-defined overall/monthly coverage and minimum-sample rules in v0.7.0.
`check-feature-quality` validates the source diagnostic, retains every rule and
returns 0 only for all-pass, 3 for failed/insufficient policy, or 2 for invalid
inputs/evidence. Independent verification can succeed with `policy_status: fail`.
A partial/tolerant policy pass never relaxes scoring/distribution completeness.

**376 tests and 28 subtests pass**, including 39 new policy cases. Hand counts
check that 2/3 fails a required decimal 0.66666667 despite its displayed rounding;
78/80 passes 0.975 but fails 0.975000000000000001. Tests retain empty, small,
future and mixed groups, enforce strict policy parsing, preserve source files
and replay a self-contained bundle after its original report is removed.
An independently retained policy digest rejects a fully regenerated replacement
using different rules; it does not authenticate events under those rules.

Ruff lint/format, strict mypy and 85 local documentation links pass. Wheel and
source archives include the new module/template and old v0.5.0 compatibility
fixture; existing quality/distribution bytes retain their contracts. Full site
refitting/replay passes. Clean installed wheels outside the source trees exercise
healthy, missing-input and insufficient policies with the performance file absent,
enforce the external pin and reject a rehashed false pass. The installed gap
case retains two passed rules and one failed rule, distinct from its one
incomplete current application.

The [public synthetic check](https://dev-belly.github.io/CreditVintage/feature-check/)
requires full coverage for all three current inputs and deliberately retains three
failures: 318/320, 319/320 and 319/320. Its four incomplete applications remain
in the denominators. These are illustrative conditions, not calibrated business
limits or evidence of real-world failure rates.

[Run the rules](START_HERE.md#creditvintage-check-explicit-coverage-conditions) ·
[Policy contract and trust limits](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_POLICY.md) ·
[Official-tool comparison](OPEN_SOURCE_ROADMAP.zh-CN.md).


## Decision-time feature coverage · 2026-10-25

[CreditVintage #33](https://github.com/dev-belly/CreditVintage/pull/33) adds
`monitor-feature-quality` and event-level diagnostic replay in v0.6.0. Every
visible application contributes three expected feature slots. The report
separates on-time availability, known late arrival, post-decision observation
and no event visible by the report cutoff; it retains small monthly counts and
null rates for empty populations. A diagnostic can verify while reporting gaps;
strict scoring/distribution paths continue to reject missing inputs.

Local validation passes **337 tests and 28 subtests**, including 27 new
quality/compatibility cases, Ruff lint/format and strict mypy. Hand examples
check exact population denominators, unique incomplete-application counts,
first-arrival delay, future exclusion and empty/small cohorts. A fixture generated
by a separately installed public v0.5.0 wheel pins all six old feature-report
file hashes; current code reproduces them exactly. The source archive includes
this compatibility fixture.

All eight [PR CI jobs](https://github.com/dev-belly/CreditVintage/actions/runs/40167747736)
pass across Ubuntu/Python 3.12 and 3.13 and Windows/Python 3.12, including installed
distributions and cross-runtime replay. The [Pages build](https://github.com/dev-belly/CreditVintage/actions/runs/40167747732)
passes; its real-Chrome desktop and mobile previews were visually reviewed.
The merged source is [`a6f6558`](https://github.com/dev-belly/CreditVintage/commit/a6f6558539b21e1d9fd614f882f8eae4e557b668).

Clean installed wheels outside both source trees replay healthy and incomplete
two-CSV diagnostics while the performance file is absent. The incomplete case
retains 80 visible current applications / 79 complete / one incomplete; the
same input still fails the strict distribution gate, and rehashed false coverage
is rejected. The complete local public-site rebuild/refitting also passes.

The [public synthetic quality case](https://dev-belly.github.io/CreditVintage/feature-quality/)
uses 480 reference / 320 visible current applications, with 316 complete current
and 160 future current applications. Its four unavailable slots are deliberately
injected. These are event-coverage diagnostics, not raw CSV null rates,
generic quality rules, credit-risk conclusions or production failure rates.

[Run the diagnostic](START_HERE.md#creditvintage-diagnose-missing-decision-time-features) ·
[Method and input contract](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_QUALITY.md) ·
[Evidently / GX / TFDV comparison](https://github.com/dev-belly/CreditVintage/blob/main/docs/COMPARISON.zh-CN.md).


## Input-distribution monitoring · 2026-10-24

[CreditVintage #32](https://github.com/dev-belly/CreditVintage/pull/32) adds
`monitor-features` and `verify-feature-monitor` in the checked v0.5.0 distribution.
Two application/feature CSVs produce a report for four numeric inputs and segment
composition. The command does not read an outcome file or fit a model. It reuses
the decision-time snapshot contract and retains input events, chosen snapshots,
cumulative/category counts, monthly counts and the rendered report for replay.

Local validation passed **310 tests and 28 subtests**, including 31 new cases,
Ruff lint/format and strict mypy. Exact hand calculations and three generated
cases agree with SciPy's independent KS implementation. Checks cover both
directions of a constant-population shift, integer principal distinctions above
`2^53`, late revisions, future applications, small months and rehashed false
evidence. A clean non-editable wheel outside both source trees verifies the
two-CSV route with the performance file absent; its 120 reference / 80 current
application counts and five monitored inputs replay, and a rehashed false
distance is rejected. The full local public-site build/refitting also passes.

Merged source: [`bc650c2`](https://github.com/dev-belly/CreditVintage/commit/bc650c2491525c892cb76b82106969362f745d65).
All [eight final PR CI jobs](https://github.com/dev-belly/CreditVintage/actions/runs/40103834623)
passed across Linux/Windows and Python 3.12/3.13. The
[Pages build](https://github.com/dev-belly/CreditVintage/actions/runs/40103834553)
also passed; its real-Chrome 1440×1600 desktop and 390×2400 mobile screenshots
were reviewed, including a correction to keep distance values visible on phones.

The [default public report](https://dev-belly.github.io/CreditVintage/feature-monitor/)
uses a different, larger synthetic fixture: 480 reference / 320 visible current
applications, with 160 future current applications. Fixed marginal distances
do not establish significance, default risk, model deterioration or causality.
Missing-feature rates, arbitrary schemas, real out-of-time validation and
independent adoption remain separate gaps.

[Run the checked package](START_HERE.md#creditvintage-inspect-input-distributions-without-labels) ·
[Method and evidence inventory](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_MONITORING.md) ·
[Comparison with established tools](https://github.com/dev-belly/CreditVintage/blob/main/docs/COMPARISON.zh-CN.md).

PITBridge [#24](https://github.com/dev-belly/PITBridge/pull/24) also follows up on
the [review in #7](https://github.com/dev-belly/PITBridge/issues/7#issuecomment-6061916414):
the optional example rejects malformed numeric text before conversion and keeps
zero-padded int64 revision handling independent of Python's integer-string digit
limit. All 137 local tests and ten PR CI jobs passed. The optional example is
source-level material; the installed v0.2.0 native importer already has the
corresponding strict syntax. This is feedback and maintenance evidence, not proof
of production adoption.

## Checked release and audit evidence integrity · 2026-10-24

PITBridge [#21](https://github.com/dev-belly/PITBridge/pull/21) publishes the
[v0.2.0 checked wheel and source archive](https://github.com/dev-belly/PITBridge/releases/tag/v0.2.0).
The successful main CI at `c04c533274e2e96e768d73ab78e99ab4ea9edd46` retained the
actual installed/replayed distributions, installed-check evidence, exact-commit
manifest and checksums. All five public assets were downloaded again and verified;
the public wheel then passed clean installation, four scalar/rolling JSON/CSV
replays and two small benchmark trials outside the checkout. This closes the
gap between main-only CSV/benchmark features and the old v0.1.0 release.
[Start here](START_HERE.md#pitbridge-historical-feature-selection) installs that wheel directly.

The work also addresses selection and review integrity in existing projects:

- **StatementTrace [#6](https://github.com/dev-belly/StatementTrace/pull/6):**
  reported revenue growth requires adjacent configured fiscal periods. A skipped
  year or date gap cannot become a valid-looking annual growth figure. Current
  facts and other ratios remain available; all nine saved demo files retain
  their bytes. The 53/52-week calendar remains supported.
- **AuditLens [#7](https://github.com/dev-belly/AuditLens/pull/7) and
  [#8](https://github.com/dev-belly/AuditLens/pull/8):** two scores/amounts one
  binary64 step apart could change the selected voucher while retaining the same
  12-digit source fingerprint. `selection-v2` retains 17 significant digits,
  quotes source fields and identifies its format. The review queue and high-risk
  extract now also preserve CR/LF/CRLF and fullwidth formula-like identities;
  a completed-workpaper regression checks the actual handoff.
- **AuditLens [#6](https://github.com/dev-belly/AuditLens/pull/6):** the existing
  cleaning draft is completed against current main. All normalized source
  columns participate in exact-duplicate detection, so conflicting currency,
  FX, invoice or approval evidence is retained for validation. Nonfinite amounts
  and overflowing FX products follow explicit missing/fallback rules. The full
  30,128-voucher pipeline leaves every report byte unchanged relative to the
  same-environment pre-cleaning baseline.
- **ControlTrace [#7](https://github.com/dev-belly/ControlTrace/pull/7) and
  [#6](https://github.com/dev-belly/ControlTrace/pull/6):** CSV policy and timeline
  interpretation have explicit replay versions. Current version 0.2.10 / format
  5 orders evidence by actual UTC instants while retaining source timestamps.
  Old formats 2–4 reconstruct their original timeline and report the legacy
  order, rather than reinterpreting an old review fingerprint. Actual 0.2.8 and
  0.2.9 synthetic exports are retained as regression fixtures. Re-running the
  0.2.9 test database correctly returns its old-order review to pending; all
  28 source JSON/CSV files and the dataset fingerprint remain byte-identical.

Local full suites pass **134 PITBridge + 42 StatementTrace + 519 AuditLens +
113 ControlTrace = 808 tests**. These counts cover implementation contracts,
not independent clients, real fraud/default outcomes or source authenticity.
The ordinary synthetic reports and numerical evidence are unchanged, apart from
the explicitly versioned AuditLens source-fingerprint record.

| Project | Main revision | Local suite | Exact main run |
| --- | --- | ---: | --- |
| PITBridge | `3715813` | 134 | [CI](https://github.com/dev-belly/PITBridge/actions/runs/40067075342) · [Pages](https://github.com/dev-belly/PITBridge/actions/runs/40067075363) |
| StatementTrace | `6804c4a` | 42 | [CI and deployment](https://github.com/dev-belly/StatementTrace/actions/runs/40066128539) |
| AuditLens | `cbc9365` | 519 | [Pipeline, tests and reproducibility](https://github.com/dev-belly/AuditLens/actions/runs/40068027568) |
| ControlTrace | `4428ea9` | 113 | [Linux and Windows CI](https://github.com/dev-belly/ControlTrace/actions/runs/40068060419) |

Two delivery problems were also resolved transparently. A CSV documentation
upload in PITBridge was truncated; [#22](https://github.com/dev-belly/PITBridge/pull/22)
restores the complete contract. Uploaded blobs are now compared with local Git
blob hashes. A later main Chrome run timed out during the initial 15-second
session creation before executing report assertions;
[#23](https://github.com/dev-belly/PITBridge/pull/23) gives only cold startup
60 seconds, preserves driver logs and keeps ordinary commands/assertions strict.
[The subsequent main CI](https://github.com/dev-belly/PITBridge/actions/runs/40067075342)
passes all ten jobs; the existing release is retained without replacement.

The remaining portfolio evidence gaps still require suitable real chronological
data and independently observed use. Additional code or test counts cannot
substitute for those. Keep public static credit data, curated filing excerpts
and synthetic event/audit cases separate when discussing results.

## Installed CSV intake and exact report identities · 2026-10-23

Five merged PRs extend existing projects: PITBridge [#19](https://github.com/dev-belly/PITBridge/pull/19)
and [#20](https://github.com/dev-belly/PITBridge/pull/20), StressAtlas
[#6](https://github.com/dev-belly/StressAtlas/pull/6), StatementTrace
[#5](https://github.com/dev-belly/StatementTrace/pull/5) and NetworkClear
[#5](https://github.com/dev-belly/NetworkClear/pull/5).

PITBridge's installed CLI now reads exact-schema scalar/rolling CSV tables with
no pandas dependency. Intake preserves leading-zero/NA-like IDs and int64
revisions, names file/physical-line errors and validates before report writes.
The installed-wheel checker runs both JSON and CSV paths outside the checkout,
fully replays four bundles and compares feature/lineage tables byte for byte.

All four projects now preserve unusual names in review CSVs and browser
selectors. Visible `text: ` markers protect formula-shaped labels; CR/LF/CRLF
remain quoted cell content. ASCII JSON selector keys prevent CR/LF/NUL and
whitespace identities from collapsing in HTML. Original JSON and financial
numeric values retain their meaning. Only saved HTML and its hash were refreshed;
source and numerical evidence files were checked byte for byte. The contracts
explain regeneration from saved JSON for earlier affected report formats.

| Repository | Main commit | Local suite | Actual Chrome selections | Main checks |
| --- | --- | ---: | ---: | --- |
| PITBridge | `9949a82` | 126 | 4 | [CI](https://github.com/dev-belly/PITBridge/actions/runs/39931482482) · [Pages](https://github.com/dev-belly/PITBridge/actions/runs/39931482576) |
| StressAtlas | `01e9843` | 80 | 10 | [CI](https://github.com/dev-belly/StressAtlas/actions/runs/39931491066) · [Pages](https://github.com/dev-belly/StressAtlas/actions/runs/39931491140) |
| StatementTrace | `bb2ac7c` | 39 | 4 | [CI and deployment](https://github.com/dev-belly/StatementTrace/actions/runs/39931468275) |
| NetworkClear | `1784cc3` | 42 | 5 | [CI and deployment](https://github.com/dev-belly/NetworkClear/actions/runs/39931475585) |

All listed main workflows passed. The 287 local tests and 23 real-Chrome
selections validate these implementation paths; they do not establish source
authenticity, production adoption or predictive quality.

## Monitoring input readiness · 2026-10-23

[CreditVintage #28](https://github.com/dev-belly/CreditVintage/pull/28), head
`2970378df99a10e0f18e507db07fcb6988f72c01`, tree
`393c9a014954cb1058628b87f113a37d213537ea`: remote and locally checked source trees
match. `preflight --as-of YYYY-MM-DD` checks mature train/calibration populations
and the visible current cohort without fitting or writing. Current outcome labels
are neither required nor counted. Not-yet-visible current applications and inputs
outside configured windows are reported separately.

Preflight and monitoring share cutoff, current-population and label-scope gates;
the fitting path and preflight share the actual historical cohort selection.
Historical populations still require 20 records and both mature outcomes; current
monitoring needs 20 visible applications and their decision-time features. An
undersized current population fails before fitting. Default evaluation preflight
retains its mature test-label requirement.

Local **273 tests + 28 subtests**, Ruff lint/format, strict mypy and whitespace
checks pass. Twenty new regressions cover guards against fitting, ignored current
outcomes, missing historical labels/classes, the 19/20-application boundary,
missing visible features, future inputs, custom calendars and real CLI workflows.
Clean 0.4.0 wheel replay outside both source trees removes every current outcome:
preflight returns 240 training, 120 calibration, 80 visible current and 40 future
current applications; actual monitoring verifies the same 80. Default evaluation
rejects the missing test outcomes. Public-data refitting and optional lineage also
pass. [Cross-platform checks](https://github.com/dev-belly/CreditVintage/pull/28/checks)
and [v0.4.0 release evidence](https://github.com/dev-belly/CreditVintage/releases/tag/v0.4.0)
retain the remote validation and checked distributions.

This checks input/cohort readiness, with no scores or PSI. It cannot guarantee
numerical fitting, useful score variation, source authenticity or predictive
quality. Existing input fields, model protocol and report verification tolerances
remain compatible; the [upgrade notes](https://github.com/dev-belly/CreditVintage/blob/main/docs/releases/v0.4.0.md)
describe the optional CLI argument and unchanged evaluation behavior.

## Checked calendar patch release · 2026-10-22

[CreditVintage #27](https://github.com/dev-belly/CreditVintage/pull/27) delivers
the calendar fix as the [v0.3.2 checked release](https://github.com/dev-belly/CreditVintage/releases/tag/v0.3.2).
The runtime implementation is unchanged from #26 below. The version bump and
upgrade notes make strict CSV/cutoff parsing available to installed-package
users; the profile, first-run commands and project brief now point to that version.
Earlier release tags and their original assets remain available.

The release contains the wheel, source archive, installed-check evidence,
commit/version manifest and SHA-256 list retained from successful main CI.
[The PR checks](https://github.com/dev-belly/CreditVintage/pull/27/checks) cover
Linux Python 3.12/3.13, Windows Python 3.12 and refitting of the same saved card
evidence on another OS/runtime. Local validation additionally passes 60 focused
release/input tests and clean 0.3.2 wheel replay outside both source trees,
including rejection of alternate dates and complete optional lineage verification.

The [upgrade notes](https://github.com/dev-belly/CreditVintage/blob/main/docs/releases/v0.3.2.md)
explain the stricter format: commands, field names, dependency pins and model
protocol are unchanged; existing generated canonical-date reports still verify.
This packaging step adds no new prediction or real-world deployment claim.

## Strict calendar inputs and saved evidence · 2026-10-22

[CreditVintage #26](https://github.com/dev-belly/CreditVintage/pull/26), head
`1925bb959d7c27528b79dee8405ed2819b04ff4c`, tree
`72b21b482c20db8425a764073e3fd721afba2db1`: the remote tree matches the locally
checked source. CSV diagnostics and monitoring previously accepted compact dates
such as `20220101` and ISO week dates while cohort JSON required `YYYY-MM-DD`.
One strict parser now covers all event CSV dates, cohort configuration, the
monitoring cutoff and saved evaluation/monitor/benchmark evidence. Diagnostics
identify the file, physical line and column; invalid dates do not create reports.

Local **253 tests + 28 subtests** pass, including 26 new workflow regressions.
Ruff lint/format, strict mypy and patch whitespace checks pass. A source-built
wheel runs in a clean environment outside both repositories: it rejects an
alternate CSV date and an ISO week cutoff, refits the 30,000-record card
experiment across five splits, verifies the report/review workflows and replays
the pinned PITBridge integration. Existing published canonical-date reports still
verify. [Cross-platform checks](https://github.com/dev-belly/CreditVintage/pull/26/checks)
retain the remote results for the exact change.

This is a source change after the [v0.3.1 release](https://github.com/dev-belly/CreditVintage/releases/tag/v0.3.1),
whose existing wheel retains its original CSV/cutoff parsing. The compatibility
notes distinguish those paths. Input-format checks do not establish source
authenticity, future-period model quality or independent adoption.

## Editable CSV workflow and input diagnostics · 2026-10-16

[CreditVintage #20](https://github.com/dev-belly/CreditVintage/pull/20), head `3c3b37c7ff80037a4cc942947027bb1f06e86be6`, tree `203cbb13b0520b1fe95d3385eeea8093f38ebded`: the remote tree matches the checked local source. New `init-inputs` writes 480 explicitly synthetic applications, 1,584 feature events, 2,880 performance rows and a complete calendar. `check-inputs` collects row/type/encoding errors, then checks relationships, decision-time features and all three mature cohorts with the actual record and snapshot contracts. It reports blocked checks explicitly, preserves input bytes and fits no model.

Local **224 tests + 28 subtests** pass. Twenty-two new input regressions cover guards against fitting classifiers/calibrators, input preservation, future-only feature revisions, missing non-event reports across all cohorts, UTF-8/BOM failures, bounded output and physical locations for multi-line CSV records. Ruff/format and strict mypy pass. A clean installed wheel generates and diagnoses the files, runs the supplied-CSV evaluation, verifies 120 holdout applications and locates an intentionally invalid principal at applications.csv line 2. [Checked v0.3.0 assets](https://github.com/dev-belly/CreditVintage/releases/tag/v0.3.0) retain that installed-check result and commit-bound checksums. This is functional reuse evidence, not independent adoption or bank-data validation.

## Numerical replay across environments · 2026-10-15

[CreditVintage #19](https://github.com/dev-belly/CreditVintage/pull/19), head `366ed3332ef9db6d0ba793aad41ea59c3c7c76bb`, tree `0d37e0a868630fcbf1e7b93efe2b9697cec50c3e`: fixes a downloaded report failing refit when newer scikit-learn changed the tree results. Version 0.2.1 pins NumPy 2.3.5, SciPy 1.17.0 and scikit-learn 1.8.0 for wheel installation and public builds. The verifier checks recorded numerical versions before fitting and reports matching requirements. The v2 protocol fits logistic regression with Newton-Cholesky and a fixed 1e-10 convergence tolerance, then uses a six-decimal input grid for isotonic calibration; raw logistic probabilities are retained without rounding and verification tolerances remain unchanged. Earlier v1 evidence retains its original model protocol and rendering, and a saved v1 experiment successfully refits with the new verifier.

Local **202 tests + 28 subtests**, Ruff/format, strict mypy and legacy evidence replay pass. The card regressions include runtime mismatch detection and invariance to tiny platform-level score drift. CI additionally transfers the same Linux/Python 3.12 card evidence and checked wheel to Linux/Python 3.13 and Windows/Python 3.12 for full source-based refitting. The first-run commands and profile links use the [v0.2.1 checked release](https://github.com/dev-belly/CreditVintage/releases/tag/v0.2.1). Earlier releases and their original validation records remain available.

## Larger card cohort and checked release · 2026-10-15

[CreditVintage #18](https://github.com/dev-belly/CreditVintage/pull/18), head
`2f6bc84741f2c5a11895b98de805a7bc56588ca1`, tree `9c1e1af0d3cfa5da997f1ca3af5cf7df84061eb1`:
the tested checkout and remote tree match. The package includes the attributed UCI 350
table, converted from original verified ZIP/Excel bytes without changing integer values,
row order or target. Five fixed 18,000/6,000/6,000 splits compare four methods and three
review capacities. All 120,000 model scores and 60 policy rows remain available.
This single historical cohort's random splits do not establish future-period availability
or the separate event pipeline's 180-day DPD target.

Local **200 tests + 28 subtests**, Ruff/format and strict mypy pass. The full suite uses
the pinned PITBridge integration. A fresh virtual environment outside the repositories
installs the source-built wheel and refits every card model, then verifies original
report/review and optional lineage paths. The complete public build and original-source
conversion also pass. Eleven new regressions cover transformation isolation, native labels,
equal review counts, changed scores/queues/ZIPs and release integrity.

The v0.2.0 release flow retains the exact CI-tested distributions, their installed-check
result, version/commit manifest and SHA-256 list. Publication accepts only successful
push-to-main CI in this repository; it downloads that exact run's artifact and rechecks it
before creating a new release. Existing tags are preserved. The first-run guide installs
that checked wheel and adds the offline card benchmark and refit commands.
See [CI and installation checks](https://github.com/dev-belly/CreditVintage/pull/18/checks)
and [release artifacts](https://github.com/dev-belly/CreditVintage/releases/tag/v0.2.0).

## Observed credit and custom calendars · 2026-10-15

[CreditVintage #16](https://github.com/dev-belly/CreditVintage/pull/16), PR head
`2cc7094c01f17911e1b43ad3facdf8bed575c8e4`, merged at
`0e33e89b69c5e9024c016cb2d05ce484b077c7c9`, tree
`971461c48154212e39b8711c551f6f1c691d3182`: the tested checkout and remote tree match.
The separate [UCI comparison](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT.md)
freezes observed original bytes and a 600/200/200 random split, learns transformations only on train,
and refits from saved source during verification. Native good/bad labels have no decision dates
or 180-day DPD target. Calibration worsened Brier from 0.162263 to 0.169376; the result is retained.

The [custom-input path](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md)
accepts strict seven-date JSON in evaluation, comparison and monitoring; model-free `preflight`
reports excluded applications and cohort counts. Tests shift complete event data four years earlier
and reject ambiguous configuration and rehashed public evidence changes.

Local validation: **178 tests + 28 subtests**, Ruff/format and strict mypy pass. A source archive
builds its wheel; a clean environment outside both checkouts verifies custom calendars, preflight,
the bundled public data, original report/review workflows and the pinned optional lineage.
The complete site build verifies the UCI report from original bytes; HTML has eight table rows and
all local result links resolve. Cross-platform results are recorded by
[CI](https://github.com/dev-belly/CreditVintage/actions/runs/38669691059): three full-suite and
three installed-distribution jobs succeeded on Linux 3.12/3.13 and Windows 3.12.
[The PR public build](https://github.com/dev-belly/CreditVintage/actions/runs/38669690897) succeeded;
its deployment is intentionally skipped for pull requests.

[TradeForge #15](https://github.com/dev-belly/TradeForge/pull/15) is merged at `bdc1f09` after its
six checks succeed. Documentation distinguishes the default synthetic experiment from observed
quote packets with hypothetical fees, latency and matching.

## Business integrity and delivery · 2026-10-13

本轮从实际失败输入补齐业务约束，保留正常演示口径。面试先用 [速讲卡](面试速讲卡.zh-CN.md)，每个案例都有源码、测试和中文运行入口。

| 项目与已核对提交 | 业务改变 | 验证证据 |
| --- | --- | --- |
| CreditVintage [#14](https://github.com/dev-belly/CreditVintage/pull/14)、[#15](https://github.com/dev-belly/CreditVintage/pull/15)；最终 PR head `036e91c`、合并 `83bf42a` | 一个读取事务捕获无标签队列与复核事件，导出可脱离数据库重放的底稿；可选外部检查点识别整包重写。重复 JSON 键递归拒绝，更新文件摘要也不能绕过。 | 本机最终 **154 tests + 28 subtests**，Ruff/format/strict mypy 通过；实际 Windows CLI 核验 48 条案例、2 条事件、47 queued / 1 resolved、完成率 1/48。[#14 CI](https://github.com/dev-belly/CreditVintage/actions/runs/38373482559)和 [#15 CI](https://github.com/dev-belly/CreditVintage/actions/runs/38393666439)六项测试/安装包任务全成功，覆盖 Linux 3.12/3.13 与 Windows 3.12。独立复查确认重复键反例由接受转为拒绝。[交付案例](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_DELIVERY.md) |
| LedgerX [#4](https://github.com/dev-belly/LedgerX/pull/4)；PR head `bd31186`、合并 `b2535f9` | 全批事件先在候选账本验证，后段失败不记入合法前缀；同 ID 同内容复用原记录，改价等内容冲突拒绝。严格 JSONL 接入只在保存成功后输出结果。 | 本机 **83 tests**、Ruff/format/mypy 通过；4 行合成输入首次 appended=3/reused=1，再次 appended=0/reused=4，日志头完全相同。失败替换保留旧文件且没有成功输出。[main CI](https://github.com/dev-belly/LedgerX/actions/runs/38393914907)在 Linux 3.11/3.12/3.13 和 Windows 3.12 全成功。[批次案例](https://github.com/dev-belly/LedgerX/blob/main/docs/BATCH_INGESTION.md) |
| AuditLens [#5](https://github.com/dev-belly/AuditLens/pull/5)；PR head `c2f85f1`、合并 `2e5b3ab` | 同 ID 只合并全部源字段一致的主数据；冲突在日期有损转换前拒绝，提示来源行号与字段而不暴露账号值。四份清洗产物先暂存，受控发布失败恢复旧内容；回滚失败保留备份并给恢复路径。 | 本机 **500 passed / 1 Windows 无 make skip**；新增 36 项，清洗共 93 项。隔离全管线维持 30,128 clean rows、300 复核样本及既有 10 份报告内容（OS 行尾除外）。[PR CI](https://github.com/dev-belly/AuditLens/actions/runs/38375496803)与 [main CI](https://github.com/dev-belly/AuditLens/actions/runs/38393916521)三平台全成功，含 notebook 和报告复现。[主数据案例](https://github.com/dev-belly/AuditLens/blob/main/docs/MASTER_DATA_CASE.zh-CN.md) |
| WeCom [#3](https://github.com/dev-belly/wecom-agent-platform/pull/3)；PR head `8c3263f`、合并 `5a20acd` | 新一代 BM25、向量与结构化行完整准备后一起发布，失败保留旧代。查询固定快照并返回它的 index_revision；旧向量等在途读者结束再清理，缩小语料不混入旧尾部。 | 安装 Chroma 后本机 **86 passed / 2 Windows/POSIX skips**；快照专项 13 项通过，包含真实 Chroma 1.5.9 持久化，无模型下载。Ruff、离线业务示例、wheel 构建与隔离导入通过。[PR CI](https://github.com/dev-belly/wecom-agent-platform/actions/runs/38394160119)三 job 全成功：Linux 87 passed / 1 optional skip，再运行真实 Chroma 1 passed；Windows 85 passed / 3 skips；前端两项测试、类型与构建通过。[索引案例](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/index-snapshots.md) |

Git HTTPS 连接失败时使用 Git-data API 发布，并核对远端 tree 与本机测试提交完全一致；表中记录实际远端 head。这里验证小型本地账务、单进程审计清洗/索引和底稿内部一致性；没有把它们说成跨进程事务、真实客户部署、材料真实性认证或收益证明。

9 月 30 日复查了六个原主项目的展示入口、方法说明、保存的结果文件与 `main` CI；10 月 1 日发布 PITBridge 和 StressAtlas，10 月 2 日新增时点滚动特征、组合尾部风险精度诊断及 PITBridge 到 CreditVintage 的源记录溯源案例。10 月 3–4 日合并数值边界、报告内容、复核文件快照和成交配置修复；10 月 6 日将联合案例依赖固定到 PITBridge 的数值修复版本。10 月 8 日补齐 TradeForge 的费用、执行窗口与在途订单撤销校验，发布 CreditVintage 的完整下载入口及旧页面兼容重放，并从实际线上 ZIP 核验源记录到模型预测。项目定位由可以运行和核验的内容支撑；合成数据上的分数仅用于展示实验流程。

10 月 9 日核对原八个主项目的已发布版本与 CI，并补齐 TradeForge 的含费成本口径、真实 CLI 表格对照及主页证据。

10 月 12 日收尾合并 AlphaForge 的初始本金回撤与安装包默认配置修复，以及 Ranxin 的云端记录归属修复；同步 10 月 11 日已合并的输入、时点和 Windows 修复。下方保留历史运行证据，新增按确切提交记录的当前检查表。

## Installed distributions and portfolio entry points · 2026-10-13

本轮改善首次访问与安装后的使用验证。没有把新增 CI 当作新增预测能力，也没有更换公开实验的数据、分母或模型结论。

| Merged change | What now gets checked | Evidence |
| :--- | :--- | :--- |
| [CreditVintage #12](https://github.com/dev-belly/CreditVintage/pull/12) | 由源码包构建 wheel，安装到全新虚拟环境，工作目录位于两个源码树之外。核心包先在没有 PITBridge 的环境运行：风险报告、早期监控、SQL 分组与 48 笔复核工作区；相同请求重放不追加事件，竞争者的旧版本请求被拒绝，完成率与标签分离检查通过。再安装固定版本的 PITBridge wheel，重放源记录与模型。 | 本机 Python 3.12：118 tests + 28 subtests；Ruff、格式与严格 mypy 通过。[PR CI](https://github.com/dev-belly/CreditVintage/actions/runs/38336627833)的三项完整测试和三项安装包检查共 6 个任务全部成功，覆盖 Linux 3.12/3.13 和 Windows 3.12；[公开站点构建](https://github.com/dev-belly/CreditVintage/actions/runs/38336627880)成功后合并到 `9332fd7`。[合并后 main CI](https://github.com/dev-belly/CreditVintage/actions/runs/38336912568)六项检查及[站点发布](https://github.com/dev-belly/CreditVintage/actions/runs/38336912571)也全部成功。 |
| [PITBridge #13](https://github.com/dev-belly/PITBridge/pull/13) | 由源码包构建 wheel；无包索引安装至全新环境，确认导入来源，再用已安装的命令生成并完整核验快照与滚动报告。补齐 README、源码/报告/issue 链接，并将原有 MIT 声明改成 SPDX 表达式，许可文件继续进入发行包。 | 本机 91 tests 全部通过，最终 wheel 的两份报告均由独立路径重放。[PR CI](https://github.com/dev-belly/PITBridge/actions/runs/38336599774)的 9 个任务全部成功：既有核心、pandas 和 Windows 快速开始检查继续保留，新增 Linux 3.11/3.12 与 Windows 3.12 安装包验证。合并到 `3d3c65b` 后，[main CI](https://github.com/dev-belly/PITBridge/actions/runs/38336776434)和 [Pages](https://github.com/dev-belly/PITBridge/actions/runs/38336776441)也成功。 |

安装验证还做了一个故障对照：从临时 CreditVintage wheel 删去 `business_groups.sql` 后，安装仍能完成，但新脚本在源码目录之外的 `analyze` 命令准确失败，指出已安装包缺少 SQL 文件。这个临时不完整的包没有提交或发布；正常 wheel 通过完整流程。这样核验的是安装包实际使用路径，而不是检查源码里恰好存在同名文件。

主页正文将历次变更移入 [CHANGELOG.md](CHANGELOG.md)，保留全部历史证据链接。首屏改成业务问题 → 在线结果 → 具体实现的入口；三个旗舰面板和所有金融项目仍可访问。公开简介采用已经公开的专业全称；置顶顺序为 CreditVintage、PITBridge、StatementTrace、StressAtlas、AlphaForge、TradeForge，优先展示金融数据与风控方向。

本机主页检查通过：5 张确定性 SVG、3 个正确链接的旗舰面板、7 份文档和本地导航。主页中的 12 个公开演示入口均返回 HTTP 200，页面标题与项目一致。这只证明入口可访问，数值与数据契约仍由每个项目的语义重放验证。

## Current main checks · 2026-10-13

Checked the ten financial project revisions during this review. The two changed projects were checked again after merge; the table names the exact validated commits rather than treating a green badge as evidence for another revision.

| Project | Main commit | Validation |
| :--- | :--- | :--- |
| PITBridge | `3d3c65b` | [Successful CI · 9 jobs](https://github.com/dev-belly/PITBridge/actions/runs/38336776434) |
| CreditVintage | `9332fd7` | [Successful CI · 6 jobs](https://github.com/dev-belly/CreditVintage/actions/runs/38336912568) |
| StressAtlas | `bc577bb` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/38050961034) |
| alphaforge | `d7153c9` | [Successful CI](https://github.com/dev-belly/alphaforge/actions/runs/38186528393) |
| TradeForge | `0d9fba9` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/38261693172) |
| AuditLens | `5f6e641` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/38111034368) |
| ControlTrace | `58b03c1` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/38260082969) |
| StatementTrace | `ed5ee1c` | [Successful CI](https://github.com/dev-belly/StatementTrace/actions/runs/38042185670) |
| NetworkClear | `27bb7c4` | [Successful CI](https://github.com/dev-belly/NetworkClear/actions/runs/38042229238) |
| LedgerX | `6725092` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/38110250708) |

## Business workflow closure · 2026-10-12

本轮在现有代码上补齐处理过程和业务查询，集中解决有失败案例的工程问题。以下测试数量对应各 PR 的本机完整验证；三个 PR 的 Linux 与 Windows 检查均成功后合并。

| Change | Concrete behavior | Validation |
| :--- | :--- | :--- |
| [CreditVintage #11](https://github.com/dev-belly/CreditVintage/pull/11) | 核验后的无标签清单进入 SQLite 工作区；认领、释放、结案、重开以追加事件记录。事务加版本防止并发覆盖，请求 ID 防止重复提交。 | 118 tests + 28 subtests；完整 Windows 命令实际生成 48 案例、处理 1 条、重复结案仍只有 2 个事件；lint、格式与严格类型通过。[PR CI](https://github.com/dev-belly/CreditVintage/actions/runs/38259829210)的 Linux 3.12/3.13 与 Windows 3.12 成功。[设计与边界](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md)。 |
| [ControlTrace #5](https://github.com/dev-belly/ControlTrace/pull/5) | 同一发现 ID 的源证据被修正后，旧关闭结论保留在历史但不套到新证据。旧表单必须重载，同版本并发提交只接受一方。 | 90 tests；实际导出重放 12 条发现、28 个源文件；[PR CI](https://github.com/dev-belly/ControlTrace/actions/runs/38259648339)的 Linux 3.11/3.12 与 Windows 3.12 成功。格式 3 新增证据绑定，格式 2 / 0.2.7 明示旧保证。[证据合同](https://github.com/dev-belly/ControlTrace/blob/main/docs/REVIEW_INTEGRITY.md)。 |
| [WeCom Agent Platform #2](https://github.com/dev-belly/wecom-agent-platform/pull/2) | 合同条件在全部索引表格行上查询；业务编号保留前导零，客户持仓用 Decimal 按币种完整汇总。缺失估值不能假装是零。 | 73 passed，2 个 Windows 不适用的既有 POSIX 用例跳过；4 个离线业务场景和源码树外 wheel 导入通过；[PR CI](https://github.com/dev-belly/wecom-agent-platform/actions/runs/38259840960)的 Linux、Windows、前端全部成功。[业务案例](https://github.com/dev-belly/wecom-agent-platform/blob/main/docs/business-workflow.md)。 |
| [TradeForge #13](https://github.com/dev-belly/TradeForge/pull/13) | 报告读取根由服务配置决定，请求只能指定根下相对子目录。拒绝绝对路径、父目录、Windows 路径语法和符号链接越界，合法 HTML 报告仍可访问。 | 本机 API/HTML 验证 48 passed，2 个需 Windows 符号链接权限的用例跳过；独立启动配置与同一外部 HTML 的修复前后对照通过。[PR CI](https://github.com/dev-belly/TradeForge/actions/runs/38260579297)的 Python 3.11–3.13、C++ 差分、ASan/UBSan 与确定性重放六项全部成功，随后合并。 |

人工处理完成率、历史事件捕获率和实际损失变化是不同指标。当前队列是合成历史分析示例，本地复核者名字是声明，证据引用不等于已验真的材料；企业查询针对已索引行，不能推断源系统完整性。这些边界都写进项目说明和[面试练习手册](INTERVIEW_PLAYBOOK.zh-CN.md)。

## SQL credit business case · 2026-10-12

已合并 [CreditVintage #10](https://github.com/dev-belly/CreditVintage/pull/10)，在原始成熟测试报告上增加 SQLite 业务分析。按全体、客群、放款月份和月份 × 客群输出 21 个组；保留 48 笔固定容量复核申请的排序，导出清单不含未来风险事件标签。[在线分析](https://dev-belly.github.io/CreditVintage/analysis/)与[中文业务讲述](https://github.com/dev-belly/CreditVintage/blob/main/docs/BUSINESS_CASE.md)从主页首个项目直接进入。

合成样本有 480 笔成熟测试申请和 107 个研究标签事件，复核组包含其中 25 个事件。精确率为 25/48 = 52.08%，捕获率为 25/107 = 23.36%；平均校准后 PD 为 18.78%，本金加权 PD 为 18.49%。10% 是全体容量，不是每个客群各选 10%，也不能据此宣称减少了实际坏账。四种分析视角包含同一批申请，不能混在一起合计。

| Verification | Evidence |
| :--- | :--- |
| SQL and Python | SQL 的条件聚合、`NULLIF`、`LAG` 和排序，与一条不执行 SQL 的 Python 路径逐组对照；数量与本金分精确匹配，比率保留八位小数，场景金额保留两位。零分母为未定义，跨月份比较使用同一客群前一个有数据的月份。 |
| Frozen source and portable replay | 原报告先复制到内存并冻结为临时快照，再核验、解析和计算；并发保存不会让分析引用一版、读取另一版。输出携带原报告六个文件的完整副本；`verify-analysis` 重新验证源报告，再重建全部 SQL、CSV、摘要和 HTML。 |
| Regression checks | 本机 Python 3.12 全部 98 tests、28 subtests 通过，含 18 个新增业务回归：不同分母、空值、排序同分、错误 SQL、整数溢出、并发快照、篡改后重算、CLI 与不覆盖现有输出。Ruff、格式检查与严格 mypy 通过。 |
| Installed package | 构建 wheel 并安装到源码目录之外；三份 SQL 与 HTML 模板完整打包，命令生成的整个分析目录与公开站点构建结果逐字节一致。四个网页分析视角在 Node DOM 检查中分别显示 6/2/12/1 行。 |
| Continuous and publication checks | [PR CI](https://github.com/dev-belly/CreditVintage/actions/runs/38203476369) 的 Linux Python 3.12/3.13 与 Windows Python 3.12 均成功；[预发布构建](https://github.com/dev-belly/CreditVintage/actions/runs/38203476361)成功。合并后 [main CI](https://github.com/dev-belly/CreditVintage/actions/runs/38203639114)三个平台和 [Pages 发布](https://github.com/dev-belly/CreditVintage/actions/runs/38203639194)也均成功，对应提交 [`a168b39`](https://github.com/dev-belly/CreditVintage/commit/a168b39ee05d3dfa56403db5a1ff7eceda7e866f)。线上 `summary.json` 与 `index.html` 返回 HTTP 200，并与已核验的本地公开构建逐字节一致。 |

## Drawdowns and cloud ownership · 2026-10-12

[AlphaForge #3](https://github.com/dev-belly/alphaforge/pull/3) 与 [Ranxin #50](https://github.com/dev-belly/ranxin-mini-program/pull/50) 已合并，原先停留的草稿与待合并状态已收尾。

| Project | Problem and resulting behavior | Verified evidence |
| :--- | :--- | :--- |
| AlphaForge | 收益率 -20%、+10% 曾因首期净值被当作起始峰值而显示零回撤；现在从初始本金计算，最大回撤为 20%，期末仍低于初始本金 12%。汇总、滚动指标、回撤区间和图表使用同一基准，首期全损仍为 100% 回撤。wheel 内含默认 YAML，源码工作区和显式配置路径继续支持。 | [PR CI](https://github.com/dev-belly/alphaforge/actions/runs/38111341159) 与合并后 [main CI](https://github.com/dev-belly/alphaforge/actions/runs/38186528393) 均全部成功：Linux Python 3.10–3.12、Windows Python 3.12，以及完整流水线/API。主分支完整运行日志确认 1,273 tests 通过、96% 覆盖率。 |
| Ranxin | 云函数管理端写入未自动保存 `_openid`，导致自己的作品查不到、重复登录/解锁插入新记录，游戏奖励无法前进；现在只保存服务端调用者身份，忽略伪造所有者，匿名读取为空且个人写入被拒绝。 | 本轮本地复查 13/13 tests 通过，36 个已跟踪 JavaScript 文件语法检查通过；[main CI](https://github.com/dev-belly/ranxin-mini-program/actions/runs/38186554507) 成功，提交 `dbb5646`。 |

Ranxin 更新的是 GitHub 源码。实际微信环境还需按[云函数说明](https://github.com/dev-belly/ranxin-mini-program/blob/main/cloudfunctions/README.md)重新部署，缺少所有者的旧记录由管理员核对后处理；本轮未操作线上数据库或云端部署。[协作边界 Issue #19](https://github.com/dev-belly/ranxin-mini-program/issues/19)继续开放，未将团队协调事项视为代码修复后的自动完成。

本轮还实际构建 AlphaForge wheel，确认其 `alphaforge/resources/default.yaml` 与源码 `configs/default.yaml` 逐字节一致，且保留 `py.typed`。已测试 PR 与合并提交的 Git tree 均为 `3817731470f5fb5d737235a54bee167863a38291`；合并后主分支的独立全量复跑与文档发布也均成功，最终验证直接对应提交 `d7153c9353c78a2966da020f5c0ddd87abd450ee`。

## Input and lifecycle repairs · 2026-10-11

这些修复已合并，当前主分支检查链接列在下一节。测试数对应各 PR 记录的验证环境，Windows 权限或可选扩展跳过继续保留原说明。

| Merged change | Reproduced failure and repair | Recorded validation |
| :--- | :--- | :--- |
| [PITBridge #12](https://github.com/dev-belly/PITBridge/pull/12) | 年份边界的 ISO 时区换算曾抛出未处理的 `OverflowError`；现在以合同错误拒绝，CLI 返回退出码 2，且不创建输出目录。 | 91 tests；覆盖两个 UTC 端点及 build/aggregate。 |
| [CreditVintage #9](https://github.com/dev-belly/CreditVintage/pull/9) | 输入或证据 CSV 的末行缺少闭引号曾被接受；严格解析后返回含文件和物理行号的合同错误，合法引号及 CRLF 仍支持。 | 80 tests、28 subtests；四个回归在修复前失败。 |
| [LedgerX #3](https://github.com/dev-belly/LedgerX/pull/3) | 账本、报价和估值截止日的 UTC 换算越界曾泄漏异常；改为 `LedgerError`，非法估值不写出结果且账本保持不变。 | 51 tests；八项事件/报价/CLI 新回归。 |
| [ControlTrace #4](https://github.com/dev-belly/ControlTrace/pull/4) | 审计截止日之后创建的账户曾进入更早的生命周期控制总体；现在排除已知未来账户，保留缺证据的人工复核与截止时刻相等的记录。 | 74 tests；两项回归核对 UTC 偏移和包含端点，底稿验证 12 个发现、28 个源文件。 |
| [TradeForge #12](https://github.com/dev-belly/TradeForge/pull/12) | 对新建、已撤销、拒绝或过期订单施加成交曾在报错前改变 `filled_base`；现在先验证状态转换，再提交成交数量。 | 本地 867 tests 通过、152 个编译/可选用例跳过；远端仍保留 C++ 对照与 sanitizers。 |
| [AuditLens #4](https://github.com/dev-belly/AuditLens/pull/4) | Windows SQLite 读连接持有文件句柄，导致仓库原子替换出现 WinError 32；显式关闭检查连接并停用读连接池，继续保留无效构建的回滚。 | Windows 464 tests 通过、1 个缺少 make 的用例跳过；十步流水线、15 个 SQL 查询、十份报告连续两次生成字节相同。 |

## Current main checks · 2026-10-12

读取十个金融项目最新 `main` 的运行记录，并逐一核对运行的完整提交 SHA 与当前主分支一致：十个项目的完整 CI 均已成功，AlphaForge 的四平台快速检查和完整流水线/API 也全部结束。下表保留本次主分支验证入口，历史测试数和运行表仍保留在后文。

| Project | Main commit | Current CI |
| :--- | :--- | :--- |
| PITBridge | `f9e8758` | [Successful CI](https://github.com/dev-belly/PITBridge/actions/runs/38110242829) |
| StressAtlas | `bc577bb` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/38050961034) |
| CreditVintage | `a168b39` | [Successful CI](https://github.com/dev-belly/CreditVintage/actions/runs/38203639114) |
| AlphaForge | `d7153c9` | [Successful full CI](https://github.com/dev-belly/alphaforge/actions/runs/38186528393) · 1,273 tests, 96% coverage |
| TradeForge | `bb27f55` | [Successful CI](https://github.com/dev-belly/TradeForge/actions/runs/38111562908) |
| AuditLens | `5f6e641` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/38111034368) |
| ControlTrace | `c3a90d8` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/38110970904) |
| LedgerX | `6725092` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/38110250708) |
| StatementTrace | `ed5ee1c` | [Successful CI and Pages](https://github.com/dev-belly/StatementTrace/actions/runs/38042185670) |
| NetworkClear | `27bb7c4` | [Successful CI and Pages](https://github.com/dev-belly/NetworkClear/actions/runs/38042229238) |

此前收尾实际请求主页里的十个在线报告入口，CreditVintage 的三页、PITBridge 的两页、StressAtlas 的两页、StatementTrace、NetworkClear 和 AlphaForge 样例页均返回 HTTP 200，标题与对应项目一致。这是页面可访问性检查；文件哈希、模型和报告重放仍由各项目所链接的 CI 核验。本轮新增 CreditVintage SQL 分析页，线上页面与摘要的逐字节检查记录在上方业务案例验证表中。

## New project releases · 2026-10-09

新增两个可安装、可复算且有在线演示的项目，补上真实公开财报处理与机构债务网络分析。下方继续保留原八个项目的固定 CI 证据；10 月 9 日补记已发布版本的检查状态，旧测试数仍对应各自修复版本。

| Project | Release commit | Validation and deployment |
| :--- | :--- | :--- |
| [StatementTrace](https://github.com/dev-belly/StatementTrace) | [`654eac1`](https://github.com/dev-belly/StatementTrace/commit/654eac1e9f73d8807c55df1eca6f8a25d6e65ad6) | [Main CI + Pages](https://github.com/dev-belly/StatementTrace/actions/runs/37864981547): Python 3.11–3.13；30 tests、独立 SQL 取数对照、九文件逐字节复算、预览复建和安装包离开源码目录后的演示核验。 |
| [NetworkClear](https://github.com/dev-belly/NetworkClear) | [`1436d53`](https://github.com/dev-belly/NetworkClear/commit/1436d538e9ccd91f5ae7792a3673e02c8619f78e) | [Main CI + Pages](https://github.com/dev-belly/NetworkClear/actions/runs/37864984853): Python 3.11–3.13；33 tests，含 100 个随机小网络独立对照；15 情景逐个穷举 256 个违约集合，核对固定点与资金勾稽、报告复算及安装包演示。 |

StatementTrace 的 33 条数据是 Apple 2023/2024 年报表格的人工摘录，原表 USD 百万转换为 USD；保留真实申报链接、比较期和 53/52 周财年，不宣称未修改 API 下载或实际重述。NetworkClear 完全使用合成债务；A 受到 50% 外部资产冲击后，B/C/D 为新增传染违约，12,020 美元内部加外部未偿债务与 3,380 美元外部债权人短缺分开展示，不把重复网络暴露包装为实际社会损失。

[StatementTrace report](https://dev-belly.github.io/StatementTrace/) · [NetworkClear report](https://dev-belly.github.io/NetworkClear/). 两个项目均在全部测试矩阵通过后发布；官方 Actions 固定到已核对发行版提交。项目说明与中文面试讲解列在 [PROJECT_BRIEFS.md](PROJECT_BRIEFS.md)。

## Cross-platform replay · 2026-10-10

在 Windows 默认 `core.autocrlf=true` 的全新克隆中复现：Git 将演示与预览从 LF 转成 CRLF，导致报告清单哈希、逐字节复算和预览核验失败；中文 Windows 默认编码还使 UTF-8 HTML 篡改测试报错，真实符号链接创建则可能被系统权限拒绝。

[StatementTrace #4](https://github.com/dev-belly/StatementTrace/pull/4) 和 [NetworkClear #4](https://github.com/dev-belly/NetworkClear/pull/4) 用 `.gitattributes` 保留 LF 字节，测试显式使用 UTF-8，并将真实符号链接用例与文件集、非空输出等检查分开；仅 Windows 创建链接的权限错误 1314 会跳过该用例。PowerShell 快速开始直接调用虚拟环境中的程序，无需激活脚本。

| Project | Local Windows Python 3.12 validation | Continuous checks |
| :--- | :--- | :--- |
| [StatementTrace](https://github.com/dev-belly/StatementTrace/pull/4) | 33 tests：32 通过、1 符号链接权限跳过；九文件与预览逐字节重放；源码目录外安装 wheel 后重建并核验六个面板。 | [四项 PR 检查成功](https://github.com/dev-belly/StatementTrace/actions/runs/38042121934)：Linux Python 3.11–3.13 + Windows Python 3.12；Windows checkout 明确使用 `core.autocrlf=true`，测试关闭 UTF-8 mode 以覆盖原生编码。 |
| [NetworkClear](https://github.com/dev-belly/NetworkClear/pull/4) | 36 tests：35 通过、1 符号链接权限跳过；九文件与预览逐字节重放；源码目录外安装 wheel 后核验 15 个场景及独立穷举结果。 | [四项 PR 检查成功](https://github.com/dev-belly/NetworkClear/actions/runs/38042122841)：同一 Linux / Windows 检查组合；Pages 发布同时等待两个平台的检查。 |

两个修复均在另外的全新 Windows 克隆中复查；财务指标、清算金额和演示内容保持原结果。Windows 本机的权限跳过不代表符号链接校验已取消，Linux CI 仍执行真实链接用例。

## Invoice trials · 2026-10-10

复查旧待办：[PITBridge #8](https://github.com/dev-belly/PITBridge/pull/8) 的 pandas/CSV 示例与 [#9](https://github.com/dev-belly/PITBridge/pull/9) 的可选适配器检查均在 10 月 9 日合并，[#7](https://github.com/dev-belly/PITBridge/issues/7) 已按完成状态关闭。10 月 10 日读取原八个主项目的最新主分支检查，均成功。

[PITBridge #10](https://github.com/dev-belly/PITBridge/pull/10) 补齐新读者的试用路径：主页链接到[三次决策的发票案例和可选 CSV 输入](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md)，中文 README 加入 pandas 命令，新增[试用反馈模板](https://github.com/dev-belly/PITBridge/issues/new?template=trial_feedback.md)。两个版本均对应 2026-01-31；2 月 1 日不可用，2 月 15 日选择 100,000 元的 `invoice-v1`，4 月 15 日才选择 135,000 元的 `invoice-v2`，API 与 CSV 全部输出字段一致。

试用复查还发现 Windows 的两类问题：原生中文编码使两个 HTML 测试失败，默认 `core.autocrlf=true` 克隆使保存的快照、滚动报告均出现 `hash mismatch: inputs.json`。显式 UTF-8 测试和 LF 属性修复后，另一次全新 Windows 克隆的两份保存报告均完整重放，CI 的 Windows 快速开始也加入保存报告与原生编码检查。

本机 Python 3.12：没有 pandas 时 80 项通过、8 项可选检查跳过；pandas 3.0.6 时 88 项全部通过，其中 CSV 专项 9 项通过。45 条快照特征、12 条滚动特征及 28 条源成员都能核验。标准库核心、时点规则和既有结果不变。

[六项 PR 检查全部成功](https://github.com/dev-belly/PITBridge/actions/runs/38043124722)：Linux Python 3.11/3.12、Linux pandas 2/3、Windows pandas 3，以及增加原生编码和保存报告检查的 Windows 快速开始。

## Input contracts and portable exports · 2026-10-10

继续检查已有项目，先复现用户可见的失败，再保留验证强度完成修复：

| Project | Reproduced problem and repair | Local validation |
| :--- | :--- | :--- |
| [StressAtlas #4](https://github.com/dev-belly/StressAtlas/pull/4) | 两个合法正赔率乘数的乘积下溢时，PD=1 曾除以零；现在先保持 PD=0/1 端点。超大整数输入返回合同错误，CLI 不再泄漏 `OverflowError`。 | 新增四项 API/CLI 回归，修复前均失败；74 tests 全通过。全新 Windows 检出保留 11 份证据的文件哈希，本机生成的场景和精度报告完整重放。 |
| [CreditVintage #8](https://github.com/dev-belly/CreditVintage/pull/8) | Windows 生成评估、监控和 lineage 页面后，默认 CRLF 写出使三个验证命令立即失败；HTML/JSON 现显式写出 UTF-8/LF，提交证据也保留 LF。 | 75 tests、28 subtests 全通过，Ruff、格式和类型检查成功；480 笔测试评估、320 笔当前监控及 480 申请/1,440 特征的联合案例重放成功。 |
| [LedgerX #2](https://github.com/dev-belly/LedgerX/pull/2) | 缺闭引号的报价 CSV 曾被接受为有效价格；现在严格解析并报告物理输入行号。Windows 检出保持已发布报价的原始字节摘要。 | 41 tests、Ruff、格式和类型检查成功；全新 Windows 检出与已发布估值完全相等。合法带引号的 CRLF 外部文件仍支持，摘要记录其实际字节。 |

三个项目均补上 Windows Python 3.12 自动检查和 PowerShell 入口，继续保留各自的 Linux 检查。CreditVintage 的三个验证器、StressAtlas 的场景及精度验证器均未改写；重新计算文件哈希后的伪造内容仍会被独立重放拒绝。LedgerX 的畸形报价不会产生估值或改变账本。

StressAtlas 另外发现一个实际平台边界：在所测试的 Windows 与 Linux 数值构建中，即使 Python、NumPy、SciPy 版本相同，随机驱动的字节指纹仍不同。保存的 Linux 演示在 Windows 只核对文件哈希；Windows 新生成的报告做完整重放，Linux 继续完整重放保存演示。中英 README 与[方法说明](https://github.com/dev-belly/StressAtlas/blob/main/docs/METHODOLOGY.md#reproducibility-and-limitations)明确这一区别，没有把摘要检查写成数值重放。

## Lead with the role

| 目标方向 | 主讲项目 | 最值得展示的证据 | 需要讲清的边界 |
| :--- | :--- | :--- | :--- |
| 公开财报 / 财务数据 | [StatementTrace](https://github.com/dev-belly/StatementTrace) | 精确财年、申报截止日、比较期、指标公式到源事实的血缘，以及独立 SQL 对照。 | 人工公开财报摘录、十一概念、日期级可得性；无周数归一化或信用评级。 |
| 交易对手 / 网络风险 | [NetworkClear](https://github.com/dev-belly/NetworkClear) | 精确债务清算、违约集合、外部短缺与逐流勾稽、独立穷举算法。 | 合成曝光，一期比例清偿；未建模火售、抵押物、优先级或真实银行风险。 |
| 金融数据工程 | [PITBridge](https://github.com/dev-belly/PITBridge) | SQL 时点关联、独立枚举、修订/删除/新鲜度、滚动 sum/mean/count 和逐成员溯源；标量信贷特征实际接入 CreditVintage。 | 依赖可信源时间和逻辑事件身份；成员数量不等于经营数据完整；集成约定为 UTC 日终，没有生产采集。 |
| 组合风控 / 压力测试 | [StressAtlas](https://github.com/dev-belly/StressAtlas) | 借款人共享违约、离散尾部 ES、可加总贡献和完整路径配对 bootstrap 的 VaR/ES 精度。 | 合成 PD/LGD/EAD；区间仅诊断固定模型下的抽样误差，不能覆盖参数校准误差或未出现的稀有损失。 |
| 银行数据 / 信贷风控 | [CreditVintage](https://github.com/dev-belly/CreditVintage) | 申请时点特征、180 天标签成熟、分离校准、跨期测试；从 PIT 源记录重建特征并重拟合模型，保留逐笔预测溯源。 | 合成借款人；联合案例与原评估样本不同；损失场景中的 LGD 是假设值；标签并非完整监管违约定义。 |
| 量化数据 / 研究工程 | [AlphaForge](https://github.com/dev-belly/alphaforge) | 从因子到组合、交易成本及报告的完整流程；信号与成交时点分离。 | 范围较大，面试优先深讲一个完整数据路径；公开样例未证明可交易优势。 |
| 金融技术 / 执行工程 | [TradeForge](https://github.com/dev-belly/TradeForge) | C++20 核心与 Python 逐事件对照，因果检查及执行成本比较。 | L2 队列近似、成交模型和合成市场会影响结论。 |
| 财务数据分析 | [AuditLens](https://github.com/dev-belly/AuditLens) | 30,128 笔凭证、九项程序、SQL 仓库、可解释评分和 300 笔复核底稿。 | 注入异常与规则口径关联，合成命中率不能作为真实舞弊识别率。 |
| IT 控制 / 证据工程 | [ControlTrace](https://github.com/dev-belly/ControlTrace) | HR、权限、工单、代码与部署关联；追加复核历史、底稿校验与规则重放。 | 记录关联不能证明源系统抽取完整，规则命中仍需要人工判断。 |
| 账务 / 数据一致性 | [LedgerX](https://github.com/dev-belly/LedgerX) | Decimal 双重记账、确定性重放与独立报价估值。 | 当前是单币种、仅做多的研究账本；尚未完成与真实券商账单的对账。 |

## What changed in this review

- 主页采用独立的 `db` 标记、黑白与荧光绿视觉，以及三张全宽重点项目面板；其他项目集中在表格中，每项直接连接源码、演示或可检查的成果。
- 银行与风控方向优先展示 CreditVintage；AlphaForge 和 TradeForge 体现研究工程与底层实现能力。
- 三个重点项目分别链接在线报告；真实更新以带日期的工作记录呈现，探索性研究和早期应用收进折叠区。
- [PROJECT_BRIEFS.md](PROJECT_BRIEFS.md) 保留有来源的简历表述和面试问题。
- 10 月 2 日复查确认八个主项目的最近 `main` CI 均成功；整理此前冲突的主页 PR，补齐 SVG 可重建性、项目卡片对应关系、本地文件和章节入口的自动检查。在线网站的可用性需要另外检查，离线 CI 不宣称覆盖外部链接。
- 新增 [PITBridge 滚动报告](https://dev-belly.github.io/PITBridge/rolling/)：4 个合成决策、12 条特征结果、28 条源成员关联；30 天净流入从 1,500 变为 4,300 的案例解释修订的可得时点。
- 新增 [StressAtlas 精度报告](https://dev-belly.github.io/StressAtlas/precision/)：20,000 条路径、300 次配对重采样、30 条区间结果及 1,500 条情景重采样记录；区分 99% 风险水平和 95% 近似区间置信水平。
- 新增 [CreditVintage × PITBridge 联合案例](https://dev-belly.github.io/CreditVintage/lineage/)：默认生成 480 笔合成申请、1,440 个源特征、192 条决策后才可得记录及 120 笔测试预测；原始事件、模型输入、预测和交互页面都保留在生成目录的固定清单中，并支持完整重放。已补齐在线交互和完整 ZIP 下载；发布流程从源码生成合成案例，核验后上线，生成数据不提交进 Git 历史。
- 已发布 [PITBridge 数值契约修复](https://github.com/dev-belly/PITBridge/pull/3)：SQLite 与独立实现统一采用有限 binary64 输入；均值和最终有限的求和不再因中间溢出被误拒绝。原始整数仍留在输入证据中，浮点计算不替代精确账务。
- 已发布 [StressAtlas 尾部秩修复](https://github.com/dev-belly/StressAtlas/pull/3)与 [LedgerX Decimal 隔离及金额精度修复](https://github.com/dev-belly/LedgerX/pull/1)：外部程序改变 Decimal 精度、舍入、指数边界或异常设置，不应改变项目自身的尾部秩或账务重放；现金和费用会核对原始金额中的非零小数位。
- 已发布 [ControlTrace 底稿 JSON 修复](https://github.com/dev-belly/ControlTrace/pull/2)：类型错误的清单或源表行返回退出码 1；重复键和非有限数值在重放前被拒绝。13 项新增回归包含更新哈希后仍不合法的输入。
- 在 GitHub 实际主页核对了新版主图和旗舰项目卡片；主页的主分支检查已成功。页面可见性与仓库方法验证分开核对。

## Main commits and CI

2026-10-09 复查确认：原八个主项目所列主分支 CI 均成功。TradeForge 的费用金额、含费 shortfall、执行窗口和订单生命周期修复均已合并；Python 3.11–3.13、C++ 逐事件对照、ASan/UBSan 与确定性重放检查成功。PITBridge 主分支新增运行示例与贡献指南，其 CI 和 Pages 构建成功；CreditVintage 联合案例仍固定到数值契约修复提交 `ed19dc6`，完整下载和源到模型重放的既有证据保留。链接固定到所列提交的运行，后续变化以各仓库 Actions 页面为准。

| Project | Main commit | CI evidence |
| :--- | :--- | :--- |
| PITBridge | `734c4e2` | [Successful CI](https://github.com/dev-belly/PITBridge/actions/runs/37775585872) |
| StressAtlas | `b8fa33a` | [Successful CI](https://github.com/dev-belly/StressAtlas/actions/runs/37089449943) |
| CreditVintage | `2f5d6b0` | [Successful main CI](https://github.com/dev-belly/CreditVintage/actions/runs/37711860986) |
| AlphaForge | `513abc6` | [Successful main CI](https://github.com/dev-belly/alphaforge/actions/runs/37167641845) |
| TradeForge | `c992354` | [Successful main CI](https://github.com/dev-belly/TradeForge/actions/runs/37866454671) |
| AuditLens | `8333060` | [Successful CI](https://github.com/dev-belly/AuditLens/actions/runs/37191026460) |
| ControlTrace | `5c42038` | [Successful CI](https://github.com/dev-belly/ControlTrace/actions/runs/37089393347) |
| LedgerX | `b66c8c5` | [Successful CI](https://github.com/dev-belly/LedgerX/actions/runs/37089464841) |

## Recent validation

10 月 3–4 日合并的数值、报告和配置修复，以及 TradeForge、AuditLens 的后续修复，均在 10 月 9 日再次核对所列主分支 CI。TradeForge 后续修复补齐含费总成本及公开演示的输出契约。表中的测试数属于所列修复版本；各 PR 保留通过的检查记录，主分支运行链接列在上方。

| Project / PR | Reproduced problem and resulting behavior | Validation |
| :--- | :--- | :--- |
| [PITBridge #3](https://github.com/dev-belly/PITBridge/pull/3) | Python 可接受的大整数在 SQLite 绑定时报错；改为显式 binary64 数值契约，并支持中间求和溢出但最终均值或抵消结果有限的滚动计算。 | 75 tests；原快照与滚动报告逐字节重放一致。 |
| [StressAtlas #3](https://github.com/dev-belly/StressAtlas/pull/3) | 调用方的低精度 Decimal 环境会改变离散分位点和尾部质量；用整数比例确定尾部秩，隔离外部精度、指数范围及 traps。 | 70 tests；20,000 路径和 300 次 bootstrap 报告重放一致。 |
| [CreditVintage #4](https://github.com/dev-belly/CreditVintage/pull/4) | 更新哈希后的伪造置信区间或页面可能通过验证；独立重算 300 次整月重采样，按核验数据重建 HTML，并拒绝重复 JSON 键。 | 70 tests、5 subtests；评估、无标签监控、公开报告和完整源到预测链路全部核验；[Python 3.12/3.13 CI](https://github.com/dev-belly/CreditVintage/actions/runs/37089359255) 成功。 |
| [CreditVintage #7](https://github.com/dev-belly/CreditVintage/pull/7) | 在线页面缺少完整包入口，本地生成也不打包；本地与网站共用固定清单 ZIP 生成，并按页面版本核验此前有效的证据包。 | 75 tests、28 subtests；Python 3.12/3.13 和发布构建成功；实际下载 ZIP 的 19 个文件、18 项哈希及完整 PIT/模型重放通过。 |
| [AlphaForge #2](https://github.com/dev-belly/alphaforge/pull/2) | 1.9 个成交延迟日被截为 1；字符串 `"false"` 开启零股；负成本增加净值。配置在成交前校验整数、布尔值和成本范围。 | 本地 1,267 tests 全部通过，含完整流水线与 API，覆盖率 96%；合并后的 Python 3.10–3.12 常规测试、lint、format、mypy、文档入口检查以及完整流水线/API 集成检查均成功，见 [主分支 CI](https://github.com/dev-belly/alphaforge/actions/runs/37167641845)。 |
| [LedgerX #1](https://github.com/dev-belly/LedgerX/pull/1) | 外部 Decimal traps 使部分卖出失败；极深小数位可能绕过记账量子约束。隔离算术环境，并把原始金额与可记账单位精确比较。 | 38 tests；格式、lint、mypy 通过，原估值案例保持一致。 |
| [ControlTrace #2](https://github.com/dev-belly/ControlTrace/pull/2) | 清单或源表行类型错误会导致未处理异常；重放前校验结构、重复 JSON 键与非有限数值，CLI 对非法底稿返回明确错误。 | 59 tests，含 13 项新增回归；格式、lint 和完整底稿重放通过。 |
| [TradeForge #2](https://github.com/dev-belly/TradeForge/pull/2) | 外部 Decimal 精度、舍入和 traps 会改变价格刻度与成交金额；改为整数比例确定 half-up 刻度，直接构造精确金额，并拒绝非有限价格。 | Python 3.11–3.13、C++ 单元与逐事件对照、ASan/UBSan 和确定性重放检查均成功。 |
| [TradeForge #3](https://github.com/dev-belly/TradeForge/pull/3)、[#4](https://github.com/dev-belly/TradeForge/pull/4)、[#5](https://github.com/dev-belly/TradeForge/pull/5) | 三次部分成交曾重复收取最低佣金；低精度可能把 0.99 美元增量佣金算成零，非法费率也可能生成虚假收益。逐子订单收取累计佣金增量，以精确有理数计算费用，并在成交前校验参数和成交输入；极小负数下溢成负零也不能绕过符号校验。 | 78 项费用回归通过，包含 400 组混合 maker/taker 部分成交独立对账；修复提交的 Python 3.11–3.13、C++ 对照、ASan/UBSan 和确定性检查均成功，合并后的主分支六项 CI 也全部成功。 |
| [TradeForge #7](https://github.com/dev-belly/TradeForge/pull/7) | 延迟开始的执行任务曾把预热成交和窗口外行情混入参与率及基准；行情跳过精确截止时刻还可能延后终场扫单。现在以窗口开始时刻作为成交量口径，窗口前事件只重建订单簿，窗口后仅用于 markout；在截止时刻按最后的窗口内行情完成终场处理，不使用未来报价。 | 六项 normalized-CSV 回归覆盖延迟开窗、无窗口内报价、窗口外 markout 与稀疏截止；合成场景 50 单位成交/100 单位窗口内成交量维持 50% 参与率。已发布树的 113 项费用/窗口组合测试通过；[PR CI](https://github.com/dev-belly/TradeForge/actions/runs/37712196848) 与[合并后主分支 CI](https://github.com/dev-belly/TradeForge/actions/runs/37738744500) 的 Python 3.11–3.13、C++ differential、ASan/UBSan 和可复现性检查均通过。 |
| [TradeForge #9](https://github.com/dev-belly/TradeForge/pull/9) | 截止撤单曾漏掉仍在传输中的子订单，随后迟到成交和替代扫单把 100 单位请求变成 150 单位成交。现在允许接受前撤单，忽略已结束订单的到达回调，并按仍存活的订单计算容量。 | 8 项 normalized-CSV 回归覆盖撤单、扫单、显式保留、截止时点到达及 1/10 笔容量限制；核对原订单在截止时点结束、没有接受或成交记录，替代扫单不超父订单数量。本地全套验证 836 项通过，152 项跳过；PR 及合并后的主分支 Python 3.11–3.13、C++ 对照、ASan/UBSan 和确定性重放均成功。 |
| [TradeForge #10](https://github.com/dev-belly/TradeForge/pull/10) | 显式费用曾未进入总 shortfall，还被相反方向的归因残差抵消。费用按请求与成交的到达价金额分别计量，BUY/SELL 均加计费用、减计净返佣，并同步 Parquet 和 SQL。 | 20 项现金成本回归覆盖双向交易、部分成交、净返佣、缺失基准、Decimal traps 和存储对账；[合并后六项主分支检查](https://github.com/dev-belly/TradeForge/actions/runs/37774684223) 全部成功。 |
| [TradeForge #11](https://github.com/dev-belly/TradeForge/pull/11) | 费用修复后，README 八行 `is_bps` 和指南归因表仍保留旧口径。按真实 CLI 更新全部数据；公开命令测试核对文档列与报告行，防止旧价格成本继续冒充含费总成本。 | 新增 3 项文档输出回归；本地全套 859 项通过、152 项跳过，135 个 Python 文件的 lint/format 与空白检查通过。[PR 检查](https://github.com/dev-belly/TradeForge/actions/runs/37865674865)及[合并后主分支检查](https://github.com/dev-belly/TradeForge/actions/runs/37866454671)的 Python 3.11–3.13、C++ 对照、sanitizers 和确定性重放均成功。 |
| [AuditLens #3](https://github.com/dev-belly/AuditLens/pull/3) | 读取后又被保存的 CSV 可能使复核计数与所引用哈希来自不同版本；改为从同一份字节快照计算摘要并解析数据。 | Python 3.11/3.12 流水线与测试成功，3.11 同时通过报告复现检查；并发保存回归核对计数与文件摘要一致。 |

这些修复补充实现层面的核验，不改变合成数据结果的业务适用边界。各 PR 提供变更文件、回归案例和远端 CI 状态。

## Newly filled gaps and the next step

PITBridge 从标量快照扩展到决策时点的滚动经营统计，导出每条贡献记录并以独立枚举核验；StressAtlas 从尾部点估计扩展到配对抽样精度诊断，重放全部情景和重采样统计。数值边界修复后，PITBridge 75 项、StressAtlas 70 项测试通过；CI 同时核验原报告和新增报告，并从输入重新生成案例。

PITBridge 的标量特征现通过明确的身份、单位、七天新鲜度和 UTC 日终约定接入 CreditVintage。联合案例从源记录选择一直核对到模型重拟合后的每条测试预测；核验还拒绝更新哈希后的伪造特征、溯源、模型输入摘要、页面内容及不一致模型配置。CreditVintage 下载与兼容修复版本的 75 项测试包含原 18 项集成回归、12 项报告篡改回归和 5 项下载/兼容回归，并有 28 项子测试通过；格式、lint 和类型检查也纳入 CI。

ControlTrace 底稿 JSON 修复版本的 59 项测试核对底稿重放、证据关联和非法 JSON 的命令行错误行为。LedgerX Decimal 隔离修复版本的 38 项测试涵盖不利 Decimal 调用环境、完整账本重放、独立报价估值，以及工作精度之后仍存在非零金额小数位的拒绝行为；lint、格式与严格类型检查通过。

PITBridge 的滚动现金流与 StressAtlas 仍是单独的研究路径，联合案例没有声称把它们接进信贷模型或组合风险引擎。StatementTrace 已新增一条公开年报摘录路径，保留来源、申报日期、实际财年和复现请求；它没有接入信贷模型。后续更广泛的真实数据集仍需核对许可、发布时间、标签定义与复现配置。

## Online evidence publication

[在线联合案例](https://dev-belly.github.io/CreditVintage/lineage/)可选择测试申请查看源记录；[完整 ZIP](https://dev-belly.github.io/CreditVintage/lineage/evidence.zip)包含源事件、模型输入、预测和清单。发布构建同时核验原评估、监控和完整联合案例；PR 只构建、主分支才部署。联合案例有 480 笔总申请、120 笔测试预测；原始风险报告的 480 笔测试申请属于另一份样例。

[该版本成功的发布构建](https://github.com/dev-belly/CreditVintage/actions/runs/37711860987)对应提交 `2f5d6b0`；[PR #7](https://github.com/dev-belly/CreditVintage/pull/7)补齐页面和本地生成的完整 ZIP 入口，并保留原页面的验证方式。10 月 8 日实际切换到测试申请 `CV202412-0019`，页面显示对应预测与三条源记录；120 个测试申请选项可用。点击页面入口下载的 ZIP 含 19 个文件，18 项清单哈希全部匹配，解压后以已发布源码重放 PIT 选择、特征和模型预测通过。ZIP 是清单外的派生下载，核验对象为解压后的文件。

[PR #6](https://github.com/dev-belly/CreditVintage/pull/6)将代码、CI 和公共网页的依赖固定到包含数值契约修复的 PITBridge `ed19dc6`。当时的 70 项测试与 5 项子测试、线上 ZIP 清单及 7 份输入/预测/指标 CSV 的对照记录仍保留；随后下载与兼容修复版本为 75 项测试和 28 项子测试。原发布脚本与报告核验记录见 [PR #5](https://github.com/dev-belly/CreditVintage/pull/5)。
