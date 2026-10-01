from ollama import chat 

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : "Write me a whatsapp message to my friend mythri asking her to meet me at"
            " the park. Keep the answer in 4 lines. "
        }
    ]
)

print(response.message.content)