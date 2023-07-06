import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

            
def get_citations_needed_count(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  
  citations_needed = 0
  
  for tag in soup.find_all(['sup', 'span'], class_=['noprint Inline-Template', 'Template-Fact']):
    if tag.text.strip().lower() == '[citation needed]':
      citations_needed += 1
      parent = tag.find_parent()
      print("Citation needed for:", parent.text.strip())
    
  return citations_needed

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

citations = get_citations_needed_count(url)
print("Total citations needed:", citations)