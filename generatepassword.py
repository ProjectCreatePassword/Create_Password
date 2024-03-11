import random
import string




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


monmdp = genpassword()

print(monmdp)


