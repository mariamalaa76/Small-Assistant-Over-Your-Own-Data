import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"))

async def generate_response(prompt: str) -> str:
    try:
        response = await client.aio.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt,
        )
        return response.text

    except Exception as error:
        raise RuntimeError(f"Failed to generate LLM response: {error}") from error