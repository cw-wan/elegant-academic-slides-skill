# Experimental Evidence

## Build a comparison contract

Before plotting, preserve the dataset, target, metric, scale, threshold, averaging rule, backbone, supervision setting, and uncertainty information for each value. Label missing results as missing; never draw them as zero.

Keep percentages and unit-interval scores consistent. Express a subtraction of percentages as percentage points, and distinguish it from relative percentage improvement. Recalculate any displayed delta from the underlying values.

If the user asks for CNN, Transformer, or additional time-series foundation model baselines, locate verified results in the selected sources. Include available model families in a compact view. If results for a requested baseline do not exist, identify the gap; do not invent a bar or imply a new experiment was run.

Report an unavailable requested experiment in the handoff or private change checklist. Put it on the slide only when it is itself relevant to the scientific discussion. Avoid filling a polished result slide with production-status notes or empty placeholder rows.

## Choose the visual for the comparison

| Question | Useful view | Constraint |
| --- | --- | --- |
| Which model performs better? | Grouped bars or dot plot | Shared metric and scale |
| How do two thresholds compare? | Paired or overlapping bars | Same metric definition except threshold |
| What changes without a component? | Paired bars or paired dots | Same evaluation configuration |
| Where does a system fail? | Timeline plus predictions and evidence | Preserve time scale and annotations |
| How do several quality dimensions differ? | Native table, optionally with heatmap | Keep exact labels and denominators |
| How much does performance vary? | Error bars or interval plot | Use only uncertainty actually reported |

Use a table when it is clearer than a crowded chart. Do not force every result into a bar chart. Keep a consistent model order across comparable panels; group families visibly when the order has scientific meaning.

## Overlap two results without hiding their meaning

Use light and dark bars at the same category position to reduce duplicated panels when both values share a meaningful numerical scale. This is an overlay, not a stack: neither bar should start at the other's endpoint.

For genuinely nested thresholds, such as a looser and stricter localization threshold under the same protocol:

1. Verify the actual values and evaluation definitions; do not assume nesting from the labels alone.
2. Draw the looser-threshold value as a wider, lighter bar behind.
3. Draw the stricter-threshold value as a narrower, darker bar in front.
4. Start both at zero and keep their category centers aligned.
5. Label both metric definitions in the legend and retain exact values in editable data.
6. Explain a visible discrepancy if the expected ordering does not hold; use grouped bars when nesting would mislead.

For different metrics such as F1 and F0.5, do not describe the bars as a stricter/looser pair or a guaranteed subset. F0.5 changes the precision-recall weighting, and its ordering relative to F1 can vary. If the user explicitly requests an overlay, label both metrics exactly, ensure neither is concealed, use clearly different widths, and keep the same zero baseline. Prefer paired bars or dots if crossing values make the overlay hard to read.

Use light/dark shades within a model's color only when contrast remains adequate. A gray/light series is acceptable if the legend and labels remove ambiguity. Use labels, width, or line cues in addition to color.

Avoid stacked totals, misleading occlusion, incompatible scales, hidden axes, and bar-chart truncation. Do not compare a localization F1 in one dataset directly with a coverage F-score in another as though they were the same quantity.

## Intermediate parsing and reasoning quality

Include a stage-specific benchmark when a system's contribution depends on structured parsing or grounding and evidence is available. Distinguish at least the reported dimensions rather than compressing them into one invented score.

Possible source-defined dimensions include compilation/pass rate, primitive validity, structural fidelity, semantic alignment, and coverage. Use the paper's exact definitions and denominators. A score among valid parses must not be presented as a score over all attempted parses.

Keep compile success and downstream quality visibly separate. When one model has higher pass rate and another has better fidelity conditional on passing, show the tradeoff. Do not choose a universal “best” model by an unstated aggregation rule.

Avoid a redundant setup slide when one benchmark slide can carry the title, short explanation, and data. If requested, transfer the useful heading and subtitle to the results page and remove the duplicate page.

## Ablations and cases

Show each full/ablated comparison within its own dataset and metric. State what the ablation removes or replaces. Keep the backbone and evaluation regime fixed or explain the difference.

Use a case study to expose the mechanism: input evidence, reference annotation, prediction, and relevant intermediate structure. Preserve all required channels and the same time alignment across panels. Clearly label a selected case; do not present it as representative of the full distribution without evidence.

For animations, preserve the actual media and test playback when possible. Use a poster frame or static fallback only with a clear delivery note. A GIF imported as its first frame is not an animated result.

## Preserve editable chart data

Retain native charts, series names, category labels, and the embedded workbook when present. Preserve workbook formulas and relationships when editing an existing deck.

Treat missing workbooks after an import/export round trip as a concrete failure to investigate. Recover the original corresponding package parts only after verifying their identity and relationships. Do not blindly copy chart parts by hard-coded slide numbers or silently replace a formula-backed workbook with literal values.

Use the active presentation backend's documented chart API and validators. A chart image may look right while its underlying editable data is missing; check both appearance and structure.
