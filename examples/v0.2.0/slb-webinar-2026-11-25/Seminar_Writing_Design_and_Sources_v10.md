# Language-Guided Time-Series Perception: Solutions and Challenges

**Chenwei Wan · SLB AI Lab Webinar · v10 · 25 November 2026**

The 23-slide English seminar incorporates the four review threads on v9. The presenter is Chenwei Wan, CIFRE PhD Researcher, AI Lab, SLB.

## Changes in v10

| Slide | Revision |
|---|---|
| 6 | The original “Grammar of the Wave” artwork deliberately overlaps the first line of the paper title. The darker editable title sits in front and the authors remain clear. |
| 7 | The upper captions identify the relative lengths of Rise and Steady. The shorter overall event spends more time rising than steady; the longer event spends more time steady than rising. Captions below identify the short and long events. Both examples use the same horizontal scale. |
| 14 | The synthesis figure pairs a single event description with two schematic draws from the same ordered primitive template. Brackets mark the duration assigned to each primitive, and a vertical measure marks the rise amplitude on the same scale for both traces. Values in the drawing illustrate the mechanism. The benchmark summary row has been removed. |
| 20 | Two lines beneath the section title introduce the subjects of the following pages: real-time multichannel detection using synthetic training data, and reasoning, prediction and decision support from detected events. |

GroundTSSyn first allocates the event duration among primitives, samples amplitudes from configured ranges and realizes the waveform. Its occurrence-variation step perturbs parameters within bounds, re-synthesizes the primitives and checks the constraints. The new figure illustrates the training purpose of those variations. Its numbers are illustrative sample counts and relative amplitudes before normalization. [Hou et al. (2026), Appendix A.2, pp. 4824–4825](https://aclanthology.org/2026.findings-emnlp.229/)

The accompanying PDF is exported from the final PPTX. The PPTX retains three embedded demonstrations and the PDF displays their still frames. Prior review decisions below are listed by version.

## Changes in v9

| Slide | Revision and source |
|---|---|
| 5 | The engineer beside the query is a full-color cutout from the original SELA conference presentation. The cutout retains the source RGB pixels of the helmet, face and blue work clothes. The measured trace, candidate windows and labels are unchanged. [Original presentation](https://github.com/cw-wan/SELA/blob/4fa7c3502ed71852c6791503fd494d210db33e42/SELA_EMNLP26_Slides.pptx) |
| 6 | Lowered the “Grammar of the Wave” wordmark and adjusted spacing before the paper title. The title sits between the event logo and the author block. |
| 7 | The schematic now uses a common horizontal duration scale for a short and a long event. Explicit labels sit below the two examples. The stable volume spans the entire pressure sequence in each event. The pressure rise also occupies a different fraction of each event. These are schematic durations. |
| 10 | All six columns have the same width. Header and data rows share the same height. The table remains editable, with the original values, color scale and conditional interpretation. |
| 20 | The chapter divider carries the heading “Challenges and research directions” with the standard page number and SLB mark in the footer. The questions are available in the speaker notes and in the following research slides. |

The PDF is exported from the final PPTX. The presentation retains the three original embedded media files. The PDF presents the corresponding static frames. The source archive includes all 18 editable SVG figures and the current design record.

## Changes in v8

| Review item | Implementation |
|---|---|
| Webinar label | Removed “AI Lab Webinar” next to the cover logo. |
| Presenter details | The two editable lines below the name give the requested position and affiliation. |
| SLB identity throughout | Slide 1 retains the supplied full-size SLB mark. Slides 2–23 reuse that image in the footer immediately left of the page number. All marks keep their source proportions. Each footer assigns separate space to the citation, mark and page number. |

## Review decisions in v7

| Slide in v6 | Slide in v7 | Revision |
|---|---|---|
| 1 | 1 | The full heartbeat description in GroundingMOMENT Figure 2 appears below the recording. Three phrases share their colors with the P wave, QRS complex and T wave. The general description comes from the paper and the recorded signal comes from LUDB. |
| 4 | 4 | Both channels span the full trace from sample 0 to 1694. An earlier similar pressure drop and the complete annotated test are visible together. The query sits above the traces. Drawdown and Buildup are marked within the later event. |
| 6 | 6 | The magnified view gives Valid Test and its nested Buildup separate interval bars. The valid test spans samples 1021–1433. Buildup begins near sample 1059 and reaches the same endpoint. The figure names Bounce and Steady on pressure and Stable on volume. Matching colors identify those three leaves in the ELT. |
| 13 | 13 | The second paper introduction uses the same EMNLP 2026 mark as the first. The publication title and authors remain, and the footer identifies the Findings track. |
| 18 | 18 | The three GroundTSBench metrics share aligned headers, method rows and right-aligned values. Event and primitive mAP share a 0–100 scale. The latency column gives seconds per sample. Inference configurations appear in the speaker notes. |
| 20 | — | The comparison slide was removed. The remaining slides and their notes were renumbered. |
| 22 | 21 | The opening question asks how to ground multichannel events in real time. A three-stage diagram presents the proposed path from event specification to labeled synthetic traces to a fast detector. The lower half compares the controls used by three existing generators with the temporal relations that grounding supervision must specify. A pressure-and-volume rule illustrates the difference. |

## Numerical and media checks

Slide 18 reproduces the GroundTSBench test results for SELA (GPT-5.4) and GroundingMOMENT (BERT-large, MOMENT-base). The reported event mAP values are 83.6 and 79.2, primitive mAP 88.3 and 88.7, and mean latency 49.0 and 1.2 seconds per sample. The published experiments used different inference backends. [Hou et al., Table 2 and Appendix D](https://aclanthology.org/2026.findings-emnlp.229/)

Slides 11, 16 and 17 contain the original three video files. The PPTX also contains 18 vector figures, 23 speaker-note pages and three native PowerPoint tables. The figure archive contains the editable SVG source for every embedded SVG. Slides 10, 21 and 22 contain the native tables.

## Lessons from Anthropic research figures

| Post and figure | Observation | Application |
|---|---|---|
| *Anthropic Economic Index report: Uneven geographic and enterprise AI adoption*, Figure 1.2 | Two aligned panels connect an aggregate comparison to its constituent interaction modes. The scale and the category names travel with the data. | Slide 6 gives the full record and the complete event separate panels. Slide 12 repeats the F1 scale and aligns the models so the effect of a stricter overlap threshold is visible in each row. [Article](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) |
| *Tracing the thoughts of a large language model*, rhyme-planning figure | The example repeats its structure across the original and intervened conditions, making the changed concept easy to follow. | Slide 21 keeps the volume condition fixed while its rule permits either pressure recovery or a rebound. [Article](https://www.anthropic.com/research/tracing-thoughts-language-model) |
| *Introducing the Anthropic Economic Index*, occupational-category figure | A common layout binds category names, concrete tasks and their measurements, allowing a reader to compare several levels of detail. | Slide 22 uses each task as a column and aligns the question, required evidence and reliability test below it. [Article](https://www.anthropic.com/research/the-anthropic-economic-index) |

Slide 10 follows Table 3 of the SELA paper. Its shared color scale runs from the lowest displayed score (0.70) to the highest (1.00). The exact values and metric names remain editable. Slide 12 uses the values from the Pressure Test experiments in Tables 2, 4 and 5. [SELA paper](https://aclanthology.org/2026.emnlp-main.290/)

## Scientific provenance

- **Heartbeats.** LUDB record 1, lead II, sampled at 500 Hz. The cover shows samples 1205–2840. The sentence below it is the complete heartbeat description in Figure 2 of Hou et al. (2026, p. 4815). The selected beat has P-wave boundaries at 1911–1955, QRS at 1979–2028, and T wave at 2120–2224. Slide 13 shows a different beat from the same recording and uses the same primitive colors. These are expert reference annotations. The GroundingMOMENT ECG inference replay is on slide 17. [Dataset](https://doi.org/10.13026/eegm-h675) · [Original publication](https://doi.org/10.1109/ACCESS.2020.3029211) · [PhysioNet](https://doi.org/10.1161/01.CIR.101.23.e215) · [License](https://opendatacommons.org/licenses/by/1-0/)
- **Pressure test.** PT_46710318 contains one expert-labeled Valid Test spanning samples 1021–1433. Window A, 456–945, was selected as a visually similar candidate. The Buildup start at approximately 1059 and the short Bounce segment are readings of the traces. KITE provides the outer event annotation. The engineer is adapted from the authors’ original task illustration. [KITE trace](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/timeseries/PT_46710318.csv) · [Expert labels](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/labels.csv) · [Original slides](https://github.com/cw-wan/SELA/blob/main/SELA_EMNLP26_Slides.pptx)
- **TimeGAN.** Yoon, Jarrett and van der Schaar (2019). *Time-series Generative Adversarial Networks*. NeurIPS 32. [Publication](https://papers.neurips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html)
- **Time Weaver.** Narasimhan et al. (2024). *Time Weaver: A Conditional Time Series Generation Model*. ICML, 37293–37320. [Publication](https://proceedings.mlr.press/v235/narasimhan24a.html)
- **CauKer.** Xie et al. (2026). *CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data*. ICLR. [Author version](https://arxiv.org/abs/2508.02879)

## Typography and figure sources

The deck uses Newsreader for display text and Inter for research labels and explanatory text. The native PowerPoint file embeds the fonts. The review copy fixes the display type so linked comments see the intended letterforms. The figure package includes 18 editable SVGs and both font licenses. [Typography reference](https://www.cs.princeton.edu/~danqic/) · [Newsreader](https://github.com/google/fonts/tree/main/ofl/newsreader) · [Inter](https://github.com/google/fonts/tree/main/ofl/inter)

## Writing and design resources

| Resource | Use in this seminar |
|---|---|
| [Elegant Academic Slides](https://github.com/cw-wan/elegant-academic-slides-skill) | Retain the original scientific argument and authorship. Give event diagrams an explicit reading order and right-align all terminal leaves of the ELT. |
| [Scientific Writing](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-writing/SKILL.md) | Report the metric, unit and experimental setting on result slides. Attribute interpretations and expert labels explicitly. |
| [Writing Clearly and Concisely](https://github.com/obra/the-elements-of-style/blob/main/skills/writing-clearly-and-concisely/SKILL.md) | Use short phrases that listeners can connect to the waveform. |
| [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | Remove repeated setup and defensive qualifiers. |
| [Academic Diagram](https://github.com/plbbl/academic-diagram-skill/blob/main/SKILL.md) | Draw and check the vector sources before inserting the figures into the presentation. |
| Presentations | Check the PowerPoint package, native tables, notes, slide renders and review copy. |
| Skill Creator (v4) | Recorded the editorial conventions established in the earlier review. |

## Scientific publications, original demos and seminar examples

- Allen (1983). *Maintaining Knowledge about Temporal Intervals.* Communications of the ACM, 26(11), 832–843. [Publication](https://doi.org/10.1145/182.358434)
- Devlin et al. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* NAACL-HLT, 4171–4186. [Publication](https://aclanthology.org/N19-1423/)
- Goswami et al. (2024). *MOMENT: A Family of Open Time-series Foundation Models.* ICML, 16115–16152. [Publication](https://proceedings.mlr.press/v235/goswami24a.html)
- Hou et al. (2026). *Language-Guided Time-Series Event Detection with Zero-Shot Cross-Modal Grounding.* Findings of EMNLP, 4813–4836. [Publication](https://aclanthology.org/2026.findings-emnlp.229/)
- Liu et al. (2024). *Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection.* ECCV. [Publication](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6319_ECCV_2024_paper.php)
- Wan et al. (2026). *Grammar of the Wave: Towards Explainable Multivariate Time Series Event Detection via Neuro-Symbolic VLM Agents.* EMNLP, 6638–6656. [Publication](https://aclanthology.org/2026.emnlp-main.290/)
- Xie et al. (2025). *ChatTS: Aligning Time Series with LLMs via Synthetic Data for Enhanced Understanding and Reasoning.* Proceedings of the VLDB Endowment, 18(8). [Publication](https://www.vldb.org/pvldb/vol18/p2385-xie.pdf)

- [KITE pressure and volume, PT_46710318](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/timeseries/PT_46710318.csv) · [expert labels](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/labels.csv) · [event descriptions](https://github.com/cw-wan/SELA/blob/main/data/PressureTest/desc.txt)
- [SELA conference deck with original lettering, graph conventions and replay](https://github.com/cw-wan/SELA/blob/main/SELA_EMNLP26_Slides.pptx) · [supplied EMNLP logo](https://github.com/cw-wan/SELA/blob/main/img/emnlp_2026.png) · [Kenney character artwork](https://kenney.nl/assets/roguelike-characters)
- [GroundTSSyn](https://github.com/houtj/GroundTSSyn) · [GroundingMOMENT model and demonstrations](https://github.com/houtj/GroundingMOMENT) · [ChatTS Fig. 4, arXiv edition](https://arxiv.org/pdf/2412.03104)
- [Jeff Dean, CIKM keynote, cover](https://research.google.com/people/jeff/CIKM-keynote-Nov2014.pdf) · [Rob Hyndman, forecast reconciliation, Zalando seminar](https://robjhyndman.com/seminars/fr_overview.html)
- [Fei-Fei Li, visual recognition talk](https://www.ted.com/talks/fei_fei_li_how_we_re_teaching_computers_to_understand_pictures) · [Michael Alley, assertion–evidence approach](https://writing.engr.psu.edu/assertion_evidence_EA.html) · [Yann LeCun, Berkeley EECS Colloquium](https://eecs.berkeley.edu/research/colloquium/220927-2/)
