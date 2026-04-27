from pymongo import MongoClient
import re
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["procurement_db"]
collection = db["orders"]

print("Cleaning data...")

for doc in collection.find():
    
    update_fields = {}

    # ✅ Clean Total Price
    price = doc.get("Total Price")
    if price:
        try:
            clean_price = float(re.sub(r"[^\d.]", "", str(price)))
        except:
            clean_price = 0.0
        update_fields["Total Price"] = clean_price

    # ✅ Clean Creation Date
    date_val = doc.get("Creation Date")
    if date_val:
        try:
            clean_date = datetime.strptime(date_val, "%m/%d/%Y")
        except:
            clean_date = None
        update_fields["Creation Date"] = clean_date

    # ✅ Update document
    if update_fields:
        collection.update_one(
            {"_id": doc["_id"]},
            {"$set": update_fields}
        )

print("✅ Data cleaned!")









# import pandas as pd
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017/")
# db = client["procurement_db"]
# collection = db["orders"]

# print("Cleaning data...")

# # Convert dates
# collection.update_many(
#     {},
#     [
#         {
#             "$set": {
#                 "Creation Date": {
#                     "$toDate": "$Creation Date"
#                 }
#             }
#         }
#     ]
# )

# # Convert Total Price to number
# collection.update_many(
#     {},
#     [
#         {
#             "$set": {
#                 "Total Price": {
#                     "$toDouble": "$Total Price"
#                 }
#             }
#         }
#     ]
# )

# print("✅ Data cleaned!")