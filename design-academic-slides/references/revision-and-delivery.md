# Revision and Delivery

## Resolve the current version

Locate the latest accepted deck and the selected assets in the available project store. An old filename, scratch path, or preview is not evidence that the bytes still exist. Recover missing artifacts from the persistent source before rebuilding or requesting another upload.

Use current document contents for facts. Do not replace a current paper's values with remembered values from a later or earlier experiment. Keep the source deck unchanged and use a new revision name or the platform's version history.

## Convert comments into operations

For multiple comments, maintain a private checklist like this:

| Target | Requested change | Preserve | Verify |
| --- | --- | --- | --- |
| ELT example | Rotate to the case-study layout | Labels and topology | Node size and edge mapping |
| Agent system | Add compilation feedback | Role assignments | Arrow direction and feedback label |
| Main chart | Combine thresholds | Values and metric definitions | Zero baseline and visible overlay |
| Case figure | Remove heading and enlarge | Aspect ratio and all evidence | Canvas fit and text legibility |
| Cover | Add selected script behind subtitle | Artwork variant and editable text | Z-order and clearances |

Resolve objects by current slide identity and content, not only by an old page number. Recheck references and numbering after a slide deletion. Do not assume annotation coordinates remain valid after rearrangement.

Preserve compatible decisions from previous rounds. If “use the lower version” clearly identifies a visible selection, use that asset without reconfirmation. If the image is unavailable and the selection cannot be resolved, ask for only the missing asset.

## Edit with a bounded scope

Record the before-state of affected slides. Prefer object-level changes to recreation. Keep untouched text, charts, notes, links, backgrounds, media, and layouts unchanged unless their dependence on the edit requires adjustment.

For a purely typographic or label edit, preserve the figure's data, layout, colors, and other labels. For a content reorganization, explain why any scientific grouping changes. Do not infer permission to redesign the whole deck from one local comment.

When several related pages share a notation, update the affected repeated semantics consistently. For example, changing a tree's active-state style requires the same convention in the method overview and case study.

## Verify the final export

Render every final slide with the available presentation renderer. Inspect changed slides at full size, then scan the complete deck for accidental changes. For a small edit, compare unchanged-slide previews with the accepted version; identical rendered pixels are useful evidence when the renderer is deterministic. Package-byte differences alone do not prove a visual change.

Check the following according to the task:

| Area | Verify |
| --- | --- |
| Package | Opens successfully, correct dimensions and slide count, no missing relationships |
| Text | Native editable text, correct fonts and glyphs, no clipping or unintended wrapping |
| Scientific content | Exact values, labels, claims, citations, and version consistency |
| Diagrams | Correct edges, roles, activation states, feedback paths, and input/output |
| Charts | Native objects, values, categories, labels, workbook and formula preservation |
| Images | Correct selected version, aspect ratio, transparency, no cropped evidence |
| Cover | Script behind subtitle, readable text, no collision with names or logos |
| Cases | Complete channels, visible annotations, consistent time axis |
| Media | Actual animation/playback when promised; static fallback identified |
| Navigation | Slide numbering and references valid; unwanted timed advance absent if requested |
| Links | Required hyperlinks resolve; final QR codes decode to intended destinations |

Run the environment's required file validators. Inspect any warnings for relevance. Fix actual defects and repeat only the checks needed to resolve the remaining risk. Do not change validators to make a broken export pass.

Do not equate a thumbnail montage, package validation, or successful import with full visual inspection. Do not claim a PowerPoint playback check based only on a static render.

## Keep the skill portable and the project reproducible

Use paths relative to the skill for reference documents. Keep project-specific source files, generated media, chart data, and authoring code in the project's own workspace. Preserve expensive or irreplaceable artifacts in the available persistent store.

For asset provenance, record source URL or supplied filename, creator where known, license or permission status, dimensions, any crop, and semantic role. Add checksums when variant identity is important. Keep source scientific data separate from formatting code.

Do not bake personal file IDs, temporary directories, credentials, private document contents, or proprietary runtime paths into a public skill. Consult the local presentation tooling for backend-specific syntax rather than copying an old implementation.

This skill package requires no bundled rendering library or paid service. Use the presentation tools actually available in the environment. If they cannot preserve an essential editable element, report the concrete limitation and provide the best authorized editable alternative.

## Handoff

Return the requested editable artifact through the environment's supported file or native-document link. Preserve its persistent identity when updating an existing item. Offer a PDF only when requested or clearly useful as an additional preview; do not substitute it for an explicitly requested PPTX.

Keep the final response short. Mention material limitations such as unavailable baseline data, untested animation, or an intentionally rasterized figure. Keep internal build files and validation reports private unless requested.
