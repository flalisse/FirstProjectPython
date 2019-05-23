'define all the method for the project'

from random import *

class Personnage:

    def __init__(self,nom,race):
        self.nom = nom
        self._race = race

    def __setteurrace(self,newrace):

        self._race = newrace

    def __getteurrace(self,race):

        return self._race






    race = property(__getteurrace,__setteurrace)


class Orc(Personnage):

    def __init__(self,nom):

        self.nom = nom
        self._caracteristiques = {
                "Santé": 20,
                "Armor": 10,
                "Attaque": 7
            }


    def __setteurcaract(self,**NewCaracteristiques):

        self._caracteristiques = NewCaracteristiques

    def __getteurcaract(self,caracteristiques):

        return self._caracteristiques

    caracteristiques = property(__getteurcaract,__setteurcaract)



class Humain(Personnage):

    def __init__(self,nom):
        self.nom =nom
        self._caracteristiques = {
                "Santé": 20,
                "Armor": 10,
                "Attaque": 9
            }


    def __setteurcaract(self,**NewCaracteristiques):

        self._caracteristiques = NewCaracteristiques

    def __getteurcaract(self,caracteristiques):

        return self._caracteristiques

    caracteristiques = property(__getteurcaract,__setteurcaract)





def choixrace():

    newrace=input("veuillez sélectionner votre race entre : Humain / Orc")

    while newrace != "Orc" and newrace != "Humain":

        return choixrace()

    Personnage.race = newrace


def LancerDès():

    ResultDès = randint(1,6)
    print("Vous avez lancé le dès -> résultat : {}".format(ResultDès))

    return ResultDès

def ChoixName():

    nom = input("Tapez le nom de votre perso: ")
    return nom






