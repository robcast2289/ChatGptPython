from openai import OpenAI

client = OpenAI(api_key = "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")

while True:

    prompt = input("\nPregunta: ")

    if prompt == "exit":
        break

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #prompt=prompt,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        max_tokens=500
    )
    
    print(f"Respuesta: {completion.choices[0].message.content}")