'define all the method for the project'



class Personnage:

    def __init__(self,race,caracteristiques):


        self._race= race
        self._caracteristiques = caracteristiques


    def __setteurrace(self,newrace):

        self._race = newrace

    def __getteurrace(self,race):

        return self._race

    def __setteurcaract(self,**NewCaracteristiques):

        self._caracteristiques = NewCaracteristiques

    def __getteurcaract(self,caracteristiques):

        return self._caracteristiques


    def __str__(self):

        return "Voici les caractéristiques de votre personnage  race : {} Caracteristiques: {}".format(self.race,self.caracteristiques)





    race = property(__getteurrace,__setteurrace)




def choixrace():

    newrace=input("veuillez sélectionner votre race entre : Humain / Orc")

    while newrace != "Orc" and newrace != "Humain":

        return choixrace()

    Personnage.race = newrace



def setupcaracteristiques():

    if Personnage.race == "Orc":
        NewCaracteristiques = {

            "Armor":5,
            "Defense":10
        }

    elif Personnage.race =="Humain":

        NewCaracteristiques = {


            "Armor":7,
            "Defense":8
        }

    Personnage.caracteristiques = NewCaracteristiques



Mousquetaire




