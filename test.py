from openai import OpenAI
import os
from dotenv import load_dotenv

# Initialize the client - it automatically uses OPENAI_API_KEY from environment variables
load_dotenv()
client = OpenAI()

# List available models
models = client.models.list()

# Iterate through models and print their IDs
for model in models.data:
    print(model.id)
