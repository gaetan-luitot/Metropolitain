""" 
Cet classe regroupe 2 variables (x et z) qui correspond à une position 
"""

class Vecteur: # On définit notre classe, que l'on appelle "Vecteur"

	def __init__(self, x, z): # Constructeur -> Lors de la création d'un nouvelle objet Vecteur, on assigne des valeurs à nos variables :
		self.x = x  
		self.z = z

		""" Cette fonction est apellée lorsqu'on écrit par exemple :
		|vec = Vecteur(3, 4)			<---- ici
		"""



	def __repr__(self): # Cette fonction sert à retourner la position du vecteur sous forme de str
		return str("["+ str(self.x)+"] [" + str(self.z) + "]")

		""" Cette fonction est apellée lorsqu'on écrit par exemple :
		|vec = Vecteur(3, 4)
		|print(vec) 					<---- ici
		"""



	def get(self): # Cette fonction sert à retourner la position du vecteur sous forme de str
		return str("["+ str(self.x)+"] [" + str(self.z) + "]")

		""" Cette fonction est apellée lorsqu'on écrit par exemple :
		|vec = Vecteur(3, 4)
		|print(vec.get()) 					<---- ici
		"""