import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'(.*) your name?', ['My name is ChatBot.', 'I am ChatBot.']),
    (r'what can you do\?', ['I can chat with you and provide basic information.', 'I\'m here to chat with you and answer your questions.']),
    (r'what is your purpose\?', ['My purpose is to assist you in your conversation.', 'I\'m here to chat with you and provide support.']),
    (r'(.) help (.)', ['Sure, I can help you with that.', 'Of course, what do you need help with?']),
    (r'(.*) (good|fine)', ['That\'s great!', 'Good to hear!']),
    (r'(.*) (bad|not good)', ['I\'m sorry to hear that.', 'Hope things get better.']),
    (r'quit', ['Bye! Take care.', 'Goodbye.']),
]

chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to ChatBot!")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

if _name_ == "_main_":
    main()
