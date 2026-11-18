"""Reproducible EDA exports for the European Banking Churn project."""
import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/salahudheenayoobi-M/European-Bank-Churn-Analysis/main/European_Bank.csv"
df = pd.read_csv(URL)
df.columns = df.columns.str.strip()
df = df.drop_duplicates().copy()
for col in ["CreditScore","Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary","Exited"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["CreditScore","Geography","Gender","Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary","Exited"])
df["Exited"] = df["Exited"].astype(int)
df["AgeGroup"] = pd.cut(df["Age"], [0,29,45,60,120], labels=["<30","30–45","46–60","60+"])
df["CreditBand"] = pd.cut(df["CreditScore"], [0,580,670,1000], labels=["Low","Medium","High"])
df["TenureGroup"] = pd.cut(df["Tenure"], [-1,2,5,10], labels=["New (0–2)","Mid-term (3–5)","Long-term (6–10)"])
df["BalanceSegment"] = np.where(df["Balance"].eq(0), "Zero balance", "Positive balance")
print("Rows after cleaning:", len(df))
print("Overall churn rate:", round(df["Exited"].mean()*100, 2), "%")
for field in ["Geography","Gender","AgeGroup","CreditBand","TenureGroup","BalanceSegment","NumOfProducts","IsActiveMember"]:
    out = df.groupby(field, observed=False).agg(customers=("Exited","size"), churned=("Exited","sum"), churn_rate=("Exited","mean")).reset_index()
    out["churn_rate_pct"] = (out["churn_rate"]*100).round(2)
    out.to_csv(f"{field.lower()}_churn_summary.csv", index=False)
profile = df.groupby("Exited").agg(customers=("Exited","size"), avg_balance=("Balance","mean"), median_balance=("Balance","median"), avg_salary=("EstimatedSalary","mean"), avg_credit_score=("CreditScore","mean")).reset_index()
profile.to_csv("financial_profile_churned_vs_retained.csv", index=False)
df.to_csv("cleaned_customer_churn.csv", index=False)
