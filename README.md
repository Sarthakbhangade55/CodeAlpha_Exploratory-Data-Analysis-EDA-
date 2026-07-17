# 📊 Task 2: Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a books dataset collected from a public website. The goal is to understand the dataset by exploring its structure, identifying trends and patterns, detecting anomalies, validating assumptions using statistics and visualizations, and assessing data quality before further analysis.

---

## 🎯 Objectives

* Ask meaningful questions before analyzing the dataset.
* Explore the dataset structure, variables, and data types.
* Generate summary statistics.
* Identify trends, patterns, and anomalies.
* Test hypotheses using statistical analysis and visualizations.
* Detect missing values, duplicate records, and other potential data quality issues.

---

## 🛠️ Technologies Used

* Python 3.13
* Pandas
* Matplotlib
* Seaborn

---

## 📂 Dataset

**Dataset File:** `books_dataset.csv`

### Dataset Features

| Feature      | Description                            |
| ------------ | -------------------------------------- |
| Title        | Name of the book                       |
| Price (£)    | Price of the book                      |
| Availability | Stock availability                     |
| Rating       | Book rating (1–5)                      |
| Page         | Page number where the book was scraped |

---

## ❓ Questions Asked Before Analysis

* How many books are available in the dataset?
* What is the average price of books?
* Which book is the most expensive?
* Which book is the least expensive?
* Which rating appears most frequently?
* Are all books available?
* Are there any missing values?
* Are there duplicate records?
* Does a higher rating correspond to a higher price?
* Are there any unusual (outlier) prices?

---

## 🔍 EDA Process

The following steps were performed during the analysis:

* Dataset preview
* Dataset shape analysis
* Column exploration
* Data type inspection
* Missing value detection
* Duplicate record detection
* Summary statistics
* Trend analysis
* Pattern identification
* Correlation analysis
* Outlier detection
* Data quality assessment

---

## 📊 Visualizations

The following charts were generated:

* Rating Distribution
* Price Distribution
* Price vs Rating (Box Plot)
* Books per Page
* Correlation Heatmap

All visualizations are saved in the **eda_outputs/** folder.

---

## 📈 Key Findings

* The dataset contains **1000 books** collected from **50 pages**.
* Book prices range from **£10.00** to **£59.99**.
* The average book price is approximately **£35.07**.
* Ratings range from **1 to 5**.
* The dataset contains **no missing values**.
* No duplicate records were found.
* Price variations exist across different rating categories.
* The dataset is clean and suitable for further analysis.

---

## 📖 Insights

The Exploratory Data Analysis revealed several useful insights:

* Most books fall within a moderate price range.
* Book ratings are distributed across all five categories.
* Price distributions vary across rating levels.
* The correlation analysis indicates the relationship between numerical variables.
* Data quality checks confirmed that the dataset is complete and consistent.

---

## 🚀 How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the EDA script:

```bash
python eda.py
```

3. View the generated visualizations inside the **eda_outputs/** folder.

---

## 📚 Learning Outcomes

This project demonstrates the following skills:

* Exploratory Data Analysis (EDA)
* Data Cleaning
* Data Validation
* Statistical Analysis
* Trend Analysis
* Pattern Recognition
* Outlier Detection
* Data Visualization
* Data Quality Assessment
* Python Programming

---

## 👨‍💻 Author

**Sarthak Bhangade**

B.Tech – Artificial Intelligence & Data Science

---

## 📄 License

This project was created for educational and internship purposes.
