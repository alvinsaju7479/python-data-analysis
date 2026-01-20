import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
data = {
    "product": ["A", "B", "C", "D"],
    "sales": [1200, 850, 430, 670]
}

df = pd.DataFrame(data)

# Basic analysis
total_sales = df["sales"].sum()
print("Total Sales:", total_sales)

# Plot
df.plot(x="product", y="sales", kind="bar", legend=False)
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
