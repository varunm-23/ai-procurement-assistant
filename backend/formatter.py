def format_answer(question, result):

    if isinstance(result, dict) and "error" in result:
        return "Sorry, I could not process your request."

    if not result:
        return "No matching records found."

    q = question.lower()
    first = result[0]

    # Total spending
    if "total spending" in q:
        return f"Total spending was ${first['total']:,.2f}"

    # Highest supplier
    if "supplier" in q and "highest" in q:
        return f"{first['_id']} had the highest spending of ${first['total_spending']:,.2f}"

    # Highest department
    if "department" in q:
        return f"{first['_id']} spent the most with ${first['total_spending']:,.2f}"

    # Top suppliers
    if "top 5" in q:
        msg = "Top 5 suppliers by spending:\n"
        for i, row in enumerate(result, 1):
            msg += f"{i}. {row['_id']} - ${row['total_spending']:,.2f}\n"
        return msg

    # Count suppliers
    if "how many suppliers" in q:
        return f"Total suppliers: {first['count']}"

    # Average
    if "average" in q:
        return f"Average purchase amount is ${first['average']:,.2f}"

    # Latest purchases
    if "latest" in q:
        return f"I found {len(result)} latest purchases."

    return f"I found {len(result)} matching records."
