# Gemini Rating CLI

## My Goal

I was fine-tuning Gemini 2.0 Flash and needed an easy way to rate its answers. So, I created a command-line interface that includes conversation rating and storage features.

Features

- Interactive chat with Gemini X model
- Save and rate conversations for future review, e.g. to improve your own prompts or fine-tune the model
- Persistent storage of conversations in JSON format
- Simple command system (`new` for new chat, `quit` to exit)
- Environment variable configuration for API key

## Getting Started
### Prerequisites

- Python 3.x
- Google Gemini API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ulrikson/gemini-rating-cli.git
cd gemini-rating-cli
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### Usage

Run the CLI:

```bash
python main.py
```

Commands

- Type your message and press Enter to chat with Gemini
- Type `new` to start a new chat session
- Type `quit` or `exit` to end the session
  - You'll be prompted to rate and save the conversation

## Project Structure

- `main.py`: Entry point of the application
- `gemini.py`: Handles interaction with the Gemini API
- `chat_manager.py`: Manages chat sessions and history
- `cli_interface.py`: Provides the command-line interface
- `conversation_storage.py`: Handles saving and loading conversations
