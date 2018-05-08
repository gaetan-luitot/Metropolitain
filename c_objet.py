class Objet:

	def __init__(self, nom, description):
		self.nom = nom
		self.description = description

listeObjet = []

def Save(self):
		with open('objets.save', 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			mon_pickler.dump(listeObjet)

def Load(self, nom):
	with open('objets.save', 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		listeObjet = mon_depickler.load()

def see():
	global listeObjet
	for i in range(1, len(listeObjet)):
		print("objet : " + listeObjet[i].nom + " -> " + listeObjet[i].description)

def Ajouter(nom, desc):
	global listeObjet
	listeObjet.append(Objet(nom, desc))


Ajouter("Briquet", "description")
Ajouter("Couteau", "description")

Save()

# Briquet 
# Couteau