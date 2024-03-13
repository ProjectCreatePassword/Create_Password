from tkinter import *
import string
import random

window = Tk()

window.columnconfigure(0, weight=1)

#-------------------------------------------------------
#Ajout fonctions
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
		return motdepasse
		entrer_mdp.config(fg="green")
	else:
		message = "Mot de passe incorrect"
		entrer_mdp.config(fg="red")
		entrer_mdp.delete(0, 100)
		entrer_mdp.insert(0, message)
		generate.grid(column=0, row=4, sticky="e")
		erreur.grid(column=1, row=1, sticky="w")


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
	entrer_mdp.config(fg="green")


#-------------------------------------------------------
#---------Propriétés de la fenêtre
window.title("test")
window.geometry("700x700")
window.maxsize(1920, 1080)
window.minsize(700, 700)
window.config(bg="#181A1B")

#-------------------------------------------------------
#---------Ajout Titre
titre = Label(window, text="Inscription", font=("Courrier", 40), fg="#631CD0", bg="#181A1B")
titre.grid(row=0, pady=30)

#------------------------------------------------------
#---------Ajout Frame form
form = Frame(window, bg="#181A1B")
form.grid(pady=100, ipady=100, sticky="ew")
form.columnconfigure(0, weight=2)
form.columnconfigure(1, weight=2)
form.columnconfigure(2, weight=2)

#-------------------------------------------------------
#---------Ajout grid
colonne1 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne1.grid(row=0, column=0, sticky="ew")
colonne2 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne2.grid(row=0, column=1, sticky="ew")
colonne3 = Label(form, text="test", bg="#181A1B", fg="#181A1B")
colonne3.grid(row=0, column=2, sticky="ew")

#-------------------------------------------------------
#---------Ajout input username
username = Entry(form, bg=("#181A1B"), fg=("white"), font=("Courrier", 15))
username.grid(row=2, column=1, pady=20, sticky="ew", padx=20)

#-------------------------------------------------------
#---------Label input username
label_username = Label(form, font=("Courrier", 12), bg="#181A1B", fg="white", text="Nom d'utilisateur:", anchor="e")
label_username.grid(row=2, column=0, sticky="ew")

#-------------------------------------------------------
#---------Message d'erreur
message = """Votre mot de passe doit contenir au moins:
- 8 caractères
- Un caractère spécial
- Une majuscule
- Une minuscule
- Un chiffre"""
erreur = Label(form, font=("Courrier", 10), bg="#181A1B", fg="red", text=message, anchor="w", justify="left")

#-------------------------------------------------------
#---------Ajout input mot de passe
entrer_mdp = Entry(form, bg=("#181A1B"), fg=("white"), font=("Courrier", 15))
entrer_mdp.grid(row=3, column=1, pady=20, sticky="ew", padx=20)

#-------------------------------------------------------
#---------Label input mot de passe
label_mdp = Label(form, font=("Courrier", 12), bg="#181A1B", fg="white", text="Mot de passe:", anchor="e")
label_mdp.grid(row=3, column=0, sticky="ew")

#-------------------------------------------------------
#---------Bouton soumettre
soumettre = Button(form, text="Envoyer", width=30, bg="#631CD0", fg="white", command=ispasswordtrue)
soumettre.grid(column=1, row=4)

#-------------------------------------------------------
#---------Bouton générer
generate = Button(form, text="Générer un mot de passe", bg="#631CD0", fg="white", command=genpassword)

#---------Afficher la fenêtre
window.mainloop()



# Espace de test____________________________________________________________________________________

#fonction checkpassword revisité pour tkinter

		# texterreur.config(text="Veuillez entrer un mot de passe correct", fg="red")
		# texterreur.grid(row=4, column=1, pady=10, sticky="ew")
