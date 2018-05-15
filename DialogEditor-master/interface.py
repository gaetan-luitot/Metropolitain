from __future__ import division
from tkinter import * 
import tkinter 
import time
import tkinter as tk
import tkinter.font as tkFont
import pickle
from c_Save import Save
from c_Vecteur import Vecteur


######################################
# Déclaration des Variables :
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
texteMike = StringVar()
photo = PhotoImage(file="brouillage.gif")
MikEtat= False
font10 = "-family {Nimbus Mono L} -size 18 -weight normal "
perso = Save(Vecteur(0,0), 0, 0, listedObjets = [])


######################################
# Déclaration des Fonctions :
######################################


def update(delay=5):#fonction qui permet l'animation du gif
    if MikEtat == True:
        global ind
        ind += 1
        if ind == 6: ind = 0
        photo.configure(format="gif -index " + str(ind))
        fen.after(delay, update)
    else:
        print('mike()')

def geoliste(g): #fontion qui permet de déterminer les coordonnées de la fenetre
    r=[i for i in range(0,len(g))if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def centrefenetre(fen):#fonction qui permet de placer  la fenêtre de jeu au centre de l'écran 
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    l= 860 #longueur de la fenêtre 
    h=650 # hauteur de la fenêtre 
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2-50))

class Fenetre(tkinter.Frame): #fenetre de jeu principal 
     def _init_(self, master=None):
        tkinter.Frame._init_(elf, master)
     centrefenetre (fen)
     fen.resizable(width=False, height=False)
     fen.title("Jeu Isn")
     fen['bg']='grey'

def inventaire():#place ou cache l'inventaire 
    global etatB
    if etatB ==False : 
       canI.place(x=5,y=5)
       etatB= True
    else:
        canI.place_forget()
        etatB= False

def mike():#gif de mike (place ou cache)
    global MikEtat
    print(MikEtat)
    if MikEtat == True:
        Mikec.place(x= 570, y=342)
        labM.place(x= 576,y= 602)
        update()
    else:
        Mikec.place_forget()
        labM.place_forget()

#A partir d'ici, je code le jeu :
def Save(self):
        with open('sauvegarde.save', 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(self._tableau)

    def Load(self):
        try:
            with open('sauvegarde.save', 'rb') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                boite_recupere = mon_depickler.load()
                self._tableau = boite_recupere

def Affichage():
    global Rep1
    global Rep2
    global Rep3
    Rep1.set("")
    Rep2.set("")
    Rep3.set("")
    texteMike.set("")
    Animation() # On affiche la description avec un animation
    if (len(chainage.Reponses) > 0 and chainage.Reponses[0].hiden == False):
        Rep1.set(chainage.Reponses[0].texte)
    if (len(chainage.Reponses) > 1 and chainage.Reponses[1].hiden == False):
        Rep2.set(chainage.Reponses[1].texte)
    if (len(chainage.Reponses) > 2 and chainage.Reponses[2].hiden == False):
        Rep3.set(chainage.Reponses[2].texte)

    if Mike == True:
        texteMike.set(chainage.mikeTexte)

def Animation():
    global MikEtat
    global Descrip
    Descrip.set("")
    if MikEtat == True:
        MikEtat = False
        mike()
        for i in range(0, len(chainage.texte)):
            Descrip.set(Descrip.get() + chainage.texte[i])
            fen.after(10, fen.update())
        MikEtat = True
        mike()
    else:
        for i in range(0, len(chainage.texte)):
            Descrip.set(Descrip.get() + chainage.texte[i])
            fen.after(10, fen.update())

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




######################################
# Déclaration des widgets Tkinter :
######################################
foreground = tk.Canvas(fen,width= 845,height=330,borderwidth=1, bg = 'black')
foreground.place(x=5, y=5)

Description = Label(foreground, padx = 20, width= 57,height=11,borderwidth=1,textvariable = Descrip, wraplength = 800, bg = 'black', fg = 'white', font = font10, anchor = W, justify = 'left')
Description.place(x=5, y=5)

Mikec = tk.Canvas(fen, width=282, height=300, bg='white')
Mikec.place(x= 570, y=342)
Mikec.create_image(0,0,anchor='nw', image=photo,tag='photo')
labM = Label(fen,width=38,height = 2,borderwidth = 2,textvariable = texteMike)
labM.place(x= 576,y= 602)
Mikec.place_forget()
labM.place_forget()

#fenetre de l'inventaire    
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

#Ici, je définis les différents emplacements de réponses. Je fais la boite de dialogue.
blue = Label(fen,bg='BLACK',width=70, height=20,borderwidth=1)
blue.place(x=5,y=342)

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

#bouton inventaire 
Button(fen,bg='GREY',text='Inventaire',width=10, height=1,borderwidth=1,command=inventaire,font=font2).place(x=8,y=315)


######################################
# Programme :
######################################
#J'importe le fichier S1.save qui a été préalablement écrit : c'est l'histoire.
with open('S1.save', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    global Scene
    Scene = mon_depickler.load()

chainage = Scene[0][0] #Chainage va nous permetrre de travailler scène par scène, coordonnées par coordonnées.
Mike = False #Mike interviendra plus tard dans l'histoire.
Affichage()
update()
 
fen.mainloop()
