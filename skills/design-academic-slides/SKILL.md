---
name: design-academic-slides
description: Create and revise evidence-led academic presentations with editable PowerPoint content, readable research figures, precise method diagrams, honest result charts, and consistent visual semantics. Use for paper-to-talk conversion, conference or seminar slides, research updates, architecture figures embedded in decks, and iterative slide-annotation fixes. Apply the SELA profile only to SELA or an explicitly requested matching style. Do not use as the primary workflow for academic posters or generic business pitch decks.
---

# Design Academic Slides

Make the research easy to follow, the evidence easy to inspect, and the result easy to edit.

Treat the user's current instructions and latest accepted design as the working contract. Use the defaults below only where that contract is silent. Resolve routine layout choices without repeatedly requesting approval.

## Read the appropriate references

| Work to do | Read |
| --- | --- |
| Establish the story, select claims, summarize a paper | [Scientific content](references/scientific-content.md) |
| Set layout, typography, density, imagery, or cover | [Visual design](references/visual-design.md) |
| Draw a system, agents, tree, or structured representation | [Scientific diagrams](references/scientific-diagrams.md) |
| Present experiments, benchmarks, or ablations | [Experimental evidence](references/experimental-evidence.md) |
| Apply comments, export PPTX, or verify a deliverable | [Revision and delivery](references/revision-and-delivery.md) |
| Continue SELA / Grammar of the Wave | [SELA profile](references/sela-profile.md), plus relevant references above |

Read only the references needed for the task. For a cover-only edit, do not repeat the paper review or redesign the experiment section.

## 1. Establish the working contract

Identify the audience, speaking duration if supplied, requested language, slide count, output format, source paper version, current accepted deck, and required changes. Reuse known decisions. Ask only when a missing answer would materially alter the result; otherwise proceed with a stated assumption.

Keep the language of an accepted deck unless the user requests a change. Use concise academic prose, retain necessary technical terms, and remove production commentary, filler slogans, and unsupported caveats from slide copy.

For an academic talk without a format instruction, prefer editable PPTX when the environment supports file delivery. Honor explicit PowerPoint, Google Slides, or other destinations. Preserve an existing deck's dimensions. Use 16:9 for a new talk unless a template or venue says otherwise.

Separate three kinds of requirements:

- **Scientific invariants:** facts, labels, values, topology, model names, evaluation settings, and source wording that must survive an edit.
- **Presentation decisions:** ordering, scale, colors, typography, grouping, visual emphasis, and animation.
- **Requested changes:** the exact objects or slides the user wants changed now.

For several annotation rounds, maintain a short private change checklist. Apply the latest instruction for each element while preserving earlier decisions that remain compatible. Never restart from an older version merely because its builder is convenient.

## 2. Define the scientific story

Give every slide one communicative job. Preserve enough evidence and explanation to do that job. One job may require several coordinated panels; it does not imply a mostly empty slide.

For a full talk, consider this sequence and adapt it to the time budget:

1. Task and concrete input/output example.
2. Research difficulty and the gap in existing approaches.
3. Representation and its theoretical basis.
4. System operation, including feedback and outputs.
5. Evaluation design and main results.
6. Component quality, ablation, and a complete case.
7. Evidence-supported takeaways and an open limitation.

Do not force this sequence or add pages to a fixed-count request. For a three-page research update, motivation, input/output, and method may be sufficient. Put extra material in backup slides only if the requested slide count permits it.

Use the selected paper and current supplied results as the source of truth. Keep versions separate. Name the precise baseline, model, metric, and setting shown. Do not add invented results to fill a requested model family.

## 3. Build the visual hierarchy

Use a restrained academic composition: a clear heading, a dominant explanatory figure or evidence view, and short supporting text. Favor open layouts with alignment and whitespace over repeated cards, thick enclosing panels, or decorative containers.

Use these starting points for a new 16:9 deck; adapt to the actual template and render:

| Element | Starting point in PowerPoint points |
| --- | --- |
| Cover title | 36–48 pt |
| Slide heading | 28–36 pt |
| Main explanatory text | 20–24 pt |
| Figure labels and data labels | 16–20 pt |
| Secondary source notes | 12–14 pt, with full details in notes |

Set type sizes in the units required by the authoring tool. At 96 DPI, 1 pt equals 4/3 CSS px. Do not silently substitute px for pt.

Use one primary sans-serif family and a stable hierarchy. Use a deliberate secondary typeface only for an appropriate purpose, such as a short quotation or a requested calligraphic cover. Keep authors, affiliations, and meaningful axis labels readable.

Increase useful density by removing repetition, tightening oversized title regions, enlarging evidence, and improving grouping. Preserve room for the audience to track the speaker. Do not shrink body text to simulate density or copy a poster's entire reading load into a talk.

## 4. Make method figures explain the method

Show actual input objects, transformations, intermediate representations, outputs, and feedback. Label arrows with what passes through them. Give each block a short functional label; put long explanations in adjacent prose or notes.

Use exact scientific structure. Preserve edges, operators, channel associations, active states, and temporal relationships. Label actual model names when relevant and supplied. Make data objects visually distinct from processing modules.

Keep semantically equivalent nodes the same size. Maintain one meaning for each color and line style. Distinguish templates from instantiated objects and active evidence from inactive alternatives. Use the same notation in overview, explanation, and case-study slides.

Use original vector assets or native editable diagram elements for exact structures. Use generated or retrieved artwork for supporting imagery when appropriate; never synthesize scientific plots, numerical results, or exact topology as decorative images.

## 5. Turn results into comparisons

Choose the view around the question: bars for category comparisons, paired views for ablations, tables for precise multidimensional results, and timelines for localization. Keep native charts and editable underlying data when the output format supports them.

Preserve the full meaning of each result: metric, threshold, unit, dataset, backbone, supervision regime, and aggregation. Use a common scale only for comparable quantities. Use light/dark overlapping bars only under the conditions in [Experimental evidence](references/experimental-evidence.md).

Evaluate intermediate stages when they are part of the contribution. Distinguish syntax or compilation success from structural fidelity, semantic alignment, evidence quality, and end-task performance. Do not label all of these simply “accuracy.”

## 6. Iterate locally and preserve editability

Before editing, inspect the affected slide and its object structure. Record the intended change and protected content. Work on the latest accepted version and produce a new revision.

Keep text as text; charts and tables as native objects; exact diagrams as editable elements where requested. Keep decorative title artwork as a separate image layer. Preserve source image proportions, logos, chart workbooks, speaker notes, and links.

For a local edit, adjust only the affected composition and dependent elements. A title removal may justify enlarging its figure; a cover edit does not justify changing experiments elsewhere.

## 7. Verify and deliver

Use the environment's current presentation-authoring and validation workflow. This skill specifies design and evidence requirements, not a particular backend. Do not copy stale internal API names, fixed scratch paths, or environment-specific helpers into a new project.

Verify in this order:

1. **Content:** required material, source fidelity, model names, values, theory boundaries, and supported takeaways.
2. **Semantics:** diagram edges, visual state encoding, chart metrics, axes, and uncertainty statements.
3. **Appearance:** render every final slide; inspect changed slides at full size and scan the whole deck for unintended changes.
4. **Editability:** inspect text, tables, charts, embedded workbook relationships, and image layers in the exported file.
5. **Use:** check links, QR codes, media, and slide-advance settings where relevant to the request.

Treat intentional cover overlap differently from an accidental collision. A passed file validator does not establish visual quality or scientific correctness. A static preview does not establish that an animation works.

Deliver the requested deck and clearly identify any material limitation. Keep build logs, tests, temporary renders, and implementation commentary out of the slides. State that PowerPoint was checked only if the final file was actually opened there.

## Completion criteria

- The task, method, and evidence can be understood at normal presentation size.
- Required scientific content is present without unsupported embellishment.
- Input, output, feedback, and visual states are explicit.
- Comparisons preserve their metrics and evaluation conditions.
- The deck remains editable in the requested format.
- The final revision implements the comments and preserves unrelated content.
