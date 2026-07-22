# Optimized RFP-Response Workflow — Engine Selection by Stage

**Source:** synthesized from the Airport Eye eval (`eval/airport-eye/scorecard.md`) and the BAC cross-case eval (`eval/bac/scorecard.md`), which compared the monolithic `rfp-analysis-and-response` skill (Track A) against the multi-stage pipeline (Track B: collateral-analyzer → requirements-mapper → section-drafter → empathy-reviewer → proposal-assembler) on compliance, grounding, and holistic quality across two domains (DIAL airside AI video-analytics; BAC airside GSE analytics). n=2 — directional, not statistical.

**Core finding that drives this workflow:** the two approaches are *different stages, not substitutes*. Track A is the better **drafting engine** (higher grounding, zero fabrication, faster). Track B's individual stages are the better **analysis, tracing, and gating** tools (coverage matrix, RTM, honest gap surfacing, tone review, parity gate). The optimal workflow is **hybrid**: Track A's drafting engine fed by Track B's analysis outputs, with Track B's gate skills around it.

**Updated after the BAC cross-case run (`eval/bac/scorecard.md`, n=2):** two Airport Eye findings did *not* generalise, and they change the workflow below:
- Track A's **polish / holistic-quality win is not reliable across domains.** Airport Eye had A 4.6 > B 4.2; BAC reversed to B 3.8 > A 3.5. When the RFP's hardest requirements align with thin collateral (BAC's FR17/FR20 camera-AI), Track A's assert-conformance-from-collateral strategy reads as overstatement. So tone/polish (stage 5) must run on **both** tracks, and the drafter (stage 4) must declare rather than assert where evidence is thin.
- **Over-claiming is engine-universal, not Track-A-specific.** Track B also over-claimed on BAC (NF19 resolution times). No single scorer caught both engines' over-claims — only the combination of compliance gate + claim-audit + holistic judge did. So the gate (stage 6) and claim-audit (stage 7) are **mandatory for both tracks**, not a Track-B-derived safety net.

---

## Track A — `rfp-analysis-and-response` (monolithic skill)

### Strengths (eval evidence)
- **Submission-ready polish** — holistic quality 4.6/5; clean register, no internal scaffolding, graceful gap-handling that reads well to evaluators.
- **High grounding, zero fabrication** — post-hoc claim audit: 0.872 grounding ratio, 0.000 hallucination (0/86). Uses explicit placeholder discipline ("to be confirmed") instead of inventing content.
- **Excellent numeric parity** — all 28 AI-agent SLA cells match BRD §3.5.4 at 1.0×; correctly adopts stricter BRD values (≤10-min incident response over RFP's ≤1 hr; TLS 1.3 over register's TLS 1.2+). No carve-out weakening or status-word over-claims.
- **Fast** — one skill invocation vs five stages; lower orchestration overhead and fewer failure points.
- **Strong raw compliance** — 57.1% pass rate on the 189-requirement gold set; 0.75 on its own extraction.

### Weaknesses (eval evidence)
- **Silent undeclared shortfalls** — the validator caught it silently dropping Phase-1 deliverables (10 cm contours, 3D mesh, ISO 19115 metadata) and whole scope areas (Land & Space, Environmental/CAQM, landside spot levels, 10-layer GIS). *This is the exact failure mode the enhanced compliance-validator was built to catch.* A lone user running only this skill may never notice.
- **No traceability artifacts** — produces no coverage matrix, no RTM. Harder to audit *why* a requirement was judged met.
- **Misses granular register requirements** — 9 register-tier numeric values left unlocated (Ambiguous) because it doesn't systematically walk the requirements register.
- **Compliance step is a snapshot, not a gate** — its internal Step 7 is high-level and strategic; it explicitly defers to the enhanced compliance-validator for anything with measurable thresholds, but nothing enforces that handoff.
- **Grounding not self-verifiable** — no evidence markers, so grounding can only be checked by a separate post-hoc audit, not during review.

---

## Track B — full pipeline (5 skills)

### Strengths (eval evidence)
- **Best audit trail / traceability** — 135-row coverage matrix (Grounded/Assertable/Gap per requirement) + 135-row RTM. Every requirement mapped to evidence or an explicit gap.
- **Most thorough requirement extraction** — 135 reqs vs Track A's 108; the gold inventory (189) shows how much either approach can miss without a dedicated mapping stage.
- **Honest gap surfacing** — 70 declared Partials vs Track A's 51; explicit `[GAP]` markers; refused to fabricate team bios, case studies, or pricing. No silent omissions except one (10 cm contours).
- **Self-reported evidence markers** — `[GROUNDED]`/`[ASSERTION]`/`[GAP]` make grounding visible inline without a separate audit.
- **Multi-stage checkpoints** — empathy-reviewer catches tone, compliance-validator catches parity, each stage's output structures the next.
- **Surfaces source conflicts** — procurement-mechanism contradiction (competitive RFP vs negotiated CR), TLS 1.3 vs 1.2, stale Singapore-hosting claim in old collateral — conflicts Track A smoothed over.

### Weaknesses (eval evidence)
- **Lower polish** — holistic 4.2/5; reads as "needs one more integration pass"; internal marker/requirement-ID leakage into prose; repeated gap-flagging across volumes.
- **Lower grounding ratio** — 0.695 vs 0.872 (partly marker granularity vs claim-counting, but partly real: more assertions).
- **Grounding is self-attested** — `[GROUNDED: source]` asserts a source link but the pipeline does not independently verify it; a false claim placed under a GROUNDED marker would pass internal review. Fabrication not caught without an external audit.
- **More blocking issues on gold** — 28 vs 21, partly from being more honest/thorough, partly a real content gap (the Operational Digital Twin functional layer G-121..G-132 was left unfilled rather than asserted at high level).
- **Heavy / fragile** — 5+ skill invocations, many agent-hours, more orchestration failure points (the eval hit several stream timeouts and a session-limit interruption).
- **Honesty reads as incompleteness** — empty Team volume and placeholder case studies can look worse to an evaluator than Track A's high-level coverage, even when the high-level coverage is the less truthful of the two.
- **Tone fixes not integrated** — empathy-reviewer annotates but the assembler strips annotations without applying rewrites; 19 unresolved review notes carried forward.

---

## Optimized workflow — best engine per stage

```
                ┌─────────────────────────────────────────────────────┐
                │  STAGE              BEST ENGINE                      │
                ├─────────────────────────────────────────────────────┤
  raw docs  →   │  1. Ingest          doc2md  (only tool that reads     │
                │                            raw docx/pdf/xlsx)        │
                ├─────────────────────────────────────────────────────┤
                │  2. Collateral      collateral-analyzer              │
                │     analysis         → brief.md + gap-report.md      │
                │                     (Track A has no equivalent)      │
                ├─────────────────────────────────────────────────────┤
                │  3. Requirement     requirements-mapper              │
                │     mapping          → coverage-matrix.md            │
                │                     (Track A's Step 7 is only a      │
                │                      snapshot; this is the real map) │
                ├─────────────────────────────────────────────────────┤
                │  4. DRAFTING        rfp-analysis-and-response        │
                │    ★ hybrid ★        (drafting mode)                 │
                │                     — fed brief.md + coverage-      │
                │                       matrix.md from stages 2-3     │
                │                     — instructed to use [GROUNDED]/  │
                │                       [ASSERTION]/[GAP] markers     │
                │                       (borrowed from section-drafter)│
                │                     — DECLARATION RULE (BAC): where  │
                │                       coverage = Gap or Assertable, │
                │                       do NOT assert Pass; declare   │
                │                       the gap or commit a delivery   │
                │                       roadmap with acceptance       │
                │                       criteria. Never assert con-   │
                │                       formance from collateral that  │
                │                       only *describes* capability.   │
                │                     WHY: Track A's prose engine has │
                │                     zero fabrication + high ground-  │
                │                     ing (0.87→0.94) across 2 cases. │
                │                     Track B's inputs stop the       │
                │                     silent-shortfall failure. The │
                │                     declaration rule stops the BAC  │
                │                     over-claim failure.             │
                ├─────────────────────────────────────────────────────┤
                │  5. Tone/voice      empathy-reviewer  (framing &    │
                │                       client-voice calibration)      │
                │                     + stop-slop  (sentence-level   │
                │                       AI tells: throat-clearing,     │
                │                       binary contrasts, em dashes,   │
                │                       false agency, vague           │
                │                       declaratives)                │
                │                     — run BOTH; they complement not │
                │                       overlap. Apply rewrites, don't │
                │                       just annotate. stop-slop scores │
                │                       narrative prose 1–10 on        │
                │                       Directness/Rhythm/Trust/        │
                │                       Authenticity/Density; revise   │
                │                       any section <35/50. RFP        │
                │                       carve-out: neither applies to   │
                │                       compliance tables, SLA/KPI     │
                │                       specs, deviation registers,    │
                │                       mandatory forms, or            │
                │                       deliverable/assumption lists. │
                │                     — (BAC) run on BOTH tracks'     │
                │                       output. Polish is NOT a       │
                │                       reliable Track-A advantage:  │
                │                       Airport Eye A 4.6 > B 4.2 but  │
                │                       BAC reversed to B 3.8 > A 3.5. │
                ├─────────────────────────────────────────────────────┤
                │  6. Compliance      compliance-validator (enhanced   │
                │     GATE  ⟲          12-step) — LOOP until no        │
                │                     blocking issues                  │
                │                     (the parity gate neither Track   │
                │                      A's Step 7 nor a single pass    │
                │                      replaces)                       │
                │                     — (BAC) MANDATORY FOR BOTH       │
                │                       TRACKS, not just a Track-B    │
                │                       safety net. Track B over-      │
                │                       claimed NF19 resolution times  │
                │                       on BAC; only the gate caught it.│
                │                     — CAPABILITY-VS-COMMITMENT CHECK │
                │                       (new, BAC): for every req the  │
                │                       draft marks Pass, require      │
                │                       either (a) a source that       │
                │                       commits to delivery (not just  │
                │                       describes capability) or       │
                │                       (b) a declared roadmap with    │
                │                       acceptance criteria. Closes    │
                │                       the sourced-but-weak-          │
                │                       conformance blind spot.        │
                ├─────────────────────────────────────────────────────┤
                │  7. Verification    claim-audit (post-hoc) — catches  │
                │     (periodic)       fabrication AND over-claims that │
                │                     self-attested markers / face-     │
                │                     value compliance miss. MANDATORY  │
                │                     FOR BOTH TRACKS (BAC: caught     │
                │                     Track B's SLA over-claim).       │
                ├─────────────────────────────────────────────────────┤
                │  8. Hand-polish     doc-coauthoring                   │
                │     (optional)       — cover letter, exec summary,   │
                │                       any section needing a live     │
                │                       collaborative loop + reader-   │
                │                       test with a fresh Claude       │
                ├─────────────────────────────────────────────────────┤
                │  9. Assemble        proposal-assembler                │
                │                     (terminal: enforces order,       │
                │                      strips markers, pre-flight       │
                │                      checklist, refuses if blocking) │
                └─────────────────────────────────────────────────────┘
```

### Why this hybrid (the one non-obvious move)

Stage 4 is the crux. The two-case eval showed:
- Track A's **drafting engine** has zero fabrication and high grounding across both cases (0.872 Airport Eye, 0.94 BAC). On Airport Eye it also won polish/holistic (4.6 vs 4.2); on BAC it **lost** holistic (3.5 vs 3.8) by asserting conformance from thin collateral.
- Track A's **weaknesses are input discipline** — without a coverage matrix it silently drops requirements (Airport Eye), *and* declaration discipline — with a coverage matrix it can still over-assert Pass where evidence is thin (BAC).

So: run Track B's analysis stages (2-3) to build the brief and coverage matrix, then hand those to Track A's drafter as constrained inputs, require it to use section-drafter's `[GROUNDED]`/`[ASSERTION]`/`[GAP]` marker discipline, **and enforce the declaration rule**: where the coverage matrix says Gap or Assertable, declare the gap or commit a roadmap with acceptance criteria — never assert Pass from capability-describing collateral. You get Track A's prose + grounding *with* Track B's "no silent shortfalls" property *and* protection against the BAC over-claim failure. Keep `section-drafter` available as a fallback if you specifically need per-file section outputs or the drafter refuses the marker discipline under Track A's prompt.

### Note on stop-slop (post-Airport-Eye addition; exercised on BAC)

`stop-slop` (https://github.com/hardikpandya/stop-slop) was integrated as the stage-5 sentence-level tone engine *after* the Airport Eye eval ran, so the Airport Eye scores in this document (holistic 4.6/4.2) do **not** reflect it. It is installed as a project skill (`.claude/skills/stop-slop/`) and wired into the project-local `rfp-analysis-and-response` (`.claude/skills/rfp-analysis-and-response/`) as both the tone standard and a mandatory `<35/50 = revise` tone gate on narrative prose — with an RFP carve-out so it never strips compliance tables, SLA/KPI specs, deviation registers, mandatory forms, or deliverable/assumption lists.

**BAC exercised it:** Track A ran the tone gate on all 10 narrative sections (cleared 39–42/50); Track B's stage-5 revised 2 sections below threshold (03: 30→38, 08: 29→38). Track A scored 5/5 on polish — so stop-slop works as a prose lever — yet Track A still lost holistic on BAC (3.5 vs 3.8) because the loss was on **grounding/honesty, not prose**. Lesson: stop-slop fixes slop, it does not fix over-claiming. The declaration rule (stage 4) and the capability-vs-commitment check (stage 6) are what address the BAC failure; stop-slop is orthogonal.

### What this workflow fixes vs either track alone
- **vs Track A alone:** adds the coverage matrix (stops silent dropped requirements, Airport Eye), the RTM (traceability), the empathy+stop-slop pass (tone — and on BAC this pass is what closed Track A's polish gap, though it still lost holistic on honesty), a real parity gate (not a snapshot), and the declaration rule (stops the BAC over-assert-from-thin-collateral failure).
- **vs Track B alone:** swaps the weaker section-drafter prose for Track A's stronger drafting engine, and ensures tone fixes are *applied* not just annotated.
- **Both gain:** a mandatory periodic post-hoc claim-audit (stage 7) + the capability-vs-commitment check (stage 6) to catch over-claims that neither self-attested markers nor face-value compliance can. The BAC case proved this is needed for **both** tracks: Track A over-claimed FR17/FR20/NF19; Track B over-claimed NF19 resolution times. No single scorer caught both.

### When to skip the hybrid and use a single track
- **Track A alone** is fine for: fast bid-strategy outlines, early-stage drafts, low-stakes RFIs, or any case where the BRD has *no measurable numeric thresholds* AND the RFP's hardest requirements are well-evidenced in collateral (the silent-shortfall AND over-claim risks are lowest there). **Do not use Track A alone when the RFP's core differentiators sit where collateral is thin** — that is exactly the BAC over-claim failure mode.
- **Track B alone** is preferable when: the submission is high-stakes, the buyer requires a compliance matrix/RTM as a deliverable, auditability matters more than polish (regulated/public-sector procurements), or the RFP's hardest requirements align with thin collateral (BAC shape) — Track B's declare-don't-assert discipline is safer there even though its raw gold-score looks worse.

### Cross-case evidence base (n=2)
| Axis | Airport Eye | BAC | Generalises? |
|---|---|---|---|
| Track A zero fabrication | 0/86 | 0/116 | **Yes** |
| Track A higher grounding | 0.872 vs 0.695 | 0.94 vs 0.580 | **Yes** |
| Track A higher holistic/polish | A 4.6 > B 4.2 | **B 3.8 > A 3.5** | **No — reversed** |
| Track B better coverage | 135 vs 108 reqs | 188 vs 59 reqs | **Yes** |
| Track B honest gap surfacing | all marked | 31 Fail + 124 [GAP] | **Yes** |
| Compliance near-tie | 57.1% vs 47.6% | 78.8% vs 34.6% (artifact) | **No — but BAC gap is a scoring artifact; real blocking 4 vs 2 is close** |
| Over-claim is Track-A-only | (untested) | Track B over-claimed too | **New: over-claim is engine-universal** |

### Open hardening (from the scorecards) that would change this recommendation
- **#4 blind repeated judging (highest priority):** would tell us if the BAC holistic reversal (A 4.6→3.5, B 4.2→3.8) is judge variance or real. If judge variance, Track A's polish advantage may still hold and stage-5-on-both-tracks is less critical.
- **#2 fabrication-injection:** inject fabricated claims into each track's draft; see if markers/claim-audit/validator catch them. Decides whether stage 7 is catching fabrication/over-claim or just measuring it.
- **#3 more cases (EAC / RCA / Dial b2b):** two more cases would make "polish advantage doesn't generalise" a pattern (n=3) rather than a single reversal, and test whether the over-claim failure is BAC-specific or universal.