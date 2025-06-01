
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

with open("birzai.txt", "r", encoding="utf-8") as file:
    birzai_text = file.read()

print("\nSveiki atvykę į Jūsų AI asistentą! \nUžduokite klausimą apie Biržus.\nNorėdami išeiti, įveskite 'exit'.\n")

messages = []

while True:
    user_input = input("Jūsų klausimas: ")

    if user_input.lower() == "exit":
        print("Išeinama iš programos")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=[
            {"role": "system","content": "You are a helpful assistant. Use the following context about Biržai to answer the user's questions."},
            {"role": "system","content": birzai_text},
            {"role": "user","content": user_input}
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    answer = response.choices[0].message.content
    print("\nAtsakymas:", answer, "\n")