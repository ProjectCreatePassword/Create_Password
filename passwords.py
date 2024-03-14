from tkinter import *
import customtkinter
import tkinter
from PIL import Image
import string
import random
from hashlib import sha512
import json
import os


message_erreur = """Votre mot de passe doit contenir
au moins:
- 8 caractères
- Un caractère spécial
- Une majuscule
- Une minuscule
- Un chiffre"""

message_correct = "Votre mot de passe est correct"

message_deja_existant = "Le mot de passe existe déjà"
#-------------------------------------------------------
#Ajout fonctions
def checkpassword(mdp):
		majuscules = string.ascii_uppercase
		minuscules = string.ascii_lowercase
		chiffre = string.digits
		spécial = string.punctuation
		maj_présente = False
		min_présente = False
		chiffre_présent = False
		spécial_présent = False
		#On vérifie si le mot de passe est supérieur à 8
		if len(mdp) >= 8:
			for char in mdp:
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


def ispasswordtrue():

	def checkpassword():
		motdepasse = entrer_mdp.get()
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

	if checkpassword():
		motdepasse = entrer_mdp.get()
		validation.configure(text=message_correct, fg="green")
		HashPassword(motdepasse)
		entrer_mdp.delete(0, 100)
	else:
		entrer_mdp.delete(0, 100)
		validation.grid(column=1, row=1)
		validation.configure(text=message_erreur, fg="red")


def genpassword():
	lettre_min = string.ascii_lowercase
	lettre_maj = string.ascii_uppercase
	chiffre = string.digits
	symbole = string.punctuation
	caractère = lettre_min + lettre_maj + symbole + chiffre
	mdp = ""
	checkpassword(mdp)
	while not checkpassword(mdp):
		mdp= ""
		for i in range(0, 15):
			cmdp = random.choice(caractère)
			mdp = mdp + cmdp
			".join return mdp"
			checkpassword(mdp)
	else:
		entrer_mdp.delete(0, 100)
		entrer_mdp.insert(0, mdp)


def HashPassword(motdepasse):
	motdepasse = motdepasse.encode()
	motdepasse_sign = sha512(motdepasse).hexdigest()
	fichier = "passwords.json"
	list_mdp_cryptés = []
	if os.path.getsize(fichier) > 0:
		#On charge les mots de passe déjà existants
		with open(fichier, "r") as file:
			list_mdp_cryptés = json.load(file)
		if motdepasse_sign in list_mdp_cryptés:
			validation.grid(column=1, row=1)
			validation.configure(text=message_deja_existant)
		else:
			#On ajoute le nouveau mot de passe crypté à la liste
			list_mdp_cryptés.append(motdepasse_sign)
			#On réécrit le fichier avec le nouveau mot de passe
			with open(fichier, "w") as file:
				json.dump(list_mdp_cryptés, file)
	else:
		with open(fichier, "w") as file:
			json.dump([motdepasse_sign], file)

def ShowPasswords():
	fichier = "passwords.json"
	with open(fichier, "r") as file:
		mdpcryptés.delete(1.0, "end")
		mdp = json.load(file)
		for element in mdp:
			mdpcryptés.grid(column=0, columnspan=3)
			mdpcryptés.configure(height=100, width=600)
			mdpcryptés.insert(1.0, (f"[ {element} ]\n________________________________________________________________________________________________\n\n"))

def toggle_visibility():
    if voir_mdp.get():
        entrer_mdp.configure(show="")
    else:
        entrer_mdp.configure(show="*")

def DidPasswordAlreadyExist():
	fichier = "passwords.json"
	list_mdp_cryptés = []
	new_mdp = []
	new_mdp.append(motdepasse_sign)
	with open(fichier, "r") as file:
		for line in file:
			mdp = json.loads(line)
			list_mdp_cryptés.append(mdp)
			for password in new_mdp:
				if new_mdp in list_mdp_cryptés:
					print("deja la")
				else:
					print("yeaaah")


#--------------------------------------------
#------------Initialisation fenêtre
window = Tk()
window.geometry("700x500")
window.minsize(700, 500)
window.title("Générateur de mots de passe")
window.configure(bg="#181A1B")

#--------------------------------------------
#------------Grille
colonne1 = Label(window, text="PasswordGenerator", font=("Courrier", 30), bg="#181A1B", fg="#181A1B")
colonne1.grid(row=1, column=0, sticky="ew")
colonne2 = Label(window, text="PasswordGenerator", font=("Courrier", 30), bg="#181A1B", fg="#181A1B")
colonne2.grid(row=1, column=1, sticky="ew")
colonne3 = Label(window, text="PasswordGenerator", font=("Courrier", 30), bg="#181A1B", fg="#181A1B")
colonne3.grid(row=1, column=2, sticky="ew")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

#--------------------------------------------
#------------Titre
titre = customtkinter.CTkLabel(master=window, text="PasswordGenerator", font=("Courrier", 30))
titre.grid(sticky="ew", column=0, row=0, columnspan=3)

#--------------------------------------------
#------------Image
image = customtkinter.CTkImage(light_image=Image.open("cadenas.png"), dark_image=Image.open("cadenas.png"),
	size=(150, 100))
image_label = customtkinter.CTkLabel(window, text="", image=image)
image_label.grid(column=2, row=0, pady=10)

#--------------------------------------------
#------------Frame contenu
contenu = Frame(window, bg="#181A1B")
contenu.grid(pady=10, column=1)

#-------------------------------------------------------
#---------Message de validationvalidation
validation = Label(window, font=("Courrier", 10), bg="#181A1B", justify="left", anchor="w")

#--------------------------------------------
#------------Input mdp
entrer_mdp = customtkinter.CTkEntry(master=contenu, show="*", bg_color="#181A1B", fg_color="#4c4f4c", corner_radius=8, width=200, placeholder_text="Entrez un mot de passe")
entrer_mdp.grid(pady=5, row=1) 

# Bouton pour rendre le mdp visible ou masqué
voir_mdp = BooleanVar()
voir_mdp.set(False)  # Mdp masqué par défaut
show_button = customtkinter.CTkCheckBox(master=window, text="Afficher le mot de passe", variable=voir_mdp, command=toggle_visibility, fg_color="white", border_width=2, border_color="#ff0000", corner_radius=8)
show_button.grid(column=2, row=2)

#--------------------------------------------
#------------Bouton générer mdp
generate = customtkinter.CTkButton(master=contenu, bg_color="#181A1B", fg_color="#631CD0", corner_radius=8, width=200 , text="Générer un mot de passe", command=genpassword)
generate.grid(pady=5, row=2)

#--------------------------------------------
#------------Bouton envoyer mdp
envoyer = customtkinter.CTkButton(master=contenu, bg_color="#181A1B", fg_color="#78BB7B", corner_radius=8, width=200, text="Envoyer", command=ispasswordtrue)
envoyer.grid(pady=5, row=3)

#--------------------------------------------
#------------Bouton show mdp
afficher = customtkinter.CTkButton(master=contenu, bg_color="#181A1B", fg_color="#0090ff", corner_radius=8, width=200, text="Afficher les mots de passe", command=ShowPasswords)
afficher.grid(pady=5, row=4)

#--------------------------------------------
#------------Label show mdp
mdpcryptés = customtkinter.CTkTextbox(master=window)

#--------------------------------------------
#------------Affichage fenêtre
window.mainloop()
