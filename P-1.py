
import os
print("Current Working Directory:", os.getcwd())

import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# 1. Load Dataset
# ----------------------------
df = pd.read_csv("Sales.csv")

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# ----------------------------
# 2. Create Required Data
# ----------------------------

# 1️⃣ Total Sales by Category
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

# 2️⃣ Sales by Region
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

# 3️⃣ Monthly Sales Trend
df['Month'] = df['Order Date'].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

# 4️⃣ Top 5 Products
top5_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

# 5️⃣ Sales by Customer Segment
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

# ----------------------------
# 3. Save Charts
# ----------------------------

# Chart 1
plt.figure()
category_sales.plot(kind='bar')
plt.title("Total Sales by Category")
plt.tight_layout()
plt.savefig("1_total_sales_by_category.png", dpi=300)
plt.show()

# Chart 2
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.tight_layout()
plt.savefig("2_sales_by_region.png", dpi=300)
plt.show()

# Chart 3
plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.tight_layout()
plt.savefig("3_monthly_sales_trend.png", dpi=300)
plt.show()

# Chart 4
plt.figure()
top5_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.tight_layout()
plt.savefig("4_top5_products.png", dpi=300)
plt.show()

# Chart 5
plt.figure()
segment_sales.plot(kind='bar')
plt.title("Sales by Customer Segment")
plt.tight_layout()
plt.savefig("5_sales_by_segment.png", dpi=300)
plt.show()