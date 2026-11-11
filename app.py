import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

st.set_page_config(page_title="Real Estate Buyer Intelligence", page_icon="🏘️", layout="wide")
st.title("Machine Learning-Based Buyer Segmentation & Investment Profiling")
st.caption("Interactive demonstration dashboard for the Real Estate Market Intelligence project.")
st.warning("DATA DISCLAIMER: The bundled dataset is synthetic practice data, not actual Parcl customer records. Findings are illustrative and must not be presented as company facts.")

uploaded = st.file_uploader("Upload an authorized buyer dataset (CSV) to replace the synthetic sample", type=["csv"])
try:
    df = pd.read_csv(uploaded) if uploaded is not None else pd.read_csv("data/real_estate_buyer_synthetic_dataset.csv")
except Exception as e:
    st.error(f"Could not load data: {e}")
    st.stop()

required = ["client_id","client_type","gender","country","region","date_of_birth","acquisition_purpose","loan_applied","referral_channel","satisfaction_score"]
missing = [c for c in required if c not in df.columns]
if missing:
    st.error("Missing required columns: " + ", ".join(missing))
    st.stop()

raw_count = len(df)
df = df.drop_duplicates().drop_duplicates(subset=["client_id"], keep="first").copy()
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], errors="coerce")
df["age"] = ((pd.Timestamp.today().normalize()-df["date_of_birth"]).dt.days/365.25).round()
df.loc[~df["age"].between(18,100), "age"] = np.nan
df["satisfaction_score"] = pd.to_numeric(df["satisfaction_score"], errors="coerce")

with st.sidebar:
    st.header("User Controls")
    countries = sorted(df["country"].dropna().astype(str).unique())
    selected_countries = st.multiselect("Country", countries, default=countries)
    regions = sorted(df.loc[df["country"].isin(selected_countries),"region"].dropna().astype(str).unique())
    selected_regions = st.multiselect("Region", regions, default=regions)
    purposes = sorted(df["acquisition_purpose"].dropna().astype(str).unique())
    selected_purposes = st.multiselect("Acquisition purpose", purposes, default=purposes)
    types = sorted(df["client_type"].dropna().astype(str).unique())
    selected_types = st.multiselect("Client type", types, default=types)

f = df[df["country"].isin(selected_countries) & df["region"].isin(selected_regions) &
       df["acquisition_purpose"].isin(selected_purposes) & df["client_type"].isin(selected_types)].copy()
if f.empty:
    st.info("No buyers match the selected filters.")
    st.stop()

m1,m2,m3,m4 = st.columns(4)
m1.metric("Buyers", f"{len(f):,}")
m2.metric("Investment purpose", f"{(f.acquisition_purpose=='Investment').mean():.1%}")
m3.metric("Loan applied", f"{(f.loan_applied=='Yes').mean():.1%}")
m4.metric("Average satisfaction", f"{f.satisfaction_score.mean():.2f}/5" if f.satisfaction_score.notna().any() else "N/A")

t1,t2,t3,t4 = st.tabs(["Buyer Segmentation Overview","Investor Behaviour","Geographic Buyer Analysis","Segment Insights"])
with t1:
    st.subheader("Buyer segmentation overview")
    a,b=st.columns(2)
    with a:
        fig,ax=plt.subplots()
        f["acquisition_purpose"].value_counts().plot(kind="bar",ax=ax)
        ax.set_title("Buyers by acquisition purpose"); ax.set_ylabel("Buyers")
        st.pyplot(fig)
    with b:
        fig,ax=plt.subplots()
        f["client_type"].value_counts().plot(kind="bar",ax=ax)
        ax.set_title("Individual vs Corporate buyers"); ax.set_ylabel("Buyers")
        st.pyplot(fig)
with t2:
    st.subheader("Investor behaviour")
    a,b=st.columns(2)
    with a:
        loan=pd.crosstab(f["acquisition_purpose"],f["loan_applied"],normalize="index")*100
        st.write("Loan application pattern (%)"); st.dataframe(loan.round(1),use_container_width=True)
    with b:
        sat=f.groupby("acquisition_purpose")["satisfaction_score"].mean().dropna()
        fig,ax=plt.subplots()
        sat.plot(kind="bar",ax=ax); ax.set_ylim(0,5)
        ax.set_title("Average satisfaction by purpose"); st.pyplot(fig)
with t3:
    st.subheader("Geographic buyer analysis")
    geo=f.groupby(["country","region"],dropna=False).size().reset_index(name="buyers").sort_values("buyers",ascending=False)
    st.dataframe(geo,use_container_width=True)
    fig,ax=plt.subplots()
    f["country"].value_counts().plot(kind="bar",ax=ax)
    ax.set_title("Buyer distribution by country"); ax.set_ylabel("Buyers")
    plt.xticks(rotation=35,ha="right"); st.pyplot(fig)
with t4:
    st.subheader("K-Means and hierarchical clustering")
    st.caption("Clusters are exploratory statistical groupings. They are not verified buyer identities or fixed market segments.")
    cat=["client_type","gender","country","region","acquisition_purpose","loan_applied","referral_channel"]
    num=["age","satisfaction_score"]
    if len(f)<4:
        st.info("Select at least four buyers for clustering.")
    else:
        max_k=min(7,len(f)-1)
        k=st.slider("Number of clusters",2,max_k,min(2,max_k))
        prep=ColumnTransformer([
            ("num",Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler())]),num),
            ("cat",Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),("encode",OneHotEncoder(handle_unknown="ignore"))]),cat)
        ])
        X=prep.fit_transform(f[cat+num])
        labels=KMeans(n_clusters=k,random_state=42,n_init=10).fit_predict(X)
        f["cluster"]=labels.astype(str)
        score=silhouette_score(X,labels) if len(set(labels))>1 else np.nan
        st.metric("K-Means silhouette score",f"{score:.3f}" if pd.notna(score) else "N/A")
        profile=f.groupby("cluster").agg(
            buyers=("client_id","count"), median_age=("age","median"),
            investment_share=("acquisition_purpose",lambda s:(s=="Investment").mean()),
            loan_share=("loan_applied",lambda s:(s=="Yes").mean()),
            avg_satisfaction=("satisfaction_score","mean"),
            corporate_share=("client_type",lambda s:(s=="Corporate").mean())
        ).round(3)
        st.write("Buyer profiles by K-Means cluster"); st.dataframe(profile,use_container_width=True)
        if len(f)>k:
            hlabels=AgglomerativeClustering(n_clusters=k).fit_predict(X.toarray() if hasattr(X,"toarray") else X)
            hs=silhouette_score(X,hlabels)
            st.metric("Hierarchical clustering silhouette score",f"{hs:.3f}")
        st.download_button("Download buyer cluster results",f.to_csv(index=False).encode(), "buyer_cluster_results.csv","text/csv")

st.subheader("Buyer data preview")
st.dataframe(f.head(100),use_container_width=True)
st.download_button("Download cleaned buyer data",f.to_csv(index=False).encode(),"cleaned_buyer_data.csv","text/csv")
