# Scientific Diagrams

## Show objects and operations

Organize a method figure around identifiable data objects and their transformations. Use compact labels, short annotations, and visible branches. Avoid replacing architecture with paragraphs inside large rectangles.

When the user provides a conference-paper figure as a style reference, inspect its grouping, typography, line weights, arrow conventions, object density, and reading order before drawing. Carry those visual principles into the new figure while preserving the new system's actual semantics. Do not substitute a generic flowchart template for an explicitly requested academic figure style.

Before drawing, list:

- External inputs and final outputs.
- Learned components, deterministic tools, and human actions if any.
- Intermediate objects and their state changes.
- Forward dependencies and feedback paths.
- Model or algorithm identities explicitly established by the source.

Use containment only for an actual scope: a shared encoder, a repeated agent population, a trainable module, or a runtime boundary. Do not use enclosure merely to fill space.

## Render a system completely

Show the output explicitly, such as predicted intervals and classes, a ranked candidate list, or a structured query. A pipeline that ends at an internal module leaves the task unexplained.

Label feedback by its information content: compilation status, error message, coherence score, evidence interval, or review request. Separate compilation feedback from comparison with the original language description. Draw arrow direction and termination carefully so a viewer can identify which component acts on feedback.

Distinguish a schema from an instance and a proposed query from an executed or validated query. Do not imply access to resources that have not been built or supplied.

## Represent multiple agents honestly

Use repeated or partially overlapping avatars to indicate a population when multiplicity matters. Add a short label such as “one inspector per class” where it explains the actual division of work. Keep dataset-specific class names in case studies unless they are needed in the overview.

Assign consistent avatars to roles. A character used as an inspector in the case study should retain that role in the overview. Give a different analyst role a distinct character. Keep the source, license, atlas, and crop coordinates with the asset manifest when using sprites.

Show agent-tool interactions rather than anthropomorphic decoration alone. Keep deterministic engine outputs visually distinct from the agent's interpretation of them.

## Trees and structured representations

Choose a consistent reading direction. Prefer a horizontal, left-to-right tree when the case study uses that convention or it makes alignment with the source description clearer.

- Put the root at the left and successive depths to the right.
- Keep all nodes in a comparable tree the same dimensions when requested; otherwise at least keep equivalent node roles dimensionally consistent.
- Fit the longest label by sizing the node system, wrapping, or using explained abbreviations. Do not shrink isolated nodes unpredictably.
- Use orderly branch spacing and clean connectors.
- Keep operator labels, leaf labels, and channel assignments faithful to the source.
- Make each edge's endpoint and branch membership unambiguous.

Use this state convention when no established project notation conflicts:

| State | Border | Interior | Additional cue |
| --- | --- | --- | --- |
| Schema operator | Solid semantic outline | White or unfilled | Operator label |
| Schema primitive | Dashed semantic outline | White or unfilled | Primitive/channel label |
| Instantiated active node | Dark semantic outline | Pale matching fill | Evidence or score if relevant |
| Inactive alternative | Muted or dashed outline | Neutral/light fill | “Inactive” or another explicit cue |

Keep instantiated nodes visually different from unfilled schema nodes. Do not use a heavy saturated fill where a dark border and light interior communicate state more clearly.

For OR, depict the alternatives actually supported by the instance. If the source example activates one branch, show the other branch as inactive. Do not make every branch active for visual symmetry. Do not turn inclusive OR into exclusive OR: if the source permits several active children, preserve that behavior.

## Pair text with structure

Place the complete selected description in a compact quotation treatment beside its tree. Align corresponding phrases and leaves through restrained shared colors or concise labels. Retain enough text for a viewer to inspect whether the tree reflects the description.

Size the quotation block to its text. Avoid an oversized empty lower region, protruding decorative border, or unnecessary “tail.” Use the same tree notation in the explanatory slide and the detailed case.

## Explain temporal flexibility

To illustrate relative duration flexibility, change the relative lengths of at least two subevents while preserving the stated temporal relations. For a rise followed by a steady interval, contrast a shorter rise/longer steady interval with a longer rise/shorter steady interval.

Keep the demonstration schematic unless drawn from actual data, and label it accordingly. Do not distort a measured signal to manufacture a result. Make the invariant topology and changing durations visually distinguishable.

## Theory-to-operator mapping

Use a compact alignment of operator, relevant relation or relation set, interval schematic, and any restriction. Verify the mapping against the selected paper. Do not infer a one-to-one relationship from similar names or collapse several relations into an unsupported equivalence.

State assumptions beside the mapping when they explain excluded relations. Keep historical attribution separate from the scientific claim about what the method implements.

## Inspect the figure

Trace a complete input-to-output path and a complete feedback cycle. Check every edge against the source. Compare the schema and instance node by node. Confirm that visual size, fill, or placement does not accidentally imply unsupported importance, activation, exclusivity, or certainty.
