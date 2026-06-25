---
layout: page
title: Individual Project (Unit 11)
permalink: /projects/individual-project/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Individual Project (Unit 11)</p>
<p>Paediatric chest X-ray, pneumonia machine learning classification: classical ML (HOG + SVM) against deep learning (ResNet50 transfer learning), with empirical comparison, explainability, subgroup analysis and one example of deployment on Azure.</p>
</div>

## What I did

I built two classifiers on the paediatric chest X-ray dataset and compared them on the same held-out test, the same metrics, the same decision threshold. Classical side: HOG features with an SVM, contrast-equalised input via CLAHE. Deep-learning side: ResNet50 with ImageNet pretrained weights, used as a frozen feature extractor with a small classification head trained on top. Evaluated cost-sensitivity, what is the impact of a missed pneumonia vs a misdiagnosis.

<div class="mk-card-buttons">
  <a href="https://github.com/protode908/eportfolio-uoe/tree/main/code/individual-presentation/" class="mk-button mk-button--primary">Browse the bundle on GitHub</a>
  <a href="/eportfolio-uoe/code/individual-presentation/notebook/MLworkflow_final_v1.0_submission.ipynb" class="mk-button">SUBMISSION NOTEBOOK</a>
  <a href="/eportfolio-uoe/code/individual-presentation/deliverables/presentation_final_v1.0.pdf" class="mk-button">PRESENTATION SLIDES (PDF)</a>
  <a href="/eportfolio-uoe/code/individual-presentation/deliverables/transcript_final_v1.0.pdf" class="mk-button">SPEAKER TRANSCRIPT (PDF)</a>
</div>

## So what I learned

What seemed a clear result then added more complexity and further validation required in the subgroup analysis. Headline results on the held-out test set:

| Metric | SVM | CNN (ResNet50, frozen base) |
|---|---:|---:|
| Test macro-F1 | 0.683 | **0.892** |
| NORMAL recall | 0.36 | **0.82** |
| 5-fold CV macro-F1 | 0.966 | 0.902 |
| CV → test generalisation gap | **28 points** | **1 point** |

The headline metrics looked solid for the CNN and weaker for the SVM. But underneath, the SVM's strong cross-validation score did not transfer to the held-out test, a clear sign of overfitting. The CNN held up way better between CV and test. Then the subgroup analysis flipped the trustworthiness picture: the CNN's pneumonia recall dropped meaningfully when image size or brightness changed, which the headline macro-F1 hides. So macro-averaged metrics paper over operationally important weaknesses. Averages do not describe trustworthiness.

Three lessons learned shaped the work. **The Keras `trainable` flag** was not a bug but a setting I had to learn to use properly after many tries. Until I got it right, the fine-tuning loop did not actually unfreeze the base, so the headline numbers belong to a frozen-base baseline. I caught it late and reframed the numbers rather than burying it. **The CNN outputs saturate above 0.99** on confident pneumonia cases. Modern networks are systematically miscalibrated, and I did not apply temperature scaling. **Threshold choice is not a technical default**: at 0.5 the SVM almost never misses pneumonia but fires 149 false alarms. The CNN at 0.5 sits at 21 misses and 41 false alarms. The right cutoff depends on what a clinician considers acceptable, which is a value question that no number alone can settle.

## What I take with me

- **Recommendation:** ResNet50 as a solid support for the clinician specialist, under conditions: clinician-set threshold on separate validation data with clinical cost input, subgroup and drift monitoring, and out-of-distribution control in place.
- **Defaults from day one.** Save the trained model work products to disk so reruns are reproducible from a single run. Verify fine-tuning end-to-end (count trainable parameters before and after unfreeze, do not trust the flag alone). Make subgroup analysis a non-optional part of the workflow from the start. Add a calibration step once probabilities matter to a downstream decision. Maintain a decision log, tagging each choice by its evidence strength as the project unfolds. Build the bibliography incrementally throughout.
- **Deployment is a process, not an architecture diagram.** Drift monitoring, subgroup performance over time, the model-update lifecycle, controls for out-of-distribution input, and the cost-asymmetry framing (a missed pneumonia is not the same as a false alarm) matter way more than the boxes-and-arrows view of where the model runs. The Azure deployment example walks through one shape of this, but the principles apply regardless of platform.

## Learning Outcomes addressed

- **LO1** (legal, social, ethical and professional issues) - dataset limitations, shortcut-learning concern, threshold-as-clinical-value framing, dual-use awareness.
- **LO2** (datasets, applicability and challenges) - single-site paediatric limitation, subgroup analysis on image size and brightness.
- **LO3** (apply and critically appraise ML techniques) - CNN-against-SVM comparison, generalisation-gap analysis, open disclosure of the fine-tuning issue with the Keras flag I had to learn as a setting, calibration discussion, occlusion-sensitivity XAI as a critical-appraisal tool.
- **LO4** (effective member of a development team) - per-decision documentation discipline that makes individual modelling choices defensible to a tutor, a future team member or a regulator.

## Feedback

*Placeholder - tutor grade and feedback to be added once received.*
