from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

openai_client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def llm(prompt):
    response = openai_client.responses.create(
        #model="llama-3.1-8b-instant",
        model="llama-3.3-70b-versatile",
        input=prompt
    )
    return response.output_text
print(llm("Hey, what's up?"))
print("OK")
