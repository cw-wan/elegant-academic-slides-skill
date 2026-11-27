# Changelog

## Example refresh — 2026-11-27

- Replace the SLB webinar example on `main` with the supplied v19 PPTX and PDF, preserving `SLB-Webinar-261125.pptx` and `SLB-Webinar-261125.pdf` and their existing paths.
- Update the example from 23 to 25 slides. Track the six showcased topics by title: pages 1, 6, 9, 10, 14, 15 become 1, 7, 10, 11, 16, 17.
- Refresh all six preview images in place and add content-based version parameters to README image URLs to avoid stale caches.
- Update file hashes and structural counts: 25 notes pages, four native tables, three embedded videos, and 25 SVG resources.
- Retain the v10 design record and v0.2.0 release tag as historical records; the skill package is unchanged.

## v0.2.0 — 2026-11-25

### Skill

- Integrate supplied edition `v2026.11.25.3`, including a shorter entry point, a Chinese usage guide, writing and annotation guidance, a sources reference, and six editable SVG examples.
- Preserve the Newsreader / Inter font preference and the separate compatibility-copy workflow.
- Review the skill against the supplied seminar design record and final example. Limit commentable review copies to agreed deliverables, text/signal lanes to relevant multimodal methods, and candidate comparisons to cases illustrating ambiguity.
- Clarify the distinction between measured values, expert annotations, interpreted boundaries, and schematic parameters. The six bundled SVG examples are not the complete figure archive mentioned in the historical design record.
- Add release and source-edition metadata to the skill entry point.

### Examples and documentation

- Archive the 23-slide SLB webinar under [`examples/v0.2.0/slb-webinar-2026-11-25/`](examples/v0.2.0/slb-webinar-2026-11-25/README.md), with the supplied PPTX, PDF, and v10 design record preserved byte-for-byte.
- Add PDF-derived previews, inline galleries in both READMEs, and an example manifest recording versions, file hashes, and preview pages.
- Preserve the design record's external skills and references in a categorized [resource catalog](docs/resources.md).
- Record the supplied PPTX's actual 17 SVG resources alongside the historical design record's count of 18. Embedded video structure was inspected; playback was not tested.
- Distribute the reviewed installation ZIP, the untouched input archive, and checksums as separate release assets.

## v0.1.0 — 2026-11-24

- Publish the original academic slides skill, English and Chinese documentation, an examples index, and a reproducible ZIP packaging script.
