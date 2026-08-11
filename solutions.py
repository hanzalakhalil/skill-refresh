"""
Solutions for pandas_exercises.py — only check AFTER attempting.
"""

import pandas as pd

sales = pd.read_csv("sales.csv", parse_dates=["date"])
customers = pd.read_csv("customers.csv")
sales["revenue"] = sales["quantity"] * sales["unit_price"]

# 1.1
revenue_by_product = sales.groupby("product")["revenue"].sum()

# 1.2
qty_by_region = sales.groupby("region")["quantity"].sum().sort_values(ascending=False)

# 1.3
avg_order_by_category = sales.groupby("category")["revenue"].mean()

# 1.4
orders_by_region_category = sales.groupby(["region", "category"]).size()

# 2.1
sales_with_customers = sales.merge(customers, on="customer_id", how="left")

# 2.2
revenue_by_tier = sales_with_customers.groupby("tier")["revenue"].sum()

# 2.3
merged_check = sales.merge(customers, on="customer_id", how="outer", indicator=True)
orphaned = merged_check[merged_check["_merge"] == "left_only"]

# 3.1
pivot_revenue = sales.pivot_table(index="region", columns="category", values="revenue", aggfunc="sum")

# 3.2
pivot_qty = sales.pivot_table(index="product", columns="region", values="quantity", aggfunc="sum", fill_value=0)

# 3.3
revenue_by_week = sales.groupby(sales["date"].dt.to_period("W"))["revenue"].sum()

if __name__ == "__main__":
    print("Revenue by product:\n", revenue_by_product, "\n")
    print("Quantity by region:\n", qty_by_region, "\n")
    print("Avg order by category:\n", avg_order_by_category, "\n")
    print("Orders by region+category:\n", orders_by_region_category, "\n")
    print("Merged sample:\n", sales_with_customers.head(), "\n")
    print("Revenue by tier:\n", revenue_by_tier, "\n")
    print("Orphaned records:\n", orphaned, "\n")
    print("Pivot revenue:\n", pivot_revenue, "\n")
    print("Pivot qty:\n", pivot_qty, "\n")
    print("Revenue by week:\n", revenue_by_week, "\n")
