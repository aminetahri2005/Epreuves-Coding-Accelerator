chemin = __file__

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    nom_fichier = chemin[i]
    print(nom_fichier, end="")
    i -= 1

print(nom_fichier[:])
