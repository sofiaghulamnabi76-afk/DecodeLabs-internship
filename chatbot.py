print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you sofia.")

    elif user == "how are you":
        print("Bot: I'm fine. Thanks for asking!")

    elif user == "your name":
        print("Bot: My name is RuleBot.")

    elif user == "thanks":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good Morning!")

    elif user == "good night":
        print("Bot: Good Night!")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")