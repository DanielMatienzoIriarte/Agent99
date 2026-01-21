import ollama

# Create a client instance (optional if running on default localhost:11434)
client = ollama.Client()

# Define the model and prompt
model_name = "mistral"
user_prompt = "What are the key differences between the Llama 2 13B and Mistral 7B models?"

# Generate a response
response = client.chat(
    model=model_name,
    messages=[{'role': 'user', 'content': user_prompt}]
)

# Print the response content
print(response['message']['content'])
