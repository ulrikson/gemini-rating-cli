import os
from dotenv import load_dotenv
from gemini import GeminiClient


def main():
    # Load environment variables
    load_dotenv()

    # Initialize the Gemini client
    client = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))

    # Create an interactive loop
    print("Welcome to Gemini CLI! (Type 'quit' to exit)")
    while True:
        # Get user input
        user_input = input("\nEnter your question: ").strip()

        # Check if user wants to quit
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        if user_input:
            # Generate content
            response = client.generate_content(user_input)
            print("\nGemini:", client.get_response_text(response))
        else:
            print("Please enter a valid question!")


if __name__ == "__main__":
    main()
