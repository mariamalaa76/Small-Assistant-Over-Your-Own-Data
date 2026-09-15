import asyncio
from llm_client import generate_response

async def main():
    response = await generate_response(
        "In one short sentence, explain what a vector database does."
    )

    print("LLM Response:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())