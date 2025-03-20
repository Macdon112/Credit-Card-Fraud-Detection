# Credit Card Fraud Detection with Machine Learning 

## Project Overview  
This project compares machine learning models (KNN, Random Forest, Decision Tree) to detect fraudulent credit card transactions using SMOTE and stratified cross-validation.  


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

1. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
2. Open the notebook:  
   ```bash  
   jupyter notebook credit_card_fraud_detection.ipynb 
   ```  

## Dataset(Synthetic Dataset)  
[creditcard_fraud.csv](Data/creditcard_fraud.csv) (Source: Synthetic)  

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