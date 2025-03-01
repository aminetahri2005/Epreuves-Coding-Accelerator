chemin = __file__

i = len(chemin) - 1  # Commence à la fin

while i >= 0 and chemin[i] != "/":
    print(chemin[i:], end="")
    i -= 1