"""
This module provides a clean interface to interact with Google's Gemini AI model.
Following SOLID principles and Python best practices.
"""

from typing import Optional, Dict, Any
import google.generativeai as genai
from google.generativeai.types import GenerateContentResponse


class GeminiClient:
    """
    A client for interacting with Google's Gemini AI model.
    Follows Single Responsibility Principle by handling only Gemini-related operations.
    """

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        """
        Initialize the Gemini client.

        Args:
            api_key: The API key for authentication
            model_name: The specific Gemini model to use
        """
        self._configure_client(api_key)
        self.model = genai.GenerativeModel(model_name)

    def _configure_client(self, api_key: str) -> None:
        """
        Configure the Gemini client with the provided API key.

        Args:
            api_key: The API key for authentication
        """
        genai.configure(api_key=api_key)

    def get_model(self) -> genai.GenerativeModel:
        """
        Get the configured Gemini model.

        Returns:
            The configured GenerativeModel instance
        """
        return self.model

    def generate_content(self, prompt: str, **kwargs) -> GenerateContentResponse:
        """
        Generate content using the Gemini model.

        Args:
            prompt: The input prompt for content generation
            **kwargs: Additional parameters to pass to the model

        Returns:
            The generated content response
        """
        return self.model.generate_content(prompt, **kwargs)

    def get_response_text(self, response: GenerateContentResponse) -> str:
        """
        Extract text from a generation response.

        Args:
            response: The generation response from Gemini

        Returns:
            The extracted text content
        """
        return response.text
