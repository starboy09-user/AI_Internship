from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv("day8chatbot.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("AI Chatbot Started")
print("Type 'exit' to stop")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    try:
        response = client.responses.create(
            model="gpt-5",
            input=user_input
        )

        print("\nAI:", response.output_text)

    except Exception as e:
        print("\nError:", e)