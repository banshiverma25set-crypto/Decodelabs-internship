print("=" * 50)
print(" Welcome to DecodeBot")
print("Simple AI Chatbot - Decode Labs Internship")
print("Type 'bye' anytime to exit")
print("=" * 50)

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user == "who created you":
        print("Bot: I was created by a Decode Labs Intern.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence. It enables machines to perform tasks that usually require human intelligence.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI where computers learn patterns from data.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language used for AI, Data Science, Web Development, and Automation.")

    elif user == "what is chatbot":
        print("Bot: A chatbot is a software program that can interact with users through text or voice.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")

    elif user == "what can you do":
        print("Bot: I can answer simple questions and demonstrate chatbot functionality.")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")