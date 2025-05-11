import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

while True:
    user_message = input("\nEnter your Question (or 'quit' to exit) : ")

    if user_message.lower() == "quit":
        print("Thanks for chatting! Goodbye!")
        break

    response = model.generate_content(user_message)

    print("\nResponse : ",response.text)