# SELA Presentation Profile

Apply this profile only to SELA / Grammar of the Wave or an explicit request to reuse its visual language. Treat it as a record of design decisions, not a frozen source of scientific results. Read the paper and deck version selected for the current task.

## Scientific framing

Introduce language-guided multivariate time-series event detection with a concrete description, multichannel signal, and predicted event intervals/classes. Explain the grounding difficulty through alignment, multichannel composition, and inspectable evidence when those themes match the selected paper.

Present Event Logic Trees before the full SELA system when this helps the audience understand the agents' intermediate objects. Show the full selected event description beside its tree in a compact quotation treatment.

Explain operators through their relationship to **Allen's interval algebra**. Verify the exact mapping from the paper; do not substitute an assumed mapping for SEQ, SYNC, GUARD, or OR. State the paper's compact, self-contained event assumption and its exclusion of disjoint before/after relations where applicable. Do not claim that ELT implements all Allen relations or that every operator corresponds to one Allen relation.

If requested, add a sourced image of the theorist or the classic publication with a short citation. Verify identity and reuse conditions. Correct the spelling to “Allen.”

## Event Logic Tree notation

- Prefer the horizontal root-to-leaf style used by the case study.
- Keep node dimensions equal within each comparable tree; repeat that grid across matching trees.
- Draw schema operators unfilled and schema primitives with dashed outlines.
- Draw instantiated active nodes with dark outlines and pale matching fills.
- Show inactive alternatives explicitly. For an OR instance with one supported child, mute the other branch; preserve inclusive-OR semantics when more than one child is supported.
- Reuse the same operator and primitive colors throughout the representation slide, system overview, and case study.

Show topological elasticity by varying the relative lengths of rise and steady phases together while retaining the stated temporal relations. Label schematic examples; do not manipulate measured data.

## SELA system overview

Show the following as a connected, readable system:

| Element | Visual treatment | Meaning to expose |
| --- | --- | --- |
| Natural-language description | Document icon and short label | Analyst's source semantics |
| Multichannel signal | Aligned channel traces | Inspector's evidence input |
| Logic Analyst | A distinct character | Builds and reviews the tree against the text |
| Logic Engine | Compact tool/module symbol | Compilation status and defined tree evaluation |
| ELT schema | Unfilled horizontal tree | Structure before grounding |
| Signal Inspectors | Overlapping or repeated characters | One agent per class when supported by the method |
| Instantiated ELT | Filled horizontal tree | Grounded primitives and active alternatives |
| Output | Interval/class labels plus evidence | What the detector returns |

Include Logic Engine feedback to the Logic Analyst about whether compilation succeeds. Separately show the analyst reviewing the structure against the language description. Compilation alone does not check semantic fidelity.

Show the inspector's tool interaction and grounded evidence clearly. Keep the generic overview free of unnecessary dataset-specific class names. Preserve concrete class names in the detailed case study.

## Character assets

The original design used Kenney's Roguelike Characters sprites, identified by the user as CC0-1.0. Recheck the downloaded asset's license and atlas before reuse; this skill does not redistribute the artwork.

- Source: https://kenney.nl/assets/roguelike-characters
- Atlas name recorded in the project: `kenney_roguelike_characters.png`
- Recorded tile size: 16 px; spacing: 1 px.
- Orange-haired inspector: column 0, row 5; crop `[0, 85, 16, 101]`.
- Turquoise-clothed inspector: column 1, row 5; crop `[17, 85, 33, 101]`.

Treat crop boxes as `[left, top, right, bottom]` with exclusive right/bottom bounds. Confirm the fetched atlas uses the same arrangement before cropping. Use nearest-neighbor scaling to retain the pixel-art appearance where supported. Choose a different character for the analyst and record that choice rather than reusing an inspector avatar.

## Experimental slides

Use only results verified from the selected source version. Do not hard-code dataset counts, model versions, or metric values from this profile.

Include an LLM parsing-quality benchmark alongside end-task results when the source supports it. Keep pass rate, valid-parse quality, structural fidelity, and semantic alignment distinct. Preserve denominators.

Include verified CNN and Transformer baselines and a useful spread of time-series foundation models when requested. Do not fill absent experiments with estimates.

For Pressure Test F1 at different IoU thresholds, consider a wide/light and narrow/dark overlay after checking the values and protocol. For Climate Hazard F1 and F0.5 coverage metrics, retain their exact labels and do not imply guaranteed nesting. Follow the experimental-evidence reference for safe alternatives.

For a full case-study slide, enlarge the supplied signal-and-tree view and remove an unhelpful heading if requested. Preserve the source aspect ratio. If two case animations are supplied for stacked presentation, retain their complete evidence and verify actual playback or disclose a static fallback.

## Cover and close

Use the latest selected calligraphic artwork for the main title only when continuing that accepted cover direction. Keep it as a transparent layer behind the upright subtitle. Move subtitle, authors, affiliations, and logos together when requested; adjust flourishes so they do not collide with author names. Do not assume “second version” identifies an image without resolving the current assets.

Keep the closing takeaways grounded in the paper's findings: representation, evidence quality, temporal structure, and remaining limitations. Keep paper/code links or QR codes only in the requested form. Remove redundant text links or closing blocks when the user asks.

## Boundaries

Do not apply these characters, Allen mapping, operator set, event assumption, or diagram states to unrelated work without checking its semantics. Reuse the underlying design principles: explicit inputs and outputs, consistent state encoding, verified theory mapping, complete evidence, and editable delivery.
