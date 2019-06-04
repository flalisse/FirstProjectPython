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
                "Attaque": 7,
                "Niveau":1,
                "XP":10
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
                "Attaque": 9,
                "Niveau":1,
                "XP":10
            }


    def __setteurcaract(self,**NewCaracteristiques):

        self._caracteristiques = NewCaracteristiques

    def __getteurcaract(self,caracteristiques):

        return self._caracteristiques

    caracteristiques = property(__getteurcaract,__setteurcaract)


    def AttaqueMassue(self,LancerDès):

        if LancerDès >= 3 :

            print("Attaque coup de massue ")
            Mob.pv-=5
        else :

            print("il rate son attaque")




class Mob:

    def __init__(self,pv,level):

        self.pv = pv
        self.level = level


    def setupCarac(self,level):

        if self.level == 1:
            self.pv = 10

        elif self.level ==2:
            self.pv = 15

        elif self.level ==3:
            self.pv = 20










def choixrace():

    newrace=input("veuillez sélectionner votre race entre : Humain / Orc")

    while newrace != "Orc" and newrace != "Humain":

        return choixrace()

    Personnage.race = newrace



def LancerDes():

    ResultDès = randint(1,3)
    print("Vous avez lancé le dès -> résultat : {}".format(ResultDès))

    if ResultDès < 4:

        FirstMob = Mob(0,0)
        return FirstMob and ApparitionMob(ResultDès,FirstMob)




def ChoixName():

    nom = input("Tapez le nom de votre perso: ")
    return nom


def ApparitionMob(ResultDès,FirstMob):


    if ResultDès == 1:



        print("apparition d'un monstre de niveau 1:")

        FirstMob.level = ResultDès
        FirstMob.setupCarac(ResultDès)
        print(FirstMob.level)
        print(FirstMob.pv)

    elif ResultDès == 2 :

        print("apparition d'un monstre de niveau 2")
        FirstMob.level = ResultDès
        FirstMob.setupCarac(ResultDès)

        print(FirstMob.level)
        print(FirstMob.pv)




    elif ResultDès == 3 :

        print("apparition d'un monstre de niveau 3 ")
        FirstMob.level = ResultDès
        FirstMob.setupCarac(ResultDès)

        print(FirstMob.level)
        print(FirstMob.pv)



    else:

        print("Pas de monstre")











