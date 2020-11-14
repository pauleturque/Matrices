import os


# boucle sur le nombre de colonnes
nbColonnes = 5
while nbColonnes > 5:
    nbColonnes = int(input("Entrez le nombre de colonnes des matrices (max 5) = "))

# boucle sur le nombre de lignes
nbLignes = 6
while nbLignes > 6:
    nbLignes = int(input("Entrez le nombre de lignes des matrices (max 6 = "))

# déclaration des matrices
mA = [[0] * nbColonnes for _ in range(nbLignes)]
mB = [[0] * nbColonnes for _ in range(nbLignes)]
mC = [[0] * nbColonnes for _ in range(nbLignes)]

x = float
y = float

# saisie de la matrice A
for x in range(0, nbColonnes - 1):
    for y in range(0, nbLignes - 1):
        mA[x][y] = int(input("A(" + str(x) + "," + str(y) + ") = "))

# saisie de la matrice B
for x in range(0, nbColonnes - 1):
    for y in range(0, nbLignes - 1):
        mB[x][y] = int(input("B(" + str(x) + "," + str(y) + ") = "))

# calcul de la matrice C
for x in range(0, nbColonnes - 1):
    for y in range(0, nbLignes - 1):
        mC[x][y] = mA[x][y] + mB[x][y]

# affichage de la matrice C
for x in range(0, nbColonnes - 1):
    for y in range(0, nbLignes - 1):
        print(f"C({x},{y}) = {mC[x][y]}")









