# Individual Presentation (Unit 11) - source bundle

Paediatric chest X-ray classification: classical ML (HOG + SVM) versus deep learning (ResNet50 transfer learning) with empirical comparison tests, explainability, subgroup analysis and a UML deployment plan. Submission 13 July 2026. This folder is the live bundle of the submission notebook, the rendered deliverables and the per-decision log that support the [Individual Project deep page on the e-portfolio site](https://protode908.github.io/eportfolio-uoe/projects/individual-project/).

## Layout

- `notebook/` - the single submission notebook (Jupyter, .ipynb). This is the executable source of every number, table and figure on the deep page.
- `deliverables/` - the rendered slides (PDF) and the speaker transcript (PDF) that go alongside the notebook for the 20-minute presentation.
- `decisions_log_v13.md` - per-decision log (~20 decisions) tagged Tier A/B/C under the three-tier decision process. Every modelling choice on the deep page resolves back to a numbered entry here.

## Files in this v13 drop

### `notebook/`

- `pneumonia_detection_ml_vs_dl_v13_submission.ipynb` - submission notebook covering EDA, HOG + SVM pipeline, ResNet50 frozen-base transfer learning, two empirical comparison tests (HOG image size, augmentation on/off), occlusion-sensitivity XAI on both models, subgroup analysis, calibration discussion, threshold sweep, deployment architecture.

### `deliverables/`

- `pneumonia_ml_vs_dl_v13_presentation.pdf` - rendered slide deck (28 slides + 3 annex).
- `pneumonia_presentation_transcript_v13.pdf` - 14-page speaker transcript (~20 minutes at 130 wpm).

### Root of this folder

- `decisions_log_v13.md` - the per-decision log (Decision 1 random seed through Decision 22 deployment architecture).
