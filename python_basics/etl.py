import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

print(page)

soup = BeautifulSoup(page, "html.parser")

titles = soup.find_all("a", class_="gem-c-document-list__item-title")
titles_texts = []

for title in titles:
  titles_texts.append(title.string)


descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions_texts = []

for description in descriptions:
  descriptions_texts.append(description.string)

print("titres: ", titles_texts)
print("descriptions: ", descriptions_texts)
