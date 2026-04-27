import pandas as pd
from pymongo import MongoClient

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["procurement_db"]
collection = db["orders"]

# Load CSV
df = pd.read_csv("D:/pennySoft_assessment/project/data/PURCHASE_ORDER_DATA.csv", low_memory=False)

# Convert NaN to None
df = df.where(pd.notnull(df), None)

# Insert into MongoDB
data = df.to_dict(orient="records")

print("Inserting data into MongoDB...")
collection.insert_many(data)

print("✅ Data loaded successfully!")