chemin = __file__

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    nom_fichier = chemin[i]
    nom_fichier_inverse = nom_fichier[::-1]
    print(nom_fichier_inverse, end="")
    i -= 1



chemin = __file__

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    nom_fichier = chemin[i]
    nom_fichier_inverse = "".join(reversed(nom_fichier))
    print(nom_fichier_inverse, end="")
    i -= 1


def right(nom_fichier):
    return nom_fichier

chemin = __file__


i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    nom_fichier = chemin[i]
    print(right(nom_fichier), end="")
    i -= 1



chemin = __file__
liste_chemin = [chemin]

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    liste_chemin.append(chemin[i])
    nom_fichier = "".join(reversed(liste_chemin))
    print(nom_fichier, end="")
    i -= 1

