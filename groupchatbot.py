# Group Chatbot - Talk with multiple LLMs in one conversation
# Supports ChatGPT, Azure OpenAI, and Claude with @ mentions
# All LLMs share the same conversation history for context awareness

# Import necessary libraries
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI, AzureOpenAI
import anthropic

# Load environment variables from .env file
load_dotenv()

# Initialize DeepSeek client
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
deepseek_api_url = "https://api.deepseek.com/v1/chat/completions"

# Initialize ChatGPT client
chatgpt_api_key = os.getenv("OPENAI_API_KEY")
chatgpt_client = OpenAI(api_key=chatgpt_api_key)

# Initialize Azure OpenAI client
azure_endpoint = os.getenv("ENDPOINT_URL")
azure_deployment = os.getenv("DEPLOYMENT_NAME")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=azure_api_key,
    api_version="2025-01-01-preview",
)

# Initialize Claude client
claude_api_key = os.getenv("ANTHROPIC_CLAUDE_API_KEY")
claude_client = anthropic.Anthropic(api_key=claude_api_key)

# Define the system message for all chatbots
system_message = "You are a helpful assistant to provide accurate information as much as you can."

# Shared conversation history (format: [{"role": "user"/"assistant", "content": "...", "model": "chatgpt"/"azure"/"claude"}])
shared_history = []

def format_history_for_chatgpt(shared_history):
    """Convert shared history to ChatGPT format"""
    messages = [{"role": "system", "content": system_message}]
    for entry in shared_history:
        messages.append({
            "role": entry["role"],
            "content": entry["content"]
        })
    return messages

def format_history_for_deepseek(shared_history):
    """Convert shared history to DeepSeek format (OpenAI-compatible)"""
    messages = [{"role": "system", "content": system_message}]
    for entry in shared_history:
        messages.append({
            "role": entry["role"],
            "content": entry["content"]
        })
    return messages

def format_history_for_azure(shared_history):
    """Convert shared history to Azure OpenAI format"""
    messages = [
        {
            "role": "system",
            "content": [{"type": "text", "text": system_message}]
        }
    ]
    for entry in shared_history:
        messages.append({
            "role": entry["role"],
            "content": [{"type": "text", "text": entry["content"]}]
        })
    return messages

def format_history_for_claude(shared_history):
    """Convert shared history to Claude format (Claude doesn't include system message in messages array)"""
    messages = []
    for entry in shared_history:
        messages.append({
            "role": entry["role"],
            "content": entry["content"]
        })
    return messages

print("=" * 60)
print("Group Chatbot - Talk with DeepSeek, ChatGPT, Azure OpenAI, and Claude")
print("=" * 60)
print("Usage:")
print("  @deepseek <your message>    - Talk with DeepSeek")
print("  @chatgpt <your message>    - Talk with ChatGPT")
print("  @azureopenai <your message> - Talk with Azure OpenAI")
print("  @claude <your message>     - Talk with Claude")
print("  Q                          - Exit")
print("=" * 60)
print("\nAll LLMs share the same conversation context!")
print("=" * 60)

# Start the chatbot loop
user_input = input("\nYour message: ")

while user_input != "Q":
    # Check which LLM to route to based on @ mention
    if user_input.startswith("@deepseek "):
        # Extract the actual message (remove @deepseek prefix)
        user_message = user_input[10:].strip()

        if not user_message:
            print("Error: Please provide a message after @deepseek")
            user_input = input("\nYour message: ")
            continue

        if not deepseek_api_key:
            print("Error: DeepSeek API key is missing. Set DEEPSEEK_API_KEY in your environment.")
            user_input = input("\nYour message: ")
            continue

        # Add user message to shared history
        shared_history.append({
            "role": "user",
            "content": user_message,
            "model": "user"
        })

        # Format history for DeepSeek (OpenAI-compatible chat completions)
        deepseek_messages = format_history_for_deepseek(shared_history)

        try:
            response_data = requests.post(
                deepseek_api_url,
                headers={
                    "Authorization": f"Bearer {deepseek_api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "deepseek-chat",
                    "messages": deepseek_messages,
                    "max_tokens": 1024
                },
                timeout=60,
            )
            response_data.raise_for_status()
            response_json = response_data.json()
            response = response_json["choices"][0]["message"]["content"]
        except (requests.RequestException, KeyError, IndexError) as error:
            print(f"Error communicating with DeepSeek: {error}")
            shared_history.pop()
            user_input = input("\nYour message: ")
            continue

        # Print response
        print(f"\n[DeepSeek] >>>> {response} <<<<\n")

        # Add response to shared history
        shared_history.append({
            "role": "assistant",
            "content": response,
            "model": "deepseek"
        })

    elif user_input.startswith("@chatgpt "):
        # Extract the actual message (remove @chatgpt prefix)
        user_message = user_input[9:].strip()

        if not user_message:
            print("Error: Please provide a message after @chatgpt")
            user_input = input("\nYour message: ")
            continue

        # Add user message to shared history
        shared_history.append({
            "role": "user",
            "content": user_message,
            "model": "user"
        })

        # Format history for ChatGPT
        chatgpt_messages = format_history_for_chatgpt(shared_history)

        # Generate ChatGPT response
        completion = chatgpt_client.chat.completions.create(
            model="gpt-5-nano",
            messages=chatgpt_messages,
            max_completion_tokens=1024
        )
        response = completion.choices[0].message.content

        # Print response
        print(f"\n[ChatGPT] >>>> {response} <<<<\n")

        # Add response to shared history
        shared_history.append({
            "role": "assistant",
            "content": response,
            "model": "chatgpt"
        })

    elif user_input.startswith("@azureopenai "):
        # Extract the actual message (remove @azureopenai prefix)
        user_message = user_input[13:].strip()

        if not user_message:
            print("Error: Please provide a message after @azureopenai")
            user_input = input("\nYour message: ")
            continue

        # Add user message to shared history
        shared_history.append({
            "role": "user",
            "content": user_message,
            "model": "user"
        })

        # Format history for Azure OpenAI
        azure_messages = format_history_for_azure(shared_history)

        # Generate Azure OpenAI response
        completion = azure_client.chat.completions.create(
            model=azure_deployment,
            messages=azure_messages,
            max_tokens=1638,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )
        response = completion.choices[0].message.content

        # Print response
        print(f"\n[Azure OpenAI] >>>> {response} <<<<\n")

        # Add response to shared history
        shared_history.append({
            "role": "assistant",
            "content": response,
            "model": "azure"
        })

    elif user_input.startswith("@claude "):
        # Extract the actual message (remove @claude prefix)
        user_message = user_input[8:].strip()

        if not user_message:
            print("Error: Please provide a message after @claude")
            user_input = input("\nYour message: ")
            continue

        # Add user message to shared history
        shared_history.append({
            "role": "user",
            "content": user_message,
            "model": "user"
        })

        # Format history for Claude
        claude_messages = format_history_for_claude(shared_history)

        # Generate Claude response
        message = claude_client.messages.create(
            model="claude-haiku-4-5-20251001",
            system=system_message,
            max_tokens=1024,
            messages=claude_messages
        )
        response = message.content[0].text

        # Print response
        print(f"\n[Claude] >>>> {response} <<<<\n")

        # Add response to shared history
        shared_history.append({
            "role": "assistant",
            "content": response,
            "model": "claude"
        })

    else:
        print("\nError: Please start your message with @deepseek, @chatgpt, @azureopenai, or @claude")
        print("Example: @deepseek Tell me about Python")

    # Get next user input
    user_input = input("\nYour message: ")

# Exit message
print("\n" + "=" * 60)
print("Goodbye! Chat session ended.")
print("=" * 60)
