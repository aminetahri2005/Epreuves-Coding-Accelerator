chemin = __file__

i = len(chemin) - 1
while i >= 0 and chemin[i] != '/':
    i -= 1

nom_fichier = chemin[i+1:]  # Extrait tout APRÈS le dernier '/'
print(nom_fichier)