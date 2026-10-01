from ollama import chat

System_msg = "You are a  BTS ARMY. Answer in BTS style. Answer in 5 lines."
history = [{"role" : "System","content" : System_msg}]
question_counter = 0

print("Welcome to BTS World...🥳")
while True:
    question = input("You:")
    if question == "":
        print("ARMY 🎀 : Please type something.")
        continue
    if question.lower().strip() == "/history":
        print("----Your Conversion so far----")
        if len(history)<2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "ARMY 🎀 "
            print(f"{speaker}:{msg["content"]}")
        print("--------------------------")
        print()
        continue
    if question.lower()strip() == "/clear":
        history = [{"role" : "system", "content" : system_msg}]
        print("Your history is cleared. Start a fresh conversation.")
        print()
        continue

    if question.lower().strip == "/help":
        print("----Available commands----")
        print("/history - dispaly conversation history")
        print("/clear - clear chat history")
        print("/help - display this list")
        print("exit - quits the chatbot")
        print("---------------------")
        print()
        continue

    if question.lower().strip() == "bye":
        print("ARMY 🎀:Goodbye user. Please come back soon! Miss you 💜💜")
        print(f"You asked{question_counter} question today. Good job!")
        break
    history.append({"role" : "user", "content":question})
    try:
        response = chat(
                model="llama3.2",
                messages = history     
            )
        reply = response.message.content
        history.append({"role" : "assistant", "content" : reply})
        print(f"ARMY 🎀 :{reply}")
        print()
        print("-------------------------")
        print()
    except Exception as e:
        print("Unknown issue. Is Ollama running?")

/personality
you type the personality
reset the system msg, print confirmation
and continue the loop
