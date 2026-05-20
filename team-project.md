---
layout: page
title: "Team Project: Project Report (Unit 6)"
permalink: /projects/team-project/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Team Project: Project Report</p>
<p>Group D Track 1: classical machine learning regression and clustering on the AB_NYC_2019 Airbnb dataset.</p>
</div>

**Module:** Machine Learning.  
**Group:** D (six members, three actively engaged).  
**Track:** 1 - Classical Machine Learning (Regression and Clustering).  
**Dataset:** AB_NYC_2019 (Dgomonov, 2019).  
**Business question:** *"Can Airbnb identify pricing patterns and listing segments in the NYC market to support hosts with competitive pricing and customise segment-specific guidance?"*

<figure id="evidence-team-kickoff-title" class="mk-fig">
  <a href="/eportfolio-uoe/assets/images/kickoff-deck-slide-01.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
    <img src="/eportfolio-uoe/assets/images/kickoff-deck-slide-01.png" alt="Kickoff deck slide 1 - Group D, Airbnb, Track 1 title">
  </a>
  <figcaption class="evidence-caption">Slide 1 of the kickoff deck: Group D, Airbnb NYC dataset, Track 1 - Classical Machine Learning (Mella, 2026a).</figcaption>
</figure>

The page is organised in three sections: the project itself (the technical artefact), my role and reflection on it, and the team-dynamics story.

## 1. The project itself

Track 1 applied classical machine learning - regression for price prediction and clustering for listing segmentation - to the AB_NYC_2019 Airbnb dataset (Dgomonov, 2019) under a CRISP-DM (Chapman et al., 2000) backbone.

<figure id="evidence-team-crispdm-approach" class="mk-fig">
  <a href="/eportfolio-uoe/assets/images/track1/presentation-slide-8-crispdm-approach.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
    <img src="/eportfolio-uoe/assets/images/track1/presentation-slide-8-crispdm-approach.png" alt="Proposed CRISP-DM-based approach for Group D Track 1, mapped to workstreams and feedback loops">
  </a>
  <figcaption class="evidence-caption">Proposed CRISP-DM-based approach mapped to the five-script pipeline and the team's workstreams, from the 9 May 2026 group meeting deck.</figcaption>
</figure>

The technical work split into a five-stage Python pipeline plus one figure-generation script. `01_data_prep.py` handles cleaning (Tasks 2.1-2.7) and produces the cleaned CSV. `02_data_exploration.py` runs dataset profiling and percentile reports. `03_eda_graphics.py` generates the EDA figures (correlation matrix, distributions, pairwise views). `04_regression.py` runs linear and polynomial regression with `StandardScaler`, reporting R², MAE and RMSE. `05_clustering.py` runs k-means with silhouette and elbow analysis. `figure3_silhouette_v1.3.py` generates the silhouette figure used as Figure 3 of the final report.

The design document brings the pipeline together with explicit phase ownership; the draft report (in flight, target 22-29 May) follows the report-section coverage map that aligns assignment, tutor guidance and PG rubric against the chosen narrative structure (Mella, 2026k).

<div class="mk-card-buttons">
  <a href="https://github.com/protode908/eportfolio-uoe/tree/main/code/team-project/" class="mk-button mk-button--primary">Browse the full Track 1 bundle on GitHub</a>
  <a href="/eportfolio-uoe/code/team-project/source/01_data_prep.py" class="mk-button">01 DATA PREP</a>
  <a href="/eportfolio-uoe/code/team-project/source/02_data_exploration.py" class="mk-button">02 DATA EXPLORATION</a>
  <a href="/eportfolio-uoe/code/team-project/source/03_eda_graphics.py" class="mk-button">03 EDA GRAPHICS</a>
  <a href="/eportfolio-uoe/code/team-project/source/04_regression.py" class="mk-button">04 REGRESSION</a>
  <a href="/eportfolio-uoe/code/team-project/source/05_clustering.py" class="mk-button">05 CLUSTERING</a>
  <a href="/eportfolio-uoe/code/team-project/source/figure3_silhouette_v1.3.py" class="mk-button">SILHOUETTE FIGURE</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_business-question-slide.pdf" class="mk-button">BUSINESS QUESTION</a>
</div>

## 2. My role and reflection

Work was split across the active members of Group D, with roles, workstreams and decisions agreed at the kick-off. I held the **Coordinator** role and contributed across four main workstreams:

| Workstream | What I did | Evidence |
|---|---|---|
| **Coordinator** | Communications, tooling, meetings, asset repository, risk management, decision log (nineteen entries). | Mella, 2026g; 2026r; 2026t |
| **ML workstream responsible** | Practical regression and clustering work through a five-script Python pipeline mapped to CRISP-DM (Chapman et al., 2000). | Mella, 2026l; 2026bp; 2026bq |
| **Written report workstream responsible** | Section structure aligned to the report-section coverage map, demand-mapping reframe mid-project (decision D-017), final integrator from draft to submission. | Mella, 2026k; 2026m; 2026n |
| **EDA and cleaning workstream support** | Five-stage EDA (load and shape -> missing-value triage -> descriptive statistics -> correlation matrix -> distribution and pairwise view), design specification, cleaning script and handover document for the workstream responsible. | Mella, 2026p; 2026q; 2026i |

<div class="mk-fig-pair">
  <figure id="evidence-team-decisions-and-definitions">
    <a href="/eportfolio-uoe/assets/images/track1/meeting-9may-decisions-and-definitions.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
      <img src="/eportfolio-uoe/assets/images/track1/meeting-9may-decisions-and-definitions.png" alt="Decisions and definitions agreed at the 9 May 2026 second team meeting">
    </a>
    <figcaption class="evidence-caption">Decisions and definitions agreed during the 9 May 2026 second team meeting: business question, workstreams and owners, next meeting and asset repository (names redacted).</figcaption>
  </figure>
  <figure id="evidence-team-timeline">
    <a href="/eportfolio-uoe/assets/images/track1/meeting-9may-timeline-task-allocation.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
      <img src="/eportfolio-uoe/assets/images/track1/meeting-9may-timeline-task-allocation.png" alt="Timeline and task allocation defined on 9 May 2026">
    </a>
    <figcaption class="evidence-caption">Timeline and task allocation defined on 9.5.2026: week, task, owner, input and output across W1–W6 (16 May → 8 June) — names redacted.</figcaption>
  </figure>
</div>

<div class="mk-card-buttons">
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_meeting-decisions-and-definitions-redacted.pdf" class="mk-button">DECISIONS AND TIMELINE (9 MAY)</a>
</div>

I designed a three-tier decision process to classify every design decision and kept the row-by-row decisions in a single companion artefact.

<figure id="evidence-team-three-tier-decision-process" class="mk-fig">
  <a href="/eportfolio-uoe/assets/images/team-project/three-tier-decision-process.svg" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
    <img src="/eportfolio-uoe/assets/images/team-project/three-tier-decision-process.svg" alt="UML activity diagram of the three-tier decision process">
  </a>
  <figcaption class="evidence-caption">The three-tier decision process applied row-by-row across cleaning, feature design, regression, clustering and visualisation (Mella, 2026bt).</figcaption>
</figure>

<div class="mk-card-buttons">
  <a href="/eportfolio-uoe/assets/evidence/team-project/three-tier-process-design-decisions.pdf" class="mk-button mk-button--primary">Three-tier process design decisions</a>
</div>

The main thing I would not repeat: I worked around partial attendance for too long before escalating it. A week 2 escalation might have re-engaged absent members faster than the 4 May escalation did.

**Carry into the Individual Presentation:** a short scope-and-limitations check; the three-tier decision process for explaining choices; and dual-metric reporting (R² + scope statement for regression; AUC + confusion matrix for classification). Keep the handover-document pattern when delegating, and escalate earlier when team availability is uneven.

<div class="mk-card-buttons">
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_meeting-summary-email-redacted.pdf" class="mk-button">9 MAY MEETING SUMMARY</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_group-meeting-presentation-12-slides.pdf" class="mk-button">9 MAY DECK</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-10_eda-handover-email-redacted.pdf" class="mk-button">EDA HANDOVER EMAIL</a>
</div>

## 3. Team dynamics

Six members reduced to three actively engaged members. Engagement-based task allocation, grounded in Weick (1976) loose coupling, kept the critical path with the active members while still leaving space for intermittent contribution. Coordination mattered as evidence (Faraj and Sproull, 2000; Cramton, 2001), not only administration. The fault-tolerant team architecture frame matches the loosely-coupled enterprise distributed systems I have architected for two decades commercially.

<figure id="evidence-team-task-allocations" class="mk-fig">
  <a href="/eportfolio-uoe/assets/images/track1/presentation-slide-3-team-status.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
    <img src="/eportfolio-uoe/assets/images/track1/presentation-slide-3-team-status.png" alt="Team status and task allocations slide from Group D Track 1 second team meeting">
  </a>
  <figcaption class="evidence-caption">Team status and task allocations agreed at the second team meeting: workstream ownership and decision-making by the active members (names redacted).</figcaption>
</figure>

The reliability-gradient allocation already in place absorbs late engagement as peripheral reviewer contribution if substantive input arrives, without re-opening the core. The team submitted the kick-off and ran the project to plan on the strength of the active three plus the structural design that anticipated this pattern from week 2.

<div class="mk-card-buttons">
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-16_progress-report-redacted.pdf" class="mk-button">16 MAY PROGRESS REPORT</a>
</div>

## Learning Outcomes addressed

| LO | Primary artefact | Discussed in |
|---|---|---|
| **LO1** - legal, social, ethical and professional issues | Scope-and-limitations statement; correlation-not-causation framing (Mella, 2026n) | #1, #3 |
| **LO2** - dataset applicability and challenges | Six ML design constraints pre-committed (D-011); cleaning rules each Tier-1 anchored (Mella, 2026o, 2026i) | #1 |
| **LO3** - applying and critically appraising ML techniques | Demand-mapping reframe (D-017); three-tier decision process; five-script Python pipeline (Mella, 2026m, 2026j, 2026l, 2026bt) | #2 |
| **LO4** - effective team member in a virtual professional environment | Handover document, design document, decision log, working agreement, progress-report cadence (Mella, 2026i, 2026h, 2026g, 2026bu) | #2, #3 |

## Feedback

*Placeholder - tutor grade and feedback to be added once received.*
