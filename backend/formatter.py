def format_answer(question, result):

    if isinstance(result, dict) and "error" in result:
        return "Sorry, I could not process your request."

    if not result:
        return "No matching records found."

    first = result[0]

    # Spending questions
    if "spend" in question.lower() or "money" in question.lower():

        if "_id" in first and "total_spending" in first:
            return f"{first['_id']} had the highest spending of ${round(first['total_spending'],2):,}"

        if "total" in first:
            if first["_id"] is None:
                return f"Total spending was ${round(first['total'],2):,}"
            return f"{first['_id']} total spending was ${round(first['total'],2):,}"
        
        # if "_id" in first and "total" in first:
        #     return f"{first['_id']} total spending was ${round(first['total'],2):,}"

    # Count questions
    if "count" in first:
        return f"{first['_id']} has {first['count']} records."

    # Generic fallback
    return f"I found {len(result)} matching records."