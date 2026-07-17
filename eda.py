import pandas as pd

# Load dataset
df = pd.read_csv("books_dataset.csv")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)

# -------------------------------------------------
# EDA Questions
# -------------------------------------------------

print("\nEDA Questions:")
print("1. How many books are available?")
print("2. What is the average price of books?")
print("3. Which book is the most expensive?")
print("4. Which book is the cheapest?")
print("5. Which rating appears most frequently?")
print("6. Are all books in stock?")
print("7. Does a higher rating correspond to a higher price?")
print("8. Are there duplicate records?")
print("9. Are there missing values?")
print("10. Are there any outliers in book prices?")

# -------------------------------------------------
# Dataset Preview
# -------------------------------------------------

print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

# -------------------------------------------------
# Dataset Structure
# -------------------------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names")
print(df.columns.tolist())

# -------------------------------------------------
# Data Types
# -------------------------------------------------

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
df.info()

# -------------------------------------------------
# Missing Values
# -------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------------------------
# Duplicate Values
# -------------------------------------------------

print("\nDuplicate Rows")
print(df.duplicated().sum())

# -------------------------------------------------
# Summary Statistics
# -------------------------------------------------

print("\nSummary Statistics")
print(df.describe())

print("\nSummary Statistics (Including Object Columns)")
print(df.describe(include="all"))

import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set_style("whitegrid")

# Create output folder if it doesn't exist
import os
os.makedirs("eda_outputs", exist_ok=True)

print("\nGenerating EDA Visualizations...")

plt.figure(figsize=(8,5))

sns.boxplot(data=df, x="Rating", y="Price (£)")

plt.title("Book Price by Rating")

plt.savefig("eda_outputs/price_vs_rating.png")
plt.close()

plt.figure(figsize=(10,5))

sns.countplot(data=df, x="Page")

plt.title("Books Collected Per Page")
plt.xlabel("Page Number")
plt.ylabel("Books")

plt.xticks(rotation=90)

plt.savefig("eda_outputs/books_per_page.png")
plt.close()


plt.figure(figsize=(6,4))

sns.heatmap(
    df[["Price (£)", "Rating", "Page"]].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Matrix")

plt.savefig("eda_outputs/correlation_heatmap.png")
plt.close()



print("\n" + "="*60)
print("EDA SUMMARY")
print("="*60)

print(f"Total Books: {len(df)}")
print(f"Average Price: £{df['Price (£)'].mean():.2f}")
print(f"Highest Price: £{df['Price (£)'].max():.2f}")
print(f"Lowest Price: £{df['Price (£)'].min():.2f}")

print("\nAverage Price by Rating")
print(df.groupby("Rating")["Price (£)"].mean())

print("\nBooks by Rating")
print(df["Rating"].value_counts().sort_index())

print("\nEDA Completed Successfully!")
print("Charts saved in 'eda_outputs' folder.")