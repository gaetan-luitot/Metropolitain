######################################
# Déclaration des librairies requises :
######################################
# from PIL import Image, ImageTk
from __future__ import division
import time
import pickle
from time import sleep
# On import 4 fois tkinter xD :
from tkinter import * 
import tkinter as tk
import tkinter.font as tkFont
import tkinter 




######################################
# Déclaration des variables :
######################################
fen=Tk()
ind = -1
font= tkFont.Font(size=14)
font2= tkFont.Font(size=13)
can_width = 99
can_height = 330
etatB=False
Descrip = StringVar()
Rep1 = StringVar()
Rep2 = StringVar()
Rep3 = StringVar()
photo = PhotoImage(file="brouillage.gif")
photo2 = PhotoImage(file="metro.gif")
MikEtat=False
animation = False




######################################
# Déclaration des Fonctions :
######################################
def update(delay=10):#fonction qui permet l'animation du gif 
    global ind
    ind += 1
    if ind == 6: ind = 0
    photo.configure(format="gif -index " + str(ind))
    if animation == False:
        fen.after(delay, update)#t

def geoliste(g): #fontion qui permet de déterminer les coordonnées de la fenetre
    r=[i for i in range(0,len(g))if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def centrefenetre(fen):#fonction qui permet de placer  la fenêtre de jeu au centre de l'écran 
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    l= 860 #longueur de la fenêtre 
    h=650 # hauteur de la fenêtre 
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2-50))

def inventaire(): # place ou cache l'inventaire 
    global etatB
    if etatB ==False : 
       canI.place(x=5,y=5)
       etatB= True
    else :
        canI.place_forget()
        etatB= False

def mike():#gif de mike (place ou cache)
    global MikEtat
    if MikEtat ==False :
        Mikec = tk.Canvas(fen, width=282, height=300, bg='white')
        Mikec.place(x= 570, y=342)
        Mikec.create_image(0,0,anchor='nw', image=photo,tag='photo')
    else :
        Mikec.place_forget()

def Load(nom):
        with open(str(nom)+'.save', 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier) #Je créé la fonction qui va importer le contenu de l'histoire. 
            global Scene
            Scene = mon_depickler.load()

def Affichage():
    global Rep1
    global Rep2
    global Rep3
    Animation() # On affiche la description avec un animation
    if len(chainage.Reponses) == 3:
        Rep1.set(chainage.Reponses[0].texte)
        Rep2.set(chainage.Reponses[1].texte)
        Rep3.set(chainage.Reponses[2].texte)
    elif len(chainage.Reponses) == 2:
        Rep1.set(chainage.Reponses[0].texte)
        Rep2.set(chainage.Reponses[1].texte)
        Rep3.set("")
    else:
        Rep1.set(chainage.Reponses[0].texte)
        Rep2.set("")
        Rep3.set("")
    if Mike == True:
        print("Mike :", chainage.mikeTexte)

def voyage(n):
    global chainage
    if n == 0 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()
    elif n == 1 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()
    elif n == 2 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()

def Animation():
    global Descrip
    Descrip.set("")
    animation = True
    for i in range(0, len(chainage.texte)):
        Descrip.set(Descrip.get() + chainage.texte[i])
        fen.update()
        sleep(0.5)
    animation = False

class Fenetre(tkinter.Frame): #fenetre de jeu principal 
     def _init_(self, master=None):
        tkinter.Frame._init_(elf, master)
     centrefenetre(fen)
     fen.resizable(width=False, height=False)
     fen.title("Jeu Isn")
     fen['bg']='grey'




######################################
# Déclaration des widgets pour Tkinter :
######################################

#fenetre de description :
Description = Label(fen,width= 121,height=4,borderwidth=1,textvariable = Descrip, wraplength = 800)
Description.place(x=5, y=140)
Label(fen,bg='BLACK',width=40,height=20,borderwidth=1).place(x= 572,y=342)
# Label bleu :
blue = Label(fen,bg='BLACK',width=80, height=20,borderwidth=1)
blue.place(x=5,y=342)
# Autre label :
Label(fen,bg='BLACK',width=40,height=20,borderwidth=1).place(x= 572,y=342)

# Réponse 1 :
Reponse1 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep1, fg = "WHITE") #Cadre pour la première réponse. 
Reponse1.bind("<Button-1>",lambda event, n = 0: voyage(n))
Reponse1.place(x = 0, y = 0)
# Ligne de séparation entre la réponse 1 et la réponse 2 :
B1 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=101) #Séparation entre la première et la deuxième.
# Réponse 2 :
Reponse2 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep2,  fg = "WHITE")#Cadre pour la deuxième réponse.
Reponse2.bind("<Button-1>",lambda event, n = 1: voyage(n))
Reponse2.place(x = 0, y = 102)
# Ligne de séparation entre la réponse 2 et la réponse 3 :
B2 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=202) #Séparation entre la deuxième et la première.
# Réponse 3 :
Reponse3 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep3,  fg = "WHITE")#Cadre pour la troisième réponse.
Reponse3.bind("<Button-1>",lambda event, n = 2: voyage(n))
Reponse3.place(x = 0, y = 203)

#image de fond de la fenetre de description :
foreground = tk.Canvas(fen,width= 845,height=330,borderwidth=1)
foreground.place(x=5, y=5)
foreground.create_image(0,0,anchor='nw',image=photo2)

# fenetre de l'inventaire, création des lignes et du texte :  
canI = tk.Canvas(fen, width=can_width, height=can_height,bg='DIMGREY')
canI.place(x=0,y=0)
canI.create_line(0,30,1005,30,fill='GREY',width=1)
canI.create_line(0,60,1005,60,fill='GREY',width=1)
canI.create_line(0,90,1005,90,fill='GREY',width=1)
canI.create_line(0,120,1005,120,fill='GREY',width=1)
canI.create_line(0,150,1005,150,fill='GREY',width=1)
canI.create_line(0,180,1005,180,fill='GREY',width=1)
canI.create_line(0,210,1005,210,fill='GREY',width=1)
canI.create_line(0,240,1005,240,fill='GREY',width=1)
canI.create_line(0,270,1005,270,fill='GREY',width=1)
canI.create_line(0,300,1005,300,fill='GREY',width=1)
canI.create_text(50, 15,text='',font=font,fill='WHITE')
canI.create_text(50, 45,text='',font=font,fill='WHITE')
canI.create_text(50, 75,text='',font=font,fill='WHITE')
canI.create_text(50, 105,text='',font=font,fill='WHITE')
canI.create_text(50, 135,text='',font=font,fill='WHITE')
canI.create_text(50, 165,text='',font=font,fill='WHITE')
canI.create_text(50, 195,text='',font=font,fill='WHITE')
canI.create_text(50, 225,text='',font=font,fill='WHITE')
canI.create_text(50, 255,text='',font=font,fill='WHITE')
canI.create_text(50, 285,text='',font=font,fill='WHITE')
canI.place_forget()

# fenêtre dialogue Mike :
labM= Label(fen,width=38,height = 2,borderwidth = 2,text='My name is Z, Mike Z').place(x= 576,y= 602)

# bouton inventaire 
Button(fen,bg='GREY',text='Inventaire',width=10, height=1,borderwidth=1,command=inventaire,font=font2).place(x=8,y=307)




######################################
# Lancement du programme :
######################################
mike() # On affiche Mike

Load("S1") # J'importe le fichier S1.save qui a été préalablement écrit : c'est l'histoire.
chainage = Scene[0][0] # Chainage va nous permetrre de travailler scène par scène, coordonnées par coordonnées.
Mike = False # Mike interviendra plus tard dans l'histoire.

Affichage() # On affiche manuelement le texte en 0;0. 

update() # On lance la fonction d'actualisation du gif
 
fen.mainloop() # On lance la boucle principale de Tkinter
