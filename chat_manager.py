"""
This module provides chat functionality for the Gemini AI model.
Following SOLID principles by separating chat management from basic API interactions.
"""

from typing import List, Dict, Optional
import google.generativeai as genai
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
        self._chat = None
        self.start_new_chat()

    def start_new_chat(self) -> None:
        """
        Start a new chat session.
        """
        self._chat = self._client.get_model().start_chat(history=[])

    def send_message(self, message: str) -> GenerateContentResponse:
        """
        Send a message in the current chat session.

        Args:
            message: The message to send

        Returns:
            The generated response
        """
        if not self._chat:
            self.start_new_chat()
        return self._chat.send_message(message)

    def get_history(self) -> List[Dict[str, str]]:
        """
        Get the current chat history.

        Returns:
            List of message dictionaries containing role and text
        """
        return self._chat.history if self._chat else []

    def get_response_text(self, response: GenerateContentResponse) -> str:
        """
        Extract text from a generation response.

        Args:
            response: The generation response from Gemini

        Returns:
            The extracted text content
        """
        return self._client.get_response_text(response) 