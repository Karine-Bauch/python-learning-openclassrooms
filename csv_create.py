import requests
from bs4 import BeautifulSoup
import csv

# Fonction pour récupérer les textes des éléments HTML (element) sélectionnés (selector) dans une liste de strings.
def extract_datas(elements):
  results = []
  for element in elements:
    results.append(element.string)
  return results;

# Fonction qui permet de charger la donnée dans un fichier csv
def load_datas(file_name, en_tete, titles, descriptions):
  with open(file_name, 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(en_tete)
    # zip permet d'itérer sur 2 listes en même temps
    for title, description in zip(titles, descriptions):
      writer.writerow([title, description]);

# Fonction qui extrait et insère les données dans un fichier csv
def etl():
  # Page à scrapper
  url = "https://www.gov.uk/search/news-and-communications"
  reponse = requests.get(url)
  page = reponse.content

  # Parse du html
  soup = BeautifulSoup(page, "html.parser")

  # Trouver tous les titres
  titles = soup.find_all("a", class_="gem-c-document-list__item-title")
  # Trouver touste les descriptions
  descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")  

  # Extraction et chargement des données dans le csv
  en_tete = ["titre", "description"]
  all_titles = extract_datas(titles)
  all_descriptions = extract_datas(descriptions)
  load_datas("data.csv", en_tete, all_titles, all_descriptions)


etl()



# titles = soup.find_all("a", class_="gem-c-document-list__item-title")
# titles_texts = []

# for title in titles:
#   titles_texts.append(title.string)


# descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
# descriptions_texts = []

# for description in descriptions:
#   descriptions_texts.append(description.string)

# print("titres: ", titles_texts)
# print("descriptions: ", descriptions_texts)


# en_tete = ["titre", "description"]

# with open('data.csv', 'w') as csv_file:
#   writer = csv.writer(csv_file, delimiter=',')
#   writer.writerow(en_tete)

#   for title, description in zip(titles_texts, descriptions_texts):
#     line = [title, description]
#     writer.writerow(line)
