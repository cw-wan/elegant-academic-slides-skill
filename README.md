<p align="center">
  <img src="skills/design-academic-slides/assets/icon.svg" width="48" height="48" alt="">
</p>

<h1 align="center">Elegant Academic Slides</h1>

<p align="center">
  <strong>Give your research a clear story and a considered design.</strong><br>
  An agent skill for academic talks, precise figures, and editable presentations.
</p>

<p align="center">
  <a href="https://github.com/cw-wan/elegant-academic-slides-skill/releases/latest"><img src="https://img.shields.io/github/v/release/cw-wan/elegant-academic-slides-skill?label=release&amp;color=4c6b5d" alt="Latest release"></a>
  <a href="skills/design-academic-slides/SKILL.md"><img src="https://img.shields.io/badge/format-SKILL.md-68758d" alt="Format: SKILL.md"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a><br>
  <a href="examples/v0.2.0/slb-webinar-2026-11-25/README.md">🖼️ See the example</a> ·
  <a href="#quick-start">🚀 Quick start</a> ·
  <a href="#explore">Guides &amp; resources</a>
</p>

---

## In practice

<p align="center">
  <a href="examples/v0.2.0/slb-webinar-2026-11-25/README.md">
    <img src="examples/v0.2.0/slb-webinar-2026-11-25/previews/overview-pages-01-06-09-10-14-15.png?v=v19-6ccf0023d0e0" width="920" alt="Seminar v19 slides 1, 7, 10, 11, 16, and 17: cover, SELA introduction, method, parsing quality, synthesis, and architecture">
  </a>
</p>

<p align="center">
  <strong>Language-Guided Time-Series Perception: Solutions and Challenges</strong><br>
  <sub>Chenwei Wan · SLB AI Lab Webinar · 25 slides · 25 November 2026</sub><br><br>
  <a href="examples/v0.2.0/slb-webinar-2026-11-25/README.md">Explore the case study</a> ·
  <a href="examples/v0.2.0/slb-webinar-2026-11-25/SLB-Webinar-261125.pptx?raw=true">Download PPTX</a> ·
  <a href="examples/v0.2.0/slb-webinar-2026-11-25/SLB-Webinar-261125.pdf">Read the PDF</a>
</p>

The preview is rendered from the supplied **v19 PDF**, refreshed on 27 November 2026. The example includes the current presentation, the historical v10 design record, source links, and full-size images. Its PPTX and PDF filenames remain unchanged so existing links continue to work.

## What it helps with

- **🧭 A story the audience can follow.** Organize one or several papers around a research question, preserving the argument and evidence.
- **📐 Figures that explain the science.** Build precise method diagrams, annotated signals, and honest comparisons. Newsreader titles and Inter labels provide the default typography, subject to your brief or template.
- **✍️ Revisions that respect your work.** Refine scientific English and apply comments to the latest accepted deck, preserving values, terminology, and unrelated slides.

This is an **instruction and reference package**. Actual PPTX creation, editing, rendering, and export depend on tools available in the host agent environment. No rendering engine or presentation library is bundled.

## Quick start

**1. Install the skill.** Download the reviewed **[v0.2.0 installation ZIP](https://github.com/cw-wan/elegant-academic-slides-skill/releases/download/v0.2.0/design-academic-slides-v0.2.0.zip)**, extract it, and place the folder here:

```text
your-project/.agents/skills/design-academic-slides/SKILL.md
```

**2. Bring your research.** Supply a paper, results, or an existing deck, then invoke **`$design-academic-slides`**. An example prompt is just below.

<details>
<summary><strong>Release assets, source edition, and folder structure</strong></summary>

Repository release **v0.2.0** is based on submitted skill edition **v2026.11.25.3**. The [release page](https://github.com/cw-wan/elegant-academic-slides-skill/releases/latest) keeps both packages:

| Asset | Purpose |
| --- | --- |
| **`design-academic-slides-v0.2.0.zip`** | Recommended installation package, reviewed for this repository release |
| `design-academic-slides_v2026.11.25.3.zip` | Unmodified submitted package, retained for provenance |
| `SHA256SUMS.txt` | SHA-256 checksums for both ZIP files |

Extract the **recommended package** and copy its `design-academic-slides/` folder into your Codex project's `.agents/skills/` directory:

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

The installation ZIP contains the skill and its six selected SVG figures. Full presentation examples and repository documentation stay in the main project. GitHub's automatically generated source archives contain the full repository.

</details>

<details>
<summary><strong>Install from GitHub with Codex, or use another agent</strong></summary>

Ask Codex:

```text
Use $skill-installer to install the skill at
https://github.com/cw-wan/elegant-academic-slides-skill/tree/main/skills/design-academic-slides
```

You can also clone the repository and copy `skills/design-academic-slides/` into your project's `.agents/skills/` directory. Keep the internal invocation name **`$design-academic-slides`**. If it does not appear after installation, restart Codex. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for supported locations.

For another agent that supports `SKILL.md`, follow its installation workflow and provide suitable presentation tools.

</details>

## Try it with your research

Supply the paper, data, existing deck, or comments needed for your task.

**Paper to talk**

```text
Use $design-academic-slides to turn the attached paper into a 12-slide,
15-minute conference talk in English. Deliver an editable PPTX. Explain
the task, method, main evidence, and limitations using the supplied sources.
```

<details>
<summary><strong>More prompts: revise a deck or prepare a Chinese research update</strong></summary>

**Revise an existing deck**

```text
Use $design-academic-slides to apply these comments to the attached deck.
Enlarge the method figure, clarify its feedback arrows, and improve the
results chart labels. Preserve the scientific values and unrelated slides.
```

**Chinese research update**

```text
使用 $design-academic-slides，把这些实验结果整理成 3 页中文组会汇报：
研究问题、方法概览、主要结果。保留准确的指标和实验设置，输出可编辑 PPTX。
```

</details>

## Explore

| Start here | What you will find |
| --- | --- |
| [Versioned examples](examples/README.md) | Actual decks, previews, and the design decisions behind them |
| [Chinese handbook](skills/design-academic-slides/references/guide.zh-CN.md) | Worked examples and practical guidance |
| [Resources and sources](docs/resources.md) | External skills, papers, datasets, typography, and design references |
| [Changelog](CHANGELOG.md) | What changed in each release |

The skill contains 18 files: its entry point, UI metadata, icon, nine reference guides, and six editable SVG examples.

<details>
<summary><strong>Browse all skill guides</strong></summary>

| Resource | Purpose |
| --- | --- |
| [SKILL.md](skills/design-academic-slides/SKILL.md) | Entry point and task routing |
| [Scientific content](skills/design-academic-slides/references/scientific-content.md) | Audience questions, seminar structure, and evidence |
| [Visual design](skills/design-academic-slides/references/visual-design.md) | Typography, covers, authorship, and branding |
| [Writing and annotations](skills/design-academic-slides/references/writing-and-annotations.md) | Scientific English and visible annotations |
| [Scientific diagrams](skills/design-academic-slides/references/scientific-diagrams.md) | Methods, logic trees, intervals, and synthetic examples |
| [Experimental evidence](skills/design-academic-slides/references/experimental-evidence.md) | Metrics, thresholds, tables, and latency |
| [Revision and delivery](skills/design-academic-slides/references/revision-and-delivery.md) | Reviews, fonts, exports, and verification |
| [SELA seminar profile](skills/design-academic-slides/references/sela-profile.md) | Optional SELA and GroundingMOMENT guidance |
| [Sources and attribution](skills/design-academic-slides/references/sources.md) | Sources connected to the skill's working practices |
| [Chinese handbook](skills/design-academic-slides/references/guide.zh-CN.md) | Explanations and worked examples in Chinese |
| [SVG examples](skills/design-academic-slides/assets/examples/) | Six selected editable seminar figures |
| [External resources](docs/resources.md) | External skills, papers, data, fonts, and presentation references |

The SELA profile applies to its named project or an explicit request to reuse that design. External skills are separately maintained references, not mandatory dependencies.

</details>

<details>
<summary><strong>Repository layout and release packaging</strong></summary>

```text
elegant-academic-slides-skill/
├── README.md
├── README.zh-CN.md
├── CHANGELOG.md
├── skills/design-academic-slides/
├── examples/
│   ├── README.md
│   └── v0.2.0/slb-webinar-2026-11-25/
│       ├── SLB-Webinar-261125.pptx
│       ├── SLB-Webinar-261125.pdf
│       ├── Seminar_Writing_Design_and_Sources_v10.md
│       ├── example.json
│       └── previews/
├── docs/resources.md
└── scripts/package_skill.py
```

See the [example index](examples/README.md) for the versioned archive layout. The prior [v0.1.0 release](https://github.com/cw-wan/elegant-academic-slides-skill/releases/tag/v0.1.0) remains available.

### Build a release package

With Python 3.10 or later, run from the repository root:

```sh
python scripts/package_skill.py v0.2.0
```

This writes `dist/design-academic-slides-v0.2.0.zip` and `dist/SHA256SUMS.txt`. To retain an original submitted package alongside the reviewed package, add `--source-archive PATH`. Generated packages are ignored by Git and distributed as Release assets.

</details>

## Scope and license

The skill focuses on academic talks and research seminars. Editable output and validation depend on the host environment's tools. This update was checked against the supplied seminar design record; see the [changelog](CHANGELOG.md) for release changes.

No repository `LICENSE` file has been added. Third-party sources are recorded in the [resource catalog](docs/resources.md) and original design record.

---

<p align="center">
  If this helps you present your research, a <strong>⭐ Star</strong> helps others find it.<br>
  <sub>Have an example to share? See the <a href="examples/README.md">example guide</a>.</sub>
</p>
