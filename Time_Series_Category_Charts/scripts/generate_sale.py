import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
NUM_RECORDS = 1200
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2024, 12, 31)

CATEGORIES = {
    "Electronics": (8000, 25000),
    "Clothing": (3000, 15000),
    "Furniture": (5000, 20000),
    "Groceries": (1000, 8000),
    "Books": (500, 6000)
}

# Generate random dates
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

data = []

for _ in range(NUM_RECORDS):
    category = random.choice(list(CATEGORIES.keys()))
    min_sale, max_sale = CATEGORIES[category]

    data.append({
        "Date": random_date(START_DATE, END_DATE).strftime("%Y-%m-%d"),
        "Category": category,
        "Sales": random.randint(min_sale, max_sale)
    })

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date (important for time series)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Save CSV
df.to_csv("data/sales_data.csv", index=False)

print("✅ sales_data.csv generated with", len(df), "records")
