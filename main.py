import string
import hashlib
import json
import os

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

