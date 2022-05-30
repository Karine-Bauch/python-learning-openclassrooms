# Définition de ma finction du calcul de Pi
def pi_calcul(total_loops):
  counter = 0 # Initialisation de mon compteur
  pi = 4 # initialisation de PI d'après le calcul prévu (4 -4/3 +4/5 -4/7 +4/9 ...)
  signe = 1 # initialisation du signe
  denominateur = 1 # initialisation du dénominateur de chaque fraction
  while counter < total_loops:
    signe *= -1 # changement de signe (si + passe en -, et vice versa)
    denominateur += 2 # Incrémentation de 2 du dénominateur
    counter += 1 # Incrémentation de 1 du compteur
    pi += (signe * 4 / denominateur) # ajout de la fraction à la valeur précédente de Pi
  print(f"la valeur de pi après {counter} boucles est de {pi}");

pi_calcul(5)
pi_calcul(100)
pi_calcul(1000)
pi_calcul(10000)
pi_calcul(50000)
pi_calcul(100000)






