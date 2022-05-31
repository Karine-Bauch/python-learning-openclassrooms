import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
reponse = requests.get(url)
page = reponse.content

# print(page)

# Test creation fonction pour code répétitif
def find(element, selector):
  results = soup.find_all(element, class_=selector)
  results_texts = []
  for result in results:
    results_texts.append(result.string)
  return results_texts;

soup = BeautifulSoup(page, "html.parser")

titles_texts = find("a", "gem-c-document-list__item-title")

# titles = soup.find_all("a", class_="gem-c-document-list__item-title")
# titles_texts = []

# for title in titles:
#   titles_texts.append(title.string)

descriptions_texts = find("p", "gem-c-document-list__item-description")

# descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
# descriptions_texts = []

# for description in descriptions:
#   descriptions_texts.append(description.string)

# print("titres: ", titles_texts)
# print("descriptions: ", descriptions_texts)


en_tete = ["titre", "description"]

with open('data.csv', 'w') as csv_file:
  writer = csv.writer(csv_file, delimiter=',')
  writer.writerow(en_tete)

  for title, description in zip(titles_texts, descriptions_texts):
    line = [title, description]
    writer.writerow(line)