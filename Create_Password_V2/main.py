# Import des différents modules
from tkinter import *
import hashlib
import string
import random
import json
import customtkinter as ctk
import os

# -------------------------------------------------------
# Ajout fonctions
def afficher_validation():
    validation.grid(column=1, row=4, pady=5)
    if erreur.winfo_ismapped():  
        erreur.grid_forget()  
    elif erreur2.winfo_ismapped():  
        erreur2.grid_forget()  
			

def afficher_erreur():
    erreur.grid(column=1, row=4, pady=5)
    if validation.winfo_ismapped():  
        validation.grid_forget()  
    elif erreur2.winfo_ismapped():  
        erreur2.grid_forget()  

def afficher_erreur_mdp_existant():
    erreur2.grid(column=1, row=4, pady=5)
    if validation.winfo_ismapped():  
        validation.grid_forget()  
    elif erreur.winfo_ismapped():  
        erreur.grid_forget()  




#-- Fonction pour vérifier si le mot de passe correspond bien aux critères
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
		# On vérifie si le mot de passe est supérieur à 8
		if len(motdepasse) >= 8:
			for char in motdepasse:
				# On vérifie que le mdp contienne au moins une majuscule
				if char in majuscules:
					maj_présente = True
				# On vérifie que le mdp contienne au moins une minuscule
				if char in minuscules:
					min_présente = True
				# On vérifie que le mdp contienne au moins un nombre
				if char in chiffre:
					chiffre_présent = True
				# On vérifie que le mdp contienne au moins un caractère spécial
				if char in spécial:
					spécial_présent = True

			return maj_présente and min_présente and chiffre_présent and spécial_présent
		return False

	if checkpassword():
		motdepasse = entrer_mdp.get()
		HashPassword(motdepasse)
		afficher_validation()
		return motdepasse
	else:
		afficher_erreur()

#----- Fonction pour générer un mot de passe
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
	".join return mdp"
	entrer_mdp.delete(0, 100)
	entrer_mdp.insert(0, mdp)

#----- Fonction pour hasher un mot de passe
def HashPassword(motdepasse):
	motdepasse_sign = hashlib.sha512(motdepasse.encode()).hexdigest()
	motdepasse_crypté = [motdepasse_sign] 
	fichier = "passwords.json"
	if motdepasse_crypté == motdepasse_crypté:
		afficher_erreur_mdp_existant()
	else:
		with open(fichier, "a") as file:
			json.dump(motdepasse_crypté, file)
			file.write("\n")

#----- Fonction pour montrer les mots de passe hashés dans le GUI
def ShowPasswords():
	fichier = "passwords.json"
	with open(fichier, "r") as file:
		mdpcryptés.delete(1.0, 1000.0)
		for line in file:
			mdp = json.loads(line)
			mdpcryptés.grid(column=0, columnspan=3)
			mdpcryptés.configure(height=100, width=600)
			mdpcryptés.insert(1.0, str(mdp)+'\n')

# Fonction du bouton pour rendre visible ou non le mdp
def toggle_visibility():
    if voir_mdp.get():
        entrer_mdp.config(show="")
    else:
        entrer_mdp.config(show="*")

#------------------------------------- Fenêtre CTK
#-------------- Thèmes et Couleurs
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#--------- Propriétés de la fenêtre
window = ctk.CTk()
window.columnconfigure(0, weight=1)
window.title("MY PASSWORD")
window.iconbitmap("Create_Password_V2/favicon.ico")
window.minsize(500, 200)
window.maxsize(500, 300)
window.config(bg="#181A1B")

#--------- Ajout Titre
titre = Label(window, text="Gestionnaire de mot de passe", font=("Courrier", 30), fg="#631CD0", bg="#181A1B")
titre.grid(row=0, pady=0)

#------------------------------------------------------
#--------- Ajout Frame form
form = Frame(window, bg="#181A1B")
form.grid(pady=10, ipady=0, sticky="ew")
form.columnconfigure(0, weight=2)
form.columnconfigure(1, weight=2)
form.columnconfigure(2, weight=2)

#-------------------------------------------------------
#--------- Ajout grid
colonne1 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne1.grid(row=0, column=0, sticky="ew")
colonne2 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne2.grid(row=0, column=1, sticky="ew")
colonne3 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne3.grid(row=0, column=2, sticky="ew")

#-------------------------------------------------------

#--------- Message de validation
message1 = "Votre mot de passe est valide."
validation = Label(form, font=("Courrier", 10), bg="#181A1B", fg="green", text=message1, anchor="w", justify="left")

#--------- Message d'erreur
message2 = """Votre mot de passe doit contenir au moins:
- 8 caractères
- Un caractère spécial
- Une majuscule
- Une minuscule
- Un chiffre"""
erreur = Label(form, font=("Courrier", 10), bg="#181A1B", fg="red", text=message2, anchor="w", justify="left")

message3 = "Ce mot de passe est déjà présent dans la bibliothèque hashlib."
erreur2 = Label(form, font=("Courrier", 10), bg="#181A1B", fg="red", text=message3, anchor="w", justify="left")
#----------------------------------------------------------------
#--------- Ajout input mot de passe
entrer_mdp = Entry(form, bg=("#181A1B"), fg=("white"), font=("Courrier", 15), insertbackground="white", show="*")
entrer_mdp.grid(row=2, column=1, pady=10, sticky="ew", padx=20)

#--------- Label input mot de passe
label_mdp = Label(form, font=("Courrier", 12), bg="#181A1B", fg="white", text="Mot de passe:", anchor="e")
label_mdp.grid(row=2, column=0, sticky="ew")

#----------------------------------------------------------------
# Bouton pour rendre le mdp visible ou masqué
voir_mdp = BooleanVar()
voir_mdp.set(False)  # Mdp masqué par défaut
show_button = Checkbutton(form, text="Afficher le mot de passe", variable=voir_mdp, command=toggle_visibility, bg="#631CD0", fg= "white", selectcolor="#181A1B")
show_button.grid(column=2, row=2)

#--------- Bouton soumettre
soumettre = Button(form, text="Envoyer", width=30, bg="#631CD0", fg="white", command=ispasswordtrue)
soumettre.grid(column=1, row=3, pady=10)
#soumettre.bind("<Return>",ispasswordtrue)

#--------- Bouton générer mdp
generate = Button(form, text="Générer un mot de passe", bg="#631CD0", fg="white", command=genpassword)

#--------- Bouton voir mdp cryptés
voir_mdpcryptés = Button(form, text="Voir mes mots de passe cryptés", width=30, bg="#631CD0", fg="white", command=ShowPasswords)
voir_mdpcryptés.grid(column=1, row=5, pady=10)
mdpcryptés = Text(window, bg="#631CD0", fg="white",)


#--------- Afficher la fenêtre
window.mainloop()



# Espace de test____________________________________________________________________________________

#fonction checkpassword revisité pour tkinter

		# texterreur.config(text="Veuillez entrer un mot de passe correct", fg="red")
		# texterreur.grid(row=3, column=1, pady=10, sticky="ew")