import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# Store all book data
books = []

# Convert ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

print("=" * 50)
print("Starting Web Scraping...")
print("=" * 50)

# Loop through all 50 pages
for page in range(1, 51):

    url = base_url.format(page)

    print(f"Scraping Page {page}/50...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        book_list = soup.find_all("article", class_="product_pod")

        for book in book_list:

            # Book Title
            title = book.h3.a["title"]

            # Book Price
            price_text = book.find("p", class_="price_color").get_text(strip=True)

            # Keep only digits and decimal point
            price = "".join(ch for ch in price_text if ch.isdigit() or ch == ".")

            if price:
                price = float(price)
            else:
                price = None

            # Availability
            availability = (
                book.find("p", class_="instock availability")
                .get_text(strip=True)
            )

            # Rating
            rating_text = book.find("p")["class"][1]
            rating = rating_map.get(rating_text, 0)

            books.append({
                "Title": title,
                "Price (£)": price,
                "Availability": availability,
                "Rating": rating,
                "Page": page
            })

        # Small delay to be polite to the server
        time.sleep(0.3)

    except requests.exceptions.RequestException as e:
        print(f"Error on page {page}: {e}")

# Create DataFrame
df = pd.DataFrame(books)

# Save CSV
df.to_csv("books_dataset.csv", index=False, encoding="utf-8-sig")

print("\n" + "=" * 50)
print("Web Scraping Completed Successfully!")
print("=" * 50)
print(f"Total Books Scraped : {len(df)}")
print(f"Total Pages Scraped : {df['Page'].nunique()}")
print(f"Dataset Saved As    : books_dataset.csv")

print("\nFirst 5 Records:")
print(df.head())