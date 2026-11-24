# Elegant Academic Slides Skill

[中文说明](README.zh-CN.md)

Create and revise evidence-led academic presentations with clear visual hierarchy, readable research figures, precise method diagrams, and editable PowerPoint content.

This repository contains the **`design-academic-slides`** agent skill: instructions and reference guides for turning papers, results, and slide comments into effective research talks. Actual slide creation, editing, rendering, and export use the presentation tools available in your agent environment. No rendering engine or presentation library is bundled.

## What it helps with

- Turn a paper into a conference talk, seminar, or research update.
- Build a clear scientific story while preserving source claims and evidence.
- Design method diagrams with explicit inputs, outputs, feedback, and consistent notation.
- Present results and ablations with accurate metrics, labels, scales, and evaluation settings.
- Apply slide comments to the latest accepted version while preserving unrelated content.
- Check scientific content, visual quality, and editability before delivery.

## Install

### Codex

Ask Codex:

```text
Use $skill-installer to install the skill at
https://github.com/cw-wan/elegant-academic-slides-skill/tree/main/design-academic-slides
```

For manual project installation, download or clone this repository and copy the **`design-academic-slides/`** folder into your project's `.agents/skills/` directory:

```text
your-project/
└── .agents/
    └── skills/
        └── design-academic-slides/
            ├── SKILL.md
            ├── agents/
            ├── assets/
            └── references/
```

Keep the folder name and internal skill name as `design-academic-slides`. The GitHub repository name is separate from the invocation name. If the installed skill does not appear, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for supported locations and discovery behavior.

For another agent that supports `SKILL.md` packages, follow that agent's installation workflow and provide suitable presentation-authoring tools.

## Use

Invoke **`$design-academic-slides`** and provide the paper, source results, existing deck, or slide comments needed for your task.

**Paper to talk**

```text
Use $design-academic-slides to turn the attached paper into a 12-slide,
15-minute conference talk in English. Deliver an editable PPTX. Explain
the task, method, main evidence, and limitations using the supplied sources.
```

**Revise an existing deck**

```text
Use $design-academic-slides to apply these comments to the attached deck.
Enlarge the method figure, clarify its feedback arrows, and improve the
results chart labels. Preserve the scientific values and unrelated slides.
```

**Research update in Chinese**

```text
使用 $design-academic-slides，把这些实验结果整理成 3 页中文组会汇报：
研究问题、方法概览、主要结果。保留准确的指标和实验设置，输出可编辑 PPTX。
```

## Package contents

| File | Purpose |
| --- | --- |
| [SKILL.md](design-academic-slides/SKILL.md) | Entry point, workflow, and completion criteria |
| [Scientific content](design-academic-slides/references/scientific-content.md) | Story, claims, paper versions, and evidence |
| [Visual design](design-academic-slides/references/visual-design.md) | Layout, typography, density, and covers |
| [Scientific diagrams](design-academic-slides/references/scientific-diagrams.md) | Method figures, structure, and visual semantics |
| [Experimental evidence](design-academic-slides/references/experimental-evidence.md) | Results, comparisons, ablations, and metrics |
| [Revision and delivery](design-academic-slides/references/revision-and-delivery.md) | Targeted edits, verification, and editable exports |
| [SELA profile](design-academic-slides/references/sela-profile.md) | Optional project-specific design guidance |
| [agents/openai.yaml](design-academic-slides/agents/openai.yaml) | Display metadata and invocation policy |
| [assets/icon.svg](design-academic-slides/assets/icon.svg) | Skill icon |

The **SELA / Grammar of the Wave** profile applies only to that project or an explicit request to reuse its visual language. It is not the default style for unrelated research. Referenced third-party character artwork is not bundled; consult its source and license before reuse.

## Scope

The skill covers academic talks and research presentations. It is not the primary workflow for academic posters or generic business pitch decks. Editable output and visual verification depend on the tools available in the host environment.

The original skill package is preserved in `design-academic-slides/`. This repository adds publication documentation and Git housekeeping. No license file was included in the source archive, and none has been added here.
