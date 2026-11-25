# Sources and attribution

Use this ledger to attribute the design work and decide when to consult an external resource. These resources informed the seminar. The package contains its own guidance and six editable seminar figures. External skills remain separately maintained references.

## Skills used and their contribution

| Resource | Application in the seminar | Working practice retained here |
|---|---|---|
| [Elegant Academic Slides](https://github.com/cw-wan/elegant-academic-slides-skill) | Underlying presentation skill and continuity with the SELA paper deck | Preserve the reviewed argument, object semantics and selected source artwork. |
| [Scientific Writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md) | Evidence and scientific qualification | Preserve metric, setting, denominator, and the distinction between a finding, an interpretation and a proposal. |
| [Writing Clearly and Concisely](https://github.com/obra/the-elements-of-style/blob/main/skills/writing-clearly-and-concisely/SKILL.md) | Short, spoken scientific English | Use direct verbs and show what action connects a query to the trace. |
| [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | English copy-editing | Remove empty framing and repeated reassurance. Preserve scientific qualifiers and author voice. |
| [Academic Diagram](https://github.com/plbbl/academic-diagram-skill/blob/main/SKILL.md) | Architecture figure planning | Inspect conference references for reading order and grouping. Prove the editable vector before composing the page. |
| Presentations, provided by the authoring environment | PPTX and online review | Check package structure, native tables, font rendering, notes, media and the actual review copy. |
| PDF, provided by the authoring environment | PDF proof and handbook delivery | Check the final page sequence, font rendering, vector figures, and still frames where the presentation contains media. |
| Skill Creator, provided by the authoring environment | Packaging and maintenance | Keep an identifiable entry point, conditional references, and coherent versioned instructions. |

For each new job, record the resources actually used, the design decision each influenced and the resulting figure or page. Keep this production ledger outside the audience-facing slides.

## Research figures and seminar models

| Source | Technique applied |
|---|---|
| [Anthropic Economic Index, September report, Fig. 1.2](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) | Align related panels, repeat the scale where needed, and keep category names tethered to the data. |
| [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model) | Hold the surrounding example fixed to make one changed condition interpretable. |
| [Introducing the Anthropic Economic Index](https://www.anthropic.com/research/the-anthropic-economic-index) | Align category, concrete example and measurement so readers can move across a row or column. |
| [Jeff Dean, CIKM keynote](https://research.google.com/people/jeff/CIKM-keynote-Nov2014.pdf) · [Rob Hyndman, Zalando seminar](https://robjhyndman.com/seminars/fr_overview.html) | Seminar references for speaker-led attribution and connecting a live industry problem to a research method. |
| [Fei-Fei Li, visual recognition talk](https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures) · [Michael Alley, assertion–evidence](https://writing.engr.psu.edu/assertion_evidence_EA.html) · [Yann LeCun, Berkeley colloquium](https://eecs.berkeley.edu/research/colloquium/220927-2/) | Seminar references for motivating a wider question, organizing evidence and connecting contributions to open problems. |

## Included artwork and data

The package includes six editable seminar figure examples. The underlying authors, datasets and paper sources are credited here and in each SVG's description. Distinguish measured results and expert labels from interpreted inner boundaries and illustrative schematic parameters. These six files are the included examples, not the complete 18-figure source archive described in the seminar's historical design record.

| Asset | Source and status |
|---|---|
| [Nested intervals](../assets/examples/nested-intervals.svg) | Seminar slide 6. [KITE trace PT_46710318](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/timeseries/PT_46710318.csv), [expert labels](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/labels.csv) and [Wan et al.](https://aclanthology.org/2026.emnlp-main.290/). Inner boundaries are interpreted from the trace. |
| [Temporal elasticity](../assets/examples/temporal-elasticity.svg) | Seminar v10, slide 7. Schematic phase shares and durations illustrate an event with fixed logical relations. [Wan et al., §3](https://aclanthology.org/2026.emnlp-main.290/). |
| [Synthesis variation](../assets/examples/synthesis-variation.svg) | Seminar v10, slide 14. GroundTSSyn construction and bounded variation are documented in [Hou et al., §5 and Appendix A.2, pp. 4824–4825](https://aclanthology.org/2026.findings-emnlp.229/). Durations and pre-normalization amplitudes are illustrative. The slide also credits Xie et al. (2025), Fig. 4, for figure design. |
| [Threshold panels](../assets/examples/localization.svg) | Seminar slide 12, Pressure Test macro F1 with source-reported standard deviations. [Wan et al., Tables 2, 4 and 5](https://aclanthology.org/2026.emnlp-main.290/). |
| [Architecture](../assets/examples/architecture.svg) | Seminar slide 15, redrawn for the talk from the model in [Hou et al.](https://aclanthology.org/2026.findings-emnlp.229/). |
| [Accuracy and latency](../assets/examples/accuracy-latency.svg) | Seminar slide 18, GroundTSBench test set. [Hou et al., Table 2 and Appendix D](https://aclanthology.org/2026.findings-emnlp.229/). |

[Microsoft’s PowerPoint font embedding guidance](https://support.microsoft.com/en-gb/office/fonts/benefits-of-embedding-custom-fonts) explains the distinction between embedding a font and relying on it being available on the recipient’s device. The user selected Newsreader and Inter as the preferred families for this skill. The seminar profile records a separate v11 Windows handoff as one recipient-specific substitution; that compatibility deck is not bundled with this skill.

The cover example discussed in the guide pairs the query in [Hou et al., Fig. 2](https://aclanthology.org/2026.findings-emnlp.229/) with a [LUDB](https://doi.org/10.13026/eegm-h675) recording. The full-resolution video demonstrations remain available from the [GroundingMOMENT project](https://github.com/houtj/GroundingMOMENT). Use original host and venue assets supplied for each presentation. Obtain font files and their licenses from [Newsreader](https://github.com/google/fonts/tree/main/ofl/newsreader) and [Inter](https://github.com/google/fonts/tree/main/ofl/inter) when needed.

The v10 slide 5 engineer cutout comes from the [original SELA presentation](https://github.com/cw-wan/SELA/blob/4fa7c3502ed71852c6791503fd494d210db33e42/SELA_EMNLP26_Slides.pptx). It serves as the example of preserving source pixels when placing an illustration inside a vector composition.
