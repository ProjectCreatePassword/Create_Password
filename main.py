import string
import hashlib
import json
import os

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
        print("Le mot de passe n'est pas valide, il ne répond pas aux critères. Veuillez réessayer.")

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






# Générateur de mdp
