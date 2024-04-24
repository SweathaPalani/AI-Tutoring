import openai

def qna(prompt):
    openai.api_key = ""
    pred_result = openai.Completion.create(
        prompt=prompt,
        temperature=0,
        max_tokens=40,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="gpt-3.5-turbo-instruct",
    )
    return pred_result["choices"][0]["text"].split("\n")
        
print(qna("who is the pm of canada?"))