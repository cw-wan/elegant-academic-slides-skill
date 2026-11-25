# Scientific diagrams

## Draw the vector first

1. Write the diagram as a set of labeled dependencies. Identify the input objects, learned components, deterministic computation, intermediates, output, and any real feedback edge.
2. Inspect the scientific reference at its intended scale. Take its reading order, grouping, use of token strips, evidence windows or axes. Use only components that exist in the selected method.
3. Build an editable SVG or a native vector diagram. Use short stage names, miniature data objects and quiet connectors. For a text-and-signal method, give the two inputs separate lanes until the stated fusion point. A two-line label can name a module and its actual model. Reserve a group boundary for an actual shared or repeated scope.
4. Render the vector by itself at the width it will occupy on the slide. Follow an entire input-to-output path with a finger. Check arrow destinations, nesting, label collisions, text size and color contrast. Place the approved visual in the slide at its original aspect ratio.
5. Keep the text-bearing SVG source. If Office needs a fallback, embed the vector with a matching raster preview. If a renderer substitutes fonts, outline a derivative and keep the original text editable in the delivered sources. Validate the figure again in the exported slide.

In a query-based architecture, show what queries attend to and what the decoder predicts. The [GroundingMOMENT architecture](../assets/examples/architecture.svg) shows separate signal and text encoders, event and primitive queries, a shared decoder and the temporal spans it returns. In an agent system, distinguish the analyst's semantic review from compiler feedback. Give an inspector an actual trace and show the evidence and interval it produces.

## Make a tree agree with the case

Use left-to-right reading when it matches the accepted tree design. Place terminal leaves on a common right-hand column, including leaves attached directly to the root. Consistent leaf widths align both edges. Preserve internal depth, parentage and branch order. Route branches with soft curves, leave space between adjacent leaves, and check that no curve appears to terminate at another branch's label.

Keep the primitive's channel in its label. Distinguish the schema from a grounded instance. Give active leaves corresponding segment labels on the signal. Mute an unused alternative while keeping it readable. Check the semantics of OR before drawing the active children. In a duration-flexibility example, keep the event relations fixed while varying the durations in explicitly schematic traces.

## Show an interval in context

| Step | Acceptance test |
|---|---|
| Select a case | The full event is present and its start and end both lie on screen. When illustrating ambiguity, include a plausible earlier or later candidate for comparison. |
| Draw the overview | Show enough of the measured record to interpret the event and, when relevant, compare candidates. Align channels on one time or sample axis. Label units, sample index, and channel identity where known. |
| Add a detail view | Locate the enlarged window in the overview. Preserve the time coordinates, channel order and signal values. |
| Encode containment | Use separate parent and child interval lanes on the same scale. Make a shared endpoint visible. Keep fills translucent enough to follow the trace. |
| Map language and structure | Pair a short on-trace primitive label with its matching phrase and tree leaf. Label observed segments and leave unsupported alternatives inactive. |
| State the evidence status | Distinguish expert annotation, model prediction and editorial interpretation. Use an approximation mark for a breakpoint inferred by eye. Carry its provenance in the notes. |

The [nested event example](../assets/examples/nested-intervals.svg) shows both a complete pressure record and a magnified test. Read the outer annotated interval first, then follow the Buildup bar and its pressure and volume primitives. Check small interval labels at presentation scale before using a crop or extension.

## Separate event length from the proportions of its phases

In a [paired duration example](../assets/examples/temporal-elasticity.svg), use the same horizontal distance per time unit. Align the starts within each local panel and give the longer event more width. Label each complete span below its endpoints. Above the pressure trace, name the relative lengths of the phases. A short event can spend most of its time rising and a long event most of its time steady. A second channel required to stay stable must extend to each event's own endpoint.

Check the example with the labels hidden: compare the total widths, then the fraction of each width taken up by the rise. Restore the labels and check that both readings match. An axis normalized to 0–100% can answer a question about phase fractions alone; an absolute-duration comparison needs a common time scale. Keep expert boundaries on measured traces distinct from invented durations in a schematic.

## Show the variation that supplies training supervision

Pair one fixed event description and ordered primitive template with two schematic waveforms. Share time and amplitude scales across draws. Mark phase durations horizontally at their boundaries and amplitude vertically from a defined baseline. State the units, normalization stage and status of example values in the figure or its accompanying explanation. A changed parameter should produce a visible change along its own axis.

In the [GroundTSSyn example](../assets/examples/synthesis-variation.svg), each draw selects a total event duration, allocates it among ordered primitives and samples amplitudes within their configured ranges. Occurrence variation can then perturb parameters, re-synthesize and check constraints. The two draws illustrate the supervision: the same description refers to the same ordered pattern across changes of timing and amplitude. Keep performance claims with the experiment that tests them. See [Hou et al., Appendix A.2](https://aclanthology.org/2026.findings-emnlp.229/).
