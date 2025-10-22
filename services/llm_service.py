import os
import openai  # ← Import module, not class
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # ← Set globally

def process_llm_message(message: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error calling OpenAI: {str(e)}"