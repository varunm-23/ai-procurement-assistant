import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_mongo_query(user_question):

    q = user_question.lower()

    # Rule based stable queries

    if "total spending" in q:
        return json.dumps([
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$Total Price"}
                }
            }
        ])

    elif "highest spending" in q and "supplier" in q:
        return json.dumps([
            {
                "$group": {
                    "_id": "$Supplier Name",
                    "total_spending": {"$sum": "$Total Price"}
                }
            },
            {"$sort": {"total_spending": -1}},
            {"$limit": 1}
        ])

    elif "department" in q and "most" in q:
        return json.dumps([
            {
                "$group": {
                    "_id": "$Department Name",
                    "total_spending": {"$sum": "$Total Price"}
                }
            },
            {"$sort": {"total_spending": -1}},
            {"$limit": 1}
        ])

    elif "top 5 suppliers" in q:
        return json.dumps([
            {
                "$group": {
                    "_id": "$Supplier Name",
                    "total_spending": {"$sum": "$Total Price"}
                }
            },
            {"$sort": {"total_spending": -1}},
            {"$limit": 5}
        ])

    elif "how many suppliers" in q:
        return json.dumps([
            {"$group": {"_id": "$Supplier Name"}},
            {"$count": "count"}
        ])

    elif "average purchase" in q:
        return json.dumps([
            {
                "$group": {
                    "_id": None,
                    "average": {"$avg": "$Total Price"}
                }
            }
        ])

    # fallback AI if unknown query
    prompt = f"""
Convert to MongoDB JSON array only.

Question: {user_question}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama:1.1b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
