import os
from Bard import Chatbot

def bard():
  token = open('token.txt', 'r').read().strip('\n').strip()

  bot = Chatbot(token)

  question = open('test.txt', 'r').read().strip('\n').strip()

  output = bot.ask(question)['content']

  print(output)
  
if __name__ == '__main__':
  bard()