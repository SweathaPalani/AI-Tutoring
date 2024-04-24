import openai

openai.api_key = ''

def get_response():
    stream = openai.ChatCompletion.create(
    
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")

if __name__ == "__main__":
    result = get_response()
    print(result)
