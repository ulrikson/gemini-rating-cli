import os
from dotenv import load_dotenv
from gemini import GeminiClient


def main():
    # Load environment variables
    load_dotenv()

    # Initialize the Gemini client
    client = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))

    # Create an interactive loop
    print("Welcome to Gemini Chat! (Type 'quit' to exit, 'new' to start a new chat)")
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()

        # Check if user wants to quit
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        # Check if user wants to start a new chat
        if user_input.lower() == "new":
            client.start_chat()
            print("\nStarted a new chat!")
            continue

        if user_input:
            # Send message and get response
            response = client.send_message(user_input)
            print("\nGemini:", client.get_response_text(response))
        else:
            print("Please enter a valid message!")


if __name__ == "__main__":
    main()
