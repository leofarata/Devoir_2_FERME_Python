

#La Class Animal =================================================
class Animal:

    def __init__(self, nom, age):

        self.nom = nom
        self.age = int(age)


    def cri(self):
        print()


#La Class Chat =================================================
class Chat(Animal):
    
    typee = "Chat"
    
    def cri(self):
        print("Miaou")
        return
    


#La Class Chien =================================================
class Chien(Animal):

    typee = "Chien"
     
    def cri(self):
        print("Ouaf")
        return


#La Class Ferme =================================================
class Ferme:

    def __init__(self,animaux):

        self.animaux = animaux


    def ajouter_animal(self, animal):
        return self.animaux.append(animal)


    def crier(self):
        for animal in self.animaux:
            animal.cri()
        return

    def tuer(self,nom_animal):
        for animal in self.animaux:
            if(animal.nom == nom_animal):
                self.animaux.remove(animal)
                break
        return

    def noms_animaux(self):
        liste_noms=[]
        for animal in self.animaux:
            liste_noms.append(animal.nom)
        return liste_noms
    
    def type_animaux(self):
        liste_types=[]
        for animal in self.animaux:
            liste_types.append(animal.typee)
        return liste_types

    def representation(self):
        print("Ferme avec",len(self.animaux),"animaux")
        return


# Instance Ferme =================================================
print()
ferme = Ferme([])
ferme.ajouter_animal(Chien("Misouris",2))
ferme.ajouter_animal(Chien("Sou",2))
ferme.ajouter_animal(Chat("Rt",2))
ferme.ajouter_animal(Chien("Lop",3))
ferme.crier()
ferme.representation()
print()
print("DEBUT DU PROGRAMME")


