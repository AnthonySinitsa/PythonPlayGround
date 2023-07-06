import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Module must be named scraper.py
# Create function named get_citations_needed_count
# takes in a url string and returns an integer.
# Create function named get_citations_needed_report
# takes in a url string and returns a report string
# the string should be formatted with each citation listed in the order found.

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

get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
print('Total citations needed:', get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))