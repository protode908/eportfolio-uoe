---
layout: page
title: Individual Project (Unit 11)
permalink: /projects/individual-project/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Individual Project (Unit 11)</p>
<p>Paediatric chest X-ray classification: classical ML (HOG + SVM) versus deep learning (ResNet50 transfer learning), with empirical comparison tests, explainability, subgroup analysis and a UML deployment plan. Submission 13 July 2026.</p>
</div>

## Project summary

I built two competing classifiers on the Kermany et al. (2018) paediatric chest X-ray dataset and compared them on the same held-out test set and the same metrics. Classical side: Histogram of Oriented Gradients (Dalal and Triggs, 2005) with a Support Vector Machine, using contrast-equalised input via CLAHE. Deep-learning side: ResNet50 (He et al., 2016) with ImageNet pretrained weights, using the frozen base as a feature extractor and training a small classification head on top. The question was not just which model scored higher. It was which model I could defend as a clinical triage candidate.

The EDA stage followed the same 5-script pipeline shape I used in the Team Project: load and check the shape, deal with missing values, run descriptive statistics, review class balance, and check distributions before drawing conclusions. The image-data version was shorter than the tabular version, but the discipline was the same. I named the assumption before using it.

## The three-tier decision process, extended

This project had many degrees of freedom: image size, HOG parameters, augmentation, validation, thresholds, classification head, training schedule, XAI method and deployment design. Not every choice had a task-specific prescription. I extended the three-tier decision process from the Team Project (Mella, 2026j) and applied it here to roughly 20 modelling decisions. Each decision was tagged:

- **Tier A** - direct peer-reviewed evidence (e.g. Kohavi, 1995 for k-fold; Dalal and Triggs, 2005 for HOG parameters; Yosinski et al., 2014 for transfer-learning principles).
- **Tier B** - established practice or domain precedent (e.g. CheXNet conventions; framework defaults from scikit-learn and Keras documentation).
- **Tier C** - project evidence from a small ablation (e.g. HOG image size selected on validation via a 64 / 128 / 192 comparison).

The point was traceability. Each important choice was evidence-backed, precedent-backed or tested. The full per-decision log lives in the decisions log linked below.

## Headline results and recommendation

| Metric | SVM | CNN (ResNet50, frozen base) |
|---|---:|---:|
| Test macro-F1 | 0.6846 | **0.7721** |
| Test accuracy | 0.7580 | 0.8141 |
| ROC-AUC | 0.9236 | **0.9612** |
| 5-fold CV macro-F1 | 0.9609 | 0.8933 (sd 0.0309) |
| CV-test generalisation gap | 27 points | **12 points** |
| NORMAL recall | 0.37 | **0.51** |

The CNN generalised about twice as cleanly as the SVM: 12-point versus 27-point CV-test gap. My recommendation is to treat ResNet50 as the triage candidate, with the SVM kept as a transparent shadow comparator for disagreement-flagging, but only under five non-negotiable safeguards:

1. The operating threshold is a clinician decision, not a hard-coded constant.
2. The region-importance heatmap is available on demand for clinician review of borderline cases. Lighter Grad-CAM is the planned routine UI surface; occlusion is roughly 100x more expensive per explanation.
3. Weekly subgroup monitoring across brightness, disease subtype and equipment vendor.
4. Explicit out-of-distribution rejection of adult X-rays.
5. Human-in-the-loop always.

Without all five, this stays a prototype.

## Lessons learned

This is the section that matters most to me. I am critical of myself here. I took on more than I should have for one person on a hard deadline. I picked a clinical-imaging problem with no prior experience in image processing or chest-X-ray imaging, then added transfer learning, two empirical comparison tests, XAI on both models, subgroup analysis, calibration discussion and a UML deployment architecture diagram. The scope matched the assignment, but it stretched the work too far. The cost showed.

**Numbers drift between runs.** The SVM macro-F1 moves 0.6480 -> 0.6846 across versions; the CNN macro-F1 moves 0.8750 -> 0.7721. Both are valid expressions of the same architecture and pipeline within the stochastic envelope reported by Bouthillier et al. (2019), but I had moments where I mixed numbers from different runs in the deck and the transcript. Reviewer rounds caught at least four of those. I need a verification standard that checks both symbolic forms (`C=10`, `0.9575`) and the verbal forms a spoken transcript uses ("C equals ten", "point nine five seven five") before I can trust cross-asset consistency.

| # | Issue | Evidence | Learning | Future action |
|---|---|---|---|---|
| 1 | My Keras unfreeze loop is inert. Keras propagates the `trainable` flag from the parent model down to nested children and overrides what looks like an explicit setting on the child. | What actually runs is a frozen-base feature extractor. | Read the framework documentation before trusting a code pattern. Document and postpone, do not paper over. | Reframe the model honestly as a frozen-base baseline (Cheplygina et al., 2019) and queue the real two-phase fine-tune as future work. |
| 2 | I do not preserve the v8 weights as a file. | When reviewer feedback prompts a swap of one XAI tool, the only path forward is a re-train, which splits the evidence chain. | Trained-model weights are first-class versioned outputs, not session state. Saving the model is methodology, not housekeeping. | Disciplined model-weight persistence going forward (Decision 21 in the decisions log). |
| 3 | My augmentation comparison runs single-seed. | The result is illustrative, not evidential. | A single-seed comparison test is not enough for stochastic CNN training. | Multi-seed averaging on stochastic comparisons. |
| 4 | Both occlusion sensitivity cases on the CNN saturate at P = 1.0000. | The heatmap dynamic range collapses to roughly two-thousandths of a probability point. The pattern, model attention on shoulder and edge regions rather than the lung field, is consistent with the shortcut-learning concern in Zech et al. (2018). | Saturated softmax limits what XAI can prove. The saturated baseline means I treat it as a warning signal for richer XAI, not as conclusive evidence. | Treat as motivation for richer XAI rather than conclusive evidence; add LIME on the SVM and Grad-CAM on the CNN as next steps. |
| 5 | I came into this project without prior experience in image processing or chest-X-ray imaging. | Without that learning, choices such as HOG resize size, CLAHE preprocessing, HOG cell parameters, augmentation policy, subgroup splits and the ethics framing would have been too arbitrary. | Domain knowledge is part of methodology. Tier C in the three-tier decision process exists for this exact situation: project evidence from a small test, used carefully by someone still learning the domain. | Invest learning time in two domain layers before design choices: image-processing basics (pixels, resolution, what HOG features capture) and chest-X-ray basics (what the target condition can look like radiographically, what artefacts can create shortcut-learning risk, which subpopulations the dataset under-represents). |

What the three-tier decision process gave me through all of this was traceability. Every decision still had a Tier A/B/C tag and a citation, even when the value turned out wrong or the implementation needed correction. That is what let me re-frame honestly rather than hide the mistake.

## What I would do differently next

- **Scope smaller.** Cover fewer arcs done deeper. The next ML-heavy piece picks one main comparison and goes deeper on validation, calibration and subgroup analysis rather than spreading across two empirical tests, two XAI methods and a deployment diagram in the same submission.
- **Persist model weights from day one.** Every result file carries the hash of the model weights it was produced from; a reviewer-driven swap of a downstream tool does not force a re-train.
- **Multi-seed averaging on stochastic comparisons.** A single-seed augmentation test is illustrative, not evidential.
- **Read the framework documentation in full** before I trust a code pattern, especially where propagation rules (Keras `trainable`, scikit pipeline `fit_transform`) override what looks like an explicit setting.

## Deliverables

The submission notebook, rendered slides, speaker transcript and full per-decision log:

<div class="mk-card-buttons">
  <a href="https://github.com/protode908/eportfolio-uoe/tree/main/code/individual-presentation/" class="mk-button mk-button--primary">Browse the full Individual Presentation bundle on GitHub</a>
  <a href="/eportfolio-uoe/code/individual-presentation/notebook/pneumonia_detection_ml_vs_dl_v13_submission.ipynb" class="mk-button">SUBMISSION NOTEBOOK</a>
  <a href="/eportfolio-uoe/code/individual-presentation/deliverables/pneumonia_ml_vs_dl_v13_presentation.pdf" class="mk-button">PRESENTATION SLIDES (PDF)</a>
  <a href="/eportfolio-uoe/code/individual-presentation/deliverables/pneumonia_presentation_transcript_v13.pdf" class="mk-button">SPEAKER TRANSCRIPT (PDF)</a>
  <a href="/eportfolio-uoe/code/individual-presentation/decisions_log_v13.md" class="mk-button">DECISIONS LOG (V13)</a>
</div>

## Learning Outcomes addressed

- **LO1** (legal, social, ethical and professional issues) - dataset limitations, shortcut-learning concern, deployment safeguards, dual-use framing.
- **LO2** (datasets, applicability and challenges) - Kermany et al. (2018) dataset, single-site limitation, subgroup analysis.
- **LO3** (apply and critically appraise ML techniques) - CNN-versus-SVM comparison, generalisation-gap analysis, empirical comparison tests, and XAI as a critical-appraisal tool.
- **LO4** (effective member of a development team) - the three-tier decision process is the documentation-led artefact that makes individual modelling choices defensible to a tutor, a future team member or a regulator.

## References

Inline references throughout this page resolve in the consolidated [References page](/eportfolio-uoe/references/). Key anchors: Kermany et al. (2018), Dalal and Triggs (2005), He et al. (2016), Yosinski et al. (2014), Cheplygina et al. (2019), Kohavi (1995), Zech et al. (2018), Bouthillier et al. (2019).
