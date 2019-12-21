import sys # ici, une librairie est importée

prenom = input("Veuillez entrer votre prenom et tapez enter : ")

test = 0
for dummy in reversed( prenom ):
    if ( dummy == "a" ):
        print( "Le nom", prenom, "contient la lettre a." )
        test = 1
        
if ( test == 0 ):
    print( "Le nom", prenom, "ne contient pas la lettre a." )
