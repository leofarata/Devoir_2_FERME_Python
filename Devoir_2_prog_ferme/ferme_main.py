from lib.ferme import *
from lib.utils import *

# MAIN =================================================
while True:
  afficher_menu()
  choix = input("Votre choix: ")

  if(choix == "1"):
      choix_Animal()
      
  elif(choix == "2"):
      choix_Cri()
      
  elif(choix == "3"):
      choix_Tuer()
      
  elif(choix == "4"):
      Afficher_Ferme()
      
  elif(choix == "5"):
      break
