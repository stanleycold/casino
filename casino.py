import math
import random

# variable argent
argent = 1000
continuer_partie = True
print("vous vous installez a la table de roulette",argent,"euros")

while continuer_partie:
    nombre_mise = - 1
    while nombre < 0 or nombre_mise > 49:
        nombre_mise = input("taper le nombre sur lequel vous voulez miser : ")
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("vous n'avez pas saisi un nombre")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("ce nombre est negatif")
        if nombre_mise > 49:
            print("ce nombre est superieur a 49")
mise = 0
while mise <=0 or mise > argent:
     mise = input("tapez le montant de votre mise : ")
     try:
         mise = int(mise)
     except ValueError:
         print("vous n'avez pas saisi un nb")
         mise = -1
         continue
     if mise <=0:
         print("la saisie est negative ou nul")
     if mise > argent:
         print("vous ne pouvez pas miser autant, vous n'avez que: ",argent, "euros")
numero_gagnant = random.randrange(50)
print("le roulette tourne --- le num gagnant : ", numero_gagnant)

# Gain du joueur

if numero_gagnant == nombre_mise:
    print("Felicitations vous obtenez ", mise * 3, "euros")
    argent += mise * 3
elif numero_gagnant % 2 == nombre_mise % 2:
    mise = math.ceil(mise * 0.5)
    argent += 
