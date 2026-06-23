import os
from dotenv import load_dotenv
from openai import OpenAI
 
 
def build_messages(user_input: str) -> list[dict]:
    """
    Builds a structured message payload for the LLM.
    Separates system instructions from user input.
    """
    return [
        {
            "role": "system",
            "content": (
                "You are a helpful AI assistant. "
                "Be concise, accurate, and clear. "
                "If you are unsure, say you are unsure."
            ),
        },
        {
            "role": "user",
            "content": user_input,
        },
    ]
 
 
def call_llm(client: OpenAI, user_input: str) -> str:
    """
    Sends a request to the LLM API and returns the text output.
    """
    messages = build_messages(user_input)
 
    response = client.chat.completions.create(
        model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
        messages=messages,
        temperature=0.2,
        max_tokens=300,
    )
 
    return response.choices[0].message.content.strip()
 
 
def main():
    """
    Entry point for the CLI assistant.
    """
    load_dotenv()
 
    api_key = os.getenv("OPENAI_API_KEY")
    base_url= os.getenv("OPEN_API_URL")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY not found. "
            "Create a .env file and add your API key."
        )
 
    client = OpenAI(base_url=base_url, api_key=api_key)
 
    print("CLI AI Assistant")
    print("Type 'exit' or 'quit' to end the session.\n")
 
    while True:
        user_input = input("You: ").strip()
 
        if user_input.lower() in {"exit", "quit","bye"}:
            print("Goodbye.")
            break
 
        if not user_input:
            print("Please enter a prompt.")
            continue
 
        try:
            answer = call_llm(client, user_input)
            print("\nAssistant:", answer, "\n")
        except Exception as e:
            print("\nError calling the AI model:")
            print(str(e), "\n")
 
 
if __name__ == "__main__":
    main()