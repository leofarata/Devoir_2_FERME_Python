from lib.ferme import *

# Menu ==================================
def afficher_menu():
    print()
    print("------ MENU PRINCIPAL PROG FERME ------")
    print("1, Ajouter un animal")
    print("2, Lancer le cri de tous les animaux de la ferme")
    print("3, Tuer un animal")
    print("4, Afficher la ferme")
    print("5, Quitter")
    print()


# Ajouter Animal ==================================
def ajouter_chat():
    nom = ""
    age = ""
    
    while (nom == "" or nom.isnumeric()):
        nom = input("Nom du chat: ")
        if(nom == ""):
            print()
            print("Vous ne devez pas laisser le champ vide")
            print()
        elif(nom.isnumeric()):
            print()
            print("Les valeurs numeriques ne sont pas acceptées")
            print()
        else:
            break
        
    while (age.isnumeric() == False):
           age = input("Age du chat: ")
           if(age.isnumeric() == False):
              print()
              print("Vous devez saisir un nombre ou un chiffre")
              print()
    print()
    ferme.ajouter_animal(Chat(nom, age))
    print("Le chat", nom, "est ne")


def ajouter_chien():
    nom = ""
    age = ""

    while (nom == "" or nom.isnumeric()):
        nom = input("Nom du chien: ")
        if(nom == ""):
            print()
            print("Vous ne devez pas laisser le champ vide")
            print()
        elif(nom.isnumeric()):
            print()
            print("Les valeurs numeriques ne sont pas acceptées")
            print()
        else:
            break
              
    while (age.isnumeric() == False):
           age = input("Age du chien: ")
           if(age.isnumeric() == False):
              print()
              print("Vous devez saisir un nombre ou un chiffre")
              print()
    print()
    ferme.ajouter_animal(Chien(nom, age))
    print("Le chien", nom, "est ne")
    

def choix_Animal():
    choix =""
    while choix not in {"1","2","3"}:
        print()
        print("------ Ajouter un animal ------")
        print("1, Chat")
        print("2, Chien")
        print("3, Retour")
        print()
        choix = input("Votre choix: ")
        if(choix == "1"):
            ajouter_chat()
        elif(choix == "2"):
            ajouter_chien()
        elif(choix == "3"):
            break
        else:
            print("Votre saisie doit etre comprise entre 1, 2 ou 3")
            print()


# Cri Animal ==================================
def choix_Cri():
    print()
    ferme.crier()
    print("Liste des animaux:", ferme.noms_animaux())

# Tuer Animal ==================================
def choix_Tuer():
    choix =""
    noms_animaux = ferme.noms_animaux()
    types_animaux = ferme.type_animaux()
    print()
    print("Liste des animaux:",noms_animaux)

    while ((choix not in noms_animaux) and (choix != "1")) :
        print()
        print("------ Tuer un animal ------")
        print("1, Retour")
        print()
        choix = input("Nom de l'animal a tuer: ")
        if(choix in noms_animaux):
            ferme.tuer(choix)
            print("Le", types_animaux[noms_animaux.index(choix)], choix, "est mort")
            print()
        elif(choix == "1"):
            break
        else:
            print("L'animal n'existe pas dans la ferme")



# Afficher Ferme ==================================
def Afficher_Ferme():
    print()
    print("Ma ferme a", len(ferme.animaux), "animaux")
    print("Liste des animaux:", ferme.noms_animaux())

    
