---
layout: page
title: Feedback
permalink: /feedback/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Feedback</p>
<p>Feedback from tutor and peers gathered throughout the module.</p>
</div>

## Team Project (Unit 6) - tutor grade and feedback

Group baseline mark: 69 / 100. My individual mark after the peer-review weighting: 100 / 100 (Distinction). Tutor feedback received 16 June 2026.

**What the tutor flagged as strong (extract):**

> "clear and generally accurate understanding of the business problem, dataset, and relevant machine-learning approaches, with appropriate use of regression and clustering framed within CRISP-DM"
>
> "focused business question and maintain alignment with pricing and segmentation objectives"
>
> "correctly identify the distinction between association and causality"

**What the tutor flagged as improvement options (extract):**

> "limited depth in articulating why specific modelling choices are optimal"
>
> "lacks sophistication and justification relative to alternative techniques (e.g. regularisation, non-linear models)"
>
> "clustering outcome largely reproduces room-type segmentation, which is already a dominant input feature"
>
> "evaluation of model performance is superficial, with no substantive discussion of overfitting, generalisability, or diagnostic checks beyond R² and RMSE"
>
> "business recommendations extend beyond the evidence presented"

**What I take from this:** five points stand out - go deeper, do alternative analysis and comparison, rationalise the alternatives, document the design-choice rationale, and base conclusions on evidence. I am already applying them in the Individual Presentation:

- **Rationalisation of alternatives.** I did not just accept the default 0.5 decision threshold. The right cutoff is a clinical-value choice that no number alone can settle, so I named it openly as a limit.
- **Design-choice rationale.** I justified the architecture choice upfront in the decision log, anchored in the small-dataset literature. When I later caught a fine-tuning issue with the Keras flag I had to learn as a setting, I reframed the numbers openly rather than burying it.
- **Base conclusions on evidence.** Every recommendation ties back to a specific result. The headline metric did not tell the whole story, so I built a generalisation check and a subgroup view that surface weaknesses the headline hides.

## Tutor escalations through the module

I needed to escalate multiple concerns and questions on how to proceed and on group dynamics, alongside more content and technical stuff related to how deep technically we should go in the report and how to manage certain requirements like client segmentation, which the dataset attributes made not possible. In all escalations I always provided my view and the proposal on how to address and proceed, in all cases the tutor to different degrees confirmed my view and my way to proceed generally. This was useful many times to provide guidance to the group both at technical and content level, and also at group dynamics level.

## Peer feedback (extracts)

Three messages of peer feedback received during the Team Project lifecycle, anonymised on the public site. All originals held in the working record.

### 8 May 2026 - kick-off debrief reply

The day after the kick-off (7 May), I sent a debrief email with outcomes, the Drive folder, next steps and a request for feedback, especially from members who could not attend. A peer replied within minutes:

> Dear Ariel
>
> Thank you for the detailed update and for organizing everything clearly. Much appreciated!

### 11 May 2026 - EDA workstream kick-off

A peer acknowledged the project setup and confirmed start on the EDA and data-cleaning workstream:

> Hi Ariel,
>
> Thank you very much for setting everything up and for all the preparation work; it's really appreciated.
>
> I'll start working on the EDA and Data Cleaning stream today, and I'll keep you updated on progress as I go along.
>
> Thanks again!

### 4 June 2026 - final report finalisation

Towards the end of the project, a peer acknowledged the final report finalisation:

> Hi Ariel,
>
> Thank you for all the effort you've put into finalizing the report. The improvements are greatly appreciated, and the final version looks ready for submission from my side.
>
> Thanks again for your hard work and coordination.

## Individual Presentation (Unit 11) - tutor grade and feedback

*TBD.*

## What I take from this feedback

Set role clarity and escalation routes from week 1, treat prolonged silence as project risk way earlier, and use formal escalation rather than absorbing it internally. Keep the documentation cadence (kick-off debrief email with outcomes, Drive folder, next steps, explicit feedback request) - it costs little and shows up in the evidence trail when contributions need to be assessed.
