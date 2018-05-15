""" 
Cette classe représente une réponse que le joueur peut choisir lors d'une scène, elle contient :
- La réponse à affichée au joueur.
- Le chemin à suivre pour continuer la suite du dialogue.
- Si la réponse à deux issues, une réussite et un échec.
- Si la réponse est caché par défaut, mais peut être débloqué.
- Si la réponse entraine des répercutions sur le joueur.



Une autre classe est définie ici car elle est liée avec notre classe "Reponse", il s'agit de la classe "Extension". 
Cette classe va être utilisé si une réponse nécessite un test dans une compétence du personnage du joueur,
et va déterminer si le test est une réussite ou un échec. Elle contient :
- La caractéristique du personnage qui utlisé pour le test.
- la difficulté du test, si le joueur entreprend une action difficile, la difficulté sera élevé.
- Le chemin ou aller en cas d'échec.
- Si l'échec du test entraine des répercutions sur le joueur.
"""

from c_vecteur import Vecteur # On import notre classe Vecteur

class Reponse: # On définit notre classe, que l'on appelle "Reponse" :

	def __init__(self, texte, x, z, hiden, extension = False, function = False): # Constructeur -> Lors de la création d'un nouvelle objet "Reponse", on assigne des valeurs à nos variables :
		self.texte = texte # La réponse que le joueur peut choisir, sous forme de str
		self.pos = Vecteur(x, z) # La position du Chainage qui répond à la réponse du PJ, sous forme d'objet "Vecteur"
		self.extend = extension # Si cette réponse à plusieur issues, si elle à plusieurs issues elle est sous forme d'objet "Extension" sinon elle égale à False
		self.hiden = hiden # Si la réponse va être caché au joueur de base et que sous certaines conditions, il peut y avoir accés, sous forme de True ou False.
		self.function = function # Si la réponse applique des choses sur le joueur comme une perte de points de vie ou un gain d'objet, sous forme de str
		




class Extension: # On définit notre classe, que l'on appelle "Extension" :

	def __init__(self, carac, difficulté, x2, z2, function = False): # Constructeur -> Lors de la création d'un nouvelle objet "Extension", on assigne des valeurs à nos variables :
		self.carac = carac # Réprésente la caractéristique mise en jeu lors du test |---|> 0 : Physique | 1 : Mental | 2 : Sociale 
		self.difficult = difficulté # La difficulté du jet de dés que le PJ devra battre
		self.pos2 = Vecteur(x2, z2) # La position du Chainage qui répond à la réponse du PJ en cas d'échec, en cas de réussite c'est la posisiton de la réponse qui sera utilisé et non celle de l'extension
		self.function = function # Si la l'échec applique des choses sur le joueur comme une perte de points de vie ou un gain d'objet, sous forme de str

		