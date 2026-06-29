# Scope and Limitations

This is an applied control demonstration, not a research result. The claims are bounded by how it was run, and the boundary is stated here, not left for a reviewer to find.

## Single configuration

Every capture uses one app, one model (`gemini-2.5-flash`), and one provider. The findings illustrate the risk classes. They are not statistical and do not generalize to other models or providers without re-running.

## Non-determinism is shown, not characterized

Output varies run to run. The LLM09 runs produced two different fabricated multiples, recorded as evidence of the behavior, not measured across a distribution. Each archived row is a single representative run.

## Author-constructed configurations

The comparison establishes that the safe instruction set contains these specific prompts where the unsafe set does not. It does not establish the safe configuration as a validated defense against an adaptive attacker. It is a demonstrated control pattern, not a hardened product.

## Severity

Severity is reasoned, not scored against a calibrated standard.

## What holds

What the lab does establish is narrower and holds. On a real model, with verbatim evidence, prompt-level controls reduce these risks but stay probabilistic, and deterministic enforcement outside the model is required as the final boundary for regulated workflows. That conclusion rests on the captures, not the framing.
