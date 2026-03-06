while True:

    user = input("You: ")

    if user.lower() == "hello":
        print("Bot: Hi there!")

    elif user.lower() == "how are you":
        print("Bot: I am fine!")

    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand")
