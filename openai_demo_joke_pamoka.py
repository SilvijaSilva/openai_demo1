
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  
# Load environment variables from .env file

token = os.getenv("MY_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

def setup_client():
    return OpenAI(
        base_url=endpoint,
        api_key=token,
    )

def generate_joke(client):

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Only answer in Lithuanian.",
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

    return response.choices[0].message.content

def write_to_file(joke):
    with open("joke.txt", "w") as file:
        file.write(joke)

client = setup_client()

joke = generate_joke(client)

write_to_file(joke)
