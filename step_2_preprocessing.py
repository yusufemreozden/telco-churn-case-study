import pandas as pd

# === 1. Veri setini oku ===
df = pd.read_csv("telco_customer_churn_full.csv")

# === 2. TotalCharges sütunu float değil, object → çevirelim ===
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")  # hatalıları NaN yap

# === 3. Eksik verileri temizle ===
df.dropna(inplace=True)

# === 4. ID sütunu model için gereksiz ===
df.drop("customerID", axis=1, inplace=True)

# === 5. Churn sütununu 1/0 yap ===
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# === 6. Binary olanları manuel encode et ===
binary_cols = ["gender", "Partner", "Dependents", "PhoneService", "PaperlessBilling"]
for col in binary_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0, "Male": 1, "Female": 0})

# === 7. Geri kalan kategorik sütunları one-hot encode et ===
df = pd.get_dummies(df, drop_first=True)

# === 8. Son hali kaydet ===
df.to_csv("telco_churn_encoded.csv", index=False)

# === 9. Kontrol amaçlı ilk 5 satırı yazdır ===
print("✅ Encode edilmiş veri:\n")
print(df.head())
print(f"\n💾 Toplam {df.shape[0]} satır, {df.shape[1]} sütun ile kaydedildi.")
