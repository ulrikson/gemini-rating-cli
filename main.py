import os
from dotenv import load_dotenv
from gemini import GeminiClient
from chat_manager import ChatManager
from cli_interface import CLIInterface


def main():
    # Load environment variables
    load_dotenv()

    # Initialize components
    client = GeminiClient(api_key=os.getenv("GEMINI_API_KEY"))
    chat_manager = ChatManager(client)
    cli = CLIInterface(chat_manager)

    # Start the CLI interface
    cli.start()


if __name__ == "__main__":
    main()
