# Chatbot Project

This repository contains two chatbot implementations: one using Azure OpenAI API and another using Anthropic's Claude API. Both chatbots provide helpful and accurate responses based on user input with conversational memory.

## Features
- **Azure OpenAI Chatbot**: Uses Azure OpenAI API for generating responses
- **Claude Chatbot**: Uses Anthropic's Claude API for generating responses
- Conversational memory: Maintains chat history throughout the session
- Dynamic configuration using environment variables
- Interactive chat loop for continuous user input and responses

## Prerequisites
- Python 3.8 or higher
- Azure OpenAI API key and endpoint (for Azure chatbot)
- Anthropic API key (for Claude chatbot)
- `python-dotenv` library for managing environment variables

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv aienv
   # On Windows
   aienv\Scripts\activate
   # On macOS/Linux
   source aienv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```env
   # Azure OpenAI Configuration
   ENDPOINT_URL=https://<your-endpoint>.openai.azure.com/
   DEPLOYMENT_NAME=<your-deployment-name>
   AZURE_OPENAI_API_KEY=<your-api-key>

   # Anthropic Claude Configuration
   ANTHROPIC_CLAUDE_API_KEY=<your-anthropic-api-key>
   ```

5. Run the desired chatbot script:
   ```bash
   # For Azure OpenAI chatbot
   python azurechatbot.py

   # For Claude chatbot
   python claudebot.py
   ```

## Usage
- Start the chatbot by running either script
- Enter your prompts in the console
- The chatbot maintains conversation history, allowing contextual responses
- Type `Q` to exit the chat loop

## File Structure
- `azurechatbot.py`: Azure OpenAI chatbot implementation
- `claudebot.py`: Anthropic Claude chatbot implementation
- `.env`: Environment variables for configuration (not tracked in git)
- `requirements.txt`: List of Python dependencies
- `README.md`: Project documentation

## Available Claude Models
The Claude chatbot uses the following model by default:
- `claude-haiku-4-5-20251001`: Claude Haiku 4.5 (fastest, most cost-effective)

Alternative models (commented in code):
- `claude-sonnet-4-5-20250929`: Claude Sonnet 4.5 (best for coding and complex tasks)

## Dependencies
- `openai`: Azure OpenAI API client
- `anthropic`: Anthropic Claude API client
- `python-dotenv`: Environment variable management

## License
This project is licensed under the MIT License.
