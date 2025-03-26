# Credit Card Fraud Detection Using Machine Learning

> A complete pipeline for detecting fraudulent credit card transactions with state-of-the-art machine learning models and robust evaluation strategies.

## Project Objective

The primary aim of this project is to identify and prevent credit card fraud by building and evaluating machine learning models that can distinguish fraudulent transactions from legitimate ones. Given the **highly imbalanced** nature of fraud detection tasks, the project incorporates advanced techniques such as **SMOTE** oversampling and **stratified cross-validation** to ensure model robustness.



## Dataset

Source: `fraud_test.csv` containing **555,719** credit card transactions.
Target Variable: `is_fraud` (0 = non-fraud, 1 = fraud)
Fraudulent records: ~0.38% of total data (2145 fraud cases)



## Exploratory Data Analysis (EDA)

Comprehensive data profiling and visualisation included:

**Fraud Distribution**: Visualised imbalance (0.38% fraud).
**Gender vs Fraud**: Compared fraud rates across genders.
**Category vs Fraud**: Identified risky transaction categories.
**Time-based Patterns**: Analyzed hourly fraud likelihood.
**Amount Trends**: High-value transactions show greater fraud correlation.
**Outlier Detection**: Boxplots for `amt`, `lat`, `long`, and `city_pop`.



## Feature Engineering

Several engineered features were introduced to enrich the predictive power of the model:

1. **Age at Transaction** (from `dob` and `trans_date_trans_time`)
2. **Time Since Last Transaction**
3. **Relative Transaction Amount** (vs average per user)
4. **Cumulative Transaction Amount**
5. **WOE Encoding** for categorical features: `merchant`, `job`, `category`, `lat`



## Data Preprocessing

Dropped redundant fields like `Unnamed: 0`, `cc_num`, `dob`, etc.
Applied **standard scaling** to normalise features.
Balanced the data using **SMOTE** to address class imbalance.
Final feature set passed rigorous correlation analysis.



## Machine Learning Models & Evaluation

Three core models were evaluated using **Stratified K-Fold Cross-Validation** (n=10):

### Random Forest Classifier
- Accuracy: **1.00**
- F1 Score: **1.00**
- ROC AUC: **1.00**
- Precision: **0.99**
- Recall: **0.99**
- Feature Importance revealed key predictors in fraud behaviour.

### Decision Tree Classifier
- Accuracy: **1.00**
- F1 Score: **1.00**
- ROC AUC: **1.00**
- Precision: **0.83**
- Recall: **0.67**

### K-Nearest Neighbors (KNN)
- Accuracy: **0.99**
- F1 Score: **0.99**
- ROC AUC: **1.00**
- Precision: **0.92**
- Recall: **0.86**



## Pipeline Framework with Dynamic Synthetic Oversampling

Implemented advanced pipeline structures using **imbalanced-learn Pipelines**:

- SMOTE applied within each fold to prevent data leakage.
- Visualised **ROC Curves**, **Precision-Recall Curves**, and **Confusion Matrices**.
- Comparative analysis confirmed **Random Forest** as the most consistent performer.



## Results Summary

| Model           | Accuracy | F1 Score | ROC AUC | Precision | Recall |
|----------------|----------|----------|---------|-----------|--------|
| Random Forest  | 1.00     | 1.00     | 1.00    | 0.99      | 0.99   |
| Decision Tree  | 1.00     | 1.00     | 1.00    | 0.83      | 0.67   |
| KNN            | 0.99     | 0.99     | 1.00    | 0.92      | 0.86   |
| RF Pipeline    | 0.9979   | 0.7346   | 0.9833  | 0.7136    | 0.7582 |
| DT Pipeline    | 0.9968   | 0.6368   | 0.8646  | 0.5646    | 0.7313 |
| KNN Pipeline   | 0.9841   | 0.2449   | 0.8606  | 0.1500    | 0.6685 |



## File Structure

Credit-Card-Fraud-Detection
Credit-Card-Fraud-Detection.ipynb
Credit-Card-Fraud-Detection.pdf  ← Download full notebook report
fraud_test.csv
README.md


Access the Full Report

Download PDF Report Credit-Card-Fraud-detection.pdf

This detailed notebook includes every visual, EDA, model, confusion matrix, performance metrics, and plots.



## Author & Skills Demonstrated

This project showcases:

Proficiency in Python, pandas, seaborn, scikit-learn, and imbalanced-learn.
Mastery of feature engineering, class imbalance handling, and model evaluation.
Expertise in building interpretable, replicable, and high-performing fraud detection systems.

Reach out for data science consulting, fraud detection modelling, or machine learning projects.



## Future Work

- Incorporate **deep learning methods** (e.g., LSTM, autoencoders)
- Deploy the model as a real-time fraud detection API
- Integrate model explainability tools like SHAP and LIME
- Continuous learning pipeline to adapt to new fraud patterns



> “Credit card fraud detection isn't just about machine learning—it's about preserving trust in the digital economy. With this project, we take a confident step toward smarter, data-driven security.” — *Nnamdi Okeke*
