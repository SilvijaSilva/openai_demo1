
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

#create a list to store all messages in the conversation
messages = []

messages.append({
    "role": "system", 
    "content": "You are a helpful assistant. Always respond in Lithuanian."
})

print("Sveiki atvykę į pokalbių programą su AI! Norėdami išeiti, įveskite 'exit'.")

def ask_ai(question, messages, client, model):
    messages.append({
        "role": "user",
        "content": question
    })

    response = client.chat.completions.create(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    ai_reply = response.choices[0].message.content
    messages.append({
        "role": "assistant",
        "content": ai_reply
    })
    
    return ai_reply

while True:
    # ask the user for a question
    question = input("Įveskite klausimą: ")

    if question.lower() == "exit":
        print("Išeinama iš programos")
        break

    ai_reply = ask_ai(question, messages, client, model)

    print("\n--- Pokalbis iki šiol ---")
    for message in messages:
        if message["role"] == "user":
            print("Jūs:", message["content"])
        elif message["role"] == "assistant":
            print("AI:", message["content"])
    print("-------------------------\n")