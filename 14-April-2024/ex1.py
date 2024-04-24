import openai

# Set your API key here
openai.api_key = ''

def ask_chat_gpt(prompt, model="gpt-3.5-turbo", max_tokens=150):

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    prompt_text = "What are the benefits of AI in healthcare?"
    result = ask_chat_gpt(prompt_text)
    print("GPT's response:", result)