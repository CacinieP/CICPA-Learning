# 中国企业会计准则最新修订（2024–2026）实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建独立的 `CAS-Revisions/` 专题模块，并系统更新会计等既有科目受影响章节，全面反映 2024–2026 年准则修订（CAS 30、解释17/18号、新会计法、可持续披露准则）。

**Architecture:** 方案采用双轮驱动架构：独立专栏 `CAS-Revisions/` 承担体系化全景研析；既有章节（01-总论、12-或有事项、23-财务报告）完成考点同步与穿透联动。通过更新 `scripts/validate.py` 确保 100% 通过自动化校验。

**Tech Stack:** Markdown, Python 3, Git

**Spec:** `docs/superpowers/specs/2026-10-13-cas-revisions-design.md`

## Global Constraints
- 严格遵循项目的“第一性原理”教学法与分层知识结构；
- 遵循 `validate.py` 的校验规则（文件命名、跨科联动标记 `🔗 跨科联动：` / `🔗 跨章联动：`、闪卡 `<!-- anki-flashcard -->` 格式）；
- 每次任务变更后必须运行 `python3 scripts/validate.py` 验证；
- 保持中英双语专业术语对应。

---

### Task 1: 适配校验脚本 `scripts/validate.py` 与目录初始化

**Files:**
- Modify: `scripts/validate.py`
- Create: `CAS-Revisions/README.md`

**Interfaces:**
- Consumes: `REPO_ROOT`
- Produces: 允许 `CAS-Revisions` 目录作为独立专题模块通过 `check_naming`，不被常规 6 科章节命名规则误报。

- [ ] **Step 1: 检查 validate.py 对非标准命名文件的拦截逻辑**

Run: `python3 -c "import re; pattern = re.compile(r'^\d{2}-.+-(basics|intermediate|advanced)\.md$'); print(pattern.match('01-财务报表列报重大重塑(CAS30新规).md'))"`
Expected: None (会被 check_naming 误报)

- [ ] **Step 2: 修改 `scripts/validate.py`，放行 `CAS-Revisions` 专题文件夹**

在 `check_naming` 函数中，对处于 `CAS-Revisions` 目录下的 Markdown 文档实施专题放行（或专题命名规则），确保既校验 6 科章节规范，又支持专题研究模块。

- [ ] **Step 3: 运行 `python3 scripts/validate.py` 验证**

Run: `python3 scripts/validate.py`
Expected: PASS (所有检查通过)

- [ ] **Step 4: 编写 `CAS-Revisions/README.md` 专题导航大纲**

包含最新准则修订时间轴（2024–2026）、重大修订地图、对注册会计师考试 6 个科目的综合影响总览。

- [ ] **Step 5: 提交 Task 1 代码**

Run: `git add scripts/validate.py CAS-Revisions/README.md && git commit -m "feat(cas): 初始化 CAS-Revisions 模块并适配校验规则"`

---

### Task 2: 编写 CAS-Revisions 核心研究专题文档

**Files:**
- Create: `CAS-Revisions/01-财务报表列报重大重塑(CAS30新规).md`
- Create: `CAS-Revisions/02-准则解释深度解析(第17号与第18号).md`
- Create: `CAS-Revisions/03-可持续披露准则与新会计法前沿.md`
- Create: `CAS-Revisions/04-准则新规与CICPA考试联动与例题演练.md`

**Interfaces:**
- Consumes: 财政部最新发布的准则、解释及新《会计法》原文精神
- Produces: 4 篇全面深入、带有标准分录模板、IFRS 对照和 Anki 闪卡的专题指南

- [ ] **Step 1: 编写 `CAS-Revisions/01-财务报表列报重大重塑(CAS30新规).md`**
深入解析财会〔2026〕11号：
- 对标 IFRS 18；
- 利润表三大类（经营、投资、筹资）划分原则与营业利润小计定义；
- 管理层业绩指标（MPMs）强制披露要求与调节表；
- 附注汇总与分解细化要求；
- 标准财务报表列报模板与典型转换案例。

- [ ] **Step 2: 编写 `CAS-Revisions/02-准则解释深度解析(第17号与第18号).md`**
深入解析解释第17号与第18号：
- 保证类质保金从“销售费用”调整至“主营业务成本/其他业务成本”的理论根源与商业实质；
- 会计政策变更追溯调整的完整分录与递延所得税影响；
- 浮动收费法下投资性房地产公允价值计量；
- 附带契约条款的负债分类（流动 vs 非流动）关键判断时点；
- 供应商融资安排的附注披露标准。

- [ ] **Step 3: 编写 `CAS-Revisions/03-可持续披露准则与新会计法前沿.md`**
深度分析：
- 《企业可持续披露准则——基本准则（试行）》（财会〔2024〕17号）“双重重要性”实质；
- 四支柱披露框架与财务报表附注的交叉钩稽机制；
- 新修改《会计法》（2024年7月）加大违法处罚幅度与强化财会监督。

- [ ] **Step 4: 编写 `CAS-Revisions/04-准则新规与CICPA考试联动与例题演练.md`**
设计：
- 涵盖会计、审计、税法、财管、战略、经济法 6 科的综合考点映射；
- 针对保证类质保金变更、利润表新分类、负债分类等的单选、多选、计算分析题原创实战题与深度解析；
- 标准 `#anki-flashcard` 闪卡集。

- [ ] **Step 5: 运行 `python3 scripts/validate.py` 验证格式与闪卡合规**

Run: `python3 scripts/validate.py`
Expected: PASS

- [ ] **Step 6: 提交 Task 2 代码**

Run: `git add CAS-Revisions/ && git commit -m "feat(cas): 完成 CAS-Revisions 4 大核心研究专题文档"`

---

### Task 3: 穿透迭代既有重点章节（会计 01、12、23 章）

**Files:**
- Modify: `CICPA-Accounting/01-总论/01-总论-basics.md`
- Modify: `CICPA-Accounting/12-或有事项/12-或有事项-basics.md`
- Modify: `CICPA-Accounting/12-或有事项/12-或有事项-intermediate.md`
- Modify: `CICPA-Accounting/23-财务报告/23-财务报告-basics.md`
- Modify: `CICPA-Accounting/23-财务报告/23-财务报告-intermediate.md`

**Interfaces:**
- Consumes: `CAS-Revisions` 中的最新准则结论
- Produces: 既有章节考点与最新准则完全同步，并添加相互指向的 `🔗 跨章联动：`

- [ ] **Step 1: 更新 `CICPA-Accounting/01-总论/01-总论-basics.md`**
在会计法规体系中补充 2024 年新《会计法》修改要点与《企业可持续披露准则——基本准则（试行）》的统驭地位，添加跨专题联动标注。

- [ ] **Step 2: 更新 `CICPA-Accounting/12-或有事项` 相关文件**
将保证类质量保证计提分录明确修正为借记“主营业务成本”（依据解释第18号），特别强调原先计入“销售费用”的处理已成为考题陷阱，并增加会计政策变更追溯调整的例题。

- [ ] **Step 3: 更新 `CICPA-Accounting/23-财务报告` 相关文件**
在利润表与报表附注章节中同步新 CAS 30 核心理念（经营/投资/筹资类别、MPMs 披露），给出新版列报框架与旧版对比。

- [ ] **Step 4: 运行 `python3 scripts/validate.py` 验证**

Run: `python3 scripts/validate.py`
Expected: PASS

- [ ] **Step 5: 提交 Task 3 代码**

Run: `git add CICPA-Accounting/ && git commit -m "feat(accounting): 穿透更新总论、或有事项与财务报告章节以适配准则新规"`

---

### Task 4: 完善根目录索引、PROGRESS.md 与全局校验

**Files:**
- Modify: `README.md`
- Modify: `PROGRESS.md`

- [ ] **Step 1: 更新 `README.md`**
在目录索引与特色专栏中增加“企业会计准则最新修订追踪（CAS Revisions 2024–2026）”专栏介绍与超链接导航。

- [ ] **Step 2: 更新 `PROGRESS.md`**
增加专题模块追踪行与章节联动更新状态记录。

- [ ] **Step 3: 运行全量校验与闪卡提取测试**

Run: `python3 scripts/validate.py`
Run: `python3 scripts/export_flashcards.py`（若存在该脚本）
Expected: 校验无错误通过，闪卡正常解析。

- [ ] **Step 4: 提交 Task 4 代码与终审**

Run: `git add README.md PROGRESS.md && git commit -m "docs: 更新 README 与 PROGRESS 索引以包含准则修订专题"`
