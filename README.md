# Azure Chatbot

This repository contains a chatbot implementation using the Azure OpenAI API. The chatbot is designed to provide helpful and accurate responses based on user input.

## Features
- Uses Azure OpenAI API for generating responses.
- Supports dynamic configuration using environment variables.
- Interactive chat loop for user input and responses.

## Prerequisites
- Python 3.8 or higher
- Azure OpenAI API key and endpoint
- `python-dotenv` library for managing environment variables

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following content:
   ```env
   ENDPOINT_URL=https://<your-endpoint>.openai.azure.com/
   DEPLOYMENT_NAME=<your-deployment-name>
   AZURE_OPENAI_API_KEY=<your-api-key>
   ```

5. Run the chatbot script:
   ```bash
   python azurechatbot.py
   ```

## Usage
- Start the chatbot by running the script.
- Enter your prompts in the console.
- Type `Q` to exit the chat loop.

## File Structure
- `azurechatbot.py`: Main script for the chatbot.
- `.env`: Environment variables for configuration.
- `requirements.txt`: List of dependencies.

## Dependencies
- `openai`
- `python-dotenv`

## License
This project is licensed under the MIT License.
