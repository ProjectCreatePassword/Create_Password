import string
import random

#--------------------------------------------------------------------------------------------

enter_username = "Entrez votre nom d'utilisateur : "
enter_mdp = "Entrez votre mot de passe : "
générer_mdp = "Mot de passe incorect. Voulez-vous entrer un autre mot de passe (1) ou en générer un automatiquement?(2)"
quitter = "Entrez 1 pour quitter le gestionnaire ou 2 pour continuer : "

# Initialisation des listes pour stocker les utilisateurs, les mots de passe et les identifiants
username = []
mdp = []
userid = []

#Fonction pour vérifier un mot de passe
def checkpassword(motdepasse):
    majuscules = string.ascii_uppercase
    minuscules = string.ascii_lowercase
    chiffre = string.digits
    spécial = string.punctuation
    maj_présente = False
    min_présente = False
    chiffre_présent = False
    spécial_présent = False
    #On vérifie si le mot de passe est supérieur à 8
    if len(motdepasse) >= 8:
        for char in motdepasse:
            #On vérifie que le mdp contienne au moins une majuscule
            if char in majuscules:
                maj_présente = True
            #On vérifie que le mdp contienne au moins une minuscule
            if char in minuscules:
                min_présente = True
            #On vérifie que le mdp contienne au moins un nombre
            if char in chiffre:
                chiffre_présent = True
            #On vérifie que le mdp contienne au moins un caractère spécial
            if char in spécial:
                spécial_présent = True

        return maj_présente and min_présente and chiffre_présent and spécial_présent
    return False

# Fonction pour générer un mot de passe correct
def genpassword():
    lettre_min = string.ascii_lowercase
    lettre_maj = string.ascii_uppercase
    chiffre = string.digits
    symbole = string.punctuation
    caractère = lettre_min + lettre_maj + symbole + chiffre
    mdp = ""
    for i in range(0, 15):
        cmdp = random.choice(caractère)
        mdp = mdp + cmdp
    return mdp



# Fonction pour ajouter un utilisateur
def adduser():
    user_choice = ""
    i = 0

    while user_choice != 1:
        user = input(enter_username)
        motdepasse = input(enter_mdp)
        #Validation du mot de passe---------------------------------
        checkpassword(motdepasse)
        while checkpassword(motdepasse) == False:
            choix_mdp = int(input(générer_mdp))
            if choix_mdp == 1:
                motdepasse = input(enter_mdp)
            elif choix_mdp == 2:
                motdepasse = genpassword()
            else:
                print("Entrée incorrecte.")
            checkpassword(motdepasse)
        else:
            # Ajout des informations de l'utilisateur dans les listes
            username.append(user)
            mdp.append(motdepasse)
            userid.append(i)

            print("Utilisateurs : ", username)
            print("Mots de passe : ", mdp)
            print("Identifiants : ", userid)

            i += 1

            user_choice = input(quitter)

            # Vérification de la saisie de l'utilisateur
            if user_choice == "1" or user_choice == "2":
                user_choice = int(user_choice)
            else:
                print("Veuillez entrer 1 ou 2.")

                # Si la saisie n'est pas valide, on annule l'ajout de l'utilisateur précédent
                username.pop(-1)
                mdp.pop(-1)
                userid.pop(-1)

    print("\n________________________________________________\n")
    return username, mdp, userid



# Fonction pour afficher les informations d'un utilisateur
def show_user(user):
    if user in username:
        i = username.index(user)
        print("Nom d'utilisateur : ", username[i])
        print("Mot de passe : ", mdp[i])
        print("Identifiant : ", userid[i])
    else:
        print("Utilisateur non trouvé.")


# Appel de la fonction pour ajouter un utilisateur
# adduser()



# Appel de la fonction pour afficher les informations de l'utilisateur 
# show_user("burton")


def conversion():
    adduser()
    str(username)
    str(mdp)
    str(userid)
    return (f"{username}, {mdp}, {userid}")

#----------------------------------------------------------------
def enregistrer_contenu_dans_fichier(nom_fichier):
    # Appel de la fonction pour obtenir le contenu
    contenu = conversion()

    # Ouverture du fichier en mode écriture
    with open(nom_fichier, "a") as fichier:
        # Écriture du contenu dans le fichier
        fichier.write(contenu)

    print("Le contenu a été enregistré dans le fichier", nom_fichier)

# Appel de la fonction pour enregistrer le contenu dans un fichier texte
enregistrer_contenu_dans_fichier("motsdepasse.txt")



