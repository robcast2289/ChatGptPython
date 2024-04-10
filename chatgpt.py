from openai import OpenAI

client = OpenAI(api_key = "")

conversation_history = []

while True:

    print("Pregunta: ")
    prompt = input()

    if prompt == "exit":
        break

    conversation_history.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #prompt=prompt,
        messages=conversation_history,
        max_tokens=500
    )

    conversation_history.append(
        {
            "role":"assistant",
            "content":completion.choices[0].message.content
        }
    )
    
    print(f"Respuesta: {conversation_history[-1]['content']}")