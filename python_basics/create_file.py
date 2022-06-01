'''
file = open("hello.txt", "w")
file.write("Hello World")
file.close()

with open("hello.txt") as file: # Quand on ne spécifie pas le mode d'ouverture du fichier, c'est "r" (read) qui est utilisé par défaut
  for line in file:
    print(line)
'''

import csv

with open('colors.csv') as file:
  reader = csv.DictReader(file, delimiter=',')
  for line in reader:
    print(line['nom'] + " travaille comme " + line['metier'] + " et sa couleur préférée est " + line['couleur_preferee'])