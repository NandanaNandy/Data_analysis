# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# from io import BytesIO
# import base64
# import os

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Load datasets
# customers = pd.read_csv("E:\Projects\Data_analysis\Customers.csv")
# products = pd.read_csv("E:\Projects\Data_analysis\Products.csv")
# transactions = pd.read_csv("E:\Projects\Data_analysis\Transactions.csv")

# # Data Preprocessing
# customers.fillna("Unknown", inplace=True)
# transactions.dropna(subset=["TotalValue"], inplace=True)

# customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])
# transactions["TransactionDate"] = pd.to_datetime(transactions["TransactionDate"])

# transactions["Month"] = transactions["TransactionDate"].dt.to_period("M").astype(str)

# # Matplotlib Graphs (for tabs)
# def get_region_distribution():
#     fig, ax = plt.subplots()
#     customers["Region"].value_counts().plot(kind="bar", color="teal", ax=ax)
#     ax.set_title("Customer Distribution by Region")
#     ax.set_xlabel("Region")
#     ax.set_ylabel("Number of Customers")
#     return fig

# def get_category_sales():
#     fig, ax = plt.subplots()
#     category_sales = transactions.merge(products, on="ProductID").groupby("Category")["TotalValue"].sum()
#     category_sales.sort_values(ascending=False).plot(kind="bar", color="orange", ax=ax)
#     ax.set_title("Sales by Product Category")
#     ax.set_ylabel("Total Revenue (USD)")
#     return fig

# def get_monthly_sales():
#     fig, ax = plt.subplots()
#     monthly_sales = transactions.groupby("Month")["TotalValue"].sum()
#     monthly_sales.plot(kind="line", marker="o", color="green", ax=ax)
#     ax.set_title("Monthly Revenue Trends")
#     ax.set_ylabel("Total Revenue (USD)")
#     return fig

# # Plotly Graphs (for tabs)
# def get_region_distribution_plotly():
#     region_counts = customers["Region"].value_counts().reset_index()
#     region_counts.columns = ["Region", "Count"]
#     fig = px.bar(
#         region_counts,
#         x="Region",
#         y="Count",
#         color="Region",
#         title="Customer Distribution by Region",
#         text="Count",
#         template="plotly_dark",
#     )
#     fig.update_traces(textposition="outside", marker=dict(line=dict(width=1.5, color="black")))
#     return fig

# def get_category_sales_plotly():
#     merged_data = transactions.merge(products, on="ProductID")
#     category_sales = merged_data.groupby("Category")["TotalValue"].sum().reset_index()
#     fig = px.pie(
#         category_sales,
#         names="Category",
#         values="TotalValue",
#         title="Revenue by Product Category",
#         template="presentation",
#         hole=0.4,
#     )
#     fig.update_traces(textinfo="percent+label")
#     return fig

# def get_monthly_sales_plotly():
#     monthly_sales = transactions.groupby("Month")["TotalValue"].sum().reset_index()
#     fig = px.line(
#         monthly_sales,
#         x="Month",
#         y="TotalValue",
#         title="Monthly Revenue Trends",
#         markers=True,
#         template="ggplot2",
#         color_discrete_sequence=["green"],
#     )
#     fig.update_traces(line=dict(width=3), marker=dict(size=10, symbol="circle"))
#     return fig

# # Convert Matplotlib figures to base64 for Dash usage
# def fig_to_base64(fig):
#     buf = BytesIO()
#     fig.savefig(buf, format="png")
#     buf.seek(0)
#     return base64.b64encode(buf.read()).decode("utf-8")

# # Define the layout of the app
# app.layout = html.Div([
#     dcc.Tabs(id="tabs", value='tab-1', children=[
#         dcc.Tab(label='Region Distribution (Matplotlib)', value='tab-1'),
#         dcc.Tab(label='Sales by Category (Matplotlib)', value='tab-2'),
#         dcc.Tab(label='Monthly Revenue Trends (Matplotlib)', value='tab-3'),
#         dcc.Tab(label='Region Distribution (Plotly)', value='tab-4'),
#         dcc.Tab(label='Revenue by Product Category (Plotly)', value='tab-5'),
#         dcc.Tab(label='Monthly Revenue Trends (Plotly)', value='tab-6'),
#     ]),
#     html.Div(id='tabs-content')
# ])

# # Define the callback to update the content based on selected tab
# @app.callback(
#     Output('tabs-content', 'children'),
#     Input('tabs', 'value')
# )
# def render_content(tab):
#     if tab == 'tab-1':
#         fig = get_region_distribution()
#         img_src = "data:image/png;base64,{}".format(fig_to_base64(fig))
#         return html.Div([html.Img(src=img_src)])
#     elif tab == 'tab-2':
#         fig = get_category_sales()
#         img_src = "data:image/png;base64,{}".format(fig_to_base64(fig))
#         return html.Div([html.Img(src=img_src)])
#     elif tab == 'tab-3':
#         fig = get_monthly_sales()
#         img_src = "data:image/png;base64,{}".format(fig_to_base64(fig))
#         return html.Div([html.Img(src=img_src)])
#     elif tab == 'tab-4':
#         fig = get_region_distribution_plotly()
#         return html.Div([dcc.Graph(figure=fig)])
#     elif tab == 'tab-5':
#         fig = get_category_sales_plotly()
#         return html.Div([dcc.Graph(figure=fig)])
#     elif tab == 'tab-6':
#         fig = get_monthly_sales_plotly()
#         return html.Div([dcc.Graph(figure=fig)])

# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
customers = pd.read_csv("E:\Projects\Data_analysis\Customers.csv")
products = pd.read_csv("E:\Projects\Data_analysis\Products.csv")
transactions = pd.read_csv("E:\Projects\Data_analysis\Transactions.csv")
print(customers.head())
print(products.head())
print(transactions.head())
print(customers.head())
print(products.head())
print(transactions.head())
print(customers.info())
print(products.info())
print(transactions.info())
print(customers.isnull().sum())
customers.fillna("Unknown", inplace=True)
transactions.dropna(subset=["TotalValue"], inplace=True)
customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])
transactions["TransactionDate"] = pd.to_datetime(transactions["TransactionDate"])
transactions["Month"] = transactions["TransactionDate"].dt.to_period("M")
region_distribution = customers["Region"].value_counts()
region_distribution.plot(kind="bar", color="teal")
plt.title("Customer Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Number of Customers")
plt.show()
category_sales = transactions.merge(products, on="ProductID").groupby("Category")["TotalValue"].sum()
category_sales.sort_values(ascending=False).plot(kind="bar", color="orange")
plt.title("Sales by Product Category")
plt.ylabel("Total Revenue (USD)")
plt.show()
monthly_sales = transactions.groupby("Month")["TotalValue"].sum()
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Revenue Trends")
plt.ylabel("Total Revenue (USD)")
plt.show()



import plotly.express as px

# Region Distribution
region_counts = customers["Region"].value_counts().reset_index()
region_counts.columns = ["Region", "Count"]

# Plotting with Plotly
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
fig.update_layout(font=dict(size=16))
fig.show()
# Merge transactions with products
merged_data = transactions.merge(products, on="ProductID")
category_sales = merged_data.groupby("Category")["TotalValue"].sum().reset_index()

# Plotting with Plotly
fig = px.pie(
    category_sales,
    names="Category",
    values="TotalValue",
    title="Revenue by Product Category",
    template="presentation",
    hole=0.4,
)
fig.update_traces(textinfo="percent+label")
fig.show()
monthly_sales = transactions.groupby("Month")["TotalValue"].sum().reset_index()

# Plotting with Plotly
fig = px.line(
    monthly_sales,
    x="Month",
    y="TotalValue",
    title="Monthly Revenue Trends",
    markers=True,
    template="ggplot2",
    color_discrete_sequence=["green"],
)
fig.update_traces(line=dict(width=3), marker=dict(size=10, symbol="circle"))
fig.show()
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# Data Preparation
monthly_sales_sorted = monthly_sales.sort_values(by="Month")
months = monthly_sales_sorted["Month"].astype(str)
values = monthly_sales_sorted["TotalValue"]

# Initialize Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Animated Monthly Revenue Growth", fontsize=16, color="darkblue")
ax.set_xlabel("Month", fontsize=14)
ax.set_ylabel("Total Revenue (USD)", fontsize=14)
bar = ax.bar(months, [0]*len(months), color="skyblue")

# Animation Function
def update(frame):
    for idx, rect in enumerate(bar):
        rect.set_height(values.iloc[idx] if idx <= frame else 0)
    return bar

# Animate!
ani = FuncAnimation(fig, update, frames=len(months), interval=500, repeat=False)
plt.show()
# Prepare data for heatmap
heatmap_data = merged_data.groupby(["Region", "Category"])["TotalValue"].sum().unstack()

# Heatmap Plot
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
