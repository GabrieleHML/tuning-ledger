<h1 align="center">Tuning Ledger</h1>

<p align="center">
  <strong>A permissioned-blockchain system for recording and certifying post-registration vehicle modifications, through an immutable Digital Modified Vehicle Passport (DMVP).</strong><br>
  A full requirements-analysis and business-planning study: from stakeholder modelling to the business plan.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/methodology-GOREM-5A6B7B" alt="GOREM">
  <img src="https://img.shields.io/badge/modelling-BPMN%20%C2%B7%20Use%20Case-4C6B8A" alt="BPMN and Use Case">
  <img src="https://img.shields.io/badge/report-LaTeX-008080?logo=latex&logoColor=white" alt="LaTeX report">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license">
</p>

This is the project for the **Information Systems** course (*Sistemi Informativi*, University of Calabria,
academic year 2025/26, Prof. Domenico Saccà), by Gabriele Hamil and Matteo Stricagnolo. It is a
**requirements-analysis and feasibility study — there is no software implementation**: the deliverables are the
models, the diagrams and the report. The full report, in Italian, is
[`Relazione/main.pdf`](Relazione/main.pdf).

## The idea

A vehicle's modifications after registration (tuning) are today hard to track and trust. **Tuning Ledger**
proposes a **permissioned blockchain** on which dealers, tuning workshops and certification bodies record each
modification into a **DMVP** — a Digital Modified Vehicle Passport bound to the chassis number. Because the
ledger is immutable and the certification authorities are explicit actors, the history of a vehicle becomes
verifiable by buyers, insurers and public authorities.

Security and trust are therefore *design* concerns of the modelled system (immutability, roles of the
certification authorities, data provenance), analysed in the report; this repository contains the analysis and
models, not a running implementation.

## Method and deliverables

The work follows the **GOREM** methodology and runs from context analysis to the economic evaluation. Every
modelling folder contains the `.drawio` sources and an `exports/` subfolder with the exported PNGs.

| Area | Contents | Exports |
| ---- | -------- | ------- |
| `Context Modeling/` | Stakeholder, Softgoal and Softgoal-Dependency diagrams; Business Model Canvas (`.tex`) | `exports/` |
| `Scenario Modeling/` | Role, Goal and Goal-Dependency diagrams | `exports/` |
| `Use Case Modeling/Use Case Diagram/` | Use-case diagrams for the five actors | `exports/` |
| `Use Case Modeling/Process Diagram/` | Processes in BPMN notation | `exports/` |
| `Project Plan/` | Component and deployment architecture, work groups; `dati_project_plan.xlsx` | `export/` |
| `Project Plan/gantt/` | Gantt charts and per-role effort sheets (`.xlsx`) | `gantt_exports/` |
| `Relazione/` | LaTeX sources of the report and the final PDF | — |
| `Presentazione/` | Final presentation (`.pptx`) | — |

## The report

Sources are in [`Relazione/`](Relazione/), one file per chapter under `capitoli/`:

1. Abstract and introduction
2. Context analysis — GOREM context modelling
3. Specific scenario — GOREM modelling, Business Model Canvas
4. Project idea — use cases in GOREM and processes in BPMN
5. SWOT analysis and evaluation of the idea
6. Project plan — architecture, technologies, planning of the two phases
7. Business plan — costs, revenues, break-even point and ROI
8. Conclusions

followed by `bibliografia.tex`. The two external papers cited in the bibliography are **not** redistributed
here; they are referenced by title and author in [`capitoli/bibliografia.tex`](Relazione/capitoli/bibliografia.tex).

## From the exam version to today

The version delivered for the exam is kept under the git tag `exam-2026`. Reworking it as a portfolio project:

- **English README** describing the project, its method and its deliverables.
- **Added an MIT license** for the authors' original work.
- **Removed third-party material.** The two cited academic papers that were bundled under
  `Relazione/riferimenti/` are no longer redistributed; they remain cited in the bibliography.
- **Housekeeping:** a `.editorconfig`, and a `.gitignore` that excludes draw.io backups and LaTeX artefacts.

## License

[MIT](LICENSE) © Gabriele Hamil, Matteo Stricagnolo. The report text, diagrams and models are the authors'
original work; externally cited works belong to their respective authors.
