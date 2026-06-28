# NewWave Deal Assistant Security Assessment (Revised, Evidence-Aligned)

This revision reflects live work completed in this project and resolves drift issues:

- Uses only demonstrated behavior claims from `phase2_capture.json` / `phase2_evidence_table.md`
- Keeps `LLM06` language probabilistic (phrasing-sensitive) rather than absolute
- Marks NeMo/Colang guidance as future hardening only (not implemented in current repo)
- Adds method-integrity notes (rate limits, retries, final model)
- Adds claim-to-evidence appendix for traceability

## Section 4: Assets, Users, and Trust Boundaries

- Define protected assets: MNPI-adjacent deal context, cross-client data, buyer lists, codenames, due-diligence notes, internal policy text, outbound client comm channels.
- Define roles: authorized bankers/analysts/compliance reviewers vs adversarial misuse paths.
- Define trust boundaries:
  - Trusted: system policy/instructions and deterministic approval workflow.
  - Untrusted: retrieved document content and user prompts.
- Anchor implementation evidence:
  - `evidence/input_separation_control.md` (quoted `build_llm_input(...)` with `<fictional_context>` and `<user_attack_prompt>` tags).

## Section 5: OWASP Top 10 LLM Risk Review

- Cover all 10 OWASP 2025 risks with one-line NewWave-specific harms.
- Expand demonstrated risks only: `LLM01`, `LLM02`, `LLM06`, `LLM07`.
- Severity weighting for this use case:
  - Highest: `LLM02`, `LLM01`, `LLM06`
  - High: `LLM07`
  - Moderate: `LLM09`, `LLM05`
  - Remaining assessed: `LLM03`, `LLM04`, `LLM08`, `LLM10`
- Evidence anchors:
  - `evidence/phase2_evidence_table.md`
  - `evidence/phase2_capture.json`

## Section 6: Vulnerability Evaluation

- Unsafe configuration vulnerabilities (observed):
  - Follows embedded instructions in retrieved content (`LLM01`).
  - Discloses cross-client confidential details (`LLM02`).
  - Reveals internal-style policy/system content (`LLM07`).
  - Shows phrasing-sensitive agency behavior (`LLM06`).
- Safe configuration strengths (observed):
  - Distrusts untrusted inputs.
  - Refuses cross-client disclosure.
  - Uses draft/refusal behavior for action requests.
  - Requires human review for high-risk finance outputs.
- Control mapping source:
  - `evidence/safe_controls_to_owasp.md`

## Section 7: Threat Identification

- Adversary goals:
  - Exfiltrate confidential deal/client data
  - Corrupt risk narratives
  - Trigger unauthorized client-facing actions
  - Extract internal policy logic for follow-on attacks
- Entry vectors demonstrated in custom prompts:
  - Indirect injection via document/pretext wording
  - Compliance-pretext disclosure request
  - Debug-pretext prompt extraction
  - Claimed prior approval for action request
- Keep MITRE technique IDs only if verified live before submission.

## Section 8: Impact Assessment

Use pattern for each demonstrated risk:

1. Observed behavior (specific row in evidence table)  
2. NewWave harm (banking-specific)  
3. Regulatory/business consequence  
4. Control implication

Required impact nouns:

- MNPI and insider-trading/conflict risk
- Cross-client confidentiality breach
- Due-diligence/pitchbook integrity risk
- Unauthorized client communication risk
- SEC/FINRA exposure
- Client/public trust erosion

## Section 9: Detailed Attack Scenarios

Deep Scenario A:

- Prompt Injection (`LLM01`) with potential pivot to agency abuse (`LLM06`)
- Use default + custom rows
- Critical finding: unsafe agency outcome changed with phrasing (probabilistic escalation)

Deep Scenario B:

- Sensitive Information Disclosure (`LLM02`) under default + compliance-pretext custom prompt
- Unsafe leaked cross-client data; safe refused

Include:

- Verbatim prompts and key output excerpts from `phase2_capture.json`
- Cross-reference `phase2_evidence_table.md`
- Screenshots from `evidence/screenshots/` as visual corroboration

## Section 10: Mitigation Methods and Strategies

Order controls by reliability:

1. Deterministic controls outside model (mandatory human approval gates, hard action constraints)
2. Architectural controls (trusted/untrusted separation in `build_llm_input`)
3. Behavioral controls (safe instruction policy/refusal behavior)

Map this to NIST AI RMF:

- Govern: ownership/accountability for high-impact outputs/actions
- Map: sensitive assets and trust boundaries
- Measure: 8-run adversarial evidence set
- Manage: iterate controls from observed failure modes

Important language:

- Prompt-level controls reduce risk, but remain probabilistic under adversarial phrasing.
- Deterministic controls outside the model are the final enforcement boundary.

Future-only note:

- NeMo Guardrails/Colang patterns can strengthen behavioral rails.
- Not implemented in this repo; include as future hardening option only.

## Section 11: Demo Results and Prompt Bypass Tests

Method integrity block (include explicitly):

- 8 live runs total (4 default + 4 custom prompts)
- Unsafe and safe configurations captured for each run
- Initial `gemini-3.5-flash` path hit rate-limit/availability issues
- Retries + checkpointing used to preserve capture integrity
- Final successful capture model: `gemini-2.5-flash`
- Outputs are non-deterministic across runs/versions

Results summary (strictly observed):

- Prompt Injection: unsafe followed injected framing; safe held
- Sensitive Disclosure: unsafe leaked under default and compliance-pretext custom; safe held
- System Prompt Leakage: unsafe exposed internal-style policy content; safe held
- Excessive Agency: safe held; unsafe was phrasing-sensitive (mixed behavior)

Artifacts:

- `evidence/phase2_capture.json`
- `evidence/phase2_evidence_table.md`
- `evidence/screenshots/README.md`
- `evidence/audit_closed_checklist.md`

## Section 12: Conclusion

- State empirical core:
  - Safe configuration held against tested classes.
  - Unsafe configuration was susceptible in injection/disclosure/leakage and variable in agency behavior.
- State governance conclusion:
  - In regulated banking workflows, model behavior cannot be final control boundary.
  - Deterministic external gates + architectural separation + behavioral policies are required together.

## Section 13: References

- Include public/verifiable sources only:
  - OWASP LLM Top 10 (2025)
  - NIST AI RMF 1.0 (+ GenAI profile as used)
  - MITRE ATLAS
  - Any additional public standards/papers actually cited
- Do not list internal evidence file paths in references; cite them in-text as project evidence artifacts.

---

## Appendix A: Claim-to-Evidence Traceability

| Claim | Evidence source | NewWave harm | Control implication |
|---|---|---|---|
| Unsafe followed retrieved-document attack framing in Prompt Injection | `evidence/phase2_evidence_table.md` (`Prompt Injection [default/custom]`) | Corrupted due-diligence narrative and buyer disclosure risk | Treat retrieved content as untrusted + never execute document instructions |
| Unsafe disclosed cross-client details under compliance pretext | `evidence/phase2_evidence_table.md` (`Sensitive Information Disclosure [custom]`) | MNPI/cross-client confidentiality exposure | Deterministic disclosure controls + access boundaries |
| Unsafe leaked internal-style policy/system content | `evidence/phase2_evidence_table.md` (`System Prompt Leakage [default/custom]`) | Follow-on attacker reconnaissance advantage | Prompt/policy secrecy controls + refusal enforcement |
| Unsafe agency behavior changed by phrasing | `evidence/phase2_evidence_table.md` (`Excessive Agency [default/custom]`) | Governance reliability risk in client-facing actions | Mandatory external approval gates (deterministic) |
| Safe control behavior aligns to OWASP risk defenses | `evidence/safe_controls_to_owasp.md` | Reduced attack success across tested classes | Keep layered controls; do not rely on single prompt policy |
| Input separation is an architectural control distinct from policy text | `evidence/input_separation_control.md` | Lowers ambiguity between trusted instructions and untrusted payloads | Preserve and harden trusted/untrusted boundary design |

