chemin = __file__ # correspond au chemin jusqu'au fichier

i = len(chemin) - 1  # Commence à la fin

while chemin[i] != "/":
    i -= 1

fichier = chemin[i+1:]
print(fichier)
