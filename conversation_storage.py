"""
This module handles the persistence of conversations for fine-tuning purposes.
"""

import json
import os
from abc import ABC, abstractmethod
from typing import List, Dict


class ConversationStorageInterface(ABC):
    """
    Abstract base class defining the interface for conversation storage.
    """

    @abstractmethod
    def save_full_conversation(
        self, messages: List[Dict[str, str]], rating: int
    ) -> None:
        """
        Save a full conversation history with its rating.

        Args:
            messages: List of message dictionaries containing role and text
            rating: The user's rating (1-5)
        """
        pass


class JSONConversationStorage(ConversationStorageInterface):
    """
    Concrete implementation of conversation storage using JSON.
    """

    def __init__(self, file_path: str = "conversations.json"):
        """
        Initialize the JSON storage.

        Args:
            file_path: Path to the JSON file
        """
        self._file_path = file_path
        self._ensure_json_exists()

    def _ensure_json_exists(self) -> None:
        """
        Ensure the JSON file exists with proper structure.
        """
        if not os.path.exists(self._file_path):
            with open(self._file_path, "w") as f:
                json.dump({"conversations": []}, f)

    def save_full_conversation(
        self, messages: List[Dict[str, str]], rating: int
    ) -> None:
        """
        Save a full conversation history to the JSON file.

        Args:
            messages: List of message dictionaries containing role and text
            rating: The user's rating (1-5)

        Raises:
            ValueError: If rating is not between 1 and 5
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        conversation = {"messages": messages, "rating": rating}

        self._save_to_json(conversation)

    def _save_to_json(self, conversation: Dict) -> None:
        """
        Save a conversation to the JSON file.

        Args:
            conversation: The conversation dictionary to save
        """
        try:
            # Read existing conversations
            with open(self._file_path, "r") as f:
                data = json.load(f)

            # Add new conversation
            data["conversations"].append(conversation)

            # Write back to file
            with open(self._file_path, "w") as f:
                json.dump(data, f, indent=2)

            print(
                f"Conversation saved successfully with rating {conversation['rating']}/5"
            )
        except Exception as e:
            print(f"Error saving conversation: {e}")
