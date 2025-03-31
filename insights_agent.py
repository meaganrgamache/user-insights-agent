# insights_agent.py

import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from schema import customer_insights_schema

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key
client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

def extract_insights(transcript):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert analyst of customer conversations. Extract structured insights carefully."},
            {"role": "user", "content": f"Here is a Gong call transcript:\n\n{transcript}"}
        ],
        tools=[{
            "type": "function",
            "function": customer_insights_schema
        }],
        tool_choice={"type": "function", "function": {"name": "extract_customer_insights"}},
        temperature=0.1
    )

    # Extract insights from the response
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls and tool_calls[0].function.arguments:
        return json.loads(tool_calls[0].function.arguments)
    return None

# Test your function with a sample transcript
if __name__ == "__main__":
    sample_transcript = """
    Customer: We've really liked how easy Render makes deployment, and the developer experience is excellent. But we're facing issues scaling our databases, and some enterprise compliance features are missing. We're motivated by ease of use, developer productivity, and reducing infrastructure management. However, concerns include database scaling difficulties and missing enterprise features.
    """

    insights = extract_insights(sample_transcript)
    print(json.dumps(insights, indent=4))

