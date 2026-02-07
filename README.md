# Banking Bot - Powered by Mistral AI Large

A conversational banking assistant built with Mistral AI Large that provides banking-related assistance.

## Features

- 💬 Conversational interface with Mistral AI Large
- 🏦 Banking-specific assistance (balance, transfers, bills, etc.)
- 📝 Conversation history tracking
- 🔒 Secure API key management via environment variables
- 🔄 Conversation reset capability

## Setup

### 1. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

The `.env` file already contains your Mistral API key.

**Important**: Never commit `.env` to version control. The `.gitignore` is configured to prevent this.

## Usage

Run the banking bot:

```bash
python banking_bot.py
```

### Interactive Commands

- **Type your question**: Ask any banking-related question
- **quit**: Exit the application
- **reset**: Clear conversation history

### Example Interactions

```
You: What services do you offer?
Bot: I can help you with account balance inquiries, transaction history, fund transfers...

You: How can I check my balance?
Bot: To check your balance, you can typically log into your online banking portal...

You: reset
Conversation history cleared.
```

## Project Structure

```
Final Banking bot 7th fab/
├── banking_bot.py          # Main bot application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (API key)
├── .gitignore             # Git ignore file
├── README.md              # This file
└── venv/                  # Virtual environment
```

## Mistral AI Model

This bot uses the **mistral-large-latest** model for:
- Advanced reasoning and understanding
- Better context awareness
- More natural conversations
- Financial domain knowledge

## Security Notes

- Never share your API key
- Keep `.env` file local and never commit to version control
- Always use environment variables for sensitive data
- The bot is designed to avoid handling actual banking credentials

## Troubleshooting

### Import Error: `mistralai`
Make sure you've installed requirements:
```bash
pip install -r requirements.txt
```

### API Key Error
Verify your `.env` file contains a valid Mistral API key:
```bash
MISTRAL_API_KEY=your_key_here
```

### Connection Error
Check your internet connection and ensure the Mistral API is accessible.

## License

Private Project
