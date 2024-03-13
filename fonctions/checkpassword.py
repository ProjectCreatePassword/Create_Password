import string



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

		retour = maj_présente and min_présente and chiffre_présent and spécial_présent
		return retour
	retour = False
	return retour



print(checkpassword("BurtoN_TylL"))




			

		



