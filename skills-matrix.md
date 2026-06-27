---
layout: page
title: Professional Development
permalink: /skills-matrix/
hide_title: true
---

<div class="section-overview">
<p class="section-overview-title">Professional Development</p>
<p>Self-assessed Skills Matrix across the twelve UoEO skill areas plus six module-specific ML skills, paired with an Action Plan for the rows where I sit at Aware or Trained, plus tutor and peer feedback received during the module.</p>
</div>

Skill levels: **Aware** (basic understanding) · **Trained** (applies independently) · **Proficient** (broad and in-depth, low supervision) · **Expert** (subject-matter expert, leads and trains others).

## Skills Matrix

| Skill area | Level | Evidence |
|---|---|---|
| 1. Commercial Awareness | **Expert** | 20+ years in IT industry leadership; cyberresiliency and cloud portfolio ownership. |
| 2. Time Management | **Proficient** | Track 1 submitted two days ahead of deadline; sustained weekly cadence across 12 units. Individual Presentation submitted on schedule with iterative tracked versions, even after catching 4-5 of my own flaws late in the cycle that forced re-runs. |
| 3. Critical Thinking and Analysis | **Proficient** | Decision log used in Track 1; variable-change probe on every tutorial notebook. In the Individual Presentation I had to learn the Keras `trainable` flag as a setting properly after many tries. Until I got it right, the fine-tuning loop did not actually unfreeze the base, so I reframed the numbers rather than burying it. I also flagged an evidence-chain split between the CNN that produced the headline numbers and the CNN that produced the XAI heatmaps, plus single-seed augmentation variance that flipped sign between two runs. |
| 4. Communication and Literacy | **Proficient** | 1,000-word executive report; CD1 cross-sector synthesis; CD2 discussion thread on LLM ethics and governance; commercial sales and pre-sales background. |
| 5. IT and Digital | **Expert** | IT Architect across enterprise estates; this e-portfolio on Jekyll and GitHub Pages; five-script Python pipeline. |
| 6. Numeracy | **Proficient** | Regression, clustering and metrics across Units 3-11; MBA quantitative methods. |
| 7. Research | **Proficient** | Harvard Cite Them Right across ~140 references; literature-anchored cleaning rules; MBA dissertation. Individual Presentation bibliography built incrementally with peer-reviewed citations for every methodological choice. CD2 thread anchored in peer-reviewed citations on LLM productivity (Noy and Zhang, 2023), reasoning limits (Shojaee et al., 2025), AI ethics (Floridi et al., 2018) and copyright (US Copyright Office, 2025). |
| 8. Interpersonal | **Expert** | Group D Coordinator role; pre-sales and sales leadership; multinational distributed teams. |
| 9. Problem-solving | **Proficient** | 20+ years in technical problem-solving roles; found five issues in my own Individual Presentation work before submission: the Keras `trainable` flag as a setting I had to learn properly (until I got it right, the base stayed frozen during fine-tuning), single-seed augmentation variance that flipped sign between runs, an evidence-chain split between the headline CNN and the XAI CNN, code-narrative drift after a parameter change, and a threshold-without-calibration risk on the clinical decision rule. |
| 10. Ethical Awareness | **Proficient** | Dual-use CNN argument across Units 9 and 10. The Individual Presentation forced ethics to be specific: single-site paediatric data, FN/FP cost asymmetry, brightness drift across subgroups, shortcut-feature risk, and threshold-as-clinical-value framing rather than a technical default. CD2 took ethics into the governance dimension: AI disclosure transparency, intellectual property and copyright, governance gap on LLM adoption as the parallel to CD1's implementation gap. |
| 11. Teamwork and Leadership | **Expert** | Group D Coordinator; engagement-based task allocation; 20+ years leading distributed teams. |
| 12. Critical Reflection | **Proficient** | 1,000-word reflective piece using a structured What/So what/Now what model; 3 W's reflection across 17 activity cards. The Individual Presentation reflection cycle disclosed mistakes openly (the Keras setting I had to learn, GPU non-determinism re-run cost) rather than burying them. CD2 summary post synthesised peer feedback on intellectual contribution and named the governance gap as the cross-cutting parallel to CD1. |
| 13. Classical ML - Regression | **Trained** | Linear, multiple and polynomial regression; Track 1 log-price model. HOG+SVM also acted as the classical comparator baseline against ResNet50 in the Individual Presentation. |
| 14. Classical ML - Clustering and Similarity | **Trained** | Jaccard, K-Means with elbow / silhouette / ARI; Track 1 segmentation. |
| 15. Deep Learning - Perceptron and MLP | **Trained** | Simple perceptron; AND in 6 epochs; 2-3-1 sigmoid XOR by back-propagation. |
| 16. Deep Learning - CNN | **Trained** | CIFAR-10 trained to 77.82% test accuracy; CNN Explainer 4-case study; individual presentation deliverable (Unit 11). For the Individual Presentation I used ResNet50 transfer learning with ImageNet pretrained weights as a frozen feature extractor and a small classification head trained on top, the right default for a small specialised dataset. One thing that stands out is the subgroup analysis: CNN pneumonia recall dropped meaningfully when image size or brightness changed, which the headline metric hides. Softmax saturation on confident pneumonia cases also showed up as a miscalibration concern, so calibration goes into the follow-up list. |
| 17. ML Evaluation and Metrics | **Trained** | Confusion matrix, F1, ROC AUC, MAE / RMSE / R²; parameter-change exercises on AUC and polynomial degree. The Individual Presentation moved me into dual-metric reporting (R² with a scope statement; macro-F1 paired with NORMAL recall) and into a cross-validation versus held-out test generalisation-gap analysis: the SVM's cross-validation score did not transfer to the held-out test, while the CNN held up way better. Subgroup analysis became a standard evaluation tool. |
| 18. Explainability | **Trained** | SHAP-style decomposition on a Matrix-Factorisation prediction; CNN Explainer pipeline walk-through. In the Individual Presentation I applied occlusion-sensitivity XAI on the ResNet50 model as a critical-appraisal tool to surface what the model actually attends to in the lung field, paired with the explicit caveat that linearity assumptions in attribution methods hide interactions. |

## Action Plan (3 to 12 months post-module)

Six development goals targeting the rows where I sit at Aware or Trained, plus selected Proficient rows where I want to push toward Expert.

| Skill area | Goal | Action | Timeline |
|---|---|---|---|
| Deep Learning | Trained -> Proficient | Self-led CNN project; read a foundational deep-learning textbook end-to-end. | 6 months |
| Python production ML | Trained -> Proficient | Deploy a small ML service with CI/CD on a personal project. | 6 months |
| Explainability | Trained -> Proficient | Apply SHAP and Integrated Gradients to one deployed model with a written case-study comparing them. | 6 months |
| Ethical Awareness | Proficient -> Expert | One position paper on dual-use CNN deployment; monthly EU AI Act tracking. | 12 months |
| Research | Proficient -> Expert | One peer-reviewable piece connecting cybersecurity and AI. | 12 months |
| Critical Reflection | Proficient -> Expert | Monthly reflective journal post-MSc; decision-log note written on one significant decision per quarter. | Ongoing |

*Reviewed and committed by Ariel Mella, 17 May 2026 (v1.1). Next review: end of MSc programme.*

## Feedback

Tutor escalations and peer feedback received during the module are consolidated on the [Feedback page](/eportfolio-uoe/feedback/).

