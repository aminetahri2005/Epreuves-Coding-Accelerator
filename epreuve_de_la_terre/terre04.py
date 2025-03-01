chemin = __file__

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    nom_fichier = chemin[i]
    i -= 1
    nom_fichier_inverse = "".join(reversed(nom_fichier))
    print(nom_fichier_inverse, end="")