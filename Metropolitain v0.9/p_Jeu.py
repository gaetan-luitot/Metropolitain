from __future__ import division
from tkinter import * 
import tkinter 
import time
import tkinter as tk
import tkinter.font as tkFont
import pickle
from c_save import Save
from c_vecteur import Vecteur
from c_reponse import *
from os import remove
from random import randint


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
texteMike.set("...")
photo = PhotoImage(file="brouillage.gif")
font10 = tkFont.Font(family="Courier New", size=16)
font13 = tkFont.Font(family="Viner Hand ITC", size=80)
listedObjets = ["Briquet", "Couteau"]
perso = Save(Vecteur(0,0), 10, 3, [""] * 10, False)
can = [] 


######################################
# Déclaration des Fonctions :
######################################


def update(delay=20):#fonction qui permet l'animation du gif
    if perso.mike == True:
        global ind
        ind += 1
        if ind == 6: ind = 0
        photo.configure(format="gif -index " + str(ind))
        fen.after(delay, update)
    else:
        pass

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
     fen['bg']='black'

def TM():
    labM.place(x=576,y=602)

def inventaire():#place ou cache l'inventaire 
    global etatB
    if etatB ==False : 
       canI.place(x=5,y=5)
       etatB= True
    else:
        canI.place_forget()
        etatB= False

def Functions(texte):
    global perso
    print(texte)
    if (texte[0] == '0'): # Gain PV
        print("Le PJ gagne : " + texte[1] + " pv")
        perso.pv += int(texte[1])
    elif (texte[0] == '1'): # Perte PV
        print("Le PJ perd : " + texte[1] + " pv")
        perso.pv -= int(texte[1])

    elif (texte[0] == '2'): # Gain Objet
        print("Le PJ gagne l'objet n° " + texte[1])
        perso.objets[int(texte[1])] = listedObjets[int(texte[1])]
        canI.itemconfigure(can[int(texte[1])], text = listedObjets[int(texte[1])])
        fen.update()

    elif (texte[0] == '3'): # On détermine le personnage
        if (texte[1] == '0'):
            perso.archetype = 0
            perso.pv = Caracts(0)[0]
            print("Le personnage est la brute !")
        elif (texte[1] == '1'):
            perso.archetype = 1
            perso.pv = Caracts(1)[0]
            print("Le personnage est le social !")
        elif (texte[1] == '2'):
            perso.archetype = 2
            perso.pv = Caracts(2)[0]
            print("Le personnage est l'intellectuel !")

    elif (texte[0] == '4'): #On cache ou non la réponse
        if (texte[1] == '0') and perso.archetype == 0:
            print("True")
            return True
        elif (texte[1] == '1') and perso.archetype == 1:
            print("True")
            return True
        elif (texte[1] == '2') and perso.archetype == 2:
            print("True")
            return True
        else:
            print("False")
            return False

    elif (texte[0] == '5'): # On gagne ou perd mike :)
        if (texte[1] == '0'):
            print("A plus mike")
            perso.mike = False
        elif (texte[1] == '1'):
            print("mike oui !")
            perso.mike = True
        

def mike():#gif de mike (place ou cache)
    global perso
    if perso.mike == True:
        BM.place(x=755,y=315)
        Mikec.place(x= 570, y=342)
        update()
    else:
        BM.place_forget()
        Mikec.place_forget()
        labM.place_forget()
        fen.update()

def Save():
    global perso
    with open('sauvegarde.save', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(perso)
        print("--------SAVE--------")
        print("Le Pj est à la pos : " + str(perso.pos))
        print("Le Pj est l'archétype : " + str(perso.archetype))
        print("Le Pj à " + str(perso.pv) + " pv")
        print("--------------------")

def Load():
    global perso
    global chainage
    try:
        with open('sauvegarde.save', 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            perso = mon_depickler.load()
            chainage = Scene[perso.pos.x][perso.pos.z]
            for i in range(0, len(perso.objets)):
                canI.itemconfigure(can[i], text = listedObjets[i])
    except:
        print("Pas de sauvegarde donc on commence une nouvelle histoire")
        chainage = Scene[0][0]

def SaveAndQuit():
    Save()
    fen.destroy()
    fen.quit()

def Caracts(x): #Je définis les caractéristiques.
    if x == 0:
        return [8,5,5] #Ici, c'est le personnage physique. On remarque que la 1ere valeur est celle du Physique, la 2ème Social, 3ème Mental
    elif x == 1:
        return [5,8,5]#Personnage social
    elif x == 2:
        return [5,5,8] #Personnage mental
    elif x == 3: # Personnage pas encore définie
        return [5, 5, 5]

def AffichageManager():
    global MikeEtat
    if perso.mike == True:
        perso.mike = False
        mike()
        Affichage()
        perso.mike = True
        mike()
    else:
        mike()
        Affichage()
    #Save()

def Affichage():
    global Rep1
    global Rep2
    global Rep3
    Rep1.set("")
    Rep2.set("")
    Rep3.set("")
    texteMike.set("...")
    Animation() # On affiche la description avec un animation
    if (len(chainage.Reponses) > 0):
        if chainage.Reponses[0].hiden == False:
            Rep1.set(chainage.Reponses[0].texte)
        elif chainage.Reponses[0].hiden == True and Functions(chainage.Reponses[0].function) == True: 
            Rep1.set(chainage.Reponses[0].texte)  
    if (len(chainage.Reponses) > 1):
        if chainage.Reponses[1].hiden == False:
            Rep2.set(chainage.Reponses[1].texte)
        elif chainage.Reponses[1].hiden == True and Functions(chainage.Reponses[1].function) == True:
            Rep2.set(chainage.Reponses[1].texte)
    if (len(chainage.Reponses) > 2):
        if chainage.Reponses[2].hiden == False:
            Rep3.set(chainage.Reponses[2].texte)
        elif chainage.Reponses[2].hiden == True and Functions(chainage.Reponses[2].function) == True:
            Rep3.set(chainage.Reponses[2].texte)
    if chainage.mikeTexte != False:
        texteMike.set(chainage.mikeTexte)

def Animation():
    global Descrip
    Descrip.set("")
    for i in range(0, len(chainage.texte)):
        Descrip.set(Descrip.get() + chainage.texte[i])
        fen.after(8, fen.update())

def de(n, difficulte):#lance de de 
    if n == "Physique":
        carac = 0
    elif n == "Social":
        carac = 1
    elif n == "Mental":
        carac = 2
    alea = randint(0,10)
    print("Jet de " + n)
    print(str(perso.archetype) + " " + str(carac))
    print(str(Caracts(perso.archetype)[carac]))
    total = Caracts(perso.archetype)[carac] + int(difficulte)
    print("Le joueur à fait : " + str(alea) + " sur " + str(total))
    if alea <= total :
        print("Réussite")
        return True
    else :
        print("Échec")
        return False 

def voyage(n):
    global chainage
    global perso
    IsGameOver() # On vérifie si le personnage est mort ou non.
    if n == 0 and Rep1.get() != "":
        if (str(type(chainage.Reponses[n].extend)) != "<class 'c_reponse.Extension'>"):
            perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
            if chainage.Reponses[n].function != False:
                Functions(chainage.Reponses[n].function)
            chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
        else:
            if (de(chainage.Reponses[n].extend.carac, chainage.Reponses[n].extend.difficult)):
                perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
                if chainage.Reponses[n].function != False:
                    Functions(chainage.Reponses[n].function)
                chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
            else:
                perso.pos = Vecteur(int(chainage.Reponses[n].extend.pos2.x), int(chainage.Reponses[n].extend.pos2.z))
                if chainage.Reponses[n].extend.function != False:
                    Functions(chainage.Reponses[n].extend.function)
                chainage = Scene[int(chainage.Reponses[n].extend.pos2.x)][int(chainage.Reponses[n].extend.pos2.z)]
        AffichageManager()
    elif n == 1 and Rep2.get() != "":
        if (str(type(chainage.Reponses[n].extend)) != "<class 'c_reponse.Extension'>"):
            perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
            if chainage.Reponses[n].function != False:
                Functions(chainage.Reponses[n].function)
            chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
        else:
            if (de(chainage.Reponses[n].extend.carac, chainage.Reponses[n].extend.difficult)):
                perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
                if chainage.Reponses[n].function != False:
                    Functions(chainage.Reponses[n].function)
                chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
            else:
                perso.pos = Vecteur(int(chainage.Reponses[n].extend.pos2.x), int(chainage.Reponses[n].extend.pos2.z))
                if chainage.Reponses[n].extend.function != False:
                    Functions(chainage.Reponses[n].extend.function)
                chainage = Scene[int(chainage.Reponses[n].extend.pos2.x)][int(chainage.Reponses[n].extend.pos2.z)]
        AffichageManager()
    elif n == 2 and Rep3.get() != "":
        if (str(type(chainage.Reponses[n].extend)) != "<class 'c_reponse.Extension'>"):
            perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
            if chainage.Reponses[n].function != False:
                Functions(chainage.Reponses[n].function)
            chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
        else:
            if (de(chainage.Reponses[n].extend.carac, chainage.Reponses[n].extend.difficult)):
                perso.pos = Vecteur(chainage.Reponses[n].pos.x, chainage.Reponses[n].pos.z)
                if chainage.Reponses[n].function != False:
                    Functions(chainage.Reponses[n].function)
                chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
            else:
                perso.pos = Vecteur(int(chainage.Reponses[n].extend.pos2.x), int(chainage.Reponses[n].extend.pos2.z))
                if chainage.Reponses[n].extend.function != False:
                    Functions(chainage.Reponses[n].extend.function)
                chainage = Scene[int(chainage.Reponses[n].extend.pos2.x)][int(chainage.Reponses[n].extend.pos2.z)]
        AffichageManager()

def IsGameOver():
    if perso.pv <= 0:
        canend.place(x =0, y= 0)
        print("Supprétion de la partie")
        remove("sauvegarde.save")
        fen.after(5000, SaveAndQuit)
        


######################################
# Déclaration des widgets Tkinter :
######################################
fen.protocol("WM_DELETE_WINDOW", SaveAndQuit)
foreground = tk.Canvas(fen,width= 845,height=330,borderwidth=1, bg = 'black')
foreground.place(x=5, y=5)

Description = Label(foreground, padx = 20, width= 80,height=11,borderwidth=1,textvariable = Descrip, wraplength = 800, bg = 'black', fg = 'white', font = font10, anchor = W, justify = 'left')
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
can.append(canI.create_text(50, 15,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 45,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 75,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 105,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 135,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 165,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 195,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 225,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 255,text='',font=font,fill='WHITE'))
can.append(canI.create_text(50, 285,text='',font=font,fill='WHITE'))
canI.place_forget()

#Ici, je définis les différents emplacements de réponses. Je fais la boite de dialogue.
blue = Label(fen,bg='BLACK',width=70, height=20,borderwidth=1)
blue.place(x=5,y=342)

# Réponse 1 :
Reponse1 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep1, wraplength = 600, fg = "WHITE") #Cadre pour la première réponse. 
Reponse1.bind("<Button-1>",lambda event, n = 0: voyage(n))
Reponse1.place(x = 0, y = 0)
# Ligne de séparation entre la réponse 1 et la réponse 2 :
B1 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=101) #Séparation entre la première et la deuxième.
# Réponse 2 :
Reponse2 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep2, wraplength = 600, fg = "WHITE")#Cadre pour la deuxième réponse.
Reponse2.bind("<Button-1>",lambda event, n = 1: voyage(n))
Reponse2.place(x = 0, y = 102)
# Ligne de séparation entre la réponse 2 et la réponse 3 :
B2 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=202) #Séparation entre la deuxième et la première.
# Réponse 3 :
Reponse3 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep3, wraplength = 600, fg = "WHITE")#Cadre pour la troisième réponse.
Reponse3.bind("<Button-1>",lambda event, n = 2: voyage(n))
Reponse3.place(x = 0, y = 203)

#bouton inventaire 
Button(fen,bg='GREY',text='Inventaire',width=10, height=1,borderwidth=1,command=inventaire,font=font2).place(x=8,y=315)

#caneves game over
canend= tk.Canvas(fen,width= 860,height=650,borderwidth=1, bg = 'black')
canend.place(x=0,y=0)
canend.create_text(860/2,650/2,text='GAME OVER',font=font13,fill='RED')
canend.place_forget()

#button Mike
BM=Button(fen,bg='GREY',text='Mike',width=10, height=1,borderwidth=1,command=TM,font=font2)
BM.place(x=755,y=315)
BM.place_forget()



######################################
# Programme :
######################################
#J'importe le fichier S1.save (grâce à la librairie pickle) qui a été préalablement écrit : c'est l'histoire.
with open('S1.save', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    global Scene
    Scene = mon_depickler.load()

Load() # On essaye de charger une sauvegarde

AffichageManager() # On affiche la scène où se trouve le joueur
 
fen.mainloop() # On lance la boucle principale de tkinter
