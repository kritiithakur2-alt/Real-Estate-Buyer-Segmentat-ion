import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="European Banking | Churn Intelligence", page_icon="🏦", layout="wide")
st.title("Customer Segmentation & Churn Pattern Analytics")
st.caption("European Banking | France • Germany • Spain")

DATA_URL = "https://raw.githubusercontent.com/salahudheenayoobi-M/European-Bank-Churn-Analysis/main/European_Bank.csv"

@st.cache_data(show_spinner="Loading and validating the banking dataset…")
def load_data(uploaded_file=None):
    if uploaded_file is not None:
        raw = pd.read_csv(uploaded_file)
    else:
        raw = pd.read_csv(DATA_URL)
    raw.columns = [str(c).strip() for c in raw.columns]
    required = ["CreditScore","Geography","Gender","Age","Tenure","Balance","NumOfProducts",
                "HasCrCard","IsActiveMember","EstimatedSalary","Exited"]
    missing = [c for c in required if c not in raw.columns]
    if missing:
        raise ValueError("Dataset is missing required columns: " + ", ".join(missing))
    df = raw.copy()
    for c in ["CreditScore","Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary","Exited"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df = df.drop_duplicates().copy()
    df = df.dropna(subset=required)
    df = df[df["Exited"].isin([0,1])]
    df["Exited"] = df["Exited"].astype(int)
    df["AgeGroup"] = pd.cut(df["Age"], bins=[0,29,45,60,120], labels=["<30","30–45","46–60","60+"], right=True)
    df["CreditBand"] = pd.cut(df["CreditScore"], bins=[0,580,670,1000], labels=["Low","Medium","High"])
    df["TenureGroup"] = pd.cut(df["Tenure"], bins=[-1,2,5,10], labels=["New (0–2)","Mid-term (3–5)","Long-term (6–10)"])
    df["BalanceSegment"] = np.where(df["Balance"].fillna(0).eq(0), "Zero balance", "Positive balance")
    df["CustomerValue"] = np.where((df["Balance"] >= df["Balance"].median()) & (df["EstimatedSalary"] >= df["EstimatedSalary"].median()), "Higher financial profile", "Other financial profile")
    return df

with st.sidebar:
    st.header("Data & filters")
    uploaded = st.file_uploader("Upload your approved CSV (optional)", type=["csv"])
    try:
        data = load_data(uploaded)
    except Exception as exc:
        st.error(f"Dataset could not be loaded: {exc}")
        st.stop()
    countries = sorted(data["Geography"].dropna().unique().tolist())
    geo = st.multiselect("Geography", countries, default=countries)
    ages = sorted(data["AgeGroup"].dropna().astype(str).unique().tolist())
    age = st.multiselect("Age group", ages, default=ages)
    credits = sorted(data["CreditBand"].dropna().astype(str).unique().tolist())
    credit = st.multiselect("Credit score band", credits, default=credits)
    tenures = sorted(data["TenureGroup"].dropna().astype(str).unique().tolist())
    tenure = st.multiselect("Tenure group", tenures, default=tenures)
    active = st.multiselect("Activity status", ["Active","Inactive"], default=["Active","Inactive"])

filtered = data[
    data["Geography"].isin(geo) &
    data["AgeGroup"].astype(str).isin(age) &
    data["CreditBand"].astype(str).isin(credit) &
    data["TenureGroup"].astype(str).isin(tenure) &
    data["IsActiveMember"].map({1:"Active",0:"Inactive"}).isin(active)
].copy()
if filtered.empty:
    st.warning("No records match these filters. Please broaden your selections.")
    st.stop()

total = len(filtered)
churned = int(filtered["Exited"].sum())
rate = churned / total if total else 0
high_value = filtered[filtered["CustomerValue"] == "Higher financial profile"]
high_rate = high_value["Exited"].mean() if len(high_value) else 0

k1,k2,k3,k4 = st.columns(4)
k1.metric("Customers analysed", f"{total:,}")
k2.metric("Churned customers", f"{churned:,}")
k3.metric("Overall churn rate", f"{rate:.1%}")
k4.metric("Higher-profile churn rate", f"{high_rate:.1%}" if len(high_value) else "N/A")

st.divider()
tab1,tab2,tab3,tab4 = st.tabs(["Churn overview","Customer segments","Financial profile","Data quality"])
with tab1:
    c1,c2 = st.columns(2)
    geo_rate = filtered.groupby("Geography", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c1.plotly_chart(px.bar(geo_rate,x="Geography",y="Churn rate (%)",color="Geography",title="Churn rate by geography",text_auto=".1f"),use_container_width=True)
    age_rate = filtered.groupby("AgeGroup", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c2.plotly_chart(px.bar(age_rate,x="AgeGroup",y="Churn rate (%)",title="Churn rate by age group",text_auto=".1f"),use_container_width=True)
    c3,c4 = st.columns(2)
    gender_rate = filtered.groupby("Gender", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c3.plotly_chart(px.bar(gender_rate,x="Gender",y="Churn rate (%)",title="Churn rate by gender",text_auto=".1f"),use_container_width=True)
    tenure_rate = filtered.groupby("TenureGroup", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c4.plotly_chart(px.bar(tenure_rate,x="TenureGroup",y="Churn rate (%)",title="Churn rate by tenure",text_auto=".1f"),use_container_width=True)
with tab2:
    c1,c2 = st.columns(2)
    credit_rate = filtered.groupby("CreditBand", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c1.plotly_chart(px.bar(credit_rate,x="CreditBand",y="Churn rate (%)",title="Churn by credit score band",text_auto=".1f"),use_container_width=True)
    balance_rate = filtered.groupby("BalanceSegment", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    c2.plotly_chart(px.bar(balance_rate,x="BalanceSegment",y="Churn rate (%)",title="Churn by balance segment",text_auto=".1f"),use_container_width=True)
    product_rate = filtered.groupby("NumOfProducts", observed=False)["Exited"].mean().mul(100).reset_index(name="Churn rate (%)")
    st.plotly_chart(px.bar(product_rate,x="NumOfProducts",y="Churn rate (%)",title="Churn by number of products",text_auto=".1f"),use_container_width=True)
with tab3:
    c1,c2 = st.columns(2)
    c1.plotly_chart(px.box(filtered,x="Exited",y="Balance",color="Exited",title="Account balance: retained vs churned"),use_container_width=True)
    c2.plotly_chart(px.box(filtered,x="Exited",y="EstimatedSalary",color="Exited",title="Estimated salary: retained vs churned"),use_container_width=True)
    profile = filtered.groupby("Exited").agg(customers=("Exited","size"),avg_balance=("Balance","mean"),median_balance=("Balance","median"),avg_salary=("EstimatedSalary","mean"),avg_credit_score=("CreditScore","mean")).reset_index()
    profile["Status"] = profile["Exited"].map({0:"Retained",1:"Churned"})
    st.dataframe(profile.drop(columns="Exited").round(2),use_container_width=True,hide_index=True)
with tab4:
    st.subheader("Dataset validation")
    quality = pd.DataFrame({"Metric":["Rows loaded after cleaning","Duplicate rows remaining","Missing values remaining","Unique geographies","Invalid churn labels"],"Value":[len(data),int(data.duplicated().sum()),int(data.isna().sum().sum()),int(data["Geography"].nunique()),int((~data["Exited"].isin([0,1])).sum())]})
    st.dataframe(quality,use_container_width=True,hide_index=True)
    st.write("Columns used in analysis")
    st.code(", ".join(data.columns.astype(str)))
    st.download_button("Download filtered customer records",filtered.to_csv(index=False).encode("utf-8"),"filtered_customer_churn.csv","text/csv")

st.divider()
st.subheader("Management interpretation")
st.write("Use the filters to isolate customer groups and compare churn rates. A higher segment churn rate indicates an association in this dataset; it does not prove that the segment attribute caused churn. Prioritise follow-up analysis, customer feedback and controlled retention tests before changing policy.")
st.caption("Data note: the default public practice dataset is a 10,000-row bank churn dataset covering France, Germany and Spain. Replace it with organisation-approved data before presenting findings as institutional results.")
