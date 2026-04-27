import json
from db import collection

def run_query(query_text):
    try:
        pipeline = json.loads(query_text)

        if isinstance(pipeline, list):
            result = list(collection.aggregate(pipeline))
        else:
            result = list(collection.find(pipeline).limit(10))

        return result

    except Exception as e:
        return {"error": str(e)}







# import json
# from db import collection

# def run_query(query_text):
#     try:
#         pipeline = json.loads(query_text)

#         if isinstance(pipeline, list):
#             result = list(collection.aggregate(pipeline))
#         else:
#             result = list(collection.find(pipeline).limit(10))

#         return result

#     except Exception as e:
#         return {"error": str(e)}