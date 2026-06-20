import requests
from bs4 import BeautifulSoup

Fballurl = "https://www.skysports.com/football-scores-fixtures/2026-06-21"
response = requests.get(Fballurl)

if response.status_code == 200:
    print("Request successful!")
else: 
    print("Request failed with status code:", response.status_code)

soup      = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(separator="\n", strip=True)    
print(soup.title)
print(page_text)



