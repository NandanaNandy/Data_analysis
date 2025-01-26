import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from mlxtend.frequent_patterns import apriori, association_rules

# Load datasets
customers = pd.read_csv("E:/Projects/Data_analysis/Customers.csv")
products = pd.read_csv("E:/Projects/Data_analysis/Products.csv")
transactions = pd.read_csv("E:/Projects/Data_analysis/Transactions.csv")


# Merge datasets
merged_data = transactions.merge(customers, on="CustomerID").merge(products, on="ProductID")
merged_data["TransactionDate"] = pd.to_datetime(merged_data["TransactionDate"])

# --- Insight 1: Top Customers by Revenue ---
top_customers = merged_data.groupby("CustomerName")["TotalValue"].sum().sort_values(ascending=False).head(10)
print("Top 10 Customers by Revenue:\n", top_customers)

# --- Insight 2: Top-Selling Products ---
top_products = merged_data.groupby("ProductName")["Quantity"].sum().sort_values(ascending=False).head(10)
print("Top 10 Best-Selling Products:\n", top_products)

# --- Insight 3: Regional Sales Performance ---
regional_sales = merged_data.groupby("Region")["TotalValue"].sum().sort_values(ascending=False)
print("Sales by Region:\n", regional_sales)

# --- Insight 4: Monthly Sales Trend ---
merged_data["Month"] = merged_data["TransactionDate"].dt.to_period("M")
monthly_sales = merged_data.groupby("Month")["TotalValue"].sum()
monthly_sales.plot(kind="line", title="Monthly Sales Trend", xlabel="Month", ylabel="Total Sales")
plt.show()

# --- Insight 5: Customer Retention Analysis ---
merged_data["FirstPurchaseDate"] = merged_data.groupby("CustomerID")["TransactionDate"].transform("min")
merged_data["CustomerLifetime"] = (merged_data["TransactionDate"] - merged_data["FirstPurchaseDate"]).dt.days
customer_lifetime = merged_data.groupby("CustomerID").agg(
    TotalSpend=("TotalValue", "sum"),
    Transactions=("TransactionID", "count"),
    Lifetime=("CustomerLifetime", "max")
).reset_index()
high_value_customers = customer_lifetime[customer_lifetime["TotalSpend"] > 500]
print("High-Value Customers:\n", high_value_customers.head())

# --- Insight 6: Demand Forecasting for a Product ---
product_name = "ProductA"
product_sales = merged_data[merged_data["ProductName"] == product_name]
monthly_product_sales = product_sales.groupby(product_sales["TransactionDate"].dt.to_period("M")).sum()

# Holt-Winters Exponential Smoothing
model = ExponentialSmoothing(monthly_product_sales["TotalValue"], trend="add", seasonal="add", seasonal_periods=12)
forecast = model.fit().forecast(12)
print(f"12-Month Demand Forecast for {product_name}:\n", forecast)

# --- Insight 7: Market Basket Analysis ---
basket = merged_data.groupby(["TransactionID", "ProductName"])["Quantity"].sum().unstack().reset_index().fillna(0)
basket.set_index("TransactionID", inplace=True)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)
frequent_itemsets = apriori(basket, min_support=0.05, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("Association Rules:\n", rules.head())

# --- Insight 8: Profitability Analysis ---
products["ProfitMargin"] = (products["Price"] - products["Price"] * 0.3) / products["Price"]  # Assuming 30% cost
profitability = merged_data.merge(products, on="ProductID").groupby("ProductName").agg(
    TotalRevenue=("TotalValue", "sum"),
    TotalProfit=("ProfitMargin", "sum")
).reset_index()
profitable_products = profitability.sort_values(by="TotalProfit", ascending=False).head(10)
print("Most Profitable Products:\n", profitable_products)

# --- Insight 9: Seasonal Product Trends ---
merged_data["Month"] = merged_data["TransactionDate"].dt.month
seasonal_products = merged_data.groupby(["Month", "ProductName"])["TotalValue"].sum().reset_index()
seasonal_std = seasonal_products.groupby("ProductName")["TotalValue"].std().sort_values(ascending=False)
print("Seasonal Products with High Variability:\n", seasonal_std.head(10))

# --- Insight 10: Time-Based Sales Patterns ---
merged_data["Hour"] = merged_data["TransactionDate"].dt.hour
hourly_sales = merged_data.groupby("Hour")["TotalValue"].sum()
hourly_sales.plot(kind="line", title="Sales by Hour of the Day", xlabel="Hour", ylabel="Total Sales")
plt.show()

daily_sales = merged_data.groupby(merged_data["TransactionDate"].dt.weekday)["TotalValue"].sum()
daily_sales.plot(kind="bar", title="Sales by Day of the Week", xlabel="Day", ylabel="Total Sales")
plt.show()
