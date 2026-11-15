# Final Verified Project Report

**Machine Learning-Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence**  
**Project context:** Unified Mentor / Parcl project brief

> **Data disclaimer:** The supplied dataset is synthetic practice data, not actual Parcl customer data. All findings are illustrative and must not be represented as company findings.

## Abstract
This project demonstrates a reproducible workflow for exploring real-estate buyer profiles using buyer type, geography, acquisition purpose, financing indicator, referral channel, age and satisfaction. It covers data quality checks, cleaning, age feature engineering, categorical encoding, numerical scaling, K-Means clustering, hierarchical clustering and an interactive Streamlit dashboard.

## 1. Problem statement and objectives
The project explores buyer groupings and patterns in investment motivation, geography, financing and satisfaction. Objectives are to inspect and clean buyer records; derive age; prepare categorical and numeric features; evaluate candidate K-Means cluster counts; compare exploratory groupings; summarize profiles; and present findings through a Streamlit dashboard.

## 2. Dataset and preparation
The original CSV contains 604 rows and 10 columns. Four exact duplicate rows were identified. After removing exact duplicates, 600 rows remained. Six rows with missing region were excluded to align the analysis set, leaving 594 rows and 594 unique client IDs. Age was derived using 11 November 2026 as the reference date. Remaining missing model features are imputed in the preprocessing pipeline.

## 3. Methodology
Categorical variables were imputed using the most frequent value and one-hot encoded. Numerical variables were median-imputed and standardized. Client ID was excluded from model features. K-Means candidates from k=2 through k=7 were evaluated using inertia and silhouette score. Agglomerative hierarchical clustering was also executed with the selected number of clusters.

## 4. Results (synthetic practice data)
- Original rows: 604
- Exact duplicate rows removed: 4
- Rows after deduplication: 600
- Records with missing region excluded: 6
- Final analysis records: 594
- Selected K-Means k: 2
- Best tested silhouette score: 0.112616

The low silhouette score indicates weak separation in the feature space. The resulting groups should be treated as exploratory profiles rather than strongly distinct natural market segments.

| K-Means cluster | Buyers | Mean satisfaction |
|---|---:|---:|
| 0 | 208 | 2.79 / 5 |
| 1 | 386 | 4.33 / 5 |

Investment purpose: 330 buyers, mean satisfaction 3.720/5. Personal use: 264 buyers, mean satisfaction 3.873/5. These are descriptive differences and do not establish causes.

## 5. Dashboard
The Streamlit application provides buyer segmentation overview, investor behaviour, geographic buyer analysis, segment insights and a data preview. It displays a synthetic-data disclaimer.

## 6. Recommendations
Treat clusters as hypotheses for further investigation, not fixed customer labels. Review investment purpose, financing and satisfaction patterns on authorized, representative data before changing business decisions. Investigate lower satisfaction through direct feedback; clustering alone cannot identify causes.

## 7. Limitations and ethical considerations
The dataset is synthetic and does not represent actual Parcl customers or company performance. Available features do not include property prices, income, budgets, transaction values or realized returns. The best tested silhouette score is low, so cluster separation is weak. Clustering is exploratory and does not establish causation. Demographic attributes must be handled responsibly and must not justify unfair or discriminatory treatment.

## 8. Conclusion
The project demonstrates a data preparation, clustering and dashboard workflow on 594 synthetic records. K-Means selected k=2 among the tested candidates, but the low silhouette score means the profiles should be interpreted cautiously. The workflow can be rerun on authorized representative data to produce business-relevant findings.
