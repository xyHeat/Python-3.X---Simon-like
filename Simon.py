from tkinter import *
from random import *

# VARIABLES

# LISTES

global suite
suite = []

# DEFINITIONS

def Reset():
    global suite
    suite = []

    global etat
    etat = "TOUR IA"

    global iteration
    iteration = int(-1)
    IA()

    global avancée
    avancée = int(0)

def CreationBoutonJoueur():
    global boutonJaune
    global boutonBleu
    global boutonVert
    global boutonRouge
    
    # -- Bouton du haut (jaune)
    boutonJaune = CANVAS.create_rectangle(100,25,300,75, fill = "yellow")
    boutonBleu = CANVAS.create_rectangle(325,100,375,300, fill = "blue")
    boutonVert = CANVAS.create_rectangle(100,325,300,375, fill = "green")
    boutonRouge = CANVAS.create_rectangle(25,100,75,300, fill = "red")


def CreationIndicateurIA():
    global indicateur
    indicateur = Label(FENETRE,text = str("INDICATEUR"), width = 30, height = 2)
    indicateur.place(x=290,y=270)

def CreationLabelScore():
    global score
    score = int(0)

    global scoreLabel
    scoreLabel = Label(FENETRE,text = str(score), width = 30, height = 2)
    scoreLabel.place(x=290,y=300)



# Définition qui gère l'IA.

global iteration
iteration = int(0)

def AttendUnPeu():
    global indicateur
    indicateur.configure(text="")
    
    FENETRE.after(500, IA)

def IA():
    # On appelle plusieur fois cette méthode.
    # La première fois est juste pour anoncer que le défilement va commencer.
    # Puis cela continue jusqu'a la fin de la Liste.
    global indicateur

    global iteration

    global suite

    global etat

    if iteration == -1:
        etat = "TOUR IA"
        
        # Dans ce cas, on préviens le joueur de cela va commencer.
        indicateur.configure(text="Préparez-vous !",fg="black")

        # Et on ajoute aléatoirement une nouvelle couleur à la Liste.
        color = str("")
        i = randint(0,3)
        if i ==  0:
            color = "yellow"
        elif i == 1:
            color = "blue"
        elif i == 2:
            color = "green"
        else:
            color = "red"
        suite.append(color)
        
        iteration = iteration + 1
        FENETRE.after(3000, IA)

    elif iteration < len(suite):

        # On affiche la couleure à afficher
        indicateur.configure(text=suite[iteration],fg=suite[iteration])

        iteration = iteration + 1        
        FENETRE.after(650, AttendUnPeu)
    else :
        indicateur.configure(text="A vous !",fg="black")

        global avancée
        avancée = int(0)
        
        etat = "TOUR JOUEUR"

# Gestion des entrée.

def Press(couleur):
    global avancée
    global suite
    global indicateur

    bonneCouleur = suite[avancée]
    if couleur == bonneCouleur:
        avancée = avancée + 1
        indicateur.configure(text = "Bien - "+bonneCouleur+ " continuez")
        if avancée == len(suite):
            # Alors on a complété la suite.
            # On ajoute un au score et on continue

            global scoreLabel, score
            score = score + 1
            scoreLabel.configure(text=score)
            
            global iteration
            iteration = int(-1)            
            FENETRE.after(1000, IA)              
    else:
        avancée = int(0)
        indicateur.configure(text = "Perdu - recommencez")
        FENETRE.after(1000, Reset)
       
    

def Click(event):
    #print("X",event.x)
    #print("Y",event.y)
    
    x = event.x
    y = event.y

    global etat
    
    if etat == "TOUR JOUEUR":
        if 100 <= x <= 300 and 25 <= y <= 75:
            # Bouton Jaune appuyé
            Press("yellow")
        elif 325 <= x <= 375 and 100 <= y <= 300:
            # Bouton Bleu appuyé
            Press("blue")
        elif 100 <= x <= 300 and 325 <= y <= 375:
            # Bouton Vert appuyé
            Press("green")
        elif 25 <= x <= 75 and 100 <= y <= 300:
            # Bouton Rouge appuyé
            Press("red")
    

# - On met en place la fenetre tkinter.
FENETRE = Tk()
FENETRE.title("SIMON")
FENETRE.configure(width = 800, height = 600, bg = "white")

FENETRE.bind("<Button-1>", Click)

CANVAS = Canvas(FENETRE, width = 400, height = 400, bd = 0, bg = "white")
CANVAS.place(x=200,y=100)

CreationBoutonJoueur()
CreationIndicateurIA()
CreationLabelScore()

Reset()

# - On fait tourner la fenetre tkinter.
FENETRE.mainloop()
