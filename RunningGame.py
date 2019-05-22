from Methods import choixrace

from Methods import Personnage,setupcaracteristiques

print("first of all select your race: ")

RaceSelect = choixrace()

Carac = setupcaracteristiques()


YourPerso = Personnage(RaceSelect,Carac)

print(YourPerso)
test
