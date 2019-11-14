import sys # ici, une librairie est importée

prenom = input("Veuillez entrer votre prenom et tapez enter : ")
PrenomInverse = ""

for dummy in reversed( prenom ):
	PrenomInverse += dummy
	print( "PrenomInverse = ", PrenomInverse )

print( "-------> End of for loop! <-------")
print( "-------> L'inverse du nom", prenom, "est", PrenomInverse, "!")