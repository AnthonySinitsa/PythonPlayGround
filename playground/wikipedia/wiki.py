import wikipedia
import os

def search(str):
  os.system('clear')
  print(wikipedia.search(str))
  
def summary(str, sentence):
  os.system('clear')
  print(wikipedia.summary(str, sentence)) # change sentence amount
  
def lang(str):
  os.system('clear')
  wikipedia.set_lang(str)
  print(summary('computer', 10))
  print()

def content(str):
  os.system('clear')
  print(wikipedia.page(str).content)
  
def images(str):
  os.system('clear')
  print(wikipedia.page(str).images)
  
def categories(str):
  os.system('clear')
  print(wikipedia.page(str).categories)  

def random(pages):
  os.system('clear')
  print(wikipedia.random(pages))
  
def html(str):
  os.system('clear')
  print(wikipedia.page(str).html())

def geosearch(lat, lon, title=None, results=10, radius=1000):
  os.system('clear')
  print(wikipedia.geosearch(lat, lon, title, results, radius))

if __name__ == '__main__':
  search('Barack')
  # summary('Barack', 10)
  # lang('fr')
  # lang('uk')
  # lang('vi')
  # lang('de')
  # content('cheesecake')
  # images('cheesecake')
  # categories('cheesecake')
  # random(pages=10)
  # html('cheesecake')
  # geosearch(47.6205, -122.3493, results=30, radius=1000)
  # radius in meters, value must be between 10 and 10000