"""
This module provides chat functionality for the Gemini AI model.
"""

from typing import List, Dict
from google.generativeai.types import GenerateContentResponse
from gemini import GeminiClient


class ChatManager:
    """
    Manages chat sessions with the Gemini AI model.
    Follows Single Responsibility Principle by handling only chat-related operations.
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

    def get_response_text(self, response: GenerateContentResponse) -> str:
        """
        Extract text from a generation response.

        Args:
            response: The generation response from Gemini

        Returns:
            The extracted text content
        """
        return self._client.get_response_text(response)
