from bs4 import BeautifulSoup
import requests
url      = "https://www.skysports.com/football/news/11095/13481245/world-cup-2026-fixture-schedule-and-uk-kick-off-times-day-by-day-breakdown-of-all-104-matches-including-england-scotland"
response = requests.get(url)
soup     = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(separator="\n", strip=True) #
print(soup.title)


