"""
Cet classe représente un Chainon du dialogue, elle contient :
- Une phrase contenant des informations sur la scène qui est entain de se dérouler et auquel le joueur va devoir faire des choix.
- De une à trois Réponses.
- La phrase que dirait Mike si le joueur l'a rencontré et qu'il à choisi de continuer l'aventure avec lui
- La position de ce chainon.
- L'indice du Chainon. [ EXPLIQUER ]
"""

from c_reponse import Reponse # On importe notre classe "Reponse"

class Chainage: # On définit notre classe, que l'on appelle "Chainage" :

	d_texte = "[Texte]" # Variable static qui contient le texte par défaut
	d_Reponses = [] # tableau static qui contient les réponses par défaut

	def __init__(self, texte, ReponsesArray, indice, posChainage = False, mikeTexte = False): # Constructeur -> Lors de la création d'un nouvelle objet "Chainage", on assigne des valeurs à nos variables :
		self.texte = texte # Phrase que le narateur communique au joueur
		self.Reponses = ReponsesArray # Contient les différentes réponses possible du joueur, sous forme de Tableau = [Reponse(), Reponse(), Reponse()] 
		self.mikeTexte = mikeTexte # Elle contient la phrase que Mike en fonction de la situation décrite par le narrateur (Si le joueur se trouve avec Mike à ce moment là), sous forme de str
		self.pos = posChainage # La position du chainage dans le tableau du dialogue, sous forme d'objet "Vecteur"
		self.indice = indice # L'indice du chainon permetant de le retouver, sous forme d'int

