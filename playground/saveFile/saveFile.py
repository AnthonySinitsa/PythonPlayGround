import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.monster.com/jobs/search?q=python%20developer&where=Spokane%2C%20WA&so=m.h.lh"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Prettify the HTML content
prettified_content = soup.prettify()

# Save the prettified HTML content to a text file
with open('indeed_page_content_prettified.txt', 'w', encoding='utf-8') as file:
    file.write(prettified_content)

print("Prettified HTML content saved to 'indeed_page_content_prettified.txt'.")

# print(soup)
# print(tables)

# df1 = pd.read_html(str(tables[0]))
# df1 = df1[0]
# print(df1)
# df2 = pd.read_html(str(tables[1]))
# df2 = df2[0]
# print(df2)

