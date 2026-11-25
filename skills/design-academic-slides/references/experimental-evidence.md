# Experimental evidence

Before plotting, record dataset, metric, denominator, threshold, unit, model or backbone, supervision, averaging, and uncertainty statistic for each experimental condition. Leave missing observations explicitly missing. Recompute any difference from the source values and match the precision of the published table.

| Comparison | Compose the view | Check |
|---|---|---|
| Localization at two thresholds | Two aligned dot-and-whisker panels. Keep one row per method, the same axis limits, and exact values beside the marks. | Define the threshold and the error statistic. Use whiskers only when the source reports variability. [Example](../assets/examples/localization.svg) |
| Several exact scores | Native editable table with readable headers. When values have comparable definitions and direction, use a shared, labeled heat scale. | Print every value. Keep the numeric range explicit, include all comparable cells, and explain conditional denominators. |
| Different measures on the same methods | Align method rows across a small set of columns. Give comparable accuracy scores a common scale. Give time its own unit and scale. Align numbers on their decimal positions or right edges. | Test the chart with its color removed. Verify that readers can identify the metric, the method and the value. [Example](../assets/examples/accuracy-latency.svg) |
| An ablation | Align full and ablated models within the same dataset, metric and backbone. Name the removed component. | Check that a changed training or inference regime is visible where it affects the result. |
| Temporal localization errors | Use reference and prediction lanes on aligned signals, including adjacent plausible regions. | Check start, end, class, source and coordinate convention for every interval. |
| Research agenda or related work | Use a native text table when row and column relationships matter. Describe what each source actually controls or measures. | Give the proposal its own evidence requirements. Preserve speaker-readable cells and linked references. |

A reported percentage-point difference is the subtraction of two scores on the same percentage scale. A relative change requires stating its baseline. A conditional quality score needs its denominator on the slide. Distinguish compilation pass rate from the structural or semantic quality measured among passing parses. Use source-defined terminology and avoid an invented overall ranking.

A speed result needs the unit and evaluation setting. If a backend difference dominates interpretation, make it visible by the result. Otherwise retain the configurations in notes and avoid generalizing a reported runtime to all deployments. Keep numerical chart data editable when available. A source SVG serves vector editing, a chart workbook serves numerical editing, and a native table serves cell editing. Check each property promised to the user.

For a demonstration, obtain the actual project media. Keep the original video or animation and its natural aspect ratio. Check that the correct file is embedded, that its poster frame is representative, and that playback works in the intended presentation environment when accessible. Record the difference between a media-integrity check and an observed playback test.

## Set the geometry of a native comparison table

Give comparable columns equal widths, matching horizontal padding, consistent numeric alignment and the precision used in the source. Wrap long headers on meaningful word boundaries. Choose the row height after laying out the longest header; a compact matrix can use the same height for both header and data rows. Size a long method-label column to its content when necessary. In the SELA parsing matrix all six columns, including the model names, share one width, and every row has the same height. Verify the widths and heights in the native cells, then inspect a render for clipped text. Preserve the labeled heat scale, exact values and denominator during geometry edits.
