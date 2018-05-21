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



	def SetToBox(self): # On assignent les infos rentrés dans les Entrys par l'utilisateur à notre boite
		# On créer trois listes qui vont contenir :
		listeTemporaire = [] # Les 0, 1, 2 ou 3 objets Reponse à appliquer à la boite (voir c_reponse.py)
		listeExtend = [] # Les 0, 1, 2 ou 3 objets Extension, si il y a des réponses qui ont des jets (voir c_reponse.py)
		listeFunction = [] # Les 0, 1, 2 ou 3 variables str si les réponses appliques des fonctions

		# Configuration de listeExtend, de la liste si les réponses possèdent des jets :
		try: # On essaye d'ajouter à notre liste l'objet Extension de la réponse 1
			listeExtend.append(self.chainageActuel.Reponses[0].extend) # Si il existe alors cela fonctionne
		except: # Sinon, si il n'existe pas : 
			listeExtend.append(False) # on ajoute False à notre liste, pour indiquer que cette fonction n'a pas de jet
		try: # La même chose mais pour la réponse 2 :
			listeExtend.append(self.chainageActuel.Reponses[1].extend)
		except:
			listeExtend.append(False)
		try: # La même chose mais pour la réponse 3 :
			listeExtend.append(self.chainageActuel.Reponses[2].extend)
		except:
			listeExtend.append(False)
		# Donc si une réponse nécessite un jet, sont attribut extend sera configuré en tant qu'objet Extend, sinon il sera égal à False

		# Configuration de listeFunction :
		try: # On essaye d'ajouter à notre liste le str de la fonction de la réponse 1
			if (self.FunctionRep1.get() != ''): # Et qu'il n'est pas nul :
				listeFunction.append(self.FunctionRep1.get()) # Si il existe et qu'il n'est pas nul alors cela fonctionne
			else : # Si il est nul alors on ajoute False
				listeFunction.append(False)
		except: # Ou si il n'existe pas, on ajoute False
			listeFunction.append(False)
		try: # La même chose pour la réponse 2 :
			if (self.FunctionRep2.get() != ''):
				listeFunction.append(self.FunctionRep2.get())
			else :
				listeFunction.append(False)
		except:
			listeFunction.append(False)
		try: # Et on fait la même chose pour la réponse 3 :
			if (self.FunctionRep3.get() != ''):
				listeFunction.append(self.FunctionRep3.get())
			else :
				listeFunction.append(False)
		except:
			listeFunction.append(False)

		# Maitenant on va configurer notre listeTemporaire, qui va contenir les réponses configurés à appliquer à la boite
		if self.texteRep1.get() != '': # Si le texte de la réponse 1 n'est pas nul, alors :
			try: # On essaye de voir si la réponse 1 existe déjà ou si c'est la première fois qu'on applique les modifications 
				if (self.chainageActuel.Reponses[0].pos.z != None): # Si c'est la première fois alors "Reponses[0].pos.z" n'existe pas et cela provoque une erreur
					# Donc si des informations existes déjà pour la réponse 1 et que l'utilisateur à changer les positions, on ajoute toutes les infos sur la réponse 1 à notre liste :
					if (self.xRep1.get() != '' and self.yRep1.get() != ''): 
						listeTemporaire.append(Reponse(self.texteRep1.get(), int(self.xRep1.get()), int(self.yRep1.get()), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
					else: # Sinon si les positions sont vides (que l'utilisateur les a éffacés), on applique celles qui étaientt configurés avant :
						listeTemporaire.append(Reponse(self.texteRep1.get(), self.chainageActuel.Reponses[0].pos.x, self.chainageActuel.Reponses[0].pos.z, bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
			except: # Si par contre, c'est la première fois qu'on applique la réponse 1 à la boite :
				if (self.xRep1.get() != '' and self.yRep1.get() != ''): # Et que l'utilisateur à rentré des coordonnées déjà existante, on ajoute les infos de la réponse 1 qui mène à un chainage déjà existant :
					listeTemporaire.append(Reponse(self.texteRep1.get(), int(self.xRep1.get()),  int(self.yRep1.get()), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
				else: # Si par contre il ne rentre pas de coordonnées, alors on ajoute notre réponse 1 et on créer un nouveau chainage pour lui :
					listeTemporaire.append(Reponse(self.texteRep1.get(), (self.x +1), self.box.GetIndice(self.x + 1), bool(self.hiden1.get()), listeExtend[0], listeFunction[0]))
					self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1), Vecteur(self.x, self.y)), self.x + 1)


		if self.texteRep2.get() != '': # On fait la même chose pour la réponse 2 :
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



		if self.texteRep3.get() != '': # Et la même chose pour la réponse 3
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


		self.chainageActuel.texte = self.texteDialogue.get() # On applique les modifications que l'utilisateur à fait sur le texte principale
		self.chainageActuel.Reponses = listeTemporaire # Et on applique les réponses contenue dans notre liste "listeTemporaire" au chainage que l'on vient de modifier
		print("I: Application des modifications sur la boite en : " + str(self.x) + " " + str(self.y)) # On indique à l'utilisateur qu'on à appliquer ses modifications à la scène
		self.box[self.x][self.y] = self.chainageActuel # Puis on applique le chainage modifié à notre scène



	def GetFromBox(self, indexX = None, indexY = None): # On prend les informations stoqué dans la boite pour les montrer à l'utilisateur
		if (indexX == None): # Si l'utilisateur ne rentre pas de coordonnées alors on prend celle où il se trouve
			indexX = self.x
		if (indexY == None):
			indexY = self.y

		self.nbBox.set('Nombres de Boites : ' + str(self.box.Len())) # On actualise les aides pour l'utilisateur
		self.nbBoxRep.set('Boites configurés : ' + str(self.LenBoxRep()))
		

		try: # On essaye d'obtenir le chainage à afficher :
			self.chainageActuel = self.box[indexX][indexY]
		except: # Si il n'existe pas on le créer, il sera vierge:
			self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(indexX), Vecteur(self.x, self.y)), indexX)
			self.chainageActuel = self.box[indexX][indexY]
		finally: # Puis dans tout les cas on actualise les widgets, donc il sera soit vierge soit déjà configuré :
			self.texteDialogue.set(self.chainageActuel.texte) # On charge le texte de la description principale
			
			if len(self.chainageActuel.Reponses) > 0: # On charge toute les infos pour la réponse une (si il y'en a une)
				self.texteRep1.set(self.chainageActuel.Reponses[0].texte) # Le texte de la réponse 1
				self.xRep1.set(self.chainageActuel.Reponses[0].pos.x) # La position du chainage où mène la réponse 1
				self.yRep1.set(self.chainageActuel.Reponses[0].pos.z)
				if (self.box[indexX][indexY].Reponses[0].function != False): # Si la réponse possède une fonction :
					self.FunctionRep1.set(str(self.box[indexX][indexY].Reponses[0].function)) # On la charge
				else: # Sinon, si la réponse 1 ne possède pas de fonction :
					self.FunctionRep1.set('') # On met notre widget vierge
				if (self.box[indexX][indexY].Reponses[0].hiden == True): # Si la réponse 1 est caché alors :  
					self.checkRep1.select() # On coche la case
				else: # Sinon :
					self.checkRep1.deselect() # On la décoche
			else: # Si il y a pas de réponse 1 alors on met tout nos widgets, de la réponse 1, vierge :
				self.texteRep1.set('')
				self.xRep1.set('')
				self.yRep1.set('')
				self.FunctionRep1.set('')
				self.checkRep1.deselect()

			if len(self.chainageActuel.Reponses) > 1: # On charge toute les infos pour la réponse deux (si il y'en a une)
				self.texteRep2.set(self.chainageActuel.Reponses[1].texte) # Le texte de la réponse 2
				self.xRep2.set(self.chainageActuel.Reponses[1].pos.x) # La position du chainage où mène la réponse 2
				self.yRep2.set(self.chainageActuel.Reponses[1].pos.z)
				if (self.box[indexX][indexY].Reponses[1].function != False): # Si la réponse 2 possède une fonction :
					self.FunctionRep2.set(str(self.box[indexX][indexY].Reponses[1].function)) # On la charge
				else: # Sinon, si la réponse 2 ne possède pas de fonction :
					self.FunctionRep2.set('') # On met notre widget vierge
				if (self.box[indexX][indexY].Reponses[1].hiden == True): # Si la réponse 2 est caché alors :  
					self.checkRep2.select() #  On coche la case
				else: # Sinon :
					self.checkRep2.deselect() # On la décoche
			else:  # Si il y a pas de réponse 2 alors on met tout nos widgets, de la réponse 2, vierge :
				self.texteRep2.set('')
				self.xRep2.set('')
				self.yRep2.set('')
				self.FunctionRep2.set('')
				self.checkRep2.deselect()

			if len(self.chainageActuel.Reponses) > 2: # On charge toute les infos pour la réponse trois (si il y'en a une)
				self.texteRep3.set(self.chainageActuel.Reponses[2].texte) # Le texte de la réponse 3
				self.xRep3.set(self.chainageActuel.Reponses[2].pos.x) # La position du chainage où mène la réponse 3
				self.yRep3.set(self.chainageActuel.Reponses[2].pos.z)
				if (self.box[indexX][indexY].Reponses[2].function != False): # Si la réponse 3 possède une fonction :
					self.FunctionRep3.set(str(self.box[indexX][indexY].Reponses[2].function))  # On la charge
				else: # Sinon, si la réponse 3 ne possède pas de fonction :
					self.FunctionRep3.set('')  # On met notre widget vierge
				if (self.box[indexX][indexY].Reponses[2].hiden == True): # Si la réponse 3 est caché alors 
					self.checkRep3.select() # On coche la case
				else: # Sinon :
					self.checkRep3.deselect() # On la décoche
			else: # Si il y a pas de réponse 3 alors on met tout nos widgets de la réponse 3 vierge :
				self.texteRep3.set('')
				self.xRep3.set('')
				self.yRep3.set('')
				self.FunctionRep3.set('')
				self.checkRep3.deselect()


		
	def LoadScene(self, nomDuFichier): # Cette fonction est appellé lors du menu, lorsque l'utilisateur appuie sur le bouton "Load"
		try: # On essaye de charger le fichier
			self.box.Load(nomDuFichier) # On charge le fichier
			print("I: Chargement du fichier " + nomDuFichier + ".save")
			self.ClearMenu() # Si le chargement du fichier à marché alors on désaffiche le menu
			self.LoadEditeur() # Puis on charge l'interface de l'éditeur de scène
			self.GetFromBox() # Et on actualise nos widgets pour pouvoir lire/modifier ce qu'il y avait dans le fichier
		except: # Si on y arrive pas, alors on indique à l'utilisateur que le fichier n'existe pas
			print("E: Le ficher n'existe pas !")
		


	def NewScene(self, nomDuFichier): # Cette fonction est appellé lors du menu, lorsque l'utilisateur appuie sur le bouton "Créer"
		# Elle sert à créer une nouvelle scène, où à en écraser une si il existe une du même nom
		teste = Boite("teste") # On créer une boite vide 
		try: # Puis on essaye de voir si un fichier portant le même nom existe
			# Car si il existe alors on indique à l'utilisateur, que si il sauvegarde cela supprimera le fichier qui existe.
			teste.Load(nomDuFichier)
			showwarning('Warning', 'Attention un fichier porte déjà ce nom, si vous sauvegarder ce nouveau fichier cela supprimera le premier !')
			print("I: Création du fichier " + nomDuFichier)
		except: # Sinon si aucun fichier portant le même nom existe alors on créer le fichier normalement :
			print("I: Création du fichier " + nomDuFichier)
		# Quoi qu'il arrive, on créer un nouveau fichier, si il ne veut pas supprimer son premier fichier, il a juste à quitter la fenêtre
		self.box.New(nomDuFichier) # On créer une nouvelle boite
		self.ClearMenu() # On désaffiche le menu
		self.LoadEditeur() # Pour pouvoir afficher l'éditeur de scène
		print("I: Création du point d'origine [0][0]")



	def Save(self): # Cette fonction est appellée lorsque l'utilisateur appuie sur le bouton "Save", elle sert à sauvegarder sa progression
		self.SetToBox() # D'abord on applique les modifications que l'utilisateur à fait à notre boite
		self.box.Save() # Puis on sauvegarde
		print("I: Sauvegarde effectuée")
		


	def ZtoYchai(self, index, indiceToFind): # Cette fonction sert à renvoyer le "y" d'un chainage d'une colonne en fonction de son indice
		for i in range(0, len(self.box[index])): # Donc pour chaque chainage de la colonne :
			if(self.box[index][i].indice == indiceToFind): # On test si l'indice du chainage et celui qu'on cherche correspondent 
				return int(i) # Si ils correspondent alors on renvoie sa position y dans la colonne



	def ZtoYrep(self, index, indiceToFind): # Cette fonction sert à renvoyer le "y" d'une réponse d'une colonne en fonction de son indice
		for i in range(0, len(self.box[index])): # Donc pour chaque chainage de notre de la colonne n° "index" :
			for x in range(0, len(self.box[index][i].Reponses)): # Et pour chaque réponse de chaque chainage :
				if (self.box[index][i].Reponses[x].pos.z == indiceToFind): # On teste si l'indice de la réponse et l'indice qu'on cherche correspondent
					return int(self.box[index][i].Reponses[x].pos.z) # Si ils correspondent alors on renvoie sa position "y" dans le tableau
		print("E: Indice recherché non trouvé") # Si on à pas trouvé on le dit à l'utilisateur



	def YtoZ(self, indexY, indexX = None): # Cette fonction sert à donner l'indice d'un chainage en fonction de sa position "y"
		if (indexX == None): # Si l'utilisateur ne donne pas de "x", alors on prend le "x" de là où il se trouve actuelemet
			indexX = self.x
		return self.box[indexX][indexY].indice # Puis on retourne l'indice du chainage



	# Cette fonction est appellée lorsque l'utilisateur appuie sur le bouton "Debug", 
	# elle sert à afficher la boite dans son ensemble pour donner une visibilité à l'utilisateur,
	# Deplus, elle va afficher en orange, là où l'utilisateur est allé, et en rouge la ou l'utilisateur se trouve, et en bleu le reste :
	def Debug(self): 
		print("\n-_-_-_-_-_ D-E-B-U-G _-_-_-_-_-\n") # On saute deux lignes pour faire de la place dans la console
		# On va donc parcourir chaque réponses, de chaque chainage, de chaque colonne du tableau et les afficher :
		for z in range(0,self.box.Lenx()): # Donc pour chaque colonne du tableau :
			print("----------### "+ str(z)+" ###----------") # On affiche le numéro de la colonne

			try: # On met nos boucle suivantes dans un "try", au cas ou il y'est une erreur :
				for i in range (0, len(self.box[z])): # Pour chaque élement dans une colonne
					# Si notre 'i' et notre 'j' correspondent avec 'x' et 'y' alors cela veut dire que c'est là où le joueur se trouve actuelement
					if (z == self.x and i == self.y): # Donc affiche ce chainage en rouge :
						self.color.write("|-| -> " + str(self.box[z][i].indice) + "\n","COMMENT")
					elif(self.Count(str(Vecteur(z, i))) == 1): # Si par contre c'est un chainage où l'utilisateur est allé précedement :
						self.color.write("|-| -> " + str(self.box[z][i].indice) + "\n","KEYWORD") # On affiche le chainage en orange
					else: # Sinon c'est un chainage normal :
						print("|-| -> " + str(self.box[z][i].indice)) # on l'affiche de la couleur de base de la console

					# Maintenant qu'on affiché la colonne et le chainage, on va afficher les réponses qui se trouve dans le chainages
					for x in range(0, len(self.box[z][i].Reponses)): # Donc pour chaque réponses qui se trouve dans le chainage :
						# Si le joueur est passé par là alors on va afficher cette réponsé en orange :
						if (str(self.box[z][i].Reponses[x].pos) == str(Vecteur(self.x, self.y)) or self.Count(str(self.box[z][i].Reponses[x].pos)) == 1):
							if (type(self.box[z][i].Reponses[x].extend) == type(Extension(None, None, None, None))): # Et si cette réponse où est allé à deux issues :
								# On affiche les deux positions où cette réponse amène et si elle est caché de base au joueur ou non :
								self.color.write("        " + str(self.box[z][i].Reponses[x].pos) + " | " + str(self.box[z][i].Reponses[x].extend.pos2) + " " + str(self.box[z][i].Reponses[x].hiden) + "\n","KEYWORD")
							else: # Par contre si cette réponse ne nécessite pas de jet et donc à une seule issue :
								self.color.write("        " + str(self.box[z][i].Reponses[x].pos) + " " + str(self.box[z][i].Reponses[x].hiden) + "\n","KEYWORD")
						else: # Sinon, si le joueur n'est pas passé par cette réponse, donc qu'elle ne se trouve pas dans l'historique :
							# Et si elle à deux issues, on affiche les deux issues de couleur normale :
							if (type(self.box[z][i].Reponses[x].extend) == type(Extension(None, None, None, None))):
								print("        " + str(self.box[z][i].Reponses[x].pos) + " | " + str(self.box[z][i].Reponses[x].extend.pos2) + " " + str(self.box[z][i].Reponses[x].hiden))
							else: # Sinon la réponse à qu'une seule issue alors :
								print("        " + str(self.box[z][i].Reponses[x].pos) + " " + str(self.box[z][i].Reponses[x].hiden))
							
			except: # En temps normal il n'est pas sensé avoir d'erreur, mais on ne sait jamais, 
				# donc si quelque chose se passe mal au dessus, au lieu que l'erreur s'affiche il y'aura écrit "E: Hum Erreur !"
				print("E: Hum erreur !")  
		# Mais quoi qu'il arrive on fait de la place et on indique que c'est la fin de l'affichage de la boite
		print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n") 



	def Delete(self): # Cette fonction est apellé lorsque l'utilisateur clique sur le bouton "Delete"
		# Elle sert à supprimer le chainage où le joueur se trouve

		if self.x != 0: # Si le joueur se trouve en x = 0, la fonction ne fais rien car il faut au moins une position 0, 0.
			repToDel = 0 # Cette variable va contenir le chiffre, représentant la réponse de la colonne précédente qui mène à ce chainage que l'on veut supprimer
			variableTemporaire = self.chainageActuel.indice # On stoque temporairement l'indice du chainage qu l'on veut supprimer
			boxToDel = [self.x, self.y] # Et on stoque dans une liste nos positions x et y
			print("I: Suppression du chainage en x : " + str(self.x) + " et y : " + str(self.y))

			self.x = self.box[boxToDel[0]][boxToDel[1]].pos.x # On assigne notre x et notre y aux x et y de la colonne précédente
			self.y = self.box[boxToDel[0]][boxToDel[1]].pos.z
			
			del self.debugArray[-1] # On supprime là ou il était dans l'historique des déplacements
	
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) # On actualise la position 
	  	
	  		# Et là on cherche qu'elle est la réponse qui mène au chainage qu'on l'on veut supprimer, car on veut aussi supprimer la réponse qui y mène
			for i in range(0, len(self.box[self.x][self.y].Reponses)): # Donc pour chaque réponse :
				if(self.box[self.x][self.y].Reponses[i].pos.z == variableTemporaire): # On test si les indices des réponses correspondent avec l'indice de la boite qu'on veut supprimer
					repToDel = i # Une fois qu'on là trouver on défini notre variable qui représente la réponse à supprimer
			
			del self.box[self.x][self.y].Reponses[repToDel] # On supprime la réponse qui mène au chainage que l'on veut supprimer
			self.box.Supprimer(boxToDel[0], boxToDel[1]) # Puis une fois tout cela fait on supprime le chainage que l'on veut supprimer
			self.GetFromBox() # Et on charge les informations de la nouvelle position où l'on se trouve



	def Count(self, obj): # Cette fonction sert à compter combien de fois il y'a une position "obj" dans la liste des positions où l'utilisateur est allé
		count = 0
		for i in range(0, len(self.debugArray)): # Donc pour chaque valeur dans la liste
			count += self.debugArray[i][1].count(obj) # On teste si elles correspondent, si elles correspondent on ajouter 1 à count
		return count

		

	def Jet(self, bouton): # Cette fonction est appellé lorsque l'utilisateur appuie sur le bouton "Jet"
		# Celle-ci va ouvrir une nouvelle fenêtre avec l'interface pour configurer le jet.
		listeTest = [self.Rep1.get(), self.Rep2.get(), self.Rep3.get()] # On créer une liste temporaire contenant les réponses de chaques boutons
		
		if (listeTest[bouton] != ''): # Si l'utilisateur à cliqué sur le bouton "Jet" d'une réponse vide, on ne fait rien, sinon :
			self.SetToBox() # On applique ce qu'il à fait à la boite

			def Valider(bouton): # On créer une fonction pour notre bouton "valider"
				variableFunc = function2.get() # On stoque temporairement dans une variable le contenue de notre StringVar function2

				if (function2.get() == ''): # Si function2 est vide alors on assigne False à notre variable temporaire sinon elle reste égal à ce qu'a rentré l'utilisateur
					variableFunc = False
				if(listeState.get() != '' and diff.get() != ''): # 
					if (x2.get() == '' and z2.get() == ''): # Si l'utilisateur n'a pas rentré de position x et y alors on en créer pour lui
						self.box[self.x][self.y].Reponses[bouton].extend = Extension(listeState.get(), diff.get(), (self.x +1), self.box.GetIndice(self.x + 1), variableFunc) # On applique le jet configuré à la boite
						self.box.Ajouter(Chainage(Chainage.d_texte, Chainage.d_Reponses, self.box.GetIndice(self.x +1)), self.x + 1) # On créer un nouveau chainage
						menu_jet.destroy() # Une fois tout cela appliqué à notre boite on quitte.
					elif (x2.get() != '' and z2.get() != ''): # Sinon si il à rentré une position x et une position y alors applique sans créer un nouveau chainage
						self.box[self.x][self.y].Reponses[bouton].extend = Extension(listeState.get(), diff.get(), x2.get(), z2.get(), variableFunc) # On applique le jet configuré à la boite
						menu_jet.destroy() # Une fois tout cela appliqué à notre boite on quitte.

			def Dejetyfication(bouton): # On créer une fonction pour notre bouton "Supprimer"
				self.box[self.x][self.y].Reponses[bouton].extend = False # On ajoute à notre
				menu_jet.destroy() # On ferme la fenêtre de jet

			def ActualiserListe(obj): # On créer une fonction pour indiquer sur qu'elle curseur se trouve la liste (Physique/Social/Mental)
				listeState.set(liste.get(str(obj.widget.curselection()[0]))) # On actualise notre variable texte contenant l'index sélectionné de la liste

			# Création d'une nouvelle fenètre
			menu_jet = Toplevel(self.editor) # On créer une nouvelle fenêtre par dessus notre fenêtre principale
			menu_jet['bg']='black' # On met le fond de couleur noir 
			menu_jet.title("Configuration Jet n°" + str(bouton + 1)) # On nomme la fenêtre 
			menu_jet.geometry("300x100") # On définit une taille pour la fenêtre
			menu_jet.resizable(0,0) # on défini que cette fenêtre ne peut pas se redimensionner
			
			# ListBox, on créer notre liste :
			liste = Listbox(menu_jet, height = 3, width = 8)
			liste.bind('<<ListboxSelect>>', ActualiserListe) # Lorsqu'on clique sur un idex de la liste ça lance la fonction ActualiserListe()
			liste.insert(1, "Physique") # Dans cette liste il y a trois paramètres : Physique / Mental / Social
			liste.insert(2, "Mental")
			liste.insert(3, "Social")
			doc = {"Social" : 2, "Mental" : 1, "Physique" : 0} # On créer un dictionaire pour convertir nos str en int (exemple : "Physique" = 0)
			liste.grid(rowspan = 3, row = 0, column = 1, sticky = NE) # Puis on place notre liste

			# On defini nos variables StringVar : 
			function2 = StringVar() # Si l'utilisateur veut que lorsque le joueur échoue le teste il se passe quelque chose, cette variable contiendra ces informations 
			# ex : le joueur échoue et perd des points de vies
			function2.set('') 
			diff = StringVar() # Contiendra la difficulté du jet
			diff.set('')
			x2 = StringVar() # Contiendra la position x si le personnage échoue
			x2.set('')
			z2 = StringVar() # Contiendra la position y si le personnage échoue
			z2.set('')
			listeState = StringVar() # Contiendra le statu de la liste (Physique, Mental ou Social)
			listeState.set('')
			
			# Boutons :  
			B_Valider = Button(menu_jet, text = "Valider", fg = 'green',  command = lambda: Valider(bouton)).grid(row = 4, column = 0) # On créer un bouton valider
			B_Supprimer = Button(menu_jet, text = "x", fg = 'red', command = lambda: Dejetyfication(bouton)).grid(row = 4, column = 3) # On créer un bouton Supprimer
			# Le bouton supprimer sert au cas ou l'utilisateur ne veut plus que cette réponse nécessite un jet

			# On créer Entry et on les positionnes :
			E_dificult = Entry(menu_jet, textvariable = diff, bg = 'white', width = 3) # Entry pour la difficulté
			E_dificult.grid(row = 0, column = 0)
			E_x2 = Entry(menu_jet, textvariable = x2, bg = 'white', width = 3) # Entry pour la position x
			E_x2.grid(row = 0, column = 2)
			E_z2 = Entry(menu_jet, textvariable = z2, bg = 'white', width = 3) # Entry pour la position y
			E_z2.grid(row = 0, column = 3)
			E_Function2 = Entry(menu_jet, textvariable = function2, bg = 'white', width = 10) # Entry pour la fonction lors d'un échec
			E_Function2.grid(row = 0, column = 4, padx = 10)
			# Label pour le liste, il sert à afficher l'état de la liste :
			labelListe = Label(menu_jet, textvariable = listeState, bg = 'white')
			labelListe.grid(row = 4 , column = 1)

			# Si la réponse possède deja un attribu "Jet" on le charge, en assignant chacune de nos variables :
			if( type(self.box[self.x][self.y].Reponses[bouton].extend) == type(Extension(None, None, None, None))): 
				diff.set(str(self.box[self.x][self.y].Reponses[bouton].extend.difficult))
				x2.set(self.box[self.x][self.y].Reponses[bouton].extend.pos2.x)
				z2.set(self.box[self.x][self.y].Reponses[bouton].extend.pos2.z)
				function2.set(self.box[self.x][self.y].Reponses[bouton].extend.function)
				liste.activate(doc[str(self.box[self.x][self.y].Reponses[bouton].extend.carac)])
				listeState.set(str(liste.get(ACTIVE)))
			
			menu_jet.mainloop() # On lance la boucle pour la nouvelle fenêtre créée 



	def Mike(self): #  Cette fonction est appellé lorsque l'utilisateur appuie sur le bouton "M", qui correspond à Mike
		# Celle-ci va ouvrir une nouvelle fenêtre avec l'interface pour configurer ce qui dit mike dans cette situation.
		def Valider(): # Un créer une fonction pour le bouton valider, qui applique les modifications
			self.box[self.x][self.y].mikeTexte = mikeTexte.get() # On applique le modifications à notre boite
			menu_mike.destroy() # Puis on détruit la fenêtre

		def Supprimer(): # Un créer une fonction pour le bouton supprimer, qui supprime ce que l'utilisateur à rentré
			self.box[self.x][self.y].mikeTexte = False # Mike ne dira alors rien à ce moment là
			menu_mike.destroy() # On ferme la fenêtre

		# Création d'une nouvelle fenêtre :
		menu_mike = Toplevel(self.editor) # On créer une nouvelle fenêtre par dessus notre fenêtre principale
		menu_mike['bg']='black' # On met le fond de couleur noir 
		menu_mike.title("Configuration Mike") # On nomme la fenêtre 
		menu_mike.geometry("400x175") # On définit une taille pour la fenêtre
		menu_mike.resizable(0,0) # Cette fenêtre n'est pas redimensionable
		
		mikeTexte = StringVar() # On créer un objet StringVar qui va contenir le texte de mike

		# On place nos widgets :
		L_MikeTexte = Label(menu_mike, textvariable = mikeTexte, width = 49, height = 8, wraplength = 350) # Label où est affiché le texte que rentre l'utilisateur
		L_MikeTexte.grid(columnspan = 4, row = 0, column = 0)
		E_MikeTexte = Entry(menu_mike, textvariable = mikeTexte, width = 49) # Entry, ou l'utilisateur peut écrire le texte de mike
		E_MikeTexte.grid(columnspan = 4, row = 1, column = 0)

		# Boutons valider
		B_MkeValider = Button(menu_mike, text = "Valider", fg = 'green', command = Valider).grid(row = 4, column = 0)
		B_MkeSupr = Button(menu_mike, text = "Supprimer", fg = 'red',command = Supprimer).grid(row = 4, column = 3)

		if (self.box[self.x][self.y].mikeTexte != False): # Si un texte existe déjà alors on le charge :
			mikeTexte.set(str(self.box[self.x][self.y].mikeTexte))

		menu_mike.mainloop() # On lance la boucle pour la nouvelle fenêtre créée 



	def Menu(self): # Cette fonction sert à retourner au menu
		self.Save() # On sauvegarde ce que le joueur à fait
		self.ClearEditeur() # On décharge l'éditeur pour pouvoir charger le menu apres
		self.debugArray = [] # On remet à 0 la liste qui contient où l'utilisateur est allé
		self.x = 0 # On remet nos position à 0
		self.y = 0
		print("\n\n\n\n\n\n\n\n\n\n") # On fait des sauts de ligne dans la console pour séparer les infos du fichier précédent avec les nouvelles infos
		self.LoadMenu() # On charge le menu



	def LenBoxRep(self): # Cette fonction sert à renvoyer le nombres de chainage qui possède des réponses
		taille = 0
		for x in range(0, self.box.Lenx()): # Pour chaque colonne
			for y in range(0, len(self.box[x])): # Et pour chque élement dans ces colonnes
				if(len(self.box[x][y].Reponses) > 0): # Si le chainage possède au moins une réponse alors on ajoute un a notre variable
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