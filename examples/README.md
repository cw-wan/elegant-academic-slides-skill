# Examples

[Repository home](../README.md) | [Chinese README](../README.zh-CN.md) | [Resources](../docs/resources.md)

Examples are archived by **repository skill release**, then by example name. Each archive keeps the supplied presentation, its design record, and its associated source skill edition together. Full decks stay here; installation ZIPs contain the skill package and selected SVG figures.

| Release | Associated source edition | Example |
| --- | --- | --- |
| [v0.2.0](v0.2.0/README.md) | v2026.11.25.3 | [Language-Guided Time-Series Perception: Solutions and Challenges](v0.2.0/slb-webinar-2026-11-25/README.md), v20, 25 slides, English, PPTX + PDF |

[![Six-slide preview of the SLB seminar](v0.2.0/slb-webinar-2026-11-25/previews/overview-pages-01-06-09-10-14-15.png?v=v20-fd66cf1a4c2c)](v0.2.0/slb-webinar-2026-11-25/README.md)

The [v0.1.0 release](https://github.com/cw-wan/elegant-academic-slides-skill/releases/tag/v0.1.0) predates the first full presentation example; no placeholder example folder is created for it.

## Add an example

Use `examples/<release>/<kebab-case-name>/`. Each example README should record:

- The task, audience, date, and language.
- The associated release and source skill edition, using known provenance.
- Available inputs, source links, and the design record.
- Actual PPTX/PDF outputs and previews rendered from them.
- Supplied prompts or reproduction steps, and checks actually performed.

Use a new version folder when the associated skill release changes. When refreshing an existing presentation, preserve established file paths, record the new source revision and hashes in its manifest, and update the preview page mapping. Git history and published release tags retain earlier snapshots.
