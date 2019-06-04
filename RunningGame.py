from Methods import *


print("first of all select your race: ")
print("give a name at your caracter : ")

NameSelect = ChoixName()

RaceSelect = choixrace()

if RaceSelect == "Orc":

    Yourperso = Orc(NameSelect)
else :
    Yourperso = Humain(NameSelect)



print(Yourperso.nom)
print(Yourperso.race)
print(Yourperso._caracteristiques)


LancerDes()



