import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the datasets
customers = pd.read_csv("E:/Projects/Data_analysis/Customers.csv")
products = pd.read_csv("E:/Projects/Data_analysis/Products.csv")
transactions = pd.read_csv("E:/Projects/Data_analysis/Transactions.csv")

# Initial Data Exploration
print(customers.head())
print(products.head())
print(transactions.head())

# Data Info and Null Check
print(customers.info())
print(products.info())
print(transactions.info())

# Null Values Handling
print(customers.isnull().sum())
customers.fillna("Unknown", inplace=True)
transactions.dropna(subset=["TotalValue"], inplace=True)

# Converting Date Columns to Datetime
customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])
transactions["TransactionDate"] = pd.to_datetime(transactions["TransactionDate"])
transactions["Month"] = transactions["TransactionDate"].dt.to_period("M")

# Region Distribution Bar Plot (Matplotlib)
region_distribution = customers["Region"].value_counts()
region_distribution.plot(kind="bar", color="teal")
plt.title("Customer Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Number of Customers")
plt.show()

# Region Distribution Bar Plot (Plotly)
region_counts = customers["Region"].value_counts().reset_index()
region_counts.columns = ["Region", "Count"]
fig = px.bar(
    region_counts,
    x="Region",
    y="Count",
    color="Region",
    title="Customer Distribution by Region",
    text="Count",
    template="plotly_dark",
)
fig.update_traces(textposition="outside", marker=dict(line=dict(width=1.5, color="black")))
fig.update_layout(
    font=dict(size=16),
    dragmode=False  # Disable dragging
)
fig.show()

# Category Sales by Product Category (Matplotlib)
category_sales = transactions.merge(products, on="ProductID").groupby("Category")["TotalValue"].sum()
category_sales.sort_values(ascending=False).plot(kind="bar", color="orange")
plt.title("Sales by Product Category")
plt.ylabel("Total Revenue (USD)")
plt.show()

# Category Sales by Product Category (Plotly Pie Chart)
merged_data = transactions.merge(products, on="ProductID")
category_sales = merged_data.groupby("Category")["TotalValue"].sum().reset_index()
fig = px.pie(
    category_sales,
    names="Category",
    values="TotalValue",
    title="Revenue by Product Category",
    template="presentation",
    hole=0.4,
)
fig.update_traces(textinfo="percent+label")
fig.update_layout(dragmode=False)  # Disable dragging
fig.show()

# Monthly Sales Trends (Matplotlib Line Plot)
monthly_sales = transactions.groupby("Month")["TotalValue"].sum()
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Revenue Trends")
plt.ylabel("Total Revenue (USD)")
plt.show()

# Monthly Sales Trends (Plotly Line Plot)
monthly_sales = transactions.groupby("Month")["TotalValue"].sum().reset_index()
monthly_sales["Month"] = monthly_sales["Month"].astype(str)  # Convert to string here

fig = px.line(monthly_sales, x="Month", y="TotalValue", title="Monthly Revenue Trends", markers=True, template="ggplot2", color_discrete_sequence=["green"])
fig.update_traces(line=dict(width=3), marker=dict(size=10, symbol="circle"))
fig.update_layout(dragmode=False)  # Disable dragging
fig.show()

# Heatmap of Revenue by Region and Category (Matplotlib)
heatmap_data = merged_data.groupby(["Region", "Category"])["TotalValue"].sum().unstack()
plt.figure(figsize=(12, 6))
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    cbar_kws={"label": "Revenue (USD)"},
)
plt.title("Revenue by Region and Category", fontsize=16)
plt.ylabel("Region", fontsize=14)
plt.xlabel("Category", fontsize=14)
plt.xticks(rotation=45)
plt.show()

# Descriptive Statistics
print(customers.describe())
print(products.describe())
print(transactions.describe())

# Check for missing values
print(customers.isnull().sum())
print(products.isnull().sum())
print(transactions.isnull().sum())

# Mean and Median Sales
mean_sales = transactions["TotalValue"].mean()
median_sales = transactions["TotalValue"].median()
print(f"Mean Sales: {mean_sales}")
print(f"Median Sales: {median_sales}")

# Year-over-Year (YoY) Sales Growth
transactions["Year"] = transactions["TransactionDate"].dt.year
sales_by_year = transactions.groupby("Year")["TotalValue"].sum()
sales_by_year_growth = sales_by_year.pct_change() * 100

# Plot YoY Growth
fig, ax = plt.subplots(figsize=(12, 6))
sales_by_year_growth.plot(ax=ax, kind="bar")
plt.title("Year-over-Year Sales Growth")
plt.xlabel("Year")
plt.ylabel("YoY Growth (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation Analysis (if you have numerical data for correlation)
correlation_matrix = transactions.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()
