# CICPA-Learning 贡献指南

欢迎参与 CICPA-Learning 项目！本项目采用**第一性原理**教学法，为 CICPA（注册会计师）考试提供开源学习笔记。

## 贡献方式

### 内容贡献

1. **补充 intermediate 层笔记** — 按 intermediate 模板撰写，覆盖典型考题解析、分录/计算模板、易混点对比
2. **补充 advanced 层笔记** — 按 advanced 模板撰写，覆盖综合题框架、跨章联动、陷阱识别
3. **纠错与补充** — 直接修改已有文件或提 Issue
4. **闪卡贡献** — 在章节末尾添加 `#anki-flashcard` 格式的闪卡
5. **跨科联动标注** — 添加 `🔗 跨科联动` 标记，链接相关章节

### 技术贡献

1. **脚本开发** — validate.py / sync_syllabus.py / export_flashcards.py 等
2. **CI 改进** — Markdown 格式检查、自动标签等
3. **PDF 生成** — Pandoc 模板优化等

## 文件结构

```
CICPA-Learning/
├── CONTRIBUTING.md          ← 你在这里
├── PROGRESS.md              ← 进度追踪
├── .github/
│   └── ISSUE_TEMPLATE/     ← Issue 模板
├── scripts/                 ← 自动化工具
├── CICPA-Accounting/        ← 会计
│   └── NN-章节名/
│       ├── README.md        ← 考试大纲考点索引
│       ├── 01-章节名-basics.md      ← 第一性原理入门
│       ├── 01-章节名-intermediate.md   ← 典型考题解析
│       └── 01-章节名-advanced.md      ← 综合实战
├── CICPA-Auditing/          ← 审计
├── CICPA-Tax/               ← 税法
├── CICPA-Law/               ← 经济法
├── CICPA-Financial Management/ ← 财务成本管理
└── CICPA-Corporate Strategy/   ← 公司战略与风险管理
```

## 贡献规范

### 内容规范

- **必须原创**：不得复制教材原文、机构讲义或历年真题原文（见 NOTICE）
- **遵循模板**：intermediate 和 advanced 必须使用下方提供的模板结构
- **中文撰写**：专业术语首次出现时附英文对照
- **每 PR 限 1-2 章**：便于审核和质量把控
- **考试大纲同步**：新增内容须对应 2026 年考试大纲（能力等级 1/2/3）

### intermediate.md 模板

```markdown
# {章节名} —— 典型考题解析

## 一、核心考法分类
本章在历年真题中的主要考法归纳。

## 二、典型例题解析
### 2.1 [题型分类1]
**题目：** ...
**解析：** ...
**答案：** ...

## 三、分录/计算模板
可直接套用的标准化处理模板。

## 四、易混点对比
| 易混点 | 区别 | 记忆技巧 |
|-------|------|---------|
| ... | ... | ... |

## 五、速记口诀

## 自测清单
- [ ]
```

### advanced.md 模板

```markdown
# {章节名} —— 综合实战

## 一、综合题解题框架
跨考点组合的标准化解题步骤。

## 二、跨章联动图谱
本章与其他章节的关联考点。

## 三、陷阱与反套路
常见出题陷阱的识别和应对方法。

## 四、真题变式推演
一题多变的变式训练。

## 五、实务衔接
知识点在真实审计/会计实务中的应用。

## 六、速记总结
```

### 闪卡格式

在 basics.md 末尾添加：

```markdown
<!-- anki-flashcard -->
Q: 问题是？
A: 答案
Tags: 科目-章节-tag
```

## 审核流程

1. PR 提交后，自动检查 Markdown 格式和文件命名规范
2. 由 maintainer 进行内容审核（准确性、原创性、模板合规性）
3. 审核通过后合并到 main 分支

## 许可说明

本仓库采用分层许可（详见 LICENSE-DOCS / LICENSE-CODE）。贡献内容默认以相同许可协议发布。第三方内容（教材原文、真题等）不在本仓库授权范围内，详见 NOTICE。

## 开始贡献

1. Fork 本仓库
2. 创建新分支：`git checkout -b intermediate/会计/06-长投`
3. 提交修改并推送到你的 Fork
4. 提交 Pull Request

如有任何问题，欢迎提 Issue 或在 Discussions 中讨论！