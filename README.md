# 📉 Telco Customer Churn – Case Study

A full-cycle data analytics project to predict customer churn in the telecom industry using logistic regression.  
This project simulates a real-world business scenario where understanding why customers leave can drive data-informed strategies to reduce churn.

---

## 📌 Project Overview

- 🎯 Goal: Predict whether a customer will churn (leave) based on demographic, contract, and usage data.
- 🏢 Industry: Telecom
- 📊 Dataset: [Telco Customer Churn - Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 🧠 Model Used: Logistic Regression
- 💻 Tools: Python, Pandas, Scikit-Learn

---

## 🧱 Project Pipeline

1. **EDA (Exploratory Data Analysis)**  
   - Dataset shape, data types, null values  
   - Churn distribution analysis

2. **Data Preprocessing**  
   - Encoding categorical features  
   - Handling missing values  
   - Feature scaling with StandardScaler

3. **Modeling**  
   - Train-test split (70–30)  
   - Logistic Regression with accuracy and classification metrics  
   - Confusion Matrix interpretation

---

## 🧾 Sample Output

✅ Doğruluk (Accuracy): 0.7953

📊 Confusion Matrix:
```
[[1378  171]
 [ 261  300]]
```

📋 Classification Report:
```
              precision    recall  f1-score   support

           0       0.84      0.89      0.86      1549
           1       0.64      0.53      0.58       561

    accuracy                           0.80      2110
   macro avg       0.74      0.71      0.72      2110
weighted avg       0.79      0.80      0.79      2110
```
---

## 🚀 Future Improvements

- Try ensemble models (Random Forest, XGBoost)
- Address class imbalance (`class_weight='balanced'`)
- Add ROC Curve and AUC Score
- Streamlit dashboard for interactive prediction
- Feature importance visualization
