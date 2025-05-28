# This script demonstrates how to use the OpenAI API to generate a joke in Lithuanian.
# using the OpenAI Python client library.

import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  
# Load environment variables from .env file

token = os.getenv("MY_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

# initialize the OpenAI client
# Note: The OpenAI client is initialized with the base URL and API key.

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Tell me a better joke about Vilnius. Always respond in Lithuanian.",
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print(response.choices[0].message.content)
# force to answer in Lithuanian
