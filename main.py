import string
import hashlib
import json
import os
# Import des noms du module
from tkinter import *
from tkinter.constants import GROOVE, LEFT
import customtkinter as ctk

ctk.set_appearance_mode("System")  



def toggle_visibility():
    if voir_mdp.get():
        mdp_utilisateur.config(show="")
    else:
        mdp_utilisateur.config(show="*")
# Fonts
font_titre= ("Verdana", 16, "bold")


# Création d'un objet "fenêtre"
fenetre = Tk()

# Titre (Label)
titre = Label(fenetre, text = "BIENVENUE SUR CREATE PASSWORD 🗝️", bg="#F97D24", fg="black", font = font_titre)

# Affichage du titre
titre.pack(anchor="center")

# Titre fenetre
fenetre.title("CREATE PASSWORD")

# Taille fenetre
fenetre.minsize(500, 200)
fenetre.maxsize(500, 200)

# Couleur fenetre
fenetre["bg"]="#F97D24"

# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE, bg="black")
Frame1.pack(side= RIGHT, fill= Y, padx=0, pady=0)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE, bg="black")
Frame2.pack(side= LEFT, fill= Y, padx=0, pady=0)

liste = Listbox(Frame2)
liste.insert(1, "- Au moins 8 caractères.")
liste.insert(2, "- Au moins 1 lettre majuscule.")
liste.insert(3, "- Au  moins 1 lettre minuscule.")
liste.insert(4, "- Au moins 1 chiffre.")
liste.insert(5, "- Au moins 1 caractère spécial.")

liste.pack(side= BOTTOM, ipadx= 35)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side= TOP, padx=2, pady=5)


# Ajout de labels
Label(Frame1, text="Veuillez entrer vos logins.", bg="#C8ADC0").pack(padx=10, pady=10)
Label(Frame2, text="").pack(padx=10, pady=10)
Label(Frame3, text="Votre mot de passe doit contenir :",bg="white").pack(padx=10, pady=10)

Text= "Nom d'uilisateur"
# Entrée nom d'utilisateur
entree_nom_utilisateur = StringVar() 
entree_nom_utilisateur.set("")

# Nom d'uilisateur                                     
nom_utilisateur = Entry(Frame1, textvariable=entree_nom_utilisateur, width=30)
nom_utilisateur.pack()

text="Mot de passe"
# Entrée mot de passe
entree_mdp = StringVar() 
entree_mdp.set("") 

# Mot de passe                                          # Cacher mdp
mdp_utilisateur = Entry(Frame1, textvariable=entree_mdp,show="*", width=30)
mdp_utilisateur.pack()

# Bouton pour rendre le mdp visible ou masqué
voir_mdp = BooleanVar()
voir_mdp.set(False)  # Mdp masqué par défaut
show_button = Checkbutton(Frame1, text="Cliquez pour afficher le mot de passe", variable=voir_mdp, command=toggle_visibility, bg="#C8ADC0")
show_button.pack()

# Favicon
fenetre.iconphoto(False, PhotoImage(file='favicon.png'))

# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()

alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    # Demande à l'utilisateur de saisir un mot de passe
    mdp_utilisateur = input("Veuillez entrer un mot de passe: ")

    # Vérification si le mot de passe correspond aux critères
    if (any(c.islower() for c in mdp_utilisateur)
        and any(c.isupper() for c in mdp_utilisateur)
        and any(c.isdigit() for c in mdp_utilisateur)
        and any(c in string.punctuation for c in mdp_utilisateur)
        and len(mdp_utilisateur) >= 8):
            print("Ce mot de passe fonctionne.")
            break  # Sortir de la boucle si le mdp est valide
    else:
        print("Ce mot de passe n'est pas valide, il ne répond pas aux critères. Veuillez réessayer.")

# Hashage du mdp avec hashlib
hashed_mdp_utilisateur = hashlib.sha256(mdp_utilisateur.encode()).hexdigest()

# Vérifier si le fichier JSON existe déjà
if os.path.exists('bibliotheque.json'):
    # Charger les mdp précédents depuis le fichier JSON
    with open('bibliotheque.json', 'r') as bibliotheque_mdp:
        mdp_codés = json.load(bibliotheque_mdp)
else:
    mdp_codés = []

# Ajouter le nouveau mot de passe haché à la liste
mdp_codés.append(hashed_mdp_utilisateur)

# Sauvegarder la liste mise à jour dans le fichier JSON
with open('bibliotheque.json', 'w') as bibliotheque_mdp:
    json.dump(mdp_codés, bibliotheque_mdp)



