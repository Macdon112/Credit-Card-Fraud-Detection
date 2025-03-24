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
