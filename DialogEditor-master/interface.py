from __future__ import division
from tkinter import * 
import tkinter 
import time
#from PIL import Image, ImageTk
from time import sleep
import tkinter as tk
import tkinter.font as tkFont
import pickle

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
Mikec=False
animIsRuning = False
font10 = "-family {Nimbus Mono L} -size 22 -weight normal "

Label(fen,bg='BLACK',width=40,height=20,borderwidth=1).place(x= 572,y=342)
Label(fen,bg='BLUE',width=80, height=20,borderwidth=1).place(x=5,y=342)
toDraw = ''
it = 0

def update(delay = 50):
    global it
    global Descrip
    global ind
    ind += 1
    if ind == 6: ind = 0
    photo.configure(format="gif -index " + str(ind))
    if len(Descrip.get()) < len(chainage.texte):
        Descrip.set(Descrip.get() + chainage.texte[it])
        it += 1
        
    fen.after(delay, update)
    
def geoliste(g):
    r=[i for i in range(0,len(g))if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def centrefenetre(fen):
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    l= 860 #longueur de la fenêtre 
    h=650 # hauteur de la fenêtre 
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2-50))

class Fenetre(tkinter.Frame):
     def _init_(self, master=None):
        tkinter.Frame._init_(elf, master)
     centrefenetre (fen)
     fen.resizable(width=False, height=False)
     fen.title("Jeu Isn")
     fen['bg']='black'

def inventaire():
    global etatB
    if etatB ==False : 
       canI.place(x=5,y=5)
       etatB= True
    else :
        canI.place_forget()
        etatB= False

foreground = tk.Canvas(fen,width= 845,height=330,borderwidth=1, bg = 'black')
foreground.place(x=5, y=5)

Description = Label(foreground,width= 44,height=10,borderwidth=1, fg = 'WHITE', textvariable = Descrip, wraplength = 800, font = font10, anchor = W, bg = 'BLACK')#fenetre de description
Description.place(x=15, y=5)
Label(fen,bg='BLACK',width=40,height=20,borderwidth=1).place(x= 572,y=342)
blue = Label(fen,bg='WHITE',width=80, height=20,borderwidth=1)
blue.place(x=5,y=342)
    
canI = tk.Canvas(fen, width=can_width, height=can_height,bg='BLACK')
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

Button(fen,bg='GREY',text='Inventaire',width=10, height=1,borderwidth=1,command=inventaire,font=font2).place(x=8,y=307)

Mikec = tk.Canvas(fen, width=282, height=300, bg='white')
Mikec.place(x= 570, y=342)
Mikec.create_image(0,0,anchor='nw', image=photo,tag='photo')
Mikec.destroy


if Mikec==False:
    Mikec.place_forget
else :
    Mikec.place(x= 570, y=342)


#A partir d'ici, je code le jeu :
def Load(nom):
		with open(str(nom)+'.save', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier) #Je créé la fonction qui va importer le contenu de l'histoire. 
			global Scene
			Scene = mon_depickler.load()

Load("S1")#J'importe le fichier .save qui a été préalablement écrit : c'est l'histoire.
chainage = Scene[0][0] #Chainage va nous permetrre de travailler scène par scène, coordonnées par coordonnées.
Mike = False #Mike interviendra plus tard dans l'histoire.
#IJe définis mes variables qui seront le texte s'affichant sur les boites de dialogues.
def Affichage():
    global Rep1
    global Rep2
    global Rep3
    Rep1.set("")
    Rep2.set("")
    Rep3.set("")
    it = 0
    Animation()
    if len(chainage.Reponses) == 3:
     Rep1.set(chainage.Reponses[0].texte)
     Rep2.set(chainage.Reponses[1].texte)
     Rep3.set(chainage.Reponses[2].texte)
    elif len(chainage.Reponses) == 2:
     Rep1.set(chainage.Reponses[0].texte)
     Rep2.set(chainage.Reponses[1].texte)
    else:
     Rep1.set(chainage.Reponses[0].texte)
     

def Animation():
    global animIsRuning
    animIsRuning = True
    global Descrip
    Descrip.set("")
    for i in range(0, len(chainage.texte)):
        fen.wait_variable(Descrip)
        Descrip.set(Descrip.get() + chainage.texte[i])
        fen.update()
        
    animIsRuning = False

def Try():
    fen.update()
    


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
    
#Ici, je définis les différents emplacements de réponses. Je fais la boite de dialogue.

Reponse1 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep1, fg = "WHITE") #Cadre pour la première réponse. 
Reponse1.bind("<Button-1>",lambda event, n = 0: voyage(n))
Reponse1.place(x = 0, y = 0)
B1 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=101) #Séparation entre la première et la deuxième.

Reponse2 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep2,  fg = "WHITE")#Cadre pour la deuxième réponse.
Reponse2.bind("<Button-1>",lambda event, n = 1: voyage(n))
Reponse2.place(x = 0, y = 102)
B2 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=202) #Séparation entre la deuxième et la première.

Reponse3 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep3,  fg = "WHITE")#Cadre pour la troisième réponse.
Reponse3.bind("<Button-1>",lambda event, n = 2: voyage(n))
Reponse3.place(x = 0, y = 203)



update()
Affichage()
 
fen.mainloop()
