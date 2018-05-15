"""
Cet classe représente les informations sur notre eprsonnages, elle contient :
- Ses Points de vies
- C'est carractéristique en physique, mental et social
- La scène où il se trouve
- La position où il se trouve dans la scène
- Si il continue l'histoire avec mike ou non
"""

class Perso(): # On définit notre classe, que l'on appelle "Perso" :

	def __init__(self, pv, physique, mental, social, scene, pos, mike): # Constructeur -> Lors de la création, on assigne des valeurs à nos variables :
		self.pv = pv # Les points de vies du joueur
		self.physique = physique # Ses points en physique
		self.mental = mental # Ses points en mental
		self.social = social # Ses points en social
		self.scene = scene # La scène à laquel il se trouve dans l'histoire
		self.pos = pos # Sa position dans la scène ( éxemple : [4][3] )
		self.mike = mike # Si le personnage continue l'histoire avec mike ou non