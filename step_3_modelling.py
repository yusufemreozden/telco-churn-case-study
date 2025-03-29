import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# === 1. Veriyi oku ===
df = pd.read_csv("telco_churn_encoded.csv")

# === 2. X ve y ayır ===
X = df.drop("Churn", axis=1)
y = df["Churn"]

# === 3. Ölçeklendirme (StandardScaler) ===
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# === 4. Eğitim ve test setlerine ayır ===
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# === 5. Logistic Regression ===
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# === 6. Tahmin ve metrikler ===
y_pred = model.predict(X_test)

print(f"✅ Doğruluk (Accuracy): {accuracy_score(y_test, y_pred):.4f}\n")
print("📊 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\n📋 Sınıflandırma Raporu:")
print(classification_report(y_test, y_pred))
