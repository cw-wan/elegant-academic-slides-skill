# Scientific Content

## Establish one authoritative source

Record the selected paper version and the provenance of each supplied result set. Check the document itself before relying on remembered numbers, dataset counts, model versions, or appendix tables. A newer result set may be valid but must not silently replace the paper version chosen for the talk.

Create a private evidence map when converting a paper or making substantial content changes:

| Slide purpose | Claim or object | Source location | Context to retain |
| --- | --- | --- | --- |
| Task | Input and output | Task definition or Figure 1 | What is given and predicted |
| Representation | Operators and assumptions | Definition or equation | Applicability and exclusions |
| Evaluation | Comparison values | Table or supplied data | Dataset, model, metric, setting |
| Case | Evidence and prediction | Figure or trace | Channels, intervals, annotations |
| Takeaway | Interpretation | Result plus analysis | Scope and remaining uncertainty |

Do not expose this production table on a slide unless requested. Use it to prevent unsupported compression.

## Explain a research gap concretely

Identify the source paper's actual difficulties. Connect each difficulty to a visible failure mode or requirement. For example, alignment, multichannel composition, and inspectable evidence are useful categories for the SELA task; they are not a mandatory three-part framework for every project.

State inputs and outputs before adding architectural detail. For a proposed pipeline, distinguish supplied inputs from assumptions, optional resources, and future components. Do not introduce a domain schema, database, gold labels, or annotation process that the actual task does not provide.

Keep exact implementation identities where they matter: the actual encoder, reranker, backbone, or classifier can be more informative than a generic “AI module.” Do not guess missing names.

## Handle definitions and theoretical lineage

Present an introduced representation with a complete concrete example. Put the source description beside its structured form so the audience can compare them.

When borrowing a theory, show the relationship at the right level:

- Name the theory correctly and cite an authoritative source.
- Map the paper's operators to the applicable theoretical relations.
- State which assumptions narrow the relationship.
- Mark omitted relations or unsupported cases explicitly.
- Distinguish inspiration, specialization, and mathematical equivalence.

Use a historical portrait or book/paper image only when requested or when it helps orient the audience. Verify identity, source, and reuse conditions. A photograph communicates historical context; it does not substitute for the mapping or a citation.

## Quote faithfully

Use a visibly quoted block for verbatim source text. Preserve the complete wording of the selected example when the user asks for it in full. If the space is insufficient, recompose the slide or divide the material with permission when slide count is fixed; do not silently truncate the example.

Use ellipses only when the omission is intentional, marked, and harmless to the explanation. Label paraphrases as descriptions rather than presenting them as exact quotations. Preserve emphasis that carries semantic information, such as primitive phrases and temporal connectives.

## Separate kinds of evidence

Distinguish:

- A representation that is syntactically valid.
- A representation that preserves the intended meaning.
- A grounding that agrees with the observed evidence.
- A computation that follows the specified operators.
- A final prediction that matches the evaluation target.

Do not describe a successful compiler check as semantic validation. Do not describe an inspectable intermediate structure as proof of faithfulness. Explain what a symbolic engine actually checks and which judgments remain with a learned model or human.

## Write useful takeaways

Derive each takeaway from a result, mechanism, or demonstrated limitation. Prefer a concise answer to “What did we learn?” over a list of module names or a promotional slogan.

Examples of appropriately qualified takeaways:

- An ablation supports the value of structured composition under the reported conditions.
- A case demonstrates where explicit temporal structure helps identify localization errors.
- A parsing benchmark shows that well-formed output and semantic fidelity require separate evaluation.

Do not turn one successful case into a universal guarantee, a confidence score into a calibrated probability, or a performance difference into a causal explanation unsupported by the experiment.

Keep source URLs and full citations in notes or a readable references slide as appropriate. Keep a short visible citation when theoretical attribution, an external photograph, or a direct quotation needs it. Do not pack tiny references into the main reading path.
