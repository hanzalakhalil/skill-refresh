"""
Pandas Refresher — sales.csv + customers.csv
==============================================
Goal: rebuild fluency in groupby, merge, and pivot_table before
moving on to LLM/RAG work.

Setup (run in your activated venv):
    pip install pandas
    python pandas_exercises.py

Work through each TODO. Uncomment the print() below it to check
your answer against solutions.py once you're done.
"""

import pandas as pd

sales = pd.read_csv("sales.csv", parse_dates=["date"])
customers = pd.read_csv("customers.csv")


# print("=== sales.csv ===")
# print(sales.head())
# print("\n=== customers.csv ===")
# print(customers.head())


# ---------------------------------------------------------------
# PART 1 — GROUPBY
# ---------------------------------------------------------------

# TODO 1.1: Total revenue per product.
# Hint: create a 'revenue' column first (quantity * unit_price),
# then group by 'product' and sum it.
# revenue_by_product = ...

sales['revenue'] = sales['quantity']*sales['unit_price']

revenue_by_product = sales.groupby('product')['revenue'].mean()

# TODO 1.2: Total quantity sold per region, sorted descending.
# qty_by_region = ...

qty_by_region = sales.groupby('region')['quantity'].sum().sort_values(ascending=False)

# TODO 1.3: Average order value (revenue) per category.
# avg_order_by_category = ...

avg_order_by_category = sales.groupby('category')['revenue'].mean()

# TODO 1.4: Number of orders per region AND category at once
# (group by a list of two columns).
# orders_by_region_category = ...

orders_by_region_category = sales.groupby(["region", "category"]).size()

# ---------------------------------------------------------------
# PART 2 — MERGE
# ---------------------------------------------------------------

# TODO 2.1: Merge sales with customers on 'customer_id' so each
# order row also shows customer_name and tier.
# sales_with_customers = ...

sales_with_customers = sales.merge(customers, on="customer_id", how="left")

# TODO 2.2: Total revenue per customer tier (Gold/Silver/Bronze).
# Requires the merged dataframe from 2.1.
# revenue_by_tier = ...

revenue_by_tier = sales_with_customers.groupby('tier')['revenue'].sum()


# TODO 2.3: Find any customer_ids in sales.csv that do NOT exist
# in customers.csv (simulates a real "orphaned record" data
# quality check — common in real freelance data-cleaning gigs).
# Hint: use an outer merge with indicator=True, then filter.
# orphaned = ...

temp = pd.merge(sales, customers, on='customer_id', how='outer', indicator=True)
orphaned = temp[temp['_merge']=='right_only']

# ---------------------------------------------------------------
# PART 3 — PIVOT TABLE
# ---------------------------------------------------------------

# TODO 3.1: Pivot table — rows = region, columns = category,
# values = revenue, aggregated by sum.
# pivot_revenue = ...

pivot_revenue = sales.pivot_table(values='revenue',index = 'region', columns='category',  aggfunc='sum')

# TODO 3.2: Pivot table — rows = product, columns = region,
# values = quantity, aggregated by sum, with missing combos
# filled as 0 instead of NaN.
# pivot_qty = ...

pivot_qty = sales.pivot_table(values='quantity', index='product', columns='region', aggfunc='sum', fill_value=0)


# TODO 3.3 (stretch): Add a date-based grouping — total revenue
# per week. Hint: sales['date'].dt.to_period('W').
# revenue_by_week = ...
revenue_by_week = sales.groupby(sales['date'].dt.to_period('W'))['revenue'].sum()


# ---------------------------------------------------------------
# Uncomment as you complete each part to sanity check your work
# ---------------------------------------------------------------
print(revenue_by_product)
print(qty_by_region)
print(avg_order_by_category)
print(orders_by_region_category)
print(sales_with_customers.head())
print(revenue_by_tier)
print(orphaned)
print(pivot_revenue)
print(pivot_qty)
print(revenue_by_week)
