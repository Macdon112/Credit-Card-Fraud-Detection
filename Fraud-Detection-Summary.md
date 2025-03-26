## Business Report & Project Outcome Summary

**Project Title Evaluating Machine Learning Methods in Credit Card Fraud Detection**

**Author**: Nnamdi Okeke
**Objective**: To identify effective machine learning techniques capable of accurately detecting fraudulent credit card transactions using synthetic, realistic transaction data.

 **Project Overview**
This project addresses a critical problem in digital finance: the rising threat of credit card fraud. Through a comparative analysis of three machine learning algorithms—Random Forest, Decision Tree, and K-Nearest Neighbours (KNN)—this study aimed to design, implement, and evaluate robust fraud detection models that are scalable and interpretable.

**Dataset Characteristics**
•	Source: Synthetic but semantically realistic credit card transaction dataset
•	Total transactions: ~555,000
•	Fraud cases: ~2,145 (Approx. 0.38% of data)
•	Imbalance Handling: SMOTE (Synthetic Minority Oversampling Technique)

**Methodology Snapshot**
--EDA: Outlier analysis, skew detection, correlation mapping
--Feature Engineering:
--txn_amount_relative_to_avg
--cumulative_txn_amount
--job, category, merchant, age_at_txn
--Model Evaluation Metrics:
--Accuracy, Precision, Recall, F1-Score, ROC-AUC
--Cross-validation: Stratified K-Fold (K=10)
--Approach B: Dynamic SMOTE integrated within a pipeline
---
 
 **Key Findings**
**Best Performing Model**: Random Forest Classifier
--•	Accuracy: 99.79%
•	F1 Score: 0.73
•	Precision: 0.71
•	Recall: 0.76
•	ROC-AUC: 0.98
--
**Least Effective: K-Nearest Neighbour (KNN)**
--•	Low recall and precision in pipeline testing
•	Computationally expensive
--

**Most Influential Features**
--•	amt (Transaction Amount)
•	job (Occupation of cardholder)
•	category (Type of transaction)
•	txn_amount_relative_to_avg
•	cumulative_txn_amount
•	merchant (Vendor identifier)
These features were consistently ranked highly in Random Forest and Decision Tree importance charts.
--

**Business Implications**
--•	Real-time Fraud Blocking: The trained model can be integrated into payment gateways to flag fraudulent transactions before they are processed.
•	Regulatory Alignment: Helps institutions meet compliance standards for fraud prevention.
•	Customer Trust: Minimises false positives, preserving customer satisfaction.
•	Data-Driven Risk Scoring: Models provide feature importance that informs policy rules and human analyst reviews.
--

 **Recommendations for Deployment**
--1.	Production-ready Pipeline: Integrate Random Forest into an API microservice.
2.	Feature Monitoring: Watch drift in amt, category, and merchant patterns.
3.	Retraining Schedule: Reassess model performance every 60-90 days.
4.	Human-in-the-loop: Use model explanations to support analyst decision-making.
5.	Dashboard Integration: Link outputs to a fraud analyst dashboard using Power BI or Streamlit.
--

**Consultant's Offer**
As a data scientist, I offer services including:
--•	Custom fraud detection system design
•	Real-time scoring architecture 
•	Model audit & risk review for compliance
•	Analyst training in ML tools and workflows
--

**Access the Full Project**
Download Full Report: Credit-Card-Fraud-detection.pdf

“Accurate fraud detection is not just a technical solution—it's a trust-building tool in a digital-first economy.” — Nnamdi Okeke

