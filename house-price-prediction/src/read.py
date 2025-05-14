import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("data/housing.csv")
"""
# Basic info
print("📄 Data Shape:", df.shape)
print("\n📌 First 5 rows:\n", df.head())
print("\n📊 Column Info:\n")
print(df.info())
print("\n🧮 Descriptive Statistics:\n", df.describe())
print("\n🧾 Null Values:\n", df.isnull().sum())
"""


# Histogram
df.hist(bins=30, figsize=(12, 8))
plt.suptitle("Distribution of Features")
plt.tight_layout()
plt.savefig("outputs/histogram.png")  # Save to file

# Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Between Features")
plt.tight_layout()
plt.savefig("outputs/heatmap.png")  # Save to file