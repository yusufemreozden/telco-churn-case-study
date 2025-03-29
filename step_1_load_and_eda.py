import pandas as pd

# === 1. CSV dosyasını oku ===
df = pd.read_csv("telco_customer_churn_full.csv")  # <- yeni dosya adıyla

# === 2. Boyut bilgisi ===
print("✅ Veri seti boyutu:", df.shape)

# === 3. İlk 5 satırı göster ===
print("\n📌 İlk 5 Satır:\n", df.head())

# === 4. Veri tiplerini incele ===
print("\n🔎 Veri Tipleri:\n", df.dtypes)

# === 5. Eksik veri kontrolü ===
print("\n🚨 Eksik Veri:\n", df.isnull().sum())

# === 6. Churn sınıfı dağılımı ===
print("\n📊 Churn Dağılımı:\n", df["Churn"].value_counts())
print("\n📊 Churn Oranı:\n", df["Churn"].value_counts(normalize=True))
