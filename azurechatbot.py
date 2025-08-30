# Relearn how to write a chatbot using Azure OpenAI API call

# Import necessary libraries
import os
from openai import AzureOpenAI
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Retrieve settings from environment variables
# ENDPOINT_URL: Azure OpenAI endpoint URL
# DEPLOYMENT_NAME: Name of the deployment
# AZURE_OPENAI_API_KEY: API key for authentication
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

print(endpoint, deployment, subscription_key)

# Initialize Azure OpenAI client with key-based authentication
# azure_endpoint: Endpoint URL for Azure OpenAI
# api_key: API key for authentication
# api_version: Version of the Azure OpenAI API
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Define the system message for the chatbot
# This message sets the behavior of the chatbot
system_message = "You are a helpful assistant to provide accurate information as much as you can."

# Initialize the chat prompt with the system message
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": system_message
            }
        ]
    },
]

# Start the chatbot loop
# The user can input prompts, and the chatbot will respond
user_prompt = input("User prompt (to stop, type `Q`): ")
# Start while loop
while not user_prompt == "Q":
    # Append the user prompt to the chat history
    chat_prompt.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                }
            ]
        }
    )

    # Generate the chatbot's response
    # model: Deployment name of the Azure OpenAI model
    # messages: Chat history including system and user messages
    # max_tokens: Maximum number of tokens in the response
    # temperature: Controls randomness in the response
    # top_p: Controls diversity via nucleus sampling
    # frequency_penalty: Penalizes new tokens based on their frequency
    # presence_penalty: Penalizes new tokens based on their presence
    completion = client.chat.completions.create(
        model=deployment,
        messages=chat_prompt,
        max_tokens=1638,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )
    response = completion.choices[0].message.content
    
    # Extract and print the chatbot's response
    print("Response: >>>>", response, "<<<<")

    # Append the chatbot's response to the chat history
    chat_prompt.append(
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": response
                }
            ]
        }
    )
    # Prompt the user for the next input
    user_prompt = input("User prompt (to stop, type `Q`): ")

# Exit the chatbot loop when the user types 'Q'
# The program ends here