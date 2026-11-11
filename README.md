REAL ESTATE BUYER SEGMENTATION — PROJECT PACKAGE

PROJECT TITLE
Machine Learning-Based Buyer Segmentation and Investment Profiling for Real Estate Market Intelligence

PACKAGE CONTENTS
- app.py: Streamlit dashboard with buyer overview, investor behaviour, geographic analysis, K-Means and hierarchical clustering.
- data/real_estate_buyer_synthetic_dataset.csv: synthetic practice dataset (604 source rows).
- notebooks/Real_Estate_Buyer_Segmentation.ipynb: reproducible analysis notebook.
- reports/Final_Real_Estate_Buyer_Segmentation_Report.pdf and .docx: updated report.
- reports/Research_Paper_Draft_Original.docx: original editable draft for reference.
- outputs/: cleaned data, cluster profiles, evaluation, geography and purpose summaries.
- requirements.txt: Python dependencies.

IMPORTANT DATA LIMITATION
The bundled dataset is synthetic practice data, not actual Parcl customer data. The report and dashboard disclose this. Do not claim synthetic results are Parcl/company findings. If an authorized company dataset is available, replace the CSV, rerun the notebook and dashboard, and update the report.

RUN DASHBOARD
1. Install Python.
2. In this folder run: pip install -r requirements.txt
3. Run: streamlit run app.py

GOOGLE COLAB
Open notebooks/Real_Estate_Buyer_Segmentation.ipynb in Google Colab. The notebook reads the CSV from ../data when run in a matching folder structure; if uploading files individually, change the read_csv path to the uploaded CSV filename.

VERIFIED COMPUTATION SUMMARY
Raw rows: 604
Exact duplicate rows removed: 4
Duplicate client IDs removed after exact-row deduplication: 0
Clean unique clients: 600
Selected K-Means k: 2
Best tested K-Means silhouette: 0.112
Hierarchical silhouette at selected k: 0.078

This ZIP is a project source-and-report package. GitHub repository creation, Streamlit deployment, and the two required video links must be completed separately.
