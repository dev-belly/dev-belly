# Start here / 从这里开始

Try the invoice case in your browser, install a project locally, or follow a
business question into its evidence and code.
先在浏览器改一个时间并核对结果，也可以本地运行项目，或直接审阅业务问题、结果和实现。

## Try in your browser

**Why can't a February decision use an invoice correction that arrived in April?**
The [PITBridge notebook](https://colab.research.google.com/github/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb)
uses one synthetic invoice to make that boundary visible. No local Python,
Git checkout, GPU or paid dataset is needed.

1. Open the notebook in Colab, sign in if prompted, and start a Python runtime.
2. Run all cells. The first code cell downloads and installs a pinned source snapshot
   of **dev-belly/PITBridge**; the remaining cells check SQL against an independent
   Python implementation and the three expected decisions below.
3. Edit `decision_at` or `correction_ingested_at` in the final code cell and rerun
   that cell. Explain why the selected revision changed or stayed the same.

| Default decision | Expected selection |
| :--- | :--- |
| February 1 | Missing: neither version was available yet |
| February 15 | Original invoice, 100,000 CNY |
| April 15 | Corrected invoice, 135,000 CNY |

浏览器案例先运行固定的三次决策，再修改最后一个代码单元的时间参数。
金额和日期都是合成输入，用于解释规则，不代表真实客户或回测收益。
Colab 需要联网安装源码并按平台要求启动运行时。

[Preview the notebook on GitHub](https://github.com/dev-belly/PITBridge/blob/main/examples/decision_time.ipynb) ·
[Report a trial result or a blocked step](https://github.com/dev-belly/PITBridge/issues/new?template=trial_feedback.md).
For local reports or CSV inputs, continue with the installation paths below.

## Try a project

想先看真实公开数据，可打开 [UCI 信贷比较](https://dev-belly.github.io/CreditVintage/public-credit-comparison/)
或按其[源码实验说明](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT_COMPARISON.md)复跑。
五次比较需要从当前源码仓库运行示例，数据与加载器复用包内实现。
下方固定版本安装路线可运行 3 万条信用卡对照、单次公开校准实验和合成事件 SQL 演示，分别解释三者口径。

These commands work from a new directory, without Git or a source checkout.
Python 3.12+ is required for both paths below; PITBridge alone supports 3.11+.
Installation needs internet access; the synthetic and bundled public examples then run offline.
Use your virtual environment's Python directly; activation is unnecessary.

下面任选一条路径。使用新的空目录；重复试用时换一个目录名。
如果某一步报错，先停止并保留错误信息。包内不包含仓库的全部示例文档，
所以这里生成自己的报告，再核验生成的结果。

| First task | Result to inspect | Pinned source or checked release |
| :--- | :--- | :--- |
| **PITBridge:** see how late information changes historical feature selection | An offline report with source records, missingness reasons and an unsafe baseline | [v0.2.0 checked wheel](https://github.com/dev-belly/PITBridge/releases/tag/v0.2.0) |
| **CreditVintage:** turn a credit evaluation into SQL cohort analysis and a review queue | An offline analysis report, group tables and a label-free queue | [v0.6.0 checked wheel](https://github.com/dev-belly/CreditVintage/releases/tag/v0.6.0) |

The URLs select the checked PITBridge v0.2.0 and CreditVintage v0.6.0 wheels.
Each is the artifact verified by main CI, with commit/version and SHA-256
evidence attached to its release. PITBridge's source is fixed at
[`c04c533`](https://github.com/dev-belly/PITBridge/commit/c04c533274e2e96e768d73ab78e99ab4ea9edd46).
The CreditVintage version check below prints `0.6.0`;
the [release notes](https://github.com/dev-belly/CreditVintage/releases/tag/v0.6.0)
describe decision-time coverage diagnostics; input distributions and monitoring preflight remain available. PITBridge has no
third-party runtime dependencies; CreditVintage pins its numerical dependencies.
These commands do not promise identical floating-point output across environments.
Follow each project's README for adapters and full tests.

### PITBridge: historical feature selection

**Windows PowerShell**

```powershell
mkdir pitbridge-first-run
cd pitbridge-first-run
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "https://github.com/dev-belly/PITBridge/releases/download/v0.2.0/pitbridge-0.2.0-py3-none-any.whl"
.\.venv\Scripts\python.exe -m pitbridge demo --out report
.\.venv\Scripts\python.exe -m pitbridge verify --out report
```

**Linux / macOS**

```bash
mkdir pitbridge-first-run
cd pitbridge-first-run
python3 -m venv .venv
.venv/bin/python -m pip install "https://github.com/dev-belly/PITBridge/releases/download/v0.2.0/pitbridge-0.2.0-py3-none-any.whl"
.venv/bin/python -m pitbridge demo --out report
.venv/bin/python -m pitbridge verify --out report
```

Open `report/report.html`. The fixed synthetic fixture has **11 observations,
15 decisions and 45 feature lookups**. Its event-only baseline uses future
knowledge in **11 selections**; the full contract changes **16 selections**,
also accounting for freshness and tombstones. These are fixture counts, not a
measured leakage rate in real financial data. The verifier checks file digests
and independently replays the selections.

查看 `report/snapshots.csv` 的来源与可用时间，再与 `report/comparison.csv` 对照。
接下来可试 [一张发票、三次决策](https://github.com/dev-belly/PITBridge/blob/main/examples/README.md)，
或阅读 [输入规则](https://github.com/dev-belly/PITBridge/blob/main/docs/DATA_CONTRACT.md)。

The checked PITBridge wheel also accepts your own three CSV tables without
pandas. Prepare `observations.csv`, `decisions.csv` and `specs.csv` using the
[exact CSV contract](https://github.com/dev-belly/PITBridge/blob/360ac96a024b0625c0bf6e171cbd82c9b6ad8b65/docs/CSV_INPUTS.md),
then run `python -m pitbridge build --csv-dir my-tables --out my-report` and
`python -m pitbridge verify --out my-report` with the environment's Python above.
Use `aggregate --csv-dir` with `rolling_specs.csv` for rolling features.
Invalid rows fail before output creation; source JSON retains the original IDs.

### CreditVintage: SQL analysis and a review queue

**Windows PowerShell**

```powershell
mkdir creditvintage-first-run
cd creditvintage-first-run
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "https://github.com/dev-belly/CreditVintage/releases/download/v0.6.0/creditvintage_research-0.6.0-py3-none-any.whl"
.\.venv\Scripts\python.exe -c "from importlib.metadata import version; print(version('creditvintage-research'))"
.\.venv\Scripts\python.exe -m creditvintage.cli run --out evaluation
.\.venv\Scripts\python.exe -m creditvintage.cli verify evaluation
.\.venv\Scripts\python.exe -m creditvintage.cli analyze evaluation --out analysis
.\.venv\Scripts\python.exe -m creditvintage.cli verify-analysis analysis
```

**Linux / macOS**

```bash
mkdir creditvintage-first-run
cd creditvintage-first-run
python3 -m venv .venv
.venv/bin/python -m pip install "https://github.com/dev-belly/CreditVintage/releases/download/v0.6.0/creditvintage_research-0.6.0-py3-none-any.whl"
.venv/bin/python -c "from importlib.metadata import version; print(version('creditvintage-research'))"
.venv/bin/python -m creditvintage.cli run --out evaluation
.venv/bin/python -m creditvintage.cli verify evaluation
.venv/bin/python -m creditvintage.cli analyze evaluation --out analysis
.venv/bin/python -m creditvintage.cli verify-analysis analysis
```

Open `analysis/index.html`. The original synthetic evaluation has **480 mature
test applications**; the analysis produces **21 group rows and 48 review-queue
rows**. The queue omits future outcome labels. Different grouping views describe
the same portfolio, so their rows must not be summed together. Verification
rebuilds the analysis from its frozen source report and checks the SQL results
against independent Python counts and sums.

先解释“固定 10% 的复核名额”和每个客群风险率的分母，再沿
[业务案例](https://github.com/dev-belly/CreditVintage/blob/main/docs/BUSINESS_CASE.md)
与 [人工复核流程](https://github.com/dev-belly/CreditVintage/blob/main/docs/REVIEW_WORKFLOW.md)
展开。这些计数来自原始评估；单独的 PITBridge 联合溯源案例使用不同样本。
合成演示不能证明真实客户违约预测、业务降损或上线效果。

### CreditVintage: editable CSVs and input diagnostics

The same installed v0.6.0 package can create complete input files before you
replace them with compatible data of your own.

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage init-inputs --out inputs/example
.\.venv\Scripts\python.exe -m creditvintage check-inputs inputs/example
.\.venv\Scripts\python.exe -m creditvintage run --applications inputs/example/applications.csv --features inputs/example/features.csv --performance inputs/example/performance.csv --config inputs/example/cohorts.json --out csv-evaluation
.\.venv\Scripts\python.exe -m creditvintage verify csv-evaluation
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage init-inputs --out inputs/example
.venv/bin/python -m creditvintage check-inputs inputs/example
.venv/bin/python -m creditvintage run --applications inputs/example/applications.csv --features inputs/example/features.csv --performance inputs/example/performance.csv --config inputs/example/cohorts.json --out csv-evaluation
.venv/bin/python -m creditvintage verify csv-evaluation
```

This smaller editable case has **480 total synthetic applications**, split
240/120/120, and verification reports **120 held-out applications**. Its
`case.json` identifies its generated origin. The earlier built-in demonstration
uses a different sample size. Input diagnostics collect file/physical-line
errors and return JSON plus exit code 2 for invalid data, without fitting or
rewriting files. Fix row errors first; blocked relationship or cohort checks
are explicitly identified. Readiness checks the documented event contract and
mature evaluation windows, not source authenticity or predictive quality.

Version 0.6.0 requires dates such as `2024-10-01` throughout the CSVs, cohort
configuration and `monitor --as-of`. Compact dates (`20241001`), ISO week dates
(`2024-W40-2`), timestamps and surrounding spaces are rejected. The checker
identifies the file, physical line and column without rewriting inputs. Reports
already generated with canonical dates remain verifiable; see the
[upgrade notes](https://github.com/dev-belly/CreditVintage/blob/main/docs/releases/v0.6.0.md).

Replace all three CSVs and edit the complete calendar for your own compatible
records. [Input contract and diagnostic output](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md).

### CreditVintage: check early monitoring before training

The installed v0.6.0 package can check monitoring inputs before fitting:

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage preflight --as-of 2024-10-01
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage preflight --as-of 2024-10-01
```

This built-in synthetic check prints JSON and writes no files. It returns
`ready_for_monitoring`, `model_fitted: false`, 960 training applications,
480 calibration applications and 320 visible current applications. Another
160 current applications are not yet visible. Historical labels must be mature;
current labels are neither required nor counted.

For your own compatible CSVs, add all three input paths and `--config` as shown
in the [monitoring-input walkthrough](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md).
The smaller editable case above has 80 visible and 40 not-yet-visible current
applications at this cutoff. Omitting `--as-of` retains mature evaluation
preflight. Readiness produces no scores or PSI and does not establish numerical
fitting success or predictive quality. The actual `monitor` command follows the
same population gates and performs the scoring checks.

### CreditVintage: diagnose missing decision-time features

The v0.6.0 diagnostic keeps every expected input slot and reports coverage
before strict distribution/scoring checks can succeed.

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage monitor-feature-quality --as-of 2024-10-01 --out feature-quality
.\.venv\Scripts\python.exe -m creditvintage verify-feature-quality feature-quality
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage monitor-feature-quality --as-of 2024-10-01 --out feature-quality
.venv/bin/python -m creditvintage verify-feature-quality feature-quality
```

Open `feature-quality/index.html`. The built-in synthetic case deliberately has
four unavailable slots: all 320 visible current applications stay in the feature
denominators, and 316 have all three inputs. Another 160 current applications
are not yet visible. Known late arrivals, post-decision observations and no
visible event are reported separately, using only records visible by the cutoff.

诊断成功生成或核验通过，仍然可以包含不完整申请。原有评分与分布检查继续拒绝
缺失的决策时特征；这里不补零、不删除这些申请，也不读取结果文件或拟合模型。
自己的数据只需两张事件表和日期配置。小月份保留计数，空人群不被显示为完整。
[Reason definitions, timing and evidence](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_QUALITY.md).

Explain why the feature denominator is 320 while the complete-application count
is 316, and why an event dated after the report cutoff cannot explain an earlier gap.

### CreditVintage: inspect input distributions without labels

The v0.6.0 wheel also compares decision-time inputs without fitting a model or
loading an outcome file, including historical outcomes.

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage monitor-features --as-of 2024-10-01 --out feature-monitor
.\.venv\Scripts\python.exe -m creditvintage verify-feature-monitor feature-monitor
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage monitor-features --as-of 2024-10-01 --out feature-monitor
.venv/bin/python -m creditvintage verify-feature-monitor feature-monitor
```

Open `feature-monitor/index.html`. The built-in synthetic case has 480 reference
and 320 visible current applications, with another 160 current applications not
yet visible. Four numeric inputs use empirical KS distance; segment composition
uses total variation. These are descriptive marginal distances, without
significance tests, automatic thresholds or a claim of model deterioration.
Small monthly samples have no distance estimate. Use a new output directory
for each run; existing reports are not overwritten.

自己的输入只需申请表、特征事件表和完整日期配置，不需要结果表。现有严格时点规则
仍适用，缺失特征不会被补零或悄悄删除；金额以整数分保留。核验会从所保存的事件
重建快照、分布与页面，不能据此证明源数据真实。
[Two-CSV input contract and arithmetic](https://github.com/dev-belly/CreditVintage/blob/main/docs/FEATURE_MONITORING.md).

Explain why this command needs no historical labels while `monitor` does, and
why a larger distribution distance does not by itself establish worse predictions.

### CreditVintage: observed public credit

The installed CreditVintage snapshot above also includes the attributed UCI
German credit table. From that same directory and environment, run:

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage public-benchmark --out public-credit
.\.venv\Scripts\python.exe -m creditvintage verify-public public-credit
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage public-benchmark --out public-credit
.venv/bin/python -m creditvintage verify-public public-credit
```

Open `public-credit/index.html`. It compares a constant reference, logistic
regression and isotonic calibration on 200 held-out records from a fixed
600/200/200 split. The package preserves the original UCI bytes and attribution;
verification refits the frozen models offline. Native good/bad labels and a
random split provide a different check from the synthetic dated-event pipeline.
They cannot establish decision-time availability or future-period performance.
[Protocol and retained negative calibration result](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT.md).

For a suitable event dataset of your own, use the
[custom calendar and preflight walkthrough](https://github.com/dev-belly/CreditVintage/blob/main/docs/CUSTOM_INPUTS.md).

### CreditVintage: 30,000 card accounts and complete model replay

The same v0.6.0 environment includes the larger UCI credit-card cohort.

**Windows PowerShell**

```powershell
.\.venv\Scripts\python.exe -m creditvintage card-benchmark --out card-credit
.\.venv\Scripts\python.exe -m creditvintage verify-card card-credit
```

**Linux / macOS**

```bash
.venv/bin/python -m creditvintage card-benchmark --out card-credit
.venv/bin/python -m creditvintage verify-card card-credit
```

Open `card-credit/index.html`. The five fixed splits each contain 18,000 train,
6,000 calibration and 6,000 test records. Four methods share the same test
cohorts and review capacities; all 120,000 scores and 60 budget comparisons are
retained. Refitting checks the original table, assignments, scores, queues,
metrics, page and downloadable evidence ZIP. The package includes its source
notice and a reproducible integer conversion; no network or Excel parser is
needed for this workflow. [Protocol](https://github.com/dev-belly/CreditVintage/blob/main/docs/CARD_CREDIT.md).

These are overlapping random partitions of one historical Taiwan cohort.
Native subsequent-default labels differ from German good/bad classification
and the synthetic 180-day DPD experiment; none of these random splits proves
future-vintage performance.

### If a step fails

Check that Python satisfies the required version and that installation finished
before running the next command. Confirm that you used the named environment's
Python and a new output directory. For feedback, include the source commit,
operating system, Python version, exact command and full error message:
[PITBridge trial](https://github.com/dev-belly/PITBridge/issues/new?template=trial_feedback.md) ·
[CreditVintage trial](https://github.com/dev-belly/CreditVintage/issues/new?template=trial_feedback.yml).
Use synthetic inputs in public reports.

## Review the work

| Role / question | Inspect a result | Follow the implementation | Ask about the limit |
| :--- | :--- | :--- | :--- |
| Public credit modeling: what does a learned score add? | [Five-split comparison](https://dev-belly.github.io/CreditVintage/public-credit-comparison/) | [Training and saved-score verification](https://github.com/dev-belly/CreditVintage/blob/main/examples/german_credit.py) | Why does static good/bad classification not establish future-vintage performance? |
| Credit / SQL analysis: which cohorts need attention? | [Cohort analysis](https://dev-belly.github.io/CreditVintage/analysis/) | [Executed SQL](https://github.com/dev-belly/CreditVintage/blob/main/src/creditvintage/business_groups.sql) | Why is 25/48 review precision different from 25/107 event capture? |
| Financial data engineering: what could a past decision know? | [Source-to-prediction explorer](https://dev-belly.github.io/CreditVintage/lineage/) | [PITBridge selection engine](https://github.com/dev-belly/PITBridge/blob/main/src/pitbridge/core.py) | Why must publication and ingestion both precede the decision? |
| Portfolio risk: how stable is a tail estimate? | [Stress precision report](https://dev-belly.github.io/StressAtlas/precision/) | [Precision method](https://github.com/dev-belly/StressAtlas/blob/main/docs/PRECISION.md) | Which uncertainty is measured, and which PD/LGD assumptions remain unvalidated? |

For each project, explain the input, decision, method, validation and boundary.
Recruiters can follow the links to inspect the evidence; candidates should use
only claims and contribution descriptions they can personally explain.

[60-second interview card](面试速讲卡.zh-CN.md) ·
[Business walkthrough](INTERVIEW_PLAYBOOK.zh-CN.md) ·
[Evidence and candidate resume wording](PROJECT_BRIEFS.md) ·
[Other roles and projects](PROJECT_BRIEFS.md#choosing-what-goes-on-a-resume)
