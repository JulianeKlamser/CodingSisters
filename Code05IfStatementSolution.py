import sys # ici, une librairie est importée

prenom = input("Veuillez entrer votre prenom et tapez enter : ")

test = 0
for dummy in reversed( prenom ):
    if ( dummy == "a" or dummy == "e" or dummy == "i" or dummy == "o" or dummy == "u"):
        print( "Le nom", prenom, "contient la lettre", dummy,"et donc au moins une voyelle." )
        test = 1
        
if ( test == 0 ):
    print( "Le nom", prenom, "ne contient aucune voyelle." )
