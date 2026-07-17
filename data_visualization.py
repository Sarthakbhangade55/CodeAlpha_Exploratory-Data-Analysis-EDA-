import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# -----------------------------
# Chart 1: Rating Distribution
# -----------------------------
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8,5))
plt.bar(rating_counts.index.astype(str), rating_counts.values)

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.savefig("rating_distribution.png")
plt.show()

# -----------------------------
# Chart 2: Price Distribution
# -----------------------------
plt.figure(figsize=(8,5))

plt.hist(df["Price (£)"], bins=15)

plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.savefig("price_distribution.png")
plt.show()

print("Charts created successfully!")