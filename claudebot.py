import anthropic
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
subscription_key = os.getenv("ANTHROPIC_CLAUDE_API_KEY")

# Initialize Anthropic client with API key
client = anthropic.Anthropic(
    api_key=subscription_key
)

# Define the system message for the chatbot
# This message sets the behavior of the chatbot
system_message = "You are a helpful assistant to provide accurate information as much as you can."

# Initialize the chat messages with the system message
chat_messages = []

# Start the chatbot loop
# The user can input prompts, and the chatbot will respond
user_prompt = input("User prompt (to stop, type `Q`): ")
# Start while loop
while not user_prompt == "Q":
    # Append the user prompt to the chat history
    chat_messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Generate the chatbot's response
    # model: Claude model to use
    # system: System message defining chatbot behavior
    # max_tokens: Maximum number of tokens in the response
    # messages: Chat history including user and assistant messages
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # Claude Haiku 4.5 (fastest, most cost-effective)
        #model="claude-sonnet-4-5-20250929",  # Claude Sonnet 4.5 (best for coding)
        system=system_message,
        max_tokens=1024,
        messages=chat_messages
    )
    response = message.content[0].text

    # Extract and print the chatbot's response
    print("Response: >>>>", response, "<<<<")

    # Append the chatbot's response to the chat history
    chat_messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
    # Prompt the user for the next input
    user_prompt = input("User prompt (to stop, type `Q`): ")

# Exit the chatbot loop when the user types 'Q'
# The program ends here
