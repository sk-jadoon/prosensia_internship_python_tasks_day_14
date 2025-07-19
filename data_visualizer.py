import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Load dataset (use raw string to avoid path issues)
df = pd.read_csv(r"C:\Users\Sidra\Downloads\sales.csv")

# Clean the data
df.dropna(inplace=True)

# Line Chart: Monthly Revenue
def plot_line_chart():
    monthly = df.groupby("Month")["Revenue"].sum()
    monthly.plot(kind='line', marker='o')
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("plots/Line_Chart.png")
    plt.clf()

# Bar Chart: Product Sales
def plot_bar_chart():
    product_sales = df.groupby("Product")["Units_Sold"].sum()
    product_sales.plot(kind='bar', color='skyblue')
    plt.title("Product-wise Sales")
    plt.xlabel("Product")
    plt.ylabel("Units Sold")
    plt.tight_layout()
    plt.savefig("plots/Bar_Chart.png")
    plt.clf()

# Pie Chart: Market Share by Region
def plot_pie_chart():
    market_share = df.groupby("Region")["Revenue"].sum()
    market_share.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Market Share by Region")
    plt.ylabel("")  # Hide y-label
    plt.tight_layout()
    plt.savefig("plots/Pie_Chart.png")
    plt.clf()

# Heatmap: Correlation (only numeric columns)
def plot_heatmap():
    numeric_df = df.select_dtypes(include='number')  # Filter only numeric columns
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("plots/Heatmap.png")
    plt.clf()

# Summary Report
def generate_summary():
    with open("Summary_Report.txt", "w") as f:
        f.write("Summary Report\n")
        f.write("------------------\n")
        f.write(f"Total Revenue: {df['Revenue'].sum():.2f}\n")
        f.write(f"Best Selling Product: {df.groupby('Product')['Units_Sold'].sum().idxmax()}\n")
        f.write(f"Top Region by Revenue: {df.groupby('Region')['Revenue'].sum().idxmax()}\n")

# Execute all functions
plot_line_chart()
plot_bar_chart()
plot_pie_chart()
plot_heatmap()
generate_summary()

print(" All plots saved in /plots folder. Summary generated.")
