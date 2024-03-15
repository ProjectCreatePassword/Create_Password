import hashlib
import random
import string
import os
import json


def verifier_mdp(mdp):
    """Verifie les conditions acceptables pour un mot de passe.
    
        ● Il doit contenir au moins 8 caractères.
        ● Il doit contenir au moins une lettre majuscule.
        ● Il doit contenir au moins une lettre minuscule.
        ● Il doit contenir au moins un chiffre.
        ● Il doit contenir au moins un caractère spécial ( ! , @, #, $, %, ^, & , *).
    """
       # Au moins une majuscule
       # Minuscule
       # Chiffre
       # caractère spéciale
    if len(mdp) < 8:
        print('Le mot de passe doit contenir au moins 8 caractères')
        return False 
    
    num_minuscule = 0
    num_majuscule = 0
    num_chiffres = 0
    num_special = 0 
    for character in mdp:
        if character in string.ascii_uppercase :
            num_majuscule = num_majuscule + 1
        if character in string.ascii_lowercase:
            num_minuscule +=1
        if character in string.digits:
            num_chiffres +=1
        if character in string.punctuation:
            num_special +=1


    if  num_majuscule == 0:
        print('ERREUR : Le mot de passe doit contenir au moins une majuscule ')
        return False
    if num_minuscule == 0:
        print('ERROR: Le mot de passe doit contenir au moins une minuscule')
        return False
    if num_special == 0:
        print("ERROR: Le mot de passe doit contenir au moins 1 caractère spécial ")
        return False
    if num_chiffres == 0:
        print("ERROR: Le mot de passe doit contenir au moins 1 chiffres ")
        return False
    return True

def generate_password(length=10):
    # Définition des caractères possibles dans le mot de passe
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Génération du mot de passe
    password = "".join(random.choice(caracteres) for _ in range(length))
    return password

mdp = generate_password(10)

def hash_password(password):
    # Crée un hachage SHA-256 du mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


while True:
    mdp = input("Ecrivez un mdp : ")
    if verifier_mdp(mdp):
        print("Success")
        break

# Hashage du mdp avec hashlib
hashed_mdp_utilisateur = hashlib.sha256(mdp.encode()).hexdigest()

# Vérifier si le fichier JSON existe déjà
if os.path.exists('bibliotheque.json'):
    # Charger les mdp précédents depuis le fichier JSON
    with open('bibliotheque.json', 'r') as bibliotheque_mdp:
        mdp_hashed = json.load(bibliotheque_mdp)
else:
    mdp_hashed = []

# Ajouter le nouveau mot de passe haché à la liste
mdp_hashed.append(hashed_mdp_utilisateur)

# Sauvegarder la liste mise à jour dans le fichier JSON
with open('bibliotheque.json', 'w') as bibliotheque_mdp:
    json.dump(mdp_hashed, bibliotheque_mdp)

