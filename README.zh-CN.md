# Elegant Academic Slides Skill

[English](README.md) · 简体中文

面向论文报告、学术会议、组会与研究进展汇报的演示文稿 skill：让科研叙事更清楚、图表更易读，并在制作与修改过程中保留证据、科学语义和内容的可编辑性。

这是一个**规范与指令型 skill**。实际 PPTX 创建、编辑、导出和渲染依赖所在 agent 环境提供的工具；它不是独立的 PPT 生成器，也没有绑定特定渲染库或付费服务。

## 可以做什么

- 将论文组织成适合口头报告的故事线，明确任务、方法、证据与结论。
- 统一版式、字体层级和颜色语义，让方法图与实验结果在投影时仍可读。
- 绘制准确的方法流程、系统结构与树形表示，保留输入、输出、反馈和节点状态。
- 按数据集、指标和评估条件组织结果比较，避免混淆量纲或编造缺失实验。
- 根据批注局部修改已有幻灯片，保留已接受的设计与无关内容。
- 指导导出后的内容、视觉与可编辑性检查；具体能力取决于可用工具。

## 安装到 Codex

### 推荐：从 Release 安装

1. 打开 [最新 Release](https://github.com/cw-wan/elegant-academic-slides-skill/releases/latest)，下载附件中的 skill ZIP。`v0.1.0` 的安装包名为 `design-academic-slides-v0.1.0.zip`。
2. 解压后得到顶层文件夹 `design-academic-slides/`。
3. 将这个完整文件夹复制到目标项目的 `.agents/skills/` 下：

```text
你的项目/
└── .agents/
    └── skills/
        └── design-academic-slides/
            ├── SKILL.md
            ├── agents/
            ├── assets/
            └── references/
```

Release ZIP 只包含可安装的 skill；完整仓库另外保留说明文档、打包脚本和持续扩充的范例目录。每个 Release 另附 `SHA256SUMS.txt`，用于核对安装包的 SHA-256 校验值。

### 从源码安装

也可以直接对 Codex 说：

```text
使用 $skill-installer 安装这个 skill：
https://github.com/cw-wan/elegant-academic-slides-skill/tree/main/skills/design-academic-slides
```

若手动下载或克隆完整仓库，请复制其中的 `skills/design-academic-slides/` 到目标项目的 `.agents/skills/` 下。

仓库名是 `elegant-academic-slides-skill`，安装后的内部调用名仍然是 **`$design-academic-slides`**。安装位置与安装器的说明见 [Codex 官方 skill 文档](https://learn.chatgpt.com/docs/build-skills)。

## 使用示例

提供论文、数据、已有 PPT 或批注后，可以这样请求：

**论文转报告**

```text
使用 $design-academic-slides，把这篇论文整理成 12 分钟的中文组会报告，
约 10 页。突出研究问题、方法机制和关键实验，生成可编辑的 PPTX。
保留准确的模型名、指标和来源；没有的数据不要补造。
```

**根据批注修改**

```text
使用 $design-academic-slides，按批注修改这份最新 PPT：放大第 4 页的方法图，
补清输入、输出和反馈路径，并调整第 7 页的结果比较。保留其他页面的内容与设计。
```

**改进方法图与实验页**

```text
使用 $design-academic-slides，优化提供的方法图和消融实验页。
保持拓扑、标签与数值不变，统一视觉状态和图表尺度，并检查导出后的可读性与可编辑性。
```

若环境缺少 PPTX 编辑或渲染能力，skill 本身不会补充这些能力。需要配合可用的演示文稿工具，并说明无法完成的验证。

## 文件与参考指南

```text
elegant-academic-slides-skill/
├── README.md
├── README.zh-CN.md
├── .gitignore
├── skills/
│   └── design-academic-slides/
│       ├── SKILL.md
│       ├── agents/
│       ├── assets/
│       └── references/
├── examples/
│   └── README.md
└── scripts/
    └── package_skill.py
```

入口是 [SKILL.md](skills/design-academic-slides/SKILL.md)。skill 内的 `agents/openai.yaml` 提供界面元数据，`assets/icon.svg` 是图标；详细规范按任务放在 `references/` 中：

| 指南 | 内容 |
| --- | --- |
| [科学内容](skills/design-academic-slides/references/scientific-content.md) | 来源、叙事、定义、引用与结论边界 |
| [视觉设计](skills/design-academic-slides/references/visual-design.md) | 版式、密度、字体、图像与颜色 |
| [科学图示](skills/design-academic-slides/references/scientific-diagrams.md) | 系统图、树结构、反馈与状态语义 |
| [实验证据](skills/design-academic-slides/references/experimental-evidence.md) | 指标、比较、消融与可编辑图表数据 |
| [修改与交付](skills/design-academic-slides/references/revision-and-delivery.md) | 版本、批注、导出与验证 |
| [SELA 专用配置](skills/design-academic-slides/references/sela-profile.md) | SELA / Grammar of the Wave 的项目设计约定 |

SELA 配置是**可选的项目专用参考**，仅用于 SELA / Grammar of the Wave，或明确要求复用其视觉语言的任务。它不是所有学术报告的默认模板，也不是实验结果的数据源。该配置引用的第三方角色素材未包含在本仓库中。

## 范例

[examples/](examples/README.md) 用于持续收录实际制作范例，目前暂无已发布的实际范例。后续每个范例使用独立的 `kebab-case` 子目录，并说明任务、输入、输出、预览和使用方式。范例与安装包分开维护，不包含在 skill Release ZIP 中。

## 构建安装包

使用 Python 3.10 或更新版本，在仓库根目录运行：

```sh
python scripts/package_skill.py v0.1.0
```

脚本会生成 `dist/design-academic-slides-v0.1.0.zip` 和 `dist/SHA256SUMS.txt`。安装包内保留单一的 `design-academic-slides/` 顶层目录；生成文件由 Git 忽略，作为 GitHub Release 附件分发。

## 许可证

本仓库当前未附 `LICENSE` 文件。
