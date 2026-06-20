import requests
from bs4 import BeautifulSoup
import csv


Fballurl = "https://www.skysports.com/football-scores-fixtures/2026-06-21"
response = requests.get(Fballurl)

if response.status_code == 200:
    print("Request successful!")
else: 
    print("Request failed with status code:", response.status_code)

soup      = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(separator="\n", strip=True)

print(soup.title)

#   # Split into non-empty lines and save to CSV
# lines = [ln.strip() for ln in page_text.split("\n") if ln.strip()]
# print(f"Extracted {len(lines)} text lines")

# csv_path = 'page_text.csv'
# with open(csv_path, 'w', encoding='utf-8', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['text'])
#     for ln in lines:
#         writer.writerow([ln])

# print(f"Saved text lines to {csv_path}")



