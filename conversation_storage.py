"""
This module handles the persistence of conversations for fine-tuning purposes.
"""

import csv
import os
from abc import ABC, abstractmethod


class ConversationStorageInterface(ABC):
    """
    Abstract base class defining the interface for conversation storage.
    """

    @abstractmethod
    def save_conversation(self, text_input: str, output: str, rating: int) -> None:
        """
        Save a conversation with its rating.

        Args:
            text_input: The user's input text
            output: The model's output text
            rating: The user's rating (1-5)
        """
        pass


class CSVConversationStorage(ConversationStorageInterface):
    """
    Concrete implementation of conversation storage using CSV.
    """

    def __init__(self, file_path: str = "examples.csv"):
        """
        Initialize the CSV storage.

        Args:
            file_path: Path to the CSV file
        """
        self._file_path = file_path
        self._ensure_csv_exists()

    def _ensure_csv_exists(self) -> None:
        """
        Ensure the CSV file exists with proper headers.
        """
        if not os.path.exists(self._file_path):
            with open(self._file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["textInput", "output", "rating"])

    def save_conversation(self, text_input: str, output: str, rating: int) -> None:
        """
        Save a conversation to the CSV file.

        Args:
            text_input: The user's input text
            output: The model's output text
            rating: The user's rating (1-5)

        Raises:
            ValueError: If rating is not between 1 and 5
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        try:
            with open(self._file_path, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([text_input, output, rating])
            print(f"Conversation saved successfully with rating {rating}/5")
        except Exception as e:
            print(f"Error saving conversation: {e}")
