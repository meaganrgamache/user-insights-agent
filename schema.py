# schema.py

customer_insights_schema = {
    "name": "extract_customer_insights",
    "description": "Extract structured customer insights from Gong call transcript.",
    "parameters": {
        "type": "object",
        "properties": {
            "sentiment": {
                "type": "string",
                "enum": ["Positive", "Neutral", "Negative"],
                "description": "Overall sentiment of the customer during the conversation."
            },
            "requirements": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Explicit and inferred customer requirements."
            },
            "pulls": {
                "type": "array",
                "items": {"type": "string"},
                "description": "The factors motivating this customer to consider a solution like Render."
            },
            "pushes": {
                "type": "array",
                "items": {"type": "string"},
                "description": "The factors that may lead this customer to not choose Render."
            }
        },
        "required": ["sentiment", "requirements", "pulls", "pushes"]
    }
}

