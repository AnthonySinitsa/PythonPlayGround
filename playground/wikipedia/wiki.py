import wikipedia
import os

def search(str):
  os.system('clear')
  print(wikipedia.search(str)) # shows different results using 'barack'
  
def summary(str, sentence):
  os.system('clear')
  print(wikipedia.summary(str, sentence)) # gives sentence summary
  
def lang(str):
  os.system('clear')
  wikipedia.set_lang(str)
  print(summary('computer', 10)) # gives summary in different languages
  print()

def content(str):
  os.system('clear')
  print(wikipedia.page(str).content) # gives multiple definitions
  
def images(str):
  os.system('clear')
  print(wikipedia.page(str).images) # images
  
def categories(str):
  os.system('clear')
  print(wikipedia.page(str).categories) # shows 'related' categories

def random(pages):
  os.system('clear')
  print(wikipedia.random(pages)) # gives random topics
  
def html(str):
  os.system('clear')
  print(wikipedia.page(str).html()) # gives html of said page

def geosearch(lat, lon, title=None, results=10, radius=1000):
  os.system('clear')
  print(wikipedia.geosearch(lat, lon, title, results, radius))

if __name__ == '__main__':
  # search('Barack')
  # summary('Barack', 10)
  # lang('fr')
  # lang('de')
  # content('cheesecake')
  # images('cheesecake')
  # categories('cheesecake')
  # random(pages=50)
  # html('cheesecake')
  geosearch(47.6205, -122.3493, results=30, radius=1000)
  # radius in meters, value must be between 10 and 10000