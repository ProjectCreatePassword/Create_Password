# Import des noms du module
from tkinter import *

# Création d'un objet "fenêtre"
fenetre = Tk()

# Titre (Label)
titre = Label(fenetre, text = "CRÉÉ TON PROPRE MOT DE PASSE")

# Affichage du titre
titre.pack()

fenetre.title("CREATE PASSWORD")

fenetre.minsize(300,200)

# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()