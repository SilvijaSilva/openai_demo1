
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()  

token = os.getenv("MY_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-nano"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
# ask the user for a question
question = input("Įveskite klausimą: ")

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": question,
        }
    ],
    temperature=1.0,
    top_p=1.0,
    model=model
)

print("\nAtsakymas:\n")
print(response.choices[0].message.content)