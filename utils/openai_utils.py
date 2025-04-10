import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")




if api_key is None:
    raise ValueError("API key not found. Please check your .env file.")

client = OpenAI(api_key=api_key)


def get_resume_response(prompt: str, api_key: str, model="gpt-4o-mini", temperature=0.7) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a career expert helping with resume optimization."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature
    )
    return response.choices[0].message.content
