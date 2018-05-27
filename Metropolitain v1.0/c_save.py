#Ici, on va définir et conserver les différentes variables qui vont permettre à nos personnage de perdurer dans le temps.
#C'est notamment ici qu'on va noter ses caracts, son inventaire, sa situation dans le temps.

"""
Cette classe représente les informations sur notre personnage, elle contient :
-sa position
-ses points de vie.
-ses caractéristiques en physique, mental et social.
-sa position dans l'histoire
-s'il a continué l'histoire avec Mike ou pas
"""

class Save:
    def __init__(self, pos, pv, archetype, objets, mike):
        self.pos = pos
        self.pv = pv
        self.archetype = archetype
        self.objets = objets 
        self.mike = mike
