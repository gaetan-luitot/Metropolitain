""" 
Cet classe, Boite, va représenter une scène, c'est à dire un ensemble de chainons regoupé en un seul objet, pour pouvoir naviguer entre eux.
Son but est de créer ce tableau de Chainage mais aussi de simplifer/personaliser son utilisation,
car on veut que notre Boite soit un tableau en 2 dimensions, donc on va créer des fonctions pour utiliser ce tableau un peu spéciale.
"""


import pickle  # On importe la classe "pickle", elle va nous servir pour enregistrer notre dialogue dans un fichier


class Boite: # On définit notre classe, que l'on appelle "Boite" :
	

	def __init__(self, nom):
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



	def __repr__(self):
		return str(self._tableau)



	def Ajouter(self, item, index):
		if index < len(self._tableau):
			self._tableau[index].append(item)
		elif index == len(self._tableau):
			self._tableau.append([item])
		else:
			print("E: Erreur l'index est trop grand !")
	


	def Inserer(self, item, indexX, indexY):
		if indexX == len(self._tableau):
			self._tableau.append([item])
		elif indexX < len(self._tableau):
			if (indexY == len(self._tableau[indexX])):
				self._tableau[indexX].append(item)
			elif (indexY < len(self._tableau[indexX])):
				self._tableau[indexX].insert(indexY, item)
			else:
				print("E: L'index Y n'existe pas")
		else:
			print("E: L'index X n'existe pas")



	def Supprimer(self, indexX, indexY):
		if indexX < len(self._tableau):
			if (indexY == 0 and indexY == len(self._tableau[indexX])-1):
				del self._tableau[indexX];
			elif (indexY < len(self._tableau[indexX])):
				del self._tableau[indexX][indexY];
			else:
				print("E: L'index Y n'existe pas")
		else:
			print("E: L'index X n'existe pas")



	def Save(self):
		with open(str(self.nom)+'.save', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(self._tableau)



	def Load(self, nom):
		with open(str(nom)+'.save', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			boite_recupere = mon_depickler.load()
			self._tableau = boite_recupere
			self.nom = nom



	def New(self, nouveauNom):
		self._tableau = []
		self.nom = nouveauNom



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



	def Lenx(self): # Cette fonction renvoie la taille du tableau mais uniquement l'axe des X, elle ne prend pas en compte la deuxième dimensions
		return len(self._tableau)
		""" Par exemple :
		|tableau = [[0, 1] [2, 3]]
		|print(tableau.Lenx()) 					<---- Afficherai le nombre : 2
		"""



	def Len(self):
		taille = 0
		for x in range(0, len(self._tableau)):
			for y in range(0, len(self._tableau[x])):
				taille += 1
		return taille
		""" Par exemple :
		|tableau = [[0, 1] [2, 3]]
		|print(tableau.Len()) 					<---- Afficherai le nombre : 4
		"""

