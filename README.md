# Real Estate Buyer Intelligence

**Project:** Machine Learning-Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence

This repository contains a Streamlit dashboard, an executed Jupyter notebook, the supplied buyer dataset, analysis outputs and project reports.

## Data disclaimer
The supplied dataset is **synthetic practice data**. It is not actual Parcl customer data and the results must not be represented as company findings.

## Repository contents
- `app.py` — Streamlit interactive dashboard
- `real_estate_buyer_synthetic_dataset.csv` — source synthetic dataset (604 rows)
- `Real_Estate_Buyer_Segmentation.ipynb` — executed, reproducible analysis notebook
- `FINAL_VERIFIED_REPORT.md` — canonical report aligned to verified analysis
- `Final_Real_Estate_Buyer_Segmentation_Report.pdf` — refreshed PDF report aligned to verified analysis
- `Final_Real_Estate_Buyer_Segmentation_Report.docx` — editable report copy retained in the repository
- `kmeans_cluster_evaluation.csv`, `kmeans_cluster_profiles.csv`, `geographic_buyer_distribution.csv`, `acquisition_purpose_summary.csv` — verified analysis summaries
- `requirements.txt` — Python dependencies

## Verified analysis snapshot
The analysis removes 4 exact duplicate rows (604 → 600), then excludes 6 records with missing region (600 → 594 unique buyers). K-Means selected k=2 from tested values 2–7; silhouette score = **0.112616**, indicating weak cluster separation.

| Cluster | Buyers | Mean satisfaction |
|---|---:|---:|
| 0 | 208 | 2.79 / 5 |
| 1 | 386 | 4.33 / 5 |

Acquisition purpose: Investment 330 buyers (mean satisfaction 3.720/5); Personal use 264 buyers (3.873/5). Treat these as exploratory descriptive patterns only.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Open `Real_Estate_Buyer_Segmentation.ipynb` in Jupyter or Google Colab and run cells from top to bottom with the CSV in the working directory.

## Interpretation and limitations
The silhouette score is low, so the two groups are not strongly separated. The dataset is synthetic and lacks actual property prices, budgets, income and realized returns. Do not use the clusters as fixed customer labels or as a basis for discriminatory decisions. Validate the workflow using authorized, representative data before business use.

## Deployment and submission
The dashboard deployment URL and required project-explanation / internship-feedback video links must be added separately once confirmed. This repository alone does not mean the internship submission form has been submitted.
