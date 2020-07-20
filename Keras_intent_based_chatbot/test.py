from chatbot import return_chat

print('Conversation started type, quit to STOP')
while True:
    inp = input("You: ")
    if inp.lower() == "quit":
        break
    res = return_chat(str(inp.lower()))
    print(res)
