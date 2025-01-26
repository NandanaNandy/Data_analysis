import pandas as pd

# Load the data
customers = pd.read_csv('customers.csv')
transactions = pd.read_csv('transactions.csv')
products = pd.read_csv('products.csv')

# Check if 'BirthYear' column exists
if 'BirthYear' not in customers.columns:
    print("DOB column is missing. Using an alternative method to calculate age.")
    # Assuming an alternative column is available for age calculation or any other method to calculate age
    # Example: Add some logic to estimate age
    # customers['Age'] = some_method_to_calculate_age(customers)

# If 'BirthYear' exists, calculate 'Age'
else:
    customers['Age'] = 2025 - customers['BirthYear']  # Assuming current year is 2025

# Merge transactions with products
transactions_with_products = pd.merge(transactions, products, on='ProductID', how='left')

# Now create a customer summary (you were attempting to group by 'CustomerID')
try:
    customer_summary = transactions_with_products.groupby('CustomerID').agg({
        'Amount': 'sum',  # Sum of amounts
        'ProductCategory': 'first'  # You can adjust this based on your needs
    }).reset_index()

    # Now we merge the customer_summary with the customers to get the full info
    customer_summary = pd.merge(customer_summary, customers[['CustomerID', 'Age']], on='CustomerID', how='left')

    # Now customer_summary should have the necessary fields: CustomerID, Age, Amount, ProductCategory
    print(customer_summary.head())

except KeyError as e:
    print(f"Column(s) {e} do not exist in the data.")
