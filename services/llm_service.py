import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Send message to OpenAI and get the response
def process_llm_message(message:str):
    try:
        response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":message}]
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error calling OpenAI: {str(e)}"