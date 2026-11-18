# Customer Segmentation & Churn Pattern Analytics in European Banking

## Abstract
Customer churn can reduce customer lifetime value, increase replacement and acquisition costs, and create uncertainty in recurring banking relationships. This project applies descriptive analytics to a public practice dataset of bank customers in France, Germany and Spain. It measures overall churn and compares churn across geography, age, gender, credit-score bands, tenure, product holdings, account balances and estimated salary. An interactive Streamlit dashboard makes the comparisons filterable for exploratory review.

**Dataset integrity note:** The default dataset is a public practice dataset and is not verified internal data from a European bank, the European Central Bank, or a government body. All results must be described as illustrative dataset findings, not institutional performance.

## 1. Introduction
Banks need to understand not only how many customers leave, but also how churn is distributed across customer groups and financial profiles. Aggregate churn rates can conceal meaningful differences between regions, age groups, tenure bands and product relationships. Segmentation-driven analysis can help frame retention hypotheses and prioritise further investigation.

## 2. Problem statement
The project addresses four analytical questions:
1. Which customer groups show comparatively higher churn?
2. How does churn vary by geography, age, gender, credit score and tenure?
3. What financial characteristics distinguish churned and retained customers?
4. Are higher-balance and higher-salary customer profiles exposed to different churn patterns?

## 3. Objectives
- Measure overall churn rate.
- Compare churn distribution across geography and demographic segments.
- Examine tenure, credit score, balance and product-holding patterns.
- Compare financial profiles of churned and retained customers.
- Present the analysis in an interactive dashboard with filters and downloadable data.

## 4. Dataset and variables
The default public dataset contains 10,000 customer records and the following analytical fields: CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary and Exited. The target variable Exited is binary: 1 indicates churn and 0 indicates retention. Identifier and surname fields are not used as analytical predictors.

## 5. Research methodology
The study uses a quantitative, descriptive and exploratory design. The CSV is loaded into Pandas, column names are normalised, exact duplicate rows are removed, analytical columns are converted to numeric types, and records with missing values in required analysis fields are excluded from the dashboard calculations. The churn label is validated as binary.

Derived segments are created as follows:
- Age: <30, 30–45, 46–60 and 60+.
- Credit score: Low (≤580), Medium (581–670) and High (>670).
- Tenure: New (0–2 years), Mid-term (3–5 years) and Long-term (6–10 years).
- Balance: zero balance and positive balance.

For each segment, churn rate is calculated as churned customers divided by all customers in that segment. Financial comparisons include mean and median balance, estimated salary and average credit score for retained and churned groups. Filters allow users to compare a selected subset of the data.

## 6. Key performance indicators
- Overall churn rate = total Exited=1 / total valid customers.
- Segment churn rate = churned customers in segment / all customers in segment.
- Churned customer count = number of records with Exited=1.
- Higher financial profile churn rate = churn rate among customers whose balance and estimated salary are both at or above the filtered dataset medians.

The dashboard calculates these indicators from the selected data at runtime; figures should be copied into the final interpretation only after the dashboard has been run and checked.

## 7. Results and interpretation
The dashboard presents churn rates by geography, age group, gender, tenure, credit-score band, balance segment and number of products. It also compares balance and estimated salary distributions between churned and retained customers. No fixed numerical result is stated in this report because the dashboard recalculates results dynamically when filters or an approved dataset are changed.

A higher observed churn rate in a segment is an association, not proof that geography, age, gender, income or another attribute caused customers to leave. Small segments should be interpreted with their customer counts, not percentages alone.

## 8. Recommendations
1. Prioritise investigation of segments with both elevated churn rates and meaningful customer counts.
2. Review service interactions, complaints and customer feedback before attributing churn to a demographic or financial characteristic.
3. Examine engagement and product usage patterns to identify service friction and opportunities to improve customer experience.
4. Test retention interventions with controlled, measurable pilots and monitor subsequent churn.
5. Refresh the analysis periodically using governed, representative and authorised data.

## 9. Limitations and ethical considerations
The default data is a public practice dataset and may not represent current banking customers or the portfolio of any named institution. Estimated salary is not necessarily verified income. Segment analysis is descriptive and cannot establish causation. Churn patterns may be affected by unobserved factors such as service quality, pricing, complaints, life events and competitor offers. Demographic information must be handled under applicable privacy and fairness requirements and must not be used to justify discriminatory treatment.

## 10. Conclusion
The project provides a reproducible workflow for measuring churn and comparing customer segments across geography, demographics, tenure and financial characteristics. The Streamlit dashboard supports interactive exploration and export. Its findings should be treated as exploratory practice results until recalculated on an authorised and representative banking dataset.

## References
- Hugging Face dataset page: https://huggingface.co/datasets/An24/Churn_Modelling
- Public dataset mirror used by the default app: https://github.com/salahudheenayoobi-M/European-Bank-Churn-Analysis
- Streamlit documentation: https://docs.streamlit.io/
- Pandas documentation: https://pandas.pydata.org/docs/
