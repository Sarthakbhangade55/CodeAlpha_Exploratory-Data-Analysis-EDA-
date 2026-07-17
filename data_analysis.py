import pandas as pd

# Load dataset
df = pd.read_csv("books_dataset.csv")

print("=" * 50)
print("BOOK DATASET ANALYSIS")
print("=" * 50)

# Total books
print(f"\nTotal Books : {len(df)}")

# Total Pages
print(f"Total Pages : {df['Page'].nunique()}")

# Average Price
print(f"\nAverage Price : £{df['Price (£)'].mean():.2f}")

# Highest Price
print(f"Highest Price : £{df['Price (£)'].max():.2f}")

# Lowest Price
print(f"Lowest Price : £{df['Price (£)'].min():.2f}")

# Average Rating
print(f"\nAverage Rating : {df['Rating'].mean():.2f}/5")

print("\nBooks by Rating")

print(df["Rating"].value_counts().sort_index())

print("\nTop 5 Most Expensive Books")

print(
    df.sort_values(
        by="Price (£)",
        ascending=False
    )[["Title", "Price (£)"]].head()
)