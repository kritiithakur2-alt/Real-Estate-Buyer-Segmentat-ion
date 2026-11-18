# Customer Segmentation & Churn Pattern Analytics in European Banking

**Unified Mentor project | Streamlit + Python + Pandas + Plotly**

## Project objective
Analyse customer churn across France, Germany and Spain, identify higher-risk segments, compare churn across demographic and financial profiles, and communicate findings through an interactive dashboard.

## Deliverables
- `app.py` — interactive Streamlit dashboard
- `eda.py` — reproducible analysis and export of KPI tables
- `RESEARCH_PAPER.md` — research paper draft and methodology
- `EXECUTIVE_SUMMARY.md` — concise stakeholder summary
- `requirements.txt` — Python dependencies

## Dataset
The dashboard defaults to a publicly accessible 10,000-row bank churn practice dataset. It contains the fields required by the brief: CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary and Exited. The dataset is a public practice dataset, not verified internal European Central Bank or commercial bank customer data. Do not describe it as actual bank customer records or as an ECB dataset. Upload an approved CSV in the dashboard to replace the default source.

Dataset reference: https://huggingface.co/datasets/An24/Churn_Modelling  
A mirror used by the default app source: https://github.com/salahudheenayoobi-M/European-Bank-Churn-Analysis

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
On Streamlit Community Cloud, select this repository, set the app file path to:
`European-Bank-Churn-Analytics/app.py`

## Analysis dimensions
- Geography: France, Spain, Germany
- Age groups: <30, 30–45, 46–60, 60+
- Credit score bands: Low, Medium, High
- Tenure: New, Mid-term, Long-term
- Balance: zero-balance vs positive-balance
- Financial profile: balance and estimated salary
- Churn target: Exited (1 = churned, 0 = retained)

## Important limitations
The commonly used churn modelling dataset is a practice dataset. It is not evidence of the performance of any named bank or regulator. Segment comparisons are descriptive and do not establish causation. Demographic characteristics should not be used to justify unfair or discriminatory customer treatment.
