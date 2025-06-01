
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

while True:
    # ask the user for a question
    question = input("Įveskite klausimą arba žodį 'exit', norėdami išeiti: ")

    if question.lower() == "exit":
        print("Išeinama iš programos")
        break

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Always respond in Lithuanian.",
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

    print("Atsakymas:")
    print(response.choices[0].message.content)