# Language-Guided Time-Series Perception: Solutions and Challenges

[Version archive](../README.md) | [All examples](../../README.md) | [Resources](../../../docs/resources.md)

**Chenwei Wan | SLB AI Lab Webinar | 25 November 2026 | 25 slides | English**

Current presentation: **v20**, refreshed on **27 November 2026**. The archive filenames remain `SLB-Webinar-261125.pptx` and `SLB-Webinar-261125.pdf` so existing external links continue to work.

This supplied seminar connects language-guided time-series perception to SELA, GroundTSSyn, and GroundingMOMENT, then develops research directions for multichannel detection and event-based decision support. It demonstrates scientific storytelling, time-series annotation, method diagrams, result comparisons, and consistent typography.

## Files

| File | Use |
| --- | --- |
| [Download PowerPoint](SLB-Webinar-261125.pptx?raw=true) | Current v20 PPTX with notes, native tables, and embedded demonstrations |
| [View PDF](SLB-Webinar-261125.pdf) · [Download PDF](SLB-Webinar-261125.pdf?raw=true) | Current v20 static 25-page export |
| [Design and source record](Seminar_Writing_Design_and_Sources_v10.md) · [Download Markdown](Seminar_Writing_Design_and_Sources_v10.md?raw=true) | Historical v10 record, retained unchanged |
| [File manifest](example.json) | Version association, file hashes, selected preview pages, and package counts |
| [External resources](../../../docs/resources.md) | Design record's external skills, papers, data, fonts, and presentation references |

## Version and provenance

| Field | Value |
| --- | --- |
| Repository release | [v0.2.0](https://github.com/cw-wan/elegant-academic-slides-skill/releases/tag/v0.2.0) |
| Associated source skill edition | v2026.11.25.3 |
| Submitted package | `design-academic-slides_v2026.11.25.3.zip` |
| Design record | `Seminar_Writing_Design_and_Sources_v10.md` |
| Current presentation revision | v20, supplied on 27 November 2026 |
| Supplied presentation filenames | `Language_Guided_Time_Series_Perception_v20.pptx` and `.pdf` |

The current PPTX and PDF preserve the supplied v20 bytes under the established archive filenames. They replaced the earlier example on `main`; the published v0.2.0 tag still contains its original snapshot. The skill association dates from that original release, and no new skill package accompanied v20. The source revision label comes from the supplied filenames, not PowerPoint's internal revision counter.

The v10 design document remains a historical source. Its page numbers and counts describe the earlier deck and should not be treated as current v20 page references.

## Preview

Images are rendered directly from the supplied v20 PDF. Existing image filenames are preserved; page labels, the manifest, and cache-version parameters identify the current content. Click to open at full resolution.

[![Seminar cover](previews/cover.png?v=v20-588fd7627f5c)](previews/cover.png?v=v20-588fd7627f5c)

[![v20 slides 1, 7, 10, 11, 16, and 17: cover, SELA introduction, method, parsing quality, synthesis, and architecture](previews/overview-pages-01-06-09-10-14-15.png?v=v20-fd66cf1a4c2c)](previews/overview-pages-01-06-09-10-14-15.png?v=v20-fd66cf1a4c2c)

### Page tracking

The same six showcase topics were matched by title and content. Their page numbers are unchanged from v19 to v20:

| Topic | Original archive | v19 | v20 |
| --- | ---: | ---: | ---: |
| Cover | 1 | 1 | 1 |
| SELA paper introduction | 6 | 7 | 7 |
| How SELA inspects a signal | 9 | 10 | 10 |
| A valid tree can still misrepresent the description | 10 | 11 | 11 |
| How GroundTSSyn generates labeled time series | 14 | 16 | 16 |
| GroundingMOMENT architecture | 15 | 17 | 17 |

The original 23 slide topics remain. Pages 6 and 13 were added in v19 to introduce the two approaches and explain how leaf confidence determines the event type. v20 retains the 25-page order and updates content within the deck.

<details>
<summary>Selected slides at full size</summary>

### Slide 7: SELA paper introduction

[![Grammar of the Wave paper introduction and event example](previews/sela-introduction.png?v=v20-5d4987bdc26e)](previews/sela-introduction.png?v=v20-5d4987bdc26e)

### Slide 10: SELA method

[![SELA signal inspection method](previews/sela-method.png?v=v20-e44d65141c01)](previews/sela-method.png?v=v20-e44d65141c01)

### Slide 11: ELT parsing quality

[![Pass rate, structural fidelity, primitive accuracy, coverage, and semantic alignment](previews/parsing-quality.png?v=v20-f431cc55a276)](previews/parsing-quality.png?v=v20-f431cc55a276)

### Slide 16: Synthetic training examples

[![GroundTSSyn duration and amplitude variation](previews/synthesis-variation.png?v=v20-f2e400432b95)](previews/synthesis-variation.png?v=v20-f2e400432b95)

</details>

## What to learn from the example

- Introduce the research question through a concrete pressure-test task.
- Preserve authorship, research citations, and the source paper's vocabulary.
- Connect descriptions to measured intervals with a logic tree and aligned time axes.
- Distinguish modules, data, outputs, and feedback in method diagrams.
- Show timing and amplitude changes on common scales in paired synthetic examples.
- Keep metric names, units, and experimental context in result comparisons.

## Package checks and limits

| Item | Observed in the supplied files |
| --- | --- |
| Slides and PDF pages | 25 PPTX slides and 25 PDF pages, widescreen |
| Speaker notes | 25 nonempty notes pages |
| Native tables | 4, on slides 11, 13, 23, and 24 |
| Embedded video | 3 MP4 files, referenced by slides 12, 18, and 19 |
| SVG assets | 25 distinct embedded SVG files and 25 SVG references |
| Font data | 5 embedded font files; font names include Newsreader and Inter families |
| Integrity | PPTX ZIP check passed; all PDF pages rendered |

The unchanged historical v10 design record describes an earlier figure set and reports 18 SVGs. The current v20 PPTX contains 25. No updated design document, complete editable-figure archive, or font-license package accompanied the v20 files. The skill's [six SVG examples](../../../skills/design-academic-slides/assets/examples/) remain the selected figures supplied with the original skill package.

PDF and PNG previews are static. Video embedding was inspected, but playback, animations, PowerPoint editing, and a full rebuild were not tested during repository publication. Research sources are attributed in the design record; publication checks do not reproduce the experiments.
