# Credit Card Fraud Detection with Machine Learning 

![image](https://github.com/user-attachments/assets/85657d6c-ad59-4d46-9f0d-9010a18eaf6d)

## Project Overview  
The growing use of credit cards  across the globe has led to a surge in fraudulent transactions, necessitating robust fraud detection mechanisms. Employing machine learning, presents a viable solution. This research evaluates the performance of various machine learning classifiers, Random Forest, Decision Tree and  KNNearest Neighbours (KNN) and data balancing techniques SMOTE and Stratified K-Fold for credit card fraud detection using a highly imbalanced dataset. The experimental results that Random Forest achieved the best metric performance. This research reveals the importance of leveraging machine learning and appropriate data-balancing techniques for optimal fraud detection in credit card transactions. This contribution is pivotal, enriching the knowledge base and providing insights into the ongoing battle against credit card fraud

![image](https://github.com/user-attachments/assets/418379cd-3d62-4a32-9fcd-146ad9cbfbf1)

Credit card fraud poses a growing threat to the financial service industry. A report from Statista shows that global losses due to credit card fraud have risen by 10%between 2020 and 2021 (Statista, 2023). This alarming trend translates into substantial losses for credit card issuers and merchant acquirers, estimating that both entities will lose over USD 30 billion in 2022 alone. E-commerce has been a critical factor in this surge in credit card fraud. As(Jain et al., 2019) Point out, the increasing popularity of online shopping creates more opportunities for fraudsters. These criminals are employing ever-more sophisticated tactics to gain access to digital payment information, and credit card fraud will constitute a staggering 73% of all card payment fraud losses within a year.

## Features and Key Steps  
1. **Data Cleaning**: Removed duplicates and irrelevant columns.
2. **Exploratory Data Analysis (EDA)
2. **Feature Engineering**: Created transaction time features.  
3. **Model Training with cross-validation**: Evaluated models using ROC-AUC and F1-score
4. **Performance Metrics (ROC-AUC, F1 Score, Precision, Recall)
  

## Results   

### Model Comparison  
| Model          | ROC-AUC | Recall |  
|----------------|---------|--------|  
| Random Forest  | 0.98    | 0.89   |  
| Decision Tree  | 0.94    | 0.85   |  
| KNN            | 0.91    | 0.82   |  

 
 
## How to Run  
https://github.com/Macdon112/Credit-Card-Fraud-Detection/blob/main/Credit-Card-Fraud-Detection/Notebooks/Fraud%20detection%20Analysis.ipynb

## Dataset(Synthetic Dataset)  
**https://www.kaggle.com/datasets/kelvinkelue/credit-card-fraud-prediction?resource=download**

Data Collection 
The dataset, named ‘fraud test’, is a synthetic dataset hence not anonymised sourced from Kaggle(Kaggle) It comprises 555,719 instances, each characterised by 22 attributes, encompassing both categorical and numerical types, and contains no null values. The attributes include:
**1. Trans_date_trans_time: Date and time of the transaction.** 
**2. Cc_num: Customer number.** 
**3. Merchant: Merchant involved in the transaction.** 
**4. Category: Type of transaction (e.g., personal, kids care).** 
**5. Amt: Transaction amount.** 
**6. First: First name of the cardholder.** 
**7. Last: Last name of the cardholder.** 
**8. Gender: Gender of the cardholder.** 
**9. Street: Street address of the cardholder.** 
**10. City: City of the cardholder.** 
**11. State: State of residence of the cardholder.** 
**12. Zip: Zip code of the cardholder’s residence.** 
**13. Lat: Latitude of the transaction location.** 
**14. Long: Longitude of the transaction location.** 
**15. City_pop: Population of the cardholder’s city.** 
**16. Job: Job title of the cardholder.** 
**17. Dob: Date of birth of the cardholder.** 
**18. Trans_num: Unique transaction ID.** 
**19. Unix_time: Timestamp of the transaction** 
**20. Merch_lat: Latitude of the merchant’s location.** 
**21. Merch_long: Longitude of the merchant’s location.** 
**22. Is_fraud: Indicates fraud status with 1 for fraud and 0 for non-fraud. This is the target variable for classification.**

## Tools Used  
- Python  
- Scikit-learn, Imbalanced-learn  
- Matplotlib/Seaborn  


## Installation
To install the required libraries, run:
```bash
pip install -r requirements.txt

How to run 
jupyter notebook credit_card_fraud_detection.ipynb


 
Run all the cells.
check the output metrics and plots

Results
1. Random forest performs best with the highest recall score
2. Fraudulent transactions are highly imbalanced, requiring oversampling

Author.
Nnamdi Okeke 
GitHub: https://github.com/Macdon112

License
