# SALES DATA ANALYTICS PROJECT

# IMPORT LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATASET

df = pd.read_csv("sales_data.csv")

# DATA PREVIEW

print(df.head())

# DATA INFO

print(df.info())


# DATA CLEANING


# CHECK NULL VALUES

print(df.isnull().sum())

# FEATURE ENGINEERING

df["Profit"] = (
    (df["Unit_Price"] - df["Unit_Cost"])
    * df["Quantity_Sold"]
)

# CONVERT DATE COLUMN

df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# CREATE MONTH COLUMN

df["Month"] = df["Sale_Date"].dt.strftime("%b")


# TOTAL REVENUE


total_revenue = df["Sales_Amount"].sum()

print("Total Revenue:", total_revenue)


# TOTAL PROFIT


total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)


# REGION WISE SALES


region_sales = (df.groupby("Region")["Sales_Amount"].sum())

print(region_sales)

# BAR CHART

region_sales.plot(kind="bar",figsize=(8,5))
plt.title("Region Wise Revenue")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()


# PRODUCT CATEGORY ANALYSIS


category_sales = (df.groupby("Product_Category")["Sales_Amount"].sum())

print(category_sales)

# PIE CHART

category_sales.plot(kind="pie",autopct='%1.1f%%',figsize=(7,7))
plt.title("Category Wise Sales")
plt.ylabel("")
plt.show()


# TOP SALES REPRESENTATIVE


top_sales_rep = (df.groupby("Sales_Rep")["Sales_Amount"].sum().sort_values(ascending=False))

print(top_sales_rep)


# PAYMENT METHOD ANALYSIS


payment_method = (df["Payment_Method"].value_counts())

print(payment_method)


# MONTHLY SALES TREND


monthly_sales = (df.groupby("Month")["Sales_Amount"].sum())

print(monthly_sales)

# LINE CHART

monthly_sales.plot(kind="line", marker="o", figsize=(8,5))

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()


# CUSTOMER TYPE ANALYSIS


customer_analysis = (df.groupby("Customer_Type")["Sales_Amount"].sum())

print(customer_analysis)


# PROFIT ANALYSIS

profit_analysis = (df.groupby("Product_Category")["Profit"].sum())

print(profit_analysis)


# BUSINESS INSIGHTS


print("\n------ BUSINESS INSIGHTS ----------")

print(
    "Top Region:",df.groupby("Region")["Sales_Amount"].sum().idxmax())

print(
    "Top Product Category:",df.groupby("Product_Category")["Sales_Amount"].sum().idxmax())

print(
    "Best Sales Representative:",df.groupby("Sales_Rep")["Sales_Amount"].sum().idxmax())

print(
    "Most Used Payment Method:",df["Payment_Method"].mode()[0])
