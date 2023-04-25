from django.shortcuts import render

# Create your views here.
import openai
openai.api_key = "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"

messages=[]
while True:
    message = input("Enter Your Question: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
