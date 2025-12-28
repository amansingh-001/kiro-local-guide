def local_guide(query):
    responses = {
        "food": "Try local street food like chaat, samosas, and pani puri.",
        "travel": "Use public transport during non-peak hours for better travel.",
        "culture": "Respect local traditions and enjoy regional festivals."
    }

    for key in responses:
        if key in query.lower():
            return responses[key]

    return "This is a simple local guide prototype."

if __name__ == "__main__":
    user_query = input("Ask the Local Guide: ")
    print(local_guide(user_query))
