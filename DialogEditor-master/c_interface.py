""" 
Cet classe, Interface, va être la classe qui va gérer la création d'une interface graphique pour configurer notre Boite,
c'est grâce à elle que un utilisateur va pouvoir créer une scène, donc sont travail est de communiqué entre l'utilisateur et la scène en création.
"""

import sys
from tkinter import *
from c_boite import *
from c_chainage import *
from c_reponse import *
from tkinter.messagebox import *
from sys import platform

"""
if platform == "linux" or platform == "linux2":
    # linux
elif platform == "darwin":
    # OS X
elif platform == "win32":"""


class Interface: # On définit notre classe, que l'on appelle "Interface" :

	def __init__(self): # Constructeur :
		try: self.color = sys.stdout.shell
		except AttributeError: raise RuntimeError("Use IDLE")
		# Fenêtre :
		self.editor = Tk() # On créer une fenêtre "editor"
		self.editor['bg']='black' # On met le fond de couleur noir 
		self.editor.title("Editeur de Scène") # On nomme la fenêtre 
		self.editor.geometry("640x460") # On définit une taille pour la fenêtre
		self.editor.resizable(0,0) # On fixe la taille pour qu'on ne puisse pas la modifier

		# Variables :
		self.lenghtOS = 520
		self.debugArray = []
		self.box = Boite("default")
		self.nbBox = StringVar()
		self.nbBoxRep = StringVar()
		self.xRep1 = StringVar()
		self.yRep1 = StringVar()
		self.xRep2 = StringVar()
		self.yRep2 = StringVar()
		self.xRep3 = StringVar()
		self.yRep3 = StringVar()
		self.FunctionRep1 = StringVar()
		self.FunctionRep2 = StringVar()
		self.FunctionRep3 = StringVar()
		self.texteRep1 = StringVar() # Texte de la réponse 1 actuel
		self.texteRep2 = StringVar() # Texte de la réponse 2 actuel
		self.texteRep3 = StringVar() # Texte de la réponse 3 actuel
		self.XGoTo = StringVar()
		self.YGoTo = StringVar()
		self.texteDialogue = StringVar() # Texte du dialogue de la Scène ou du PNJ
		self.texteDialogue.set("[Texte]")
		self.x = 0 # x position actuel
		self.y = 0 # y position actuel
		self.pos = StringVar() # Texte de la position actuel
		self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y)) #
		self.nomFichierBoite = StringVar() # Texte de la position actuel
		self.nomFichierBoite.set("Nom du fichier")
		self.chainageActuel = Chainage(self.texteDialogue.get(), [[self.texteRep1.get(), 0, 0, False], [self.texteRep2.get(), 0, 0, False],[self.texteRep3.get(), 0, 0, False]], 0)
		self.hiden1 = IntVar()
		self.hiden2 = IntVar()
		self.hiden3 = IntVar()
		
		self.Define() # On créer notre fenêtre de base
		self.LoadMenu() # On charge le menu au début
		self.Start() # On commence une boucle Tkinter  

	def Start(self): # start mainloop
		self.editor.mainloop()

	def Define(self): # Création de tout les widgets de base
		# Paned Windows :
		self.X = PanedWindow(self.editor, orient = HORIZONTAL)
		self.Y = PanedWindow(self.editor, orient = HORIZONTAL)
		# Canvas :
		self.Fond = Canvas(self.editor, bg = 'black', width= 640, height = 460)
		# LabelFrame :
		self.X.add(Label(self.editor, text = '', bg = 'black', anchor = NW, width = 91))
		self.Y.add(Label(self.editor, text = '', bg = 'black', anchor = NW, width = 2, height = 31))
		# On affiche tout :
		self.X.grid(columnspan = 640, rowspan = 460, row = 0, column = 0, sticky = NW)
		self.Y.grid(rowspan = 460, columnspan = 640, row = 0, column = 0, sticky = NW)
		self.Fond.grid(rowspan = 460, columnspan = 640, row = 0, column = 0, sticky = NW)

	def LoadMenu(self):
		print("I: Chargement du menu")
		# Entry
		self.Fichier = Entry(self.editor, textvariable = self.nomFichierBoite, width = 18) # Nom du Fichier à charger ou à créer

		# Button :
		self.New = Button(self.editor, text = "Créer", command = lambda: self.NewScene(self.nomFichierBoite.get())) # Créer une nouvelle boite
		self.Load = Button(self.editor, text = "Charger", command = lambda: self.LoadScene(self.nomFichierBoite.get())) # Charger une boite déjà existante

		self.PackMenu() # On charge les éléments du Menu

	def PackMenu(self):
		# Label :
		self.Fichier.grid(columnspan = 640, rowspan = 460, row = 100, column = 150, sticky = NW)
		# Button :
		self.New.grid(columnspan = 640, rowspan = 460, row = 150, column = 150, sticky = NW)
		self.Load.grid(columnspan = 640, rowspan = 460, row = 150, column = 225, sticky = NW)

	def ClearMenu(self):
		print("I: Déchargement du menu")
		self.New.grid_forget()
		self.Load.grid_forget()
		self.Fichier.grid_forget()

	def LoadEditeur(self):
		print("I: Chargement de l'interface d'édition")
		# LabelFrame :
		self.TopHelp = Label(self.editor, textvariable = self.nbBox, bg = 'white', width = 20) # Help : Nombre de chainages crées
		self.TopHelpTwo = Label(self.editor, textvariable = self.nbBoxRep, bg = 'white', width = 20) # Help : [à définir]
		self.TexteLabel = Label(self.editor, textvariable = self.texteDialogue, bg = 'white', width = 75, height = 10, wraplength = self.lenghtOS, anchor = NW) # Affichage du texte écrit
		self.InfoPosVar = Label(self.editor, textvariable = self.pos, bg = 'white', width = 5, height = 2) # Help : Position actuel

		# Entry :
		self.Texte = Entry(self.editor, textvariable = self.texteDialogue, width = 88) # Texte du PNJ 
		self.Rep1 = Entry(self.editor, textvariable = self.texteRep1, width = 104) # Réponse 1 du PJ
		self.Rep2 = Entry(self.editor, textvariable = self.texteRep2, width = 104) # Réponse 2 du PJ
		self.Rep3 = Entry(self.editor, textvariable = self.texteRep3, width = 104) # Réponse 3 du PJ
		self.EntryxRep1 = Entry(self.editor, textvariable = self.xRep1, width = 2)
		self.EntryyRep1 = Entry(self.editor, textvariable = self.yRep1, width = 2)
		self.EntryxRep2 = Entry(self.editor, textvariable = self.xRep2, width = 2)
		self.EntryyRep2 = Entry(self.editor, textvariable = self.yRep2, width = 2)
		self.EntryxRep3 = Entry(self.editor, textvariable = self.xRep3, width = 2)
		self.EntryyRep3 = Entry(self.editor, textvariable = self.yRep3, width = 2)
		self.E_FunctionRep1 = Entry(self.editor, textvariable = self.FunctionRep1, width = 14)
		self.E_FunctionRep2 = Entry(self.editor, textvariable = self.FunctionRep2, width = 14)
		self.E_FunctionRep3 = Entry(self.editor, textvariable = self.FunctionRep3, width = 14)
		self.E_XGoto = Entry(self.editor, textvariable = self.XGoTo, width = 2)
		self.E_YGoto = Entry(self.editor, textvariable = self.YGoTo, width = 2)


		# Button :
		self.B_Save = Button(self.editor, text = "Save", command = self.Save) # Bouton pour sauvegarder la boite
		self.B_Delete = Button(self.editor, text = "Delete", command = self.Delete) # Bouton pour sauvegarder la boite
		self.B_Debug = Button(self.editor, text = "Debug", command = self.Debug) # Bouton afficher à quoi ressemble la boite
		self.B_Return = Button(self.editor, text = "Return", command = self.Return) # Bouton de navigation à travers la boite : retourner en arrière
		self.B_Mike = Button(self.editor, text = "M", command = self.Mike)
		self.B_Jet1 = Button(self.editor, text = "Jet", command = lambda: self.Jet(0), width = 2)  
		self.B_Jet2 = Button(self.editor, text = "Jet", command = lambda: self.Jet(1), width = 2)  
		self.B_Jet3 = Button(self.editor, text = "Jet", command = lambda: self.Jet(2), width = 2)  
		self.ButtonRep1 = Button(self.editor, text = "Réponse 1", command = lambda: self.ApplyCurrent(0), width = 13) # Btn navigation : aller vers chainage suivant
		self.ButtonRep2 = Button(self.editor, text = "Réponse 2", command = lambda: self.ApplyCurrent(1), width = 13) # Btn navigation : aller vers chainage suivant
		self.ButtonRep3 = Button(self.editor, text = "Réponse 3", command = lambda: self.ApplyCurrent(2), width = 13) # Btn navigation : aller vers chainage suivant
		self.B_Menu = Button(self.editor, text = "Menu", command = self.Menu)
		self.B_Goto = Button(self.editor, text = "Go !", command = self.GoTo)

		# CheckBox :
		self.checkRep1 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden1 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')
		self.checkRep2 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden2 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')
		self.checkRep3 = Checkbutton(self.editor, text = "Cacher", variable = self.hiden3 , bg = 'white', activebackground = 'white', activeforeground = 'black', fg = 'black')

		self.PackEditeur() # On affiche le tout
		
	def PackEditeur(self): # Update de tout les Widgets
		# UI help :
		self.TopHelp.grid(columnspan = 640, rowspan = 460, row = 0, column = 210, sticky = NW)
		self.TopHelpTwo.grid(columnspan = 640, rowspan = 460, row = 21, column = 210, sticky = NW)
		self.InfoPosVar.grid(columnspan = 640, rowspan = 460, row = 100, column = 0, sticky = NW)

		# UI Other:
		self.B_Save.grid(columnspan = 640, rowspan = 460, row = 0, column = 600, sticky = NW)
		self.B_Return.grid(columnspan = 640, rowspan = 460, row = 0, column = 0, sticky = NW)
		self.B_Debug.grid(columnspan = 640, rowspan = 460, row = 26, column = 589, sticky = NW)
		self.B_Delete.grid(columnspan = 640, rowspan = 460, row = 26, column = 0, sticky = NW)
		self.B_Mike.grid(columnspan = 640, rowspan = 460, row = 100, column = 600, sticky = NW)

		# Texte :
		self.Texte.grid(columnspan = 640, rowspan = 460, row = 210, column = 55, sticky = NW)
		self.TexteLabel.grid(columnspan = 640, rowspan = 460, row = 56, column = 55, sticky = NW)

		# widgets "Button" pour les Réponses :
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

	def ClearEditeur(self):
		print("I: Déchargement de l'interface d'éditions")
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

	def Return(self):
		if (self.x != 0):
			self.SetToBox()
			self.x = int(self.debugArray[-1][0].x)
			self.y = int(self.debugArray[-1][0].z)
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y))
			del self.debugArray[-1]
			self.GetFromBox()


	def ApplyCurrent(self, nbButton): # On ajoute à notre tableau box le chainage que l'on vient de créer
		repTemporaire = [self.texteRep1.get(), self.texteRep2.get(), self.texteRep3.get()]
		if(repTemporaire[nbButton] == ''):
			print("I: La réponse est vide, veuillez en créer une pour pouvoir y accéder !")
		else:
			self.SetToBox()
			temp = self.x
			self.debugArray.append([Vecteur(self.x, self.y) ,str(Vecteur(self.x, self.y))])
			self.x = self.chainageActuel.Reponses[nbButton].pos.x
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y))
			if (temp == self.chainageActuel.Reponses[nbButton].pos.x +1):
				self.y = self.ZtoYrep(self.x - 1, self.chainageActuel.Reponses[nbButton].pos.z)
			elif (self.x == 0):
				self.y = self.ZtoYrep(self.x, self.chainageActuel.Reponses[nbButton].pos.z)
			else:
				self.y = self.chainageActuel.Reponses[nbButton].pos.z
			self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y))
			self.GetFromBox()

	def SetToBox(self): # On assignent les infos rentrés dans les Entrys à notre variables chainageActuel
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
		print(str(index) + " " + str(indiceToFind))
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
				print("Hum Erreur !")
				
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

	def Menu(self):
		self.Save()
		self.ClearEditeur()
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


	def GoTo(self):
		if (self.XGoTo.get() != '' and self.YGoTo.get() != ''):
			newX = int(self.XGoTo.get())
			newY = int(self.YGoTo.get())
			try:
				
				temp = self.box[newX][newY]
			except:
				print("E: L'index n'existe pas !")
			else:
				self.SetToBox()
				self.debugArray.append([Vecteur(self.x, self.y) ,str(Vecteur(self.x, self.y))])
				self.x = newX
				self.y = newY
				self.pos.set("x : " + str(self.x) + "\ny : " + str(self.y))
				self.GetFromBox()
			self.XGoTo.set('')
			self.YGoTo.set('')