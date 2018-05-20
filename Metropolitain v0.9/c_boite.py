""" 
Cet classe, Boite, va représenter une scène, c'est à dire un ensemble de chainons regoupé en un seul objet, pour pouvoir naviguer entre eux.
Son but est de créer ce tableau de Chainage mais aussi de simplifer/personaliser son utilisation,
car on veut que notre Boite soit un tableau en 2 dimensions, donc on va créer des fonctions pour utiliser ce tableau un peu spéciale.
"""

import pickle  # On importe la classe "pickle", elle va nous servir pour enregistrer notre dialogue dans un fichier


class Boite: # On définit notre classe, que l'on appelle "Boite" :
	

	def __init__(self, nom): # Constructeur -> Lors de la création d'un nouvelle objet Boite, on assigne des valeurs à nos variables :
		self.nom = nom # Nom de la scène
		self._tableau = [[]] # Notre tableau à deux dimensions en question, par défaut vide



	def __getitem__(self, index): # Cette méthode spéciale est appelée quand on fait objet[index]
		return self._tableau[index]
		""" Cette fonction est apellée lorsqu'on écrit par exemple :
		|newBoite = Boite("Scène 1")
		|print(newBoite[0]) 					<---- ici
		"""



	def __setitem__(self, index, valeur): # Cette méthode est appelée quand on écrit objet[index] = valeur
		self._tableau[index] = valeur



	def __repr__(self): # Cette fonction sert à retourner le tableau sous forme de str
		return str(self._tableau)

		""" Cette fonction est apellée lorsqu'on écrit par exemple :
		|newBoite = Boite("ma Boite")
		|print(newBoite) 					<---- ici
		"""



	def Ajouter(self, item, index): # Cette fonction sert à ajouter un chainage à la fin d'une colonne
		if index < len(self._tableau): # Si la colonne existe déjà alors on l'ajoute dans la colonne
			self._tableau[index].append(item)
		elif index == len(self._tableau): # Sinon si l'index de la colonne n'existe pas mais qu'il peut être ajouter alors on ajoute une colonne
			self._tableau.append([item])
		else: # Sinon si l'index est trop grand on dit qu'il y a une erreur
			print("E: Erreur l'index est trop grand !")
	


	def Inserer(self, item, indexX, indexY): # Cette fonction sert à inserer au sein du colonnes un chainage
		if indexX == len(self._tableau): # Si on doit créer une nouvelle colonne alors le chainage sera forcement en haut donc on peut utiliser la fonction append()
			self._tableau.append([item])
		elif indexX < len(self._tableau): # Sinon si l'index existe 
			if (indexY == len(self._tableau[indexX])): # et que l'on veut inserer le chainage à la fin de la colonne alors on utilise la fonction append()
				self._tableau[indexX].append(item)
			elif (indexY < len(self._tableau[indexX])): # ou si on veut inserer le chainage au milieu de la colonne on utilise la fonction insert()
				self._tableau[indexX].insert(indexY, item)
			else:
				print("E: L'index Y n'existe pas") # Sinon cela veux dire que l'index "y", n'existe pas, donc on signale l'erreur
		else:
			print("E: L'index X n'existe pas") # Sinon cela veut dire que l'index "x" est trop grand ou négatif



	def Supprimer(self, indexX, indexY): # Cette fonction sert à supprimer un chainage dans le tableau
		if indexX < len(self._tableau): # 
			if (indexY == 0 and indexY == len(self._tableau[indexX])-1): # Si l'index qu'on veut supprimer et le dernier de la colonne alors on supprime la colonne directement
				del self._tableau[indexX];
			elif (indexY < len(self._tableau[indexX])): # Sinon si le chainage n'est pas le dernier alors on le supprime dans la colonne
				del self._tableau[indexX][indexY];
			else:
				print("E: L'index Y n'existe pas") # Sinon cela veux dire que l'index "y", n'existe pas, donc on ne peut pas le supprimer
		else:
			print("E: L'index X n'existe pas") # Sinon cela veux dire que l'index "x" n'existe, donc on ne peut pas le supprimer



	def Save(self): # Cette fonction sert à sauvegarder notre objet boite
		with open(str(self.nom)+'.save', 'wb') as fichier: # Pour cela on créer ou écrase un fichier qui porte le nom de la boite suivi de ".save"
			mon_pickler = pickle.Pickler(fichier) # En utilisant la librairie pickle
			mon_pickler.dump(self._tableau) 



	def Load(self, nom): # Cette fonction sert à charger un fichier préalablement sauvegardé
		with open(str(nom)+'.save', 'rb') as fichier: # On essaye d'ouvrir le fichier "nom".save
			mon_depickler = pickle.Unpickler(fichier)
			boite_recupere = mon_depickler.load()
			self._tableau = boite_recupere # Si ça marche on assigne nos variables à ceux sauvegardés
			self.nom = nom



	def New(self, nouveauNom): # Cette fonction sert à réinitialiser une boite, à la remettre à zéro
		self._tableau = [] # Avec un tableau vide 
		self.nom = nouveauNom # et un nouveau nom



	def GetYndex(self, index):
		return int(len(self._tableau[index]) -1)



	def GetIndice(self, indeX): 
		listeTemp = []
		try:
			if(str(type(self._tableau[indeX][len(self._tableau[indeX]) -1])) == "<class 'c_chainage.Chainage'>"):
				for i in range(0, len(self._tableau[indeX])): # Refaire cette boucle, tu veux qu'elle te renvoe quoi ?
					print("i :" + str(i) + " - " + "indice : " + str(self._tableau[indeX][i].indice))
					if self._tableau[indeX][i].indice != i:
						# print("return : " + str(i))
						print("Return ---> " + str(i) + " ou plutôt ça : " + str(self._tableau[indeX][i].indice))
						return i
				for i in range(0, len(self._tableau[indeX])):
					listeTemp.append(int(self._tableau[indeX][i].indice))


				for i in range(0, len(self._tableau[indeX])):
					if (listeTemp.count(i) == 0):
						return i

				return (self._tableau[indeX][len(self._tableau[indeX]) -1].indice + 1)
			else:
				print("E: L'index \"[" + str(indeX) + "]" + "[" + str(len(self._tableau[indeX]) -1) + "]" +"\" de la boite ne contient pas un Chainage!")
				return -1
		except: # Si c'est le premier :	
			return 0



	def Lenx(self): # Cette fonction renvoie le nombre de colonnes dans le tableau, elle ne prend pas en compte la deuxième dimensions
		return len(self._tableau) # Pour cela on utilise la fonction qui len()
		""" Par exemple :
		|tableau = [[0, 1] [2, 3]]
		|print(tableau.Lenx()) 				<---- Afficherai le nombre : 2, car il y a deux colonnes
		"""



	def Len(self): # Cette fonction renvoie le nombre d'élement dans la totalité du tableau, elle prend donc en compte les deux dimensions
		taille = 0 # Pour cela on défint une variable égale à 0, qui va être incrémenté pour chaque élement du tableau :
		for x in range(0, len(self._tableau)):
			for y in range(0, len(self._tableau[x])):
				taille += 1
		return taille # Et on renvoie la taille
		""" Par exemple :
		|tableau = [[0, 1] [2, 3]]
		|print(tableau.Len()) 				<---- Afficherai le nombre : 4, car il y a 4 éléments dans le tableau
		"""

