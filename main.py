import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name?', ['My name is Chatbot.', 'I am Chatbot.']],
    ['how are you?', ['I am doing well, thank you.', 'I am fine, thanks.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'See you later.']],
]

chatbot = Chat(pairs, reflections)

chatbot.converse()
