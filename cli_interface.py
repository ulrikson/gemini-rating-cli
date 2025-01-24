"""
This module provides a command-line interface for interacting with the chat system.
"""

from chat_manager import ChatManager
from conversation_storage import CSVConversationStorage


class CLIInterface:
    """
    Handles command-line interface interactions for the chat system.
    Follows Single Responsibility Principle by handling only CLI-related operations.
    """

    def __init__(
        self, chat_manager: ChatManager, conversation_storage: CSVConversationStorage
    ):
        """
        Initialize the CLI interface.

        Args:
            chat_manager: The ChatManager instance to use for chat operations
            conversation_storage: The ConversationStorage instance to handle data persistence
        """
        self._chat_manager = chat_manager
        self._conversation_storage = conversation_storage

    def start(self) -> None:
        """
        Start the interactive CLI loop.
        """
        print(
            "Welcome to Fine Tuning Chat! (Type 'quit' to exit, 'new' to start a new chat)"
        )

        while True:
            # Get user input
            user_input = self._get_input()

            # Process commands or exit
            if self._should_exit(user_input):
                print("Goodbye!")
                break

            if self._handle_commands(user_input):
                continue

            # Process regular message
            if user_input:
                self._process_message(user_input)
            else:
                print("Please enter a valid message!")

    def _get_input(self) -> str:
        """
        Get input from the user.

        Returns:
            The cleaned user input
        """
        return input("\nYou: ").strip()

    def _should_exit(self, user_input: str) -> bool:
        """
        Check if the user wants to exit.

        Args:
            user_input: The user's input

        Returns:
            True if the user wants to exit, False otherwise
        """
        wants_to_exit = user_input.lower() in ["quit", "exit", "q"]
        if wants_to_exit:
            self._collect_conversation_feedback()
        return wants_to_exit

    def _collect_conversation_feedback(self) -> None:
        """
        Collect feedback about the conversation from the user.
        """
        if not self._chat_manager.get_history():  # No messages in history
            return

        save_response = (
            input("Do you want to save this conversation? (y/n): ").strip().lower()
        )
        if save_response == "y":
            while True:
                try:
                    rating = int(input("Please rate this conversation (1-5): ").strip())
                    if 1 <= rating <= 5:
                        self._conversation_storage.save_conversation(
                            self._chat_manager.get_first_user_message(),
                            self._chat_manager.get_last_assistant_message(),
                            rating
                        )
                        break
                    print("Please enter a number between 1 and 5")
                except ValueError:
                    print("Please enter a valid number")

    def _handle_commands(self, user_input: str) -> bool:
        """
        Handle special commands.

        Args:
            user_input: The user's input

        Returns:
            True if a command was handled, False otherwise
        """
        if user_input.lower() == "new":
            self._chat_manager.start_new_chat()
            print("\nStarted a new chat!")
            return True
        return False

    def _process_message(self, message: str) -> None:
        """
        Process a regular chat message.

        Args:
            message: The message to process
        """
        response = self._chat_manager.send_message(message)
        print("\nGemini:", self._chat_manager.get_response_text(response))
