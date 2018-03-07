from tkinter import *
from random import *

global suite
# Liste qui regroupe les couleurs à jouer dans le bon ordre.
suite = []


# ----- PARTIE AFFICHAGE ET RESET -----

# Fonction qui remet à zéro le jeu.
# Quand on lance le programme ou lorsque l'on perd.
def Reset():

    # On reset la suite de couleurs.
    global suite
    suite = []

    # On définit l'état du jeu sur "TOUR IA"
    # Pour que le joueur ne puisse pas casser le jeu
    global etat
    etat = "TOUR IA"

    # On reset l'avancée du joueur
    # Pour remettre à zéro et reprendre du début.
    global avancée
    avancée = int(0)

    # On définit l'itération sur -1.
    # L'itération est la variable qui aide l'IA.
    global iteration
    iteration = int(-1)

    # Et on appelle l'IA pour commencer une suite de couleur.
    IA()


# Fonction qui créer les rectangles qui font office de boutons pour le joueur.
def CreationBoutonJoueur():
    # On enregistre les rectangles dans des variables globales si on veut les modifier plus tard.
    global boutonJaune
    global boutonBleu
    global boutonVert
    global boutonRouge
    
    # -- Bouton du haut (jaune)
    boutonJaune = CANVAS.create_rectangle(100,25,300,75, fill = "yellow")
    
    # -- Bouton de droite (bleu)
    boutonBleu = CANVAS.create_rectangle(325,100,375,300, fill = "blue")
    
    # -- Bouton du bas (vert)
    boutonVert = CANVAS.create_rectangle(100,325,300,375, fill = "green")
    
    # -- Bouton de gauche (rouge)
    boutonRouge = CANVAS.create_rectangle(25,100,75,300, fill = "red")


# Fonction qui créer le Label qui nous indique l'état du jeu
# Il va afficher la suite de couleurs, nous dire quand c'est au tour du joueur, quand la suite va commencer, etc...
def CreationIndicateurIA():
    # Pour pouvoir modifier le texte, on est obligés de l'enregistrer dans une variable globale.
    global indicateur
    indicateur = Label(FENETRE,text = str("INDICATEUR"), width = 30, height = 2)
    indicateur.place(x=290,y=270)


# Fonction qui créer le Label qui affiche le score du joueur.
# Le score augmente de 1 à chaque fois que le joueur réussi une suite complete.
def CreationLabelScore():
    # De même que pour l'indicateur, on doit renseigner ces deux valeurs dans des variables globales.
    global score
    score = int(0)

    global scoreLabel
    scoreLabel = Label(FENETRE,text = str(score), width = 30, height = 2)
    scoreLabel.place(x=290,y=300)



# ----- PARTIE IA -----

# C'est ici qu'est initialisée la variable iteration.
global iteration
iteration = int(0)

# Fonction qui permet d'afficher un blanc entre chaque couleur de la suite.
# Pour permettre au joueur de savoir si une couleure est présente deux fois de suite dans la suite.
def AttendUnPeu():
    # On reset le text de l'indicateur.
    global indicateur
    indicateur.configure(text="")

    # On continue la fonction IA, dans 500 milisecondes (une demi seconde)
    FENETRE.after(500, IA)

# Fonction qui gère l'IA en fonction de la valeur de la variable iteration.
# Cette fonction va être appellée plusieur fois de suite avant que cela ne soit au tour du joueur.
def IA():

    # On commence par appeller toutes les variables globales qui seront utiles.
    global indicateur
    global iteration
    global suite
    global etat

    # Lorsque cette fonction est appellée au début du jeu, ou après le tour du joueur,
    # la variable iteration vaut -1.
    # On effecturas donc la première boucle.
    if iteration == -1:

        # En premier, on empêche le joueur d'interargir avec les boutons,
        # en définissant l'état du jeu par "TOUR IA"
        # Elle peut déjà avoir cette valeur si la fonction Reset a été appelée juste avant.
        etat = "TOUR IA"
        
        # On modifie le text de l'indicateur pour prévenir le joueur que la suite va commencer.
        indicateur.configure(text="Préparez-vous !",fg="black")



        # On ajoute aléatoirement une nouvelle couleur à la Liste.
        # Pour ce faire, on prend une variable temporaire nommée "color" vide.
        color = str("")

        # On définit une variable aléatoire en 0 et 3 compris.
        # En fonction de cette valeur, on ajoute une couleur à la Liste.
        i = randint(0,3)
        
        if i ==  0:
            # Si i = 0, alors on ajoute à la liste la couleur jaune.
            color = "yellow"
        elif i == 1:
            # Si i = 1, alors on ajoute à la liste la couleur bleu.
            color = "blue"
        elif i == 2:
            # Si i = 2, alors on ajoute à la liste la couleur vert.
            color = "green"
        else:
            # Sinon (si i = 3), alors on ajoute à la liste la couleur rouge.
            color = "red"

        # Et on ajoute la valeur de la variable temporaire "color" à la suite.
        suite.append(color)

        # Si les termes de couleur sont en anglais, c'est pour pouvoir modifier la couleur de l'indicateur.

        # On ajoute 1 à la valeur de l'iteration pour pouvoir passer à l'étape suivante.        
        iteration = iteration + 1

        # Puis réappelle la fonction IA dans 3000 milisecondes (3 secondes)
        FENETRE.after(3000, IA)

        # Du point de vue du joueur, il verra le message "Préparez-vous !" s'afficher en noir pendant 3 secondes.

    # La seconde fois que cette fonction est appelée, iteration vaut 0 (-1 + 1 = 0).
    # Dans tout les cas, il y a au moins une couleur dans la liste car on est passé par l'étape précédente.
    # On va donc passer par cette boucle.
    elif iteration < len(suite):

        # Tant qu'il restera des couleur à afficher dans la liste, on refera cette boucle.

        # On affiche la couleure à afficher.
        indicateur.configure(text=suite[iteration],fg=suite[iteration])

        # On ajoute 1 à iteration.
        iteration = iteration + 1

        # On ne réappelle pas directement la fonction IA.
        # Mais on appelle celle qui donne un pause au joueur (juste au dessus de la fonction IA).
        FENETRE.after(650, AttendUnPeu)


    # Enfin, si iteration vaut le nombre de couleur dans la liste, c'est au tour du joueur.
    # On appliquera cette boucle et on réappellera la fonction IA lorsque le joueur aura fini ou se sera trompé.
    else :
        # On configure l'indicateur pour que le joueur sache que cela est son tour.
        indicateur.configure(text="A vous !",fg="black")

        # On reset l'avancée du joueur pour éviter les bugs possibles.
        global avancée
        avancée = int(0)

        # Et on permet au joueur d'utiliser les boutons.
        etat = "TOUR JOUEUR"



# ----- PARTIE JOUEUR ET GESTION DES ENTREES -----

# Fonction qui est indirectement appellée lorsque le joueur a clické sur un bouton.
def Press(couleur):
    # Comme toujours, on appelle les variables globales qui sont utiles.
    global avancée
    global suite
    global indicateur
    global etat

    # On a besoin d'une variable qui nous dise quelle est la bonne couleur à utiliser.
    bonneCouleur = suite[avancée]

    # Si la couleur choisie est la bonne, ...
    if couleur == bonneCouleur:

        # ... alors on ajoute un a l'avancée, ...
        avancée = avancée + 1

        # ... on confirme au joueur qu'il a bien choisi sa couleur, ...
        indicateur.configure(text = "Bien - "+bonneCouleur+ " continuez")

        # ... et on vérifie si le joueur à fini la suite.
        if avancée == len(suite):
            # Dans ce cas, on ajoute un au score.
            global scoreLabel, score
            score = score + 1
            scoreLabel.configure(text=score)

            # On reset l'iteration sur -1 et on réappelle la fonction de l'IA.
            global iteration
            iteration = int(-1)            
            FENETRE.after(1000, IA)              

    # Si ce n'est pas la bonne couleur, ...
    else:
        # On reset l'avancée.
        avancée = int(0)

        # On previens le joueur qu'il a perdu.
        indicateur.configure(text = "Perdu - recommencez")

        # on l'empêche de cliquer partout.
        etat = "TOUR IA"

        # Et on appelle la fonction Reset 1000 miliseconde splus tard (1 seconde).
        FENETRE.after(1000, Reset)
       
    

# Fonction qui est appelée lorsque le joueur clique quelque part.
def Click(event):

    # On peut utiliser ces prints pour obtenir les coordonnées du click.
    #print("X",event.x)
    #print("Y",event.y)

    # On enregistre les coordonnées du click pour y acceder plus facilement.
    x = event.x
    y = event.y

    # On appelle la seule variable globale dont on a besoin.
    global etat

    # C'est ici qu'intervient la variable etat:
    # On analyse  le click seulement si elle vaut "TOUR JOUEUR".
    # C'est pour cela qu'on empêche le joueur de jouer en la définissant sur "TOUR IA".
    # Dans la pratique, on l'en empêche tant que la variable ne vaut pas "TOUR JOUEUR".
    if etat == "TOUR JOUEUR":

        # On sait sur quel bouton le joueur à appuyer en fonction de ces coordonnées
        # On appelle alors la Fonction Press juste au dessus.
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
    

# ----- PARTIE TKINTER -----

# On met en place la fenetre tkinter.
FENETRE = Tk()
FENETRE.title("SIMON")
FENETRE.configure(width = 800, height = 600, bg = "white")

# On attribue la clique gauche de la souris à la fonction qui analyse les clicks.
FENETRE.bind("<Button-1>", Click)

# On setup le Canvas.
CANVAS = Canvas(FENETRE, width = 400, height = 400, bd = 0, bg = "white")
CANVAS.place(x=200,y=100)

# On appelle les fonctions d'affichages.
CreationBoutonJoueur()
CreationIndicateurIA()
CreationLabelScore()

# On Reset et commence le jeu.
Reset()

# Et on fait tourner la fenetre tkinter.
FENETRE.mainloop()
