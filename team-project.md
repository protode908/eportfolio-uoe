---
layout: page
title: "Team Project: Project Report (Unit 6)"
permalink: /projects/team-project/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Team Project: Project Report</p>
<p>Group D, Track 1: classical ML regression and clustering applied to the AB_NYC_2019 Airbnb dataset, to answer the business question and provide a tangible business outcome. Overall methodology CRISP-DM. Work products: typical project management such as presentations, critical path, work breakdown structure, etc., multiple Python scripts and notebooks for EDA and ML workstream, including graph generation. Final deliverable word report submitted.</p>
</div>

**Business question:** *"Can Airbnb identify pricing patterns and listing segments in the NYC market to support hosts with competitive pricing and customise segment-specific guidance?"*

<figure id="evidence-team-kickoff-title" class="mk-fig">
  <a href="/eportfolio-uoe/assets/images/kickoff-deck-slide-01.png" target="_blank" rel="noopener" aria-label="Open full-size image in new tab">
    <img src="/eportfolio-uoe/assets/images/kickoff-deck-slide-01.png" alt="Kickoff deck slide 1 - Group D, Airbnb, Track 1 title">
  </a>
  <figcaption class="evidence-caption">Kickoff deck slide 1: Group D, Airbnb NYC, Track 1 classical machine learning.</figcaption>
</figure>

## What I did

The ask was classical ML for price prediction and customer segmentation on the Airbnb NYC 2019 dataset, but the dataset had partial price data and no real client data, so the price work applied workarounds on the available features and the customer segmentation used room type as a proxy. I held the coordinator role and as individual contributor owned the ML and report deliverable workstreams, with support to the EDA and cleaning workstream. The technical work was a five-stage Python pipeline: cleaning, normalisation, standardisation so thus regression and clustering can work with the data, creating temporal tables to accommodate certain type of data for calculations, cleaning, etc. Three of six members were actively engaged across the six weeks.

<div class="mk-card-buttons">
  <a href="https://github.com/protode908/eportfolio-uoe/tree/main/code/team-project/" class="mk-button mk-button--primary">Browse the full Track 1 bundle on GitHub</a>
  <a href="/eportfolio-uoe/code/team-project/deliverables/groupD_track1_final_report_v1.0.pdf" class="mk-button">FINAL REPORT (PDF)</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-22_ml-results-and-design-internal-redacted.pdf" class="mk-button">ML RESULTS AND DESIGN</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_business-question-slide.pdf" class="mk-button">BUSINESS QUESTION</a>
</div>

## So what I learned

The three K-means segments mapped almost one-to-one to room type (private rooms 45%, entire homes 53%, shared rooms 2%). That was expected because room type was both a clustering input and the strongest observed price signal. So the segments work as guidance for hosts comparing against same-type peers, not as a definitive customer typology. For the business question, this supports type-aware pricing benchmarks plus segment-aware guidance. There were some discussions and difficult choices to make around the assignment requirements (price and client) as the data for both was incomplete and in the case of clients directly inexistent. So the approach was rather applying workarounds that ended up on a non clean feature selection and so on. I wonder if for real work in real life the answer would not be: get me a better dataset. The methodological lesson the tutor feedback also pointed at stands out: when an input feature dominates the clustering output, the analytical value of the segmentation drops. That was an obvious choice that should have popped up earlier in critical thinking, looking in retrospect.

On the team side: accommodation effort (1:1 catch-up calls, asynchronous task options, multi-channel sharing) did not translate into contribution. Inclusivity is the right first response, but it has to be balanced with protecting the active contributors. When accommodation does not yield follow-up, the right next step is early formal escalation, not more internal absorption. The team submitted on the strength of the active three, plus the structural design that anticipated this pattern from week 2.

<div class="mk-card-buttons">
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-09_meeting-decisions-and-definitions-redacted.pdf" class="mk-button">9 MAY DECISIONS</a>
  <a href="/eportfolio-uoe/assets/evidence/unit-6/2026-05-16_progress-report-redacted.pdf" class="mk-button">16 MAY PROGRESS REPORT</a>
</div>

## What I take with me

Into the Individual Presentation: scope-and-limits up front, dual-metric reporting (R² with scope statement, AUC plus confusion matrix), and the handover-document pattern when delegating. Into future group work: set role clarity and escalation routes from week 1, treat prolonged silence as project risk way earlier, use the formal escalation route rather than absorbing the situation inside the group. I also take with me the dual-role frame, coordinator and hands-on contributor in parallel, as a deliberate choice.

## Learning Outcomes addressed

| LO | How it was evidenced |
|---|---|
| **LO1** - legal, social, ethical and professional issues | Scope-and-limitations statement, correlation-not-causation framing. |
| **LO2** - dataset applicability and challenges | Six ML design constraints pre-committed, cleaning rules anchored to peer-reviewed sources. |
| **LO3** - applying and critically appraising ML techniques | Demand-mapping reframe (D-017), decision log, five-script Python pipeline. |
| **LO4** - effective team member in a virtual professional environment | Handover document, design document, decision log, working agreement, progress-report cadence. |

## Feedback

Group baseline mark: 69 / 100. Individual mark: 100 / 100 (Distinction). Tutor feedback received 16 June 2026.

Full tutor feedback, the 5 May tutor escalation conversation and peer feedback received during the module are consolidated on the [Feedback page](/eportfolio-uoe/feedback/).
