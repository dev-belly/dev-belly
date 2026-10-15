# Start here / 从这里开始

Choose one project to try, or follow a business question into its evidence and code.
先选一个项目完成运行与核验；也可以直接审阅业务问题、结果和实现。

想先看真实公开数据，可打开 [UCI 信贷比较](https://dev-belly.github.io/CreditVintage/public-credit/)
或按其[源码实验说明](https://github.com/dev-belly/CreditVintage/blob/main/docs/PUBLIC_CREDIT.md)复跑。
它需要当前源码仓库里的数据与示例；下方固定快照的包安装路线仍运行原有合成演示。

## Try a project

These commands work from a new directory, without Git or a source checkout.
Python 3.12+ is required for both paths below; PITBridge alone supports 3.11+.
Installation needs internet access, then the synthetic examples run offline.
Use your virtual environment's Python directly; activation is unnecessary.

下面任选一条路径。使用新的空目录；重复试用时换一个目录名。
如果某一步报错，先停止并保留错误信息。包内不包含仓库的全部示例文档，
所以这里生成自己的报告，再核验生成的结果。

| First task | Result to inspect | Source snapshot checked on 2026-10-14 |
| :--- | :--- | :--- |
| **PITBridge:** see how late information changes historical feature selection | An offline report with source records, missingness reasons and an unsafe baseline | [4ba8bde](https://github.com/dev-belly/PITBridge/tree/4ba8bde70161bd8b95cb22b5141d3768353690e6) |
| **CreditVintage:** turn a credit evaluation into SQL cohort analysis and a review queue | An offline analysis report, group tables and a label-free queue | [83bf42a](https://github.com/dev-belly/CreditVintage/tree/83bf42aafa7fd14dfe4953e9055f2ac25c353eaf) |

The URLs below pin source commits, rather than a moving branch or a package-index
release. Dependencies retain their declared version ranges; these commands do
not promise byte-identical floating-point output across environments. Follow
each project's README for current development, optional adapters and full tests.

### PITBridge: historical feature selection

**Windows PowerShell**

```powershell
mkdir pitbridge-first-run
cd pitbridge-first-run
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "https://codeload.github.com/dev-belly/PITBridge/zip/4ba8bde70161bd8b95cb22b5141d3768353690e6"
.\.venv\Scripts\python.exe -m pitbridge demo --out report
.\.venv\Scripts\python.exe -m pitbridge verify --out report
```

**Linux / macOS**

```bash
mkdir pitbridge-first-run
cd pitbridge-first-run
python3 -m venv .venv
.venv/bin/python -m pip install "https://codeload.github.com/dev-belly/PITBridge/zip/4ba8bde70161bd8b95cb22b5141d3768353690e6"
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

### CreditVintage: SQL analysis and a review queue

**Windows PowerShell**

```powershell
mkdir creditvintage-first-run
cd creditvintage-first-run
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install "https://codeload.github.com/dev-belly/CreditVintage/zip/83bf42aafa7fd14dfe4953e9055f2ac25c353eaf"
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
.venv/bin/python -m pip install "https://codeload.github.com/dev-belly/CreditVintage/zip/83bf42aafa7fd14dfe4953e9055f2ac25c353eaf"
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
| Public credit modeling: what does a learned score add? | [Five-split comparison](https://dev-belly.github.io/CreditVintage/public-credit/) | [Training and saved-score verification](https://github.com/dev-belly/CreditVintage/blob/main/examples/german_credit.py) | Why does static good/bad classification not establish future-vintage performance? |
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
