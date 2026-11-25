# SELA and GroundingMOMENT seminar profile

Use this profile for *Language-Guided Time-Series Perception: Solutions and Challenges* or a user-requested match. Slide numbers refer to the 23-page SLB seminar v10. Use the current paper and deck as the authority when the work changes.

| Pages | Scientific and editorial choices |
|---|---|
| 1 | Introduce Chenwei Wan, CIFRE PhD Researcher, AI Lab, SLB. The cover motif is a real lead-II recording with a selected heartbeat. The full short source description sits below it. Three phrases correspond to P wave, QRS complex and T wave through shared color and direct labels. |
| 2–5 | Open with an operational pressure-test question, position event grounding among familiar tasks, then show a complete measured record with two similar candidates. Use temporal language and cross-channel evidence to distinguish them. |
| 6–12 | Introduce the SELA paper with its author list and venue mark. Show Buildup as a child interval of Valid Test and match tree leaves to on-trace primitives. Explain duration flexibility and the source-defined mapping to Allen's interval algebra. Follow the Logic Analyst, Logic Engine and Signal Inspectors through to an interval and evidence. Present parsing fidelity, the recorded case, then strict localization. |
| 13–19 | Introduce the GroundingMOMENT paper with its author list and the matching venue mark. Identify the Findings track in the source. Show training data synthesis, the model and its interval outputs, original drilling and ECG replays, accuracy and latency, and transfer results. |
| 20–22 | Open with the heading “Challenges and research directions” and one short preview per following research page, in order. Show the proposed chain from event specification through labeled traces to a fast detector. Compare existing generators by their control signal before illustrating the required cross-channel rule. Then link perception, reasoning, prediction and decision support to their evidence and reliability checks. |
| 23 | Give full references. Maintain page-specific citations throughout the seminar. |

## Objects to preserve

- A complete full-record view and a separate detail view. In PT_46710318, the expert-labeled Valid Test spans samples 1021–1433. The Buildup start near 1059 is interpreted from the traces and is marked approximate. Label Bounce and Steady on pressure and Stable on volume. Ground one possible branch without changing the semantics of OR.
- Right-aligned terminal ELT leaves, soft curves, stable channel labels and an identifiable active state. Verify the scientific assumptions behind the operator mapping in Wan et al. Connect compiler feedback to the analyst and distinguish that feedback from semantic review.
- Slide 5 uses the original full-color engineer illustration, cropped from the SELA conference PPTX. On slide 6 the muted “Grammar of the Wave” artwork sits behind the first line of the editable paper title.
- Slide 7 contrasts a short total duration with rise longer than steady and a long total duration with rise shorter than steady. Stable volume spans each full event. Above-trace labels express the phase balance; below-trace labels name each event length. [Editable schematic](../assets/examples/temporal-elasticity.svg)
- Slide 10 uses six equal native columns, one common row height and a labeled heat scale. Slide 14 shows one description with two annotated draws, sampled phase durations and baseline-relative amplitudes. Its main sentence gives the purpose of the training pairs. [Editable synthesis diagram](../assets/examples/synthesis-variation.svg)
- The two information lanes of GroundingMOMENT, its event and primitive queries, shared decoder and separate span outputs. Keep the architecture distinct from both training-data synthesis and waveform-level inference demonstrations.
- Native tables for parsing, generator controls and the roadmap. The threshold chart uses two aligned dot-and-whisker panels. The trade-off chart separates accuracy and seconds per sample. Retain original replay media in the presentation copy.
- The original host logo at the upper left of the cover, and one compact host mark immediately left of each subsequent page number. The conference mark identifies paper introductions. Continue the main seminar in Newsreader for titles and Inter for body and data labels. Carry forward the latest approved content. The v11 Windows compatibility copy used Times New Roman and Arial for native text while retaining the original diagram outlines. Its font mapping applies only to that delivery.

The review delivery comprises the numbered PPTX, its matching PDF, the commentable copy, vector sources and design record. All three embedded demonstrations have static frames in the PDF.

[SELA publication](https://aclanthology.org/2026.emnlp-main.290/) · [GroundingMOMENT publication](https://aclanthology.org/2026.findings-emnlp.229/) · [SELA slides and project](https://github.com/cw-wan/SELA) · [GroundingMOMENT demonstrations](https://github.com/houtj/GroundingMOMENT)
