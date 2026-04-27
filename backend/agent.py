import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_mongo_query(user_question):

    # reliable hardcoded queries first
    q = user_question.lower()

    if "total spending" in q:
        return """
[
  {
    "$group": {
      "_id": null,
      "total": { "$sum": "$Total Price" }
    }
  }
]
"""

    if "highest spending supplier" in q or "supplier has the highest spending" in q:
        return """
[
  {
    "$group": {
      "_id": "$Supplier Name",
      "total_spending": { "$sum": "$Total Price" }
    }
  },
  { "$sort": { "total_spending": -1 } },
  { "$limit": 1 }
]
"""

    prompt = f"""
Return ONLY valid MongoDB JSON array.
No explanation.
No markdown.

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

    raw = response.json()["response"].strip()

    # extract JSON array only
    match = re.search(r'\[.*\]', raw, re.DOTALL)

    if match:
        return match.group(0)

    return "[]"







# import requests

# OLLAMA_URL = "http://localhost:11434/api/generate"

# def generate_mongo_query(user_question):

#     prompt = f"""
# You are a MongoDB expert.

# Convert the user question into valid MongoDB aggregation JSON only.

# Return ONLY JSON array.

# Examples:

# Question: Which department spent the most money?
# [
#   {{
#     "$group": {{
#       "_id": "$Department Name",
#       "total_spending": {{ "$sum": "$Total Price" }}
#     }}
#   }},
#   {{ "$sort": {{ "total_spending": -1 }} }},
#   {{ "$limit": 1 }}
# ]

# Question: {user_question}
# """

#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": "tinyllama:1.1b",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     return response.json()["response"].strip()







# import requests
# import json
# import re

# OLLAMA_URL = "http://localhost:11434/api/generate"

# def generate_mongo_query(user_question):
#     prompt = f"""
# You are a MongoDB expert.

# Convert the user question into ONLY valid JSON MongoDB aggregation pipeline.

# Rules:
# 1. Output only JSON array
# 2. No explanation
# 3. No markdown
# 4. No text before or after JSON

# Example:
# [
#   {{
#     "$group": {{
#       "_id": null,
#       "total": {{ "$sum": "$Total Price" }}
#     }}
#   }}
# ]

# Question: {user_question}
# """

#     response = requests.post(
#         OLLAMA_URL,
#         json={
#             "model": "tinyllama:1.1b",
#             "prompt": prompt,
#             "stream": False
#         }
#     )

#     raw = response.json()["response"].strip()

#     # extract JSON array only
#     match = re.search(r'\[.*\]', raw, re.DOTALL)
#     if match:
#         return match.group(0)

#     return raw