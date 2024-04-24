import openai

openai.api_key = ''

def get_response():
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "Who won the world series in 2020?"}
    ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    result = get_response()
    print(result)
