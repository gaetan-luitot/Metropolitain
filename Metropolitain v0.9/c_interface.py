""" 
Cet classe, Interface, va être la classe qui va gérer la création d'une interface graphique pour configurer notre Boite,
c'est grâce à elle que un utilisateur va pouvoir créer une scène, donc sont travail est de communiqué entre l'utilisateur et la scène en création.
"""

from tkinter import *
from c_boite import *
from c_chainage import *
from c_reponse import *
from tkinter.messagebox import *
from sys import platform, stdout

class Interface:

	def __init__(self): # Constructeur :

		# Prérequis avant de créer notre fenêtre :  
		if (platform == "linux" or platform == "linux2"): # tkinter est géré différement sur linux et sur windows
			self.lenghtOS = 600 # Les carractère prennent moins de place sur linux
			self.tailleEditeur = 850 # Et la fenêtre est plus petite
		else: # Si l'utilisateur n'est pas sur linux alors on met nos variables comme ceci :
			self.lenghtOS = 520
			self.tailleEditeur = 640

		# Les lignes de codes suivantes sont requise pour afficher des couleurs sur l'IDLE de python
		try: self.color = stdout.shell
		except AttributeError: raise RuntimeError("Use IDLE")

		# On créer notre Fenêtre Tkinter :
		self.editor = Tk() # On créer une fenêtre "editor"
		self.editor['bg']='black' # On met le fond de couleur noir 
		self.editor.title("Editeur de Scène") # On nomme la fenêtre "Editeur de Scène"
		self.editor.geometry(str(self.tailleEditeur) + "x460") # On définit une taille pour la fenêtre avec différentes valeurs selon le système d'exploitation
		self.editor.resizable(0,0) # On fixe la taille pour qu'on ne puisse pas la modifier

		# Variables que l'on va avoir besoins :		
		self.debugArray = [] # C'est un tableau qui va contenir les positions où l'utilisateur est passé dans la création de la scène
		self.box = Boite("default") # Scène actuel sur laquel l'uitlisateur travail, objet de type "Boite"
		# Les variables StringVar() sont des objets utilisés par Tkinter pour utiliser des variables de type str,
		# qui s'actualise à chaque fois qu'on change la phrase.
		self.nbBox = StringVar() # Représente le nombre de chainons créée dans la scène
		self.nbBoxRep = StringVar() # Représente le nombre de chainons avec des réponses créée dans la scène
		self.xRep1 = StringVar() # Représente la position x du chainon vers laquel la réponse 1 pointe
		self.yRep1 = StringVar() # Représente la position y du chainon vers laquel la réponse 1 pointe
		self.xRep2 = StringVar() # Représente la position x du chainon vers laquel la réponse 2 pointe
		self.yRep2 = StringVar() # Représente la position y du chainon vers laquel la réponse 2 pointe
		self.xRep3 = StringVar() # Représente la position x du chainon vers laquel la réponse 3 pointe
		self.yRep3 = StringVar() # Représente la position y du chainon vers laquel la réponse 3 pointe
		self.FunctionRep1 = StringVar() # Représente une variable str si la réponse 1 affecte quelque chose
		self.FunctionRep2 = StringVar() # Représente une variable str si la réponse 2 affecte quelque chose
		self.FunctionRep3 = StringVar() # Représente une variable str si la réponse 3 affecte quelque chose
		self.texteRep1 = StringVar() # Texte affiché au joueur de la réponse 1 actuel
		self.texteRep2 = StringVar() # Texte affiché au joueur de la réponse 2 actuel
		self.texteRep3 = StringVar() # Texte affiché au joueur de la réponse 3 actuel
		self.XGoTo = StringVar() # répresente la position x de la boite vers laquel le joueur veut aller
		self.YGoTo = StringVar() # répresente la position y de la boite vers laquel le joueur veut aller
		self.texteDialogue = StringVar() # Représente le texte qui décrit se qu'il se passe en réponse à la réponse du joueur
		self.x = 0 # variable int représentant a position x à laquel le joueur se trouve dans la boite
		self.y = 0 # variable int représentant a position y à laquel le joueur se trouve dans la boite
		self.pos = StringVar() # Texte qui représente la position actuel de l'utilisateur dans la boite
		self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) # on définie la position actuelle en x = 0 | y = 0 de base
		self.nomFichierBoite = StringVar() # Texte du nom de la scène
		self.nomFichierBoite.set("Nom du fichier") # Définition par défaut du nom de la scène
		self.chainageActuel = Chainage(self.texteDialogue.get(), Chainage.d_Reponses, 0) #[[self.texteRep1.get(), 0, 0, False], [self.texteRep2.get(), 0, 0, False],[self.texteRep3.get(), 0, 0, False]], 0)
		self.hiden1 = IntVar() # Variable Int de Tkinter égal à 1 ou 0 pour savoir si par défaut la réponse 1 est caché au joueur
		self.hiden2 = IntVar() # Variable Int de Tkinter égal à 1 ou 0 pour savoir si par défaut la réponse 2 est caché au joueur
		self.hiden3 = IntVar() # Variable Int de Tkinter égal à 1 ou 0 pour savoir si par défaut la réponse 3 est caché au joueur
		
		self.Define() # On lance notre fonction Define() qui créer notre fenêtre de base
		self.LoadMenu() # On charge le menu au début
		self.Start() # On commence la boucle 



	def Start(self): # start mainloop
		self.editor.mainloop() # On commence la boucle principale Tkinter



	def Define(self): # Création de tout les widgets de base
		# Paned Windows :
		# Ce sont deux barres une verticale et une horizontale que je vais utiliser pour positioner des widgets avec des pixels
		self.X = PanedWindow(self.editor, orient = HORIZONTAL)
		self.Y = PanedWindow(self.editor, orient = HORIZONTAL)
		# Canvas : # On met un fond noir 
		self.Fond = Canvas(self.editor, bg = 'black', width= 640, height = 460)
		# LabelFrame :
		self.X.add(Label(self.editor, text = '', bg = 'black', anchor = NW, width = 91))
		self.Y.add(Label(self.editor, text = '', bg = 'black', anchor = NW, width = 2, height = 31))
		# On affiche tout avec la fonction grid :
		self.X.grid(columnspan = 640, rowspan = 460, row = 0, column = 0, sticky = NW)
		self.Y.grid(rowspan = 460, columnspan = 640, row = 0, column = 0, sticky = NW)
		self.Fond.grid(rowspan = 460, columnspan = 640, row = 0, column = 0, sticky = NW)



	def LoadMenu(self): # Fonction qui charge le menu
		print("I: Chargement du menu") # On indique qu'on charge le menu à l'utilisateur
		# Entry
		self.Fichier = Entry(self.editor, textvariable = self.nomFichierBoite, width = 18) # Entry qui va contenir le nom du Fichier à charger ou à créer

		# Button :
		self.New = Button(self.editor, text = "Créer", command = lambda: self.NewScene(self.nomFichierBoite.get())) # Bouton qui va créer une nouvelle boite
		self.Load = Button(self.editor, text = "Charger", command = lambda: self.LoadScene(self.nomFichierBoite.get())) # Bouton qui va charger une boite déjà existante

		self.PackMenu() # On lance la fonction qui charge les éléments du Menu



	def PackMenu(self): # On affiche les éléments du menu qu'on à précement chargé
		# Label :
		self.Fichier.grid(columnspan = 640, rowspan = 460, row = 100, column = 150, sticky = NW)
		# Button :
		self.New.grid(columnspan = 640, rowspan = 460, row = 150, column = 150, sticky = NW)
		self.Load.grid(columnspan = 640, rowspan = 460, row = 150, column = 225, sticky = NW)



	def ClearMenu(self): # Fonction qui suprimme tout les widgets du menu
		print("I: Déchargement du menu") # On indique à l'utilisateur qu'on décharge le menu
		self.New.grid_forget()
		self.Load.grid_forget()
		self.Fichier.grid_forget()



	def LoadEditeur(self): # Fonction qui charge les widgets pour l'éditeur de scène
		print("I: Chargement de l'interface d'édition")
		# LabelFrame :
		self.TopHelp = Label(self.editor, textvariable = self.nbBox, bg = 'white', width = 20) # Label qui indique le nombre de chainages crées
		self.TopHelpTwo = Label(self.editor, textvariable = self.nbBoxRep, bg = 'white', width = 20) # Label qui indique le nombre de chainages avec des réponses créer
		self.TexteLabel = Label(self.editor, textvariable = self.texteDialogue, bg = 'white', width = 75, height = 10, wraplength = self.lenghtOS, anchor = NW) # Label qui affichage du texte que l'utilisateur écrit
		self.InfoPosVar = Label(self.editor, textvariable = self.pos, bg = 'white', width = 5, height = 2) # Label qui idique la position actuel de l'utilisateur dans la scène

		# Entry :
		self.Texte = Entry(self.editor, textvariable = self.texteDialogue, width = 88) # Entry où l'utilisateur va pouvoir écrire ce qu'il se passe dans ce chainon
		self.Rep1 = Entry(self.editor, textvariable = self.texteRep1, width = 104) # Entry où l'utilisateur va pouvoir écrire la réponse 1 que le joueur va pouvoir choisir
		self.Rep2 = Entry(self.editor, textvariable = self.texteRep2, width = 104) # Entry où l'utilisateur va pouvoir écrire la réponse 2 que le joueur va pouvoir choisir
		self.Rep3 = Entry(self.editor, textvariable = self.texteRep3, width = 104) # Entry où l'utilisateur va pouvoir écrire la réponse 3 que le joueur va pouvoir choisir
		self.EntryxRep1 = Entry(self.editor, textvariable = self.xRep1, width = 2) # Entry où l'utilisateur va pouvoir écrire la position x du chainon vers laquel la réponse 1 pointe
		self.EntryyRep1 = Entry(self.editor, textvariable = self.yRep1, width = 2) # Entry où l'utilisateur va pouvoir écrire la position y du chainon vers laquel la réponse 1 pointe
		self.EntryxRep2 = Entry(self.editor, textvariable = self.xRep2, width = 2) # Entry où l'utilisateur va pouvoir écrire la position x du chainon vers laquel la réponse 2 pointe
		self.EntryyRep2 = Entry(self.editor, textvariable = self.yRep2, width = 2) # Entry où l'utilisateur va pouvoir écrire la position y du chainon vers laquel la réponse 2 pointe
		self.EntryxRep3 = Entry(self.editor, textvariable = self.xRep3, width = 2) # Entry où l'utilisateur va pouvoir écrire la position x du chainon vers laquel la réponse 3 pointe
		self.EntryyRep3 = Entry(self.editor, textvariable = self.yRep3, width = 2) # Entry où l'utilisateur va pouvoir écrire la position y du chainon vers laquel la réponse 3 pointe
		self.E_FunctionRep1 = Entry(self.editor, textvariable = self.FunctionRep1, width = 14) # Entry où l'utilisateur va pouvoir écrire si la réponse 1 va influencer sur quelque chose
		self.E_FunctionRep2 = Entry(self.editor, textvariable = self.FunctionRep2, width = 14) # Entry où l'utilisateur va pouvoir écrire si la réponse 2 va influencer sur quelque chose
		self.E_FunctionRep3 = Entry(self.editor, textvariable = self.FunctionRep3, width = 14) # Entry où l'utilisateur va pouvoir écrire si la réponse 3 va influencer sur quelque chose
		self.E_XGoto = Entry(self.editor, textvariable = self.XGoTo, width = 2) # Entry ou l'utilisateur va pouvoir écrire la position x vers laquel il souhaite aller
		self.E_YGoto = Entry(self.editor, textvariable = self.YGoTo, width = 2) # Entry ou l'utilisateur va pouvoir écrire la position y vers laquel il souhaite aller

		# Button :
		self.B_Save = Button(self.editor, text = "Save", command = self.Save) # Bouton pour sauvegarder la boite
		self.B_Delete = Button(self.editor, text = "Delete", command = self.Delete) # Bouton pour sauvegarder la boite
		self.B_Debug = Button(self.editor, text = "Debug", command = self.Debug) # Bouton afficher à quoi ressemble la boite
		self.B_Return = Button(self.editor, text = "Return", command = self.Return) # Bouton de navigation à travers la boite : retourner en arrière
		self.B_Mike = Button(self.editor, text = "M", command = self.Mike) # Bouton pour configurer le dialogue de mike pour ce chainon
		self.B_Jet1 = Button(self.editor, text = "Jet", command = lambda: self.Jet(0), width = 2) # Bouton pour configurer si le réponse 1 va avoir deux issues possible ou non
		self.B_Jet2 = Button(self.editor, text = "Jet", command = lambda: self.Jet(1), width = 2) # Bouton pour configurer si le réponse 2 va avoir deux issues possible ou non
		self.B_Jet3 = Button(self.editor, text = "Jet", command = lambda: self.Jet(2), width = 2) # Bouton pour configurer si le réponse 3 va avoir deux issues possible ou non
		self.ButtonRep1 = Button(self.editor, text = "Réponse 1", command = lambda: self.ApplyCurrent(0), width = 13) # Btn navigation : aller vers chainage suivant de la réponse 1
		self.ButtonRep2 = Button(self.editor, text = "Réponse 2", command = lambda: self.ApplyCurrent(1), width = 13) # Btn navigation : aller vers chainage suivant de la réponse 2
		self.ButtonRep3 = Button(self.editor, text = "Réponse 3", command = lambda: self.ApplyCurrent(2), width = 13) # Btn navigation : aller vers chainage suivant de la réponse 3
		self.B_Menu = Button(self.editor, text = "Menu", command = self.Menu) # Est le bouton qui va permettre à l'utilisateur de revenir en arrière
		self.B_Goto = Button(self.editor, text = "Go !", command = self.GoTo) # Est le bouton qui va permettre à l'utilisiteur d'aller là ou il veut dans la scène

		# CheckBox :
		# Ce sont des boutons à cocher, si ils sont cochés cela veut dire que la réponse en question va être caché au joueur par défaut :
		self.checkRep1 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden1 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')
		self.checkRep2 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden2 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')
		self.checkRep3 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden3 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')

		self.PackEditeur() # On affiche le tout sur notre fenêtre
		


	def PackEditeur(self): # On affiche sur la fenêtre tout les Widgets nécessaire à l'éditeur de scène (précedement créer)
		# On place les aides pour l'utilisateur (le nombres de boites créer, celles configurés et la position où il se trouve dans le tableau) :
		self.TopHelp.grid(columnspan = 640, rowspan = 460, row = 0, column = 210, sticky = NW)
		self.TopHelpTwo.grid(columnspan = 640, rowspan = 460, row = 21, column = 210, sticky = NW)
		self.InfoPosVar.grid(columnspan = 640, rowspan = 460, row = 100, column = 0, sticky = NW)

		# Les label Texte :
		self.Texte.grid(columnspan = 640, rowspan = 460, row = 210, column = 55, sticky = NW)
		self.TexteLabel.grid(columnspan = 640, rowspan = 460, row = 56, column = 55, sticky = NW)

		# Les Boutons 
		self.B_Save.grid(columnspan = 640, rowspan = 460, row = 0, column = 600, sticky = NW)
		self.B_Return.grid(columnspan = 640, rowspan = 460, row = 0, column = 0, sticky = NW)
		self.B_Debug.grid(columnspan = 640, rowspan = 460, row = 26, column = 589, sticky = NW)
		self.B_Delete.grid(columnspan = 640, rowspan = 460, row = 26, column = 0, sticky = NW)
		self.B_Mike.grid(columnspan = 640, rowspan = 460, row = 100, column = 600, sticky = NW)

		# widgets "Bouton" pour les Réponses :
		self.ButtonRep1.grid(columnspan = 640, rowspan = 460, row = 260, column = 0, sticky = NW)
		self.ButtonRep2.grid(columnspan = 640, rowspan = 460, row = 326, column = 0, sticky = NW)
		self.ButtonRep3.grid(columnspan = 640, rowspan = 460, row = 391, column = 0, sticky = NW)
		self.B_Jet1.grid(columnspan = 640, rowspan = 460, row = 260, column = 210, sticky = NW)
		self.B_Jet2.grid(columnspan = 640, rowspan = 460, row = 326, column = 210, sticky = NW)
		self.B_Jet3.grid(columnspan = 640, rowspan = 460, row = 391, column = 210, sticky = NW)
		self.B_Menu.grid(columnspan = 640, rowspan = 460, row = 0, column = 75, sticky = NW)
		self.B_Goto.grid(columnspan = 640, rowspan = 460, row = 0, column = 450, sticky = NW)

		# CheckBox Réponses : 
		self.checkRep1.grid(columnspan = 640, rowspan = 460, row = 260, column = 280, sticky = NW)
		self.checkRep2.grid(columnspan = 640, rowspan = 460, row = 326, column = 280, sticky = NW)
		self.checkRep3.grid(columnspan = 640, rowspan = 460, row = 391, column = 280, sticky = NW)

		# Entry Réponses :
		self.Rep1.grid(columnspan = 640, rowspan = 460, row = 287, column = 10, sticky = NW)
		self.Rep2.grid(columnspan = 640, rowspan = 460, row = 353, column = 10, sticky = NW)
		self.Rep3.grid(columnspan = 640, rowspan = 460, row = 418, column = 10, sticky = NW)
		self.EntryxRep1.grid(columnspan = 640, rowspan = 460, row = 265, column = 120, sticky = NW)
		self.EntryyRep1.grid(columnspan = 640, rowspan = 460, row = 265, column = 150, sticky = NW)
		self.EntryxRep2.grid(columnspan = 640, rowspan = 460, row = 331, column = 120, sticky = NW)
		self.EntryyRep2.grid(columnspan = 640, rowspan = 460, row = 331, column = 150, sticky = NW)
		self.EntryxRep3.grid(columnspan = 640, rowspan = 460, row = 396, column = 120, sticky = NW)
		self.EntryyRep3.grid(columnspan = 640, rowspan = 460, row = 396, column = 150, sticky = NW)
		self.E_FunctionRep1.grid(columnspan = 640, rowspan = 460, row = 263, column = 400, sticky = NW)
		self.E_FunctionRep2.grid(columnspan = 640, rowspan = 460, row = 329, column = 400, sticky = NW)
		self.E_FunctionRep3.grid(columnspan = 640, rowspan = 460, row = 394, column = 400, sticky = NW)
		self.E_XGoto.grid(columnspan = 640, rowspan = 460, row = 32, column = 442, sticky = NW)
		self.E_YGoto.grid(columnspan = 640, rowspan = 460, row = 32, column = 472, sticky = NW)



	def ClearEditeur(self): # On supprime les widgets de l'éditeur de scène
		print("I: Déchargement de l'interface d'éditions") # On indique qu'on décharge l'interface de l'éditeur de scène
		self.TopHelp.grid_forget()
		self.TopHelpTwo.grid_forget()
		self.InfoPosVar.grid_forget()
		self.B_Save.grid_forget()
		self.B_Return.grid_forget()
		self.B_Debug.grid_forget()
		self.B_Delete.grid_forget()
		self.Texte.grid_forget()
		self.TexteLabel.grid_forget()
		self.ButtonRep1.grid_forget()
		self.ButtonRep2.grid_forget()
		self.ButtonRep3.grid_forget()
		self.B_Mike.grid_forget()
		self.B_Jet1.grid_forget()
		self.B_Jet2.grid_forget()
		self.B_Jet3.grid_forget()
		self.checkRep1.grid_forget()
		self.checkRep2.grid_forget()
		self.checkRep3.grid_forget()
		self.Rep1.grid_forget()
		self.Rep2.grid_forget()
		self.Rep3.grid_forget()
		self.EntryxRep1.grid_forget()
		self.EntryyRep1.grid_forget()
		self.EntryxRep2.grid_forget()
		self.EntryyRep2.grid_forget()
		self.EntryxRep3.grid_forget()
		self.EntryyRep3.grid_forget()
		self.E_FunctionRep1.grid_forget()
		self.E_FunctionRep2.grid_forget()
		self.E_FunctionRep3.grid_forget()
		self.B_Menu.grid_forget()
		self.E_XGoto.grid_forget()
		self.E_YGoto.grid_forget()
		self.B_Goto.grid_forget()



	def Return(self): # Cette fonction sert à retourner au chainon ou l'utilisateur se trouvais précedement
		if (self.x != 0): # Si on l'utilisateur se trouve en x = 0, on ne fait rien, sinon :
			self.SetToBox() # On applique ce que l'utilisateur à modifié
			self.x = int(self.debugArray[-1][0].x) # On se rend à la position x de la position où l'utilisateur se trouvais précedement
			self.y = int(self.debugArray[-1][0].z) # On se rend à la position y de la position où l'utilisateur se trouvais précedement
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) # On indique à l'utilisateur la nouvelle position 
			del self.debugArray[-1] # On supprime la où l'utilisateur se trouve de l'historique de la où il est allé
			self.GetFromBox() # On Affiche à l'utilisateur le nouveau chainon



	def ApplyCurrent(self, nbButton): # On applique à notre scène le chainage que l'on vient de créer et on se rend à la position à laquel la réponse tend
		repTemporaire = [self.texteRep1.get(), self.texteRep2.get(), self.texteRep3.get()] # On créer un tableau contenant les réponses, y compris les réponses vides
		if(repTemporaire[nbButton] == ''): # On vérfie que l'utilisateur ne clique pas sur une réponse non configuré
			print("I: La réponse est vide, veuillez en créer une pour pouvoir y accéder !") # Si il à cliqué sur une réponse non configuré on lui indique
		else: # Sinon :
			self.SetToBox() # On applique les modifications faites à la boite
			temp = self.x # On stoque temporairement l'emplacement x où l'on se trouve
			self.debugArray.append([Vecteur(self.x, self.y) ,str(Vecteur(self.x, self.y))]) # On ajoute dans une liste la position x et y sous formes de vecteur
			# Cette liste va être utiliser pour afficher là où on a était avec la fonction Debug() et pour revenir en arrière avec la fonction Return()
			self.x = self.chainageActuel.Reponses[nbButton].pos.x # On définie notre x à la position où la réponse choisi amène
			# Pour le y, on assigne le z de la réponse sur laquel on à cliqué en tant que y par le biais de la fonction ZtoYrep()
			# Pour plus d'informations sur pourquoi on passe par la fonction ZtoYrep() voir dans le compte-rendu à Explication de l'éditeur de dialogue
			if (temp == self.x +1): # Si notre x actuel est égal à l'ancien x + 1, on utilise les réponses de la colonne précedente
				self.y = self.ZtoYrep(self.x - 1, self.chainageActuel.Reponses[nbButton].pos.z) # On assigne notre nouvelle y
			elif (self.x == 0):
				self.y = self.ZtoYrep(self.x, self.chainageActuel.Reponses[nbButton].pos.z) # On assigne notre nouvelle y
			else: # Si notre x précédent et notre x actuel ne se suivent pas et que notre x n'est pas égal à zéro alors on assigne normalement notre y :
				self.y = self.chainageActuel.Reponses[nbButton].pos.z # On assigne notre nouvelle y
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) # On actualise l'affichage de la position de l'utilisateur
			self.GetFromBox() # Une fois que notre x et notre y est actualisé, on cherche à obtenir (si il y'en à) les infos à notre nouvelles positions



	def SetToBox(self): # On assignent les infos rentrés dans les Entrys à notre variables chainageActuel pour pouvoir 
		listeTemporaire = []
		listeExtend = []
		listeFunction = []

		# Configuration de listeExtend :
		try:
			listeExtend.append(self.chainageActuel.Reponses[0].extend)
		except:
			listeExtend.append(False)
		try:
			listeExtend.append(self.chainageActuel.Reponses[1].extend)
		except:
			listeExtend.append(False)
		try:
			listeExtend.append(self.chainageActuel.Reponses[2].extend)
		except:
			listeExtend.append(False)

		# Configuration de listeFunction :
		try:
			if (self.FunctionRep1.get() != ''):
				listeFunction.append(self.FunctionRep1.get())
			else :
				listeFunction.append(False)
		except:
			listeFunction.append(False)
		try:
			if (self.FunctionRep2.get() != ''):
				listeFunction.append(self.FunctionRep2.get())
			else :
				listeFunction.append(False)
		except:
			listeFunction.append(False)
		try:
			if (self.FunctionRep3.get() != ''):
				listeFunction.append(self.FunctionRep3.get())
			else :
				listeFunction.append(False)
		except:
			listeFunction.append(False)


		if self.texteRep1.get() != '':
			try:
				if (self.chainageActuel.Reponses[0].pos.z != None): # On regarde si notre réponse est déjà configuré :
					if (self.xRep1.get() != '' and self.yRep1.get() != ''): # Si on veut utiliser une boite plusieurs fois
						listeTemporaire.append(Reponse(self.texteRep1.get(), int(self.xRep1.get()), int(self.yRep1.get()), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
					else:
						listeTemporaire.append(Reponse(self.texteRep1.get(), self.chainageActuel.Reponses[0].pos.x, self.chainageActuel.Reponses[0].pos.z, bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
			except:
				if (self.xRep1.get() != '' and self.yRep1.get() != ''):
					listeTemporaire.append(Reponse(self.texteRep1.get(), int(self.xRep1.get()),  int(self.yRep1.get()), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
				else:
					listeTemporaire.append(Reponse(self.texteRep1.get(), (self.x +1), self.box.GetIndice(self.x + 1), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
					self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1), Vecteur(self.x, self.y)), self.x + 1)


		if self.texteRep2.get() != '':
			try:
				if (self.chainageActuel.Reponses[1].pos.z != None): # On regarde si notre réponse est déjà configuré :
					if (self.xRep2.get() != '' and self.yRep2.get() != ''): # Si on veut utiliser une boite plusieurs fois
						listeTemporaire.append(Reponse(self.texteRep2.get(), int(self.xRep2.get()), int(self.yRep2.get()), bool(self.hiden2.get()), listeExtend[1], listeFunction[1]))
					else:
						listeTemporaire.append(Reponse(self.texteRep2.get(), self.chainageActuel.Reponses[1].pos.x, self.chainageActuel.Reponses[1].pos.z, bool(self.hiden2.get()), listeExtend[1], listeFunction[1]))
			except:
				if (self.xRep2.get() != '' and self.yRep2.get() != ''):
					listeTemporaire.append(Reponse(self.texteRep2.get(), int(self.xRep2.get()),  int(self.yRep2.get()), bool(self.hiden2.get()), listeExtend[1], listeFunction[1]))
				else:
					listeTemporaire.append(Reponse(self.texteRep2.get(), (self.x +1), self.box.GetIndice(self.x + 1), bool(self.hiden2.get()), listeExtend[1], listeFunction[1]))
					self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1), Vecteur(self.x, self.y)), self.x + 1)



		if self.texteRep3.get() != '':
			try:
				if (self.chainageActuel.Reponses[2].pos.z != None): # On regarde si notre réponse est déjà configuré :
					if (self.xRep3.get() != '' and self.yRep3.get() != ''): # Si on veut utiliser une boite plusieurs fois
						listeTemporaire.append(Reponse(self.texteRep3.get(), int(self.xRep3.get()), int(self.yRep3.get()), bool(self.hiden3.get()), listeExtend[2], listeFunction[2]))
					else:
						listeTemporaire.append(Reponse(self.texteRep3.get(), self.chainageActuel.Reponses[2].pos.x, self.chainageActuel.Reponses[2].pos.z, bool(self.hiden3.get()), listeExtend[2], listeFunction[2]))
			except:
				if (self.xRep3.get() != '' and self.yRep3.get() != ''):
					listeTemporaire.append(Reponse(self.texteRep3.get(), int(self.xRep3.get()),  int(self.yRep3.get()), bool(self.hiden3.get()), listeExtend[2], listeFunction[2]))
				else:
					listeTemporaire.append(Reponse(self.texteRep3.get(), (self.x +1), self.box.GetIndice(self.x + 1), bool(self.hiden3.get()), listeExtend[2], listeFunction[2]))
					self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1), Vecteur(self.x, self.y)), self.x + 1)


		self.chainageActuel.texte = self.texteDialogue.get()
		self.chainageActuel.Reponses = listeTemporaire
		print("I: Application des modifications sur la boite en : " + str(self.x) + " " + str(self.y))
		self.box[self.x][self.y] = self.chainageActuel



	def GetFromBox(self, indexX = None, indexY = None): # On actualise les widgets sur un nouveau Chainage 
		if (indexX == None):
			indexX = self.x
		if (indexY == None):
			indexY = self.y

		self.nbBox.set('Nombres de Boites : ' + str(self.box.Len()))
		self.nbBoxRep.set('Boites configurés : ' + str(self.LenBoxRep()))
		

		try: # On essaye d'obtenir l'index :
			self.chainageActuel = self.box[indexX][indexY]
		except: # Si il n'existe pas on le créer:
			self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(indexX), Vecteur(self.x, self.y)), indexX)
			self.chainageActuel = self.box[indexX][indexY]
		finally: # Puis dans tout les cas on actualise les widgets :
			self.texteDialogue.set(self.chainageActuel.texte)
			if len(self.chainageActuel.Reponses) > 0:
				self.texteRep1.set(self.chainageActuel.Reponses[0].texte)
				self.xRep1.set(self.chainageActuel.Reponses[0].pos.x)
				self.yRep1.set(self.chainageActuel.Reponses[0].pos.z)
				if (self.box[indexX][indexY].Reponses[0].function != False):
					self.FunctionRep1.set(str(self.box[indexX][indexY].Reponses[0].function))
				else:
					self.FunctionRep1.set('')
				if (self.box[indexX][indexY].Reponses[0].hiden == True):
					self.checkRep1.select()
				else:
					self.checkRep1.deselect()
			else:
				self.texteRep1.set('')
				self.xRep1.set('')
				self.yRep1.set('')
				self.FunctionRep1.set('')
				self.checkRep1.deselect()

			if len(self.chainageActuel.Reponses) > 1:
				self.texteRep2.set(self.chainageActuel.Reponses[1].texte)
				self.xRep2.set(self.chainageActuel.Reponses[1].pos.x)
				self.yRep2.set(self.chainageActuel.Reponses[1].pos.z)
				if (self.box[indexX][indexY].Reponses[1].function != False):
					self.FunctionRep2.set(str(self.box[indexX][indexY].Reponses[1].function))
				else:
					self.FunctionRep2.set('')
				if (self.box[indexX][indexY].Reponses[1].hiden == True):
					self.checkRep2.select()
				else:
					self.checkRep2.deselect()
			else:
				self.texteRep2.set('')
				self.xRep2.set('')
				self.yRep2.set('')
				self.FunctionRep2.set('')
				self.checkRep2.deselect()

			if len(self.chainageActuel.Reponses) > 2:
				self.texteRep3.set(self.chainageActuel.Reponses[2].texte)
				self.xRep3.set(self.chainageActuel.Reponses[2].pos.x)
				self.yRep3.set(self.chainageActuel.Reponses[2].pos.z)
				if (self.box[indexX][indexY].Reponses[2].function != False):
					self.FunctionRep3.set(str(self.box[indexX][indexY].Reponses[2].function))
				else:
					self.FunctionRep3.set('')
				if (self.box[indexX][indexY].Reponses[2].hiden == True):
					self.checkRep3.select()
				else:
					self.checkRep3.deselect()
			else:
				self.texteRep3.set('')
				self.xRep3.set('')
				self.yRep3.set('')
				self.FunctionRep3.set('')
				self.checkRep3.deselect()


		
	def LoadScene(self, nomDuFichier):
		try:
			self.box.Load(nomDuFichier)
			print("I: Chargement du fichier " + nomDuFichier + ".save")
			self.ClearMenu()
			self.LoadEditeur()
			self.GetFromBox()
		except:
			print("E: Le ficher n'existe pas !")
		


	def NewScene(self, nomDuFichier):
		teste = Boite("teste")
		try:
			teste.Load(nomDuFichier)
			showwarning('Warning', 'Attention un fichier porte déjà ce nom, si vous sauvegarder ce nouveau fichier cela supprimera le premier !')
			print("I: Création du fichier " + nomDuFichier)
		except:
			print("I: Création du fichier " + nomDuFichier)
		self.box.New(nomDuFichier)
		self.ClearMenu()
		self.LoadEditeur()
		self.GetFromBox()
		print("I: Création du point d'origine [0][0]")



	def Save(self):
		self.SetToBox()
		self.box.Save()
		self.GetFromBox()
		print("I: Sauvegarde effectuée")
		


	def ZtoYchai(self, index, indiceToFind):
		for i in range(0, len(self.box[index])):
			if(self.box[index][i].indice == indiceToFind):
				print("return -> " + str(x))
				return int(i)



	def ZtoYrep(self, index, indiceToFind):
		for i in range(0, len(self.box[index])):
			for x in range(0, len(self.box[index][i].Reponses)):
				if (self.box[index][i].Reponses[x].pos.z == indiceToFind):
					return int(self.box[index][i].Reponses[x].pos.z)
		print("E: Indice recherché non trouvé")



	def YtoZ(self, indexY, indexX = None):
		if (indexX == None):
			indexX = self.x
		return self.box[indexX][indexY].indice



	def Debug(self):
		print("\n_\n")
		for z in range(0,self.box.Lenx()):
			
			print("----------### "+ str(z)+" ###----------")
			try:
				for i in range (0, len(self.box[z])):
					if (z == self.x and i == self.y):
						self.color.write("|-| -> " + str(self.box[z][i].indice) + "\n","COMMENT")
					elif(self.Count(str(Vecteur(z, i))) == 1):
						self.color.write("|-| -> " + str(self.box[z][i].indice) + "\n","KEYWORD")
					else:
						print("|-| -> " + str(self.box[z][i].indice))

					for x in range(0, len(self.box[z][i].Reponses)):
						if (str(self.box[z][i].Reponses[x].pos) == str(Vecteur(self.x, self.y)) or self.Count(str(self.box[z][i].Reponses[x].pos)) == 1):
							if (type(self.box[z][i].Reponses[x].extend) == type(Extension(None, None, None, None))):
								self.color.write("        " + str(self.box[z][i].Reponses[x].pos) + " | " + str(self.box[z][i].Reponses[x].extend.pos2) + " " + str(self.box[z][i].Reponses[x].hiden) + "\n","KEYWORD")
							else:
								self.color.write("        " + str(self.box[z][i].Reponses[x].pos) + " " + str(self.box[z][i].Reponses[x].hiden) + "\n","KEYWORD")
						else:
							if (type(self.box[z][i].Reponses[x].extend) == type(Extension(None, None, None, None))):
								print("        " + str(self.box[z][i].Reponses[x].pos) + " | " + str(self.box[z][i].Reponses[x].extend.pos2) + " " + str(self.box[z][i].Reponses[x].hiden))
							else:
								print("        " + str(self.box[z][i].Reponses[x].pos) + " " + str(self.box[z][i].Reponses[x].hiden))
							
			except:
				raise
				print("Hum erreur !")
		print("\n_\n")



	def Delete(self):
		if self.x != 0:
			if (len(self.box[self.x][self.y].Reponses) != 0):
				self.DeleteAllWays() # On supprime les sous chemins
			repToDel = 0
			variableTemporaire = self.chainageActuel.indice
			boxToDel = [self.x, self.y]
	
			self.x = self.box[boxToDel[0]][boxToDel[1]].pos.x
			self.y = self.box[boxToDel[0]][boxToDel[1]].pos.z
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y))
			del self.debugArray[-1]
	  	
			for i in range(0, len(self.box[self.x][self.y].Reponses)):
				if(self.box[self.x][self.y].Reponses[i].pos.z == variableTemporaire):
					repToDel = i
			
			del self.box[self.x][self.y].Reponses[repToDel]
			self.box.Supprimer(boxToDel[0], boxToDel[1])
			self.GetFromBox()
		


	def DeleteAllWays(self):
		xActu = self.x
		yActu = self.y
		listeChainesupp = []
		liste2D = [[self.box[xActu][yActu].indice]]
		rangeX = 0
		last = None
		while True:
			for j in range(0, len(liste2D[rangeX])):
				try:
					yActu = last.Reponses[j].pos.z
				except:
					yActu = self.y
				for i in range(0, len(self.box[xActu][yActu].Reponses)):
					listeChainesupp.append(self.box[xActu][yActu].Reponses[i].pos)
					try:
						liste2D[rangeX +1].append(self.box[xActu][yActu].Reponses[i].pos)
					except:
						liste2D.append([self.box[xActu][yActu].Reponses[i].pos])


			try:
				if len(liste2D[rangeX +1]) == 0:
					break
			except:
				break
			else:
				last = self.box[xActu][yActu]
				rangeX += 1
				xActu += 1

		# Maintenant on supprime tout :
		for i in range(1, len(listeChainesupp)+1):
			self.box.Supprimer(int(listeChainesupp[-i].x), int(listeChainesupp[-i].z))



	def Count(self, obj):
		count = 0
		for i in range(0, len(self.debugArray)):
			count += self.debugArray[i][1].count(obj)
		return count

		

	def Jet(self, bouton):
		listeTest = [self.Rep1.get(), self.Rep2.get(), self.Rep3.get()]
		
		if (listeTest[bouton] != ''):
			self.SetToBox()

			def Valider(bouton):
				variableFunc = function2.get()

				if (function2.get() == ''):
					variableFunc = False
				if(listeState.get() != '' and diff.get() != ''):
					if (x2.get() == '' and z2.get() == ''):
						self.box[self.x][self.y].Reponses[bouton].extend = Extension(listeState.get(), diff.get(), (self.x +1), self.box.GetIndice(self.x + 1), variableFunc)
						self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1)), self.x + 1)
						menu_jet.destroy()
					elif (x2.get() != '' and z2.get() != ''):
						self.box[self.x][self.y].Reponses[bouton].extend = Extension(listeState.get(), diff.get(), x2.get(), z2.get(), variableFunc)
						menu_jet.destroy()

			def Dejetyfication(bouton):
				self.box[self.x][self.y].Reponses[bouton].extend = False
				menu_jet.destroy()

			def ActualiserListe(obj):
				listeState.set(liste.get(str(obj.widget.curselection()[0])))

			# Création d'une nouvelle fenètre
			menu_jet = Toplevel(self.editor)
			menu_jet['bg']='black' # On met le fond de couleur noir 
			menu_jet.title("Configuration Jet") # On nomme la fenêtre 
			menu_jet.geometry("300x100") # On définit une taille pour la fenêtre
			menu_jet.resizable(0,0)
			
			# ListBox :
			liste = Listbox(menu_jet, height = 3, width = 8)
			liste.bind('<<ListboxSelect>>', ActualiserListe)
			liste.insert(1, "Physique")
			liste.insert(2, "Mental")
			liste.insert(3, "Social")
			doc = {"Social" : 2, "Mental" : 1, "Physique" : 0}
			liste.grid(rowspan = 3, row = 0, column = 1, sticky = NE)

			# StringVar : 
			function2 = StringVar() 
			function2.set('')
			diff = StringVar() 
			diff.set('')
			x2 = StringVar() 
			x2.set('')
			z2 = StringVar() 
			z2.set('')
			listeState = StringVar() 
			listeState.set('')
			
			# Boutons :  
			B_Valider = Button(menu_jet, text = "Valider", fg = 'green',  command = lambda: Valider(bouton)).grid(row = 4, column = 0)
			B_X = Button(menu_jet, text = "x", fg = 'red', command = lambda: Dejetyfication(bouton)).grid(row = 4, column = 3)

			# Entry :
			E_dificult = Entry(menu_jet, textvariable = diff, bg = 'white', width = 3)
			E_dificult.grid(row = 0, column = 0)
			E_x2 = Entry(menu_jet, textvariable = x2, bg = 'white', width = 3)
			E_x2.grid(row = 0, column = 2)
			E_z2 = Entry(menu_jet, textvariable = z2, bg = 'white', width = 3)
			E_z2.grid(row = 0, column = 3)
			E_Function2 = Entry(menu_jet, textvariable = function2, bg = 'white', width = 10)
			E_Function2.grid(row = 0, column = 4, padx = 10)
			labelListe = Label(menu_jet, textvariable = listeState, bg = 'white')
			labelListe.grid(row = 4 , column = 1)

			if( type(self.box[self.x][self.y].Reponses[bouton].extend) == type(Extension(None, None, None, None))): # Si le bouton est deja extend on load :
				diff.set(str(self.box[self.x][self.y].Reponses[bouton].extend.difficult))
				x2.set(self.box[self.x][self.y].Reponses[bouton].extend.pos2.x)
				z2.set(self.box[self.x][self.y].Reponses[bouton].extend.pos2.z)
				function2.set(self.box[self.x][self.y].Reponses[bouton].extend.function)
				liste.activate(doc[str(self.box[self.x][self.y].Reponses[bouton].extend.carac)])
				listeState.set(str(liste.get(ACTIVE)))
			

			menu_jet.mainloop()



	def Mike(self):
		def Valider():
			self.box[self.x][self.y].mikeTexte = mikeTexte.get()
			menu_mike.destroy()

		def Supprimer():
			self.box[self.x][self.y].mikeTexte = False
			menu_mike.destroy()

		menu_mike = Toplevel(self.editor)
		menu_mike['bg']='black' # On met le fond de couleur noir 
		menu_mike.title("Configuration Mike") # On nomme la fenêtre 
		menu_mike.geometry("400x175") # On définit une taille pour la fenêtre
		menu_mike.resizable(0,0)
		
		mikeTexte = StringVar()

		L_MikeTexte = Label(menu_mike, textvariable = mikeTexte, width = 49, height = 8, wraplength = 350)
		L_MikeTexte.grid(columnspan = 4, row = 0, column = 0)
		E_MikeTexte = Entry(menu_mike, textvariable = mikeTexte, width = 49) # Texte du PNJ 
		E_MikeTexte.grid(columnspan = 4, row = 1, column = 0)

		# Boutons valider
		B_MkeValider = Button(menu_mike, text = "Valider", fg = 'green', command = Valider).grid(row = 4, column = 0)
		B_MkeValider = Button(menu_mike, text = "Supprimer", fg = 'red',command = Supprimer).grid(row = 4, column = 3)

		if (self.box[self.x][self.y].mikeTexte != False):
			mikeTexte.set(str(self.box[self.x][self.y].mikeTexte))

		menu_mike.mainloop()



	def Menu(self): # Cette fonction sert à retourner au menu
		self.Save() # On sauvegarde ce que le joueur à fait
		self.ClearEditeur() # On décharge l'éditeur pour pouvoir charger le menu apres
		self.debugArray = []
		self.x = 0
		self.y = 0
		print("\n\n\n\n\n\n\n\n\n\n")
		self.LoadMenu()



	def LenBoxRep(self):
		taille = 0
		for x in range(0, self.box.Lenx()):
			for y in range(0, len(self.box[x])):
				if(len(self.box[x][y].Reponses) > 0):
					taille += 1
		return taille



	def GoTo(self): # Cette fonction est utilisé lorsque que l'utilisateur va appuyer sur le bouton Go, elle sert à se rendre n'importe où dans la scène
		if (self.XGoTo.get() != '' and self.YGoTo.get() != ''): # Si l'utilisateur n'a pas rentré de coordonnées on ne fait rien sinon :
			newX = int(self.XGoTo.get()) # On stoque nos deux nouvelles coordonnées dans 2 variables temporaires :
			newY = int(self.YGoTo.get())
			try: # On essaye d'obetnir ce qui se trouve à la nouvelle position :
				temp = self.box[newX][newY]
			except: # Si cette position n'existe pas on le dit :
				print("E: L'index n'existe pas !")
			else: # Sinon, cette position existe alors on s'y rend :
				self.SetToBox() # On applique les modifications que l'utilisateur à fait sur la chainon ou il se trouve
				self.debugArray.append([Vecteur(self.x, self.y) ,str(Vecteur(self.x, self.y))]) # On ajoute là où l'utilisateur se trouve actuelement dans l'historique 
				self.x = newX # On applique les nouvelles coordonéees
				self.y = newY
				self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) # On affiche le changement de coordonnées à l'utilisateur
				self.GetFromBox() # On obtient les informations la nouvelles boites où l'on se trouve désormais
			self.XGoTo.set('') # On vide les cases où le joueur à rentré les coordonnées
			self.YGoTo.set('')