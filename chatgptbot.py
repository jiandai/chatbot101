# Chatbot using OpenAI GPT API

# Import necessary libraries
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

# Define the system message for the chatbot
# This message sets the behavior of the chatbot
system_message = "You are a helpful assistant to provide accurate information as much as you can."

# Initialize the chat messages with the system message
chat_messages = [
    {
        "role": "system",
        "content": system_message
    }
]

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
    # model: OpenAI model to use
    # messages: Chat history including system, user, and assistant messages
    # max_tokens: Maximum number of tokens in the response
    # temperature: Controls randomness in the response
    # top_p: Controls diversity via nucleus sampling
    completion = client.chat.completions.create(
        model="gpt-5-nano",  # GPT-5 nano (fast and cost-effective)
        #model="gpt-4o",  # GPT-4o (most capable)
        messages=chat_messages,
        max_tokens=1024,
        temperature=0.7,
        top_p=0.95
    )
    response = completion.choices[0].message.content

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
