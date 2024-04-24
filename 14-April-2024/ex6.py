import openai

openai.api_key = ''

def get_response():
    try:
        # Create text embeddings
        response = openai.Embedding.create(
            model="text-embedding-ada-002",
            input="The food was delicious and the waiter...",
            encoding_format="float"
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    result = get_response()
    if result:
        print(result)
