# Simple AI Chatbot

print("🤖 Chatbot: Hello! I am your AI assistant.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("🤖 Chatbot: Hi there!")

    elif user == "how are you":
        print("🤖 Chatbot: I am just code, but I'm doing great!")

    elif user == "your name":
        print("🤖 Chatbot: I am your simple AI chatbot.")

    elif user == "bye":
        print("🤖 Chatbot: Goodbye! 👋")
        break

    else:
        print("🤖 Chatbot: Sorry, I don't understand that.")
