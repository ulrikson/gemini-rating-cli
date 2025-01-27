"""
This module provides chat functionality for the Gemini AI model.
"""

from typing import List, Dict
from google.generativeai.types import GenerateContentResponse
from gemini import GeminiClient


class ChatManager:
    """
    Manages chat sessions with the Gemini AI model.
    """

    def __init__(self, client: GeminiClient):
        """
        Initialize the chat manager.

        Args:
            client: The GeminiClient instance to use for chat
        """
        self._client = client
        self._history: List[Dict[str, str]] = []

    def start_new_chat(self) -> None:
        """
        Start a new chat session.
        """
        self._history = []

    def send_message(self, message: str) -> GenerateContentResponse:
        """
        Send a message in the current chat session.

        Args:
            message: The message to send

        Returns:
            The generated response
        """
        # Add user message to history
        self._history.append({"role": "user", "text": message})

        # Create a context-aware prompt with chat history
        history_prompt = "\n".join(
            [f"{msg['role']}: {msg['text']}" for msg in self._history]
        )
        response = self._client.generate_content(history_prompt)

        # Add assistant's response to history
        response_text = self.get_response_text(response)
        self._history.append({"role": "assistant", "text": response_text})

        return response

    def get_history(self) -> List[Dict[str, str]]:
        """
        Get the current chat history.

        Returns:
            List of message dictionaries containing role and text
        """
        return self._history

    def get_first_user_message(self) -> str:
        """
        Get the first message sent by the user in the chat.

        Returns:
            The first user message text, or empty string if none exists
        """
        return next((msg["text"] for msg in self._history if msg["role"] == "user"), "")

    def get_last_assistant_message(self) -> str:
        """
        Get the last message sent by the assistant in the chat.

        Returns:
            The last assistant message text, or empty string if none exists
        """
        return next(
            (
                msg["text"]
                for msg in reversed(self._history)
                if msg["role"] == "assistant"
            ),
            "",
        )

    def get_response_text(self, response: GenerateContentResponse) -> str:
        """
        Extract text from a generation response.

        Args:
            response: The generation response from Gemini

        Returns:
            The extracted text content
        """
        return self._client.get_response_text(response)
