# Relearn how to write a chatbot using Azure OpenAI API call

import os
from openai import AzureOpenAI
from dotenv import load_dotenv # type: ignore

# Load environment variables from .env file
load_dotenv()

# Retrieve settings from environment variables
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

print(endpoint, deployment, subscription_key)

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

# Prepare the chat prompt
system_message = "You are a helpful assistant to provide accurate information as much as you can."
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

# Get user input
user_prompt = input("User prompt (to stop, type `Q`): ")
# Start while loop
while not user_prompt == "Q":
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

    # Generate the completion
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
    
    print("Response: >>>>", response, "<<<<")
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
    user_prompt = input("User prompt (to stop, type `Q`): ")

# Stop the loop if the user types 'Q'