import sys # ici, une librairie est importée


prenom = input("Veuillez entrer votre prenom et tapez enter : ")
print( "Bienvenue chez coding sisters", prenom, "!" )

nom = input("Veuillez entrer votre nom et tapez enter : ")
numLet = len(nom) # count number of letters
print( "Votre nom,", nom, ", a", numLet, "lettres." )