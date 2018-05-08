
pvDuJoueur = 0
inventaireDuJoueur = []
toutLesObjets = []

def Functions(texte):
	if (texte[0] == '0'): # Gain PV
		print("Le PJ gagne : " + texte[1] + " pv")
		# pvDuJoueur += texte[1] 

	elif (texte[0] == '1'): # Perte PV
		print("Le PJ perd : " + texte[1] + " pv")
		# pvDuJoueur -= texte[1] 

	elif (texte[0] == '2'): # Gain Objet
		print("Le PJ gagne l'objet n° " + texte[1])
		# inventaireDuJoueur.append(toutLesObjets[texte[0]])

	elif (texte[0] == '3'): # Perte Objet
		print("Le PJ perd l'objet n° " + texte[1] + " de son inventaire")

	elif (texte[0] == '4'): # Gain Carac
		if (texte[1] == '0'): # Physique
			print("Le PJ gagne " + texte[2] + " en physique")
		elif (texte[1] == '1'): # Mental
			print("Le PJ gagne " + texte[2] + " en mental")
		elif (texte[1] == '2'): # Sociale
			print("Le PJ gagne " + texte[2] + " en sociale")

	elif (texte[0] == '5'): # Perte Carac
		if (texte[1] == '0'): # Physique
			print("Le PJ perd " + texte[2] + " en physique")
		elif (texte[1] == '1'): # Mental
			print("Le PJ perd " + texte[2] + " en mental")
		elif (texte[1] == '2'): # Sociale
			print("Le PJ perd " + texte[2] + " en sociale")


Functions("04")
Functions("12")
Functions("22")
Functions("32")
Functions("412")
Functions("521")