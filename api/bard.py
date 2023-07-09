import os
from Bard import Chatbot

token = open('token.txt', 'r').read().strip('\n').strip()

bot = Chatbot(token)

output = bot.ask('write a python function that takes 2 nums as input and determines whether they are even or odd')['content']

print(output)