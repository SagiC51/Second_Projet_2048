#####################################################################
# Docstring
#
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/Second_Projet_2048
#########################################

# ------------------------- Bibliothèques ------------------------- #
import copy
from secrets import choice
import tkinter as tk
import random as random

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 4
# ----------------------- Varaibles Globale ----------------------- #
Score = 0
Grille = []  # Grille
liste = []
Run = False
# ------------------------ Partie Fonction ------------------------ #


def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'  # A modifier


def grille():
    "Initialisation de notre grille et de la configuration Courante."
    global Grille, Run, Score
    # i et j nous permettent de gérer les coordonnées des points délimitants le
    # canvas
    Run = True
    Score = 0
    Grille = []  # Grille
    for i in range(0, N):
        intermediaire = []
        for j in range(1, N+1):
            xh = (j-1)*HEIGHT_CANVAS/N
            yh = i*HEIGHT_CANVAS/N
            xb = j*HEIGHT_CANVAS/N
            yb = (i+1)*WIDHT_CANVAS/N
            intermediaire.append(Canvas.create_rectangle(xh, yh, xb, yb,
                                                         fill=rgbtohex
                                                         (208, 193, 180),
                                                         outline=rgbtohex
                                                         (187, 173, 160),
                                                         width=10))
        Grille.append(intermediaire)
    print(Grille, "Grille")
    spawn()


def spawn():
    global Grille, liste
    liste = copy.deepcopy(Grille)
    for i in range(0, len(liste)):
        for j in range(0, len(liste)):
            liste[i][j] -= liste[i][j]
    for k in range(0, 2):
        aleat_x = random.randint(0, len(liste)-1)
        aleat_y = random.randint(0, len(liste)-1)
        if liste[aleat_x][aleat_y] == 0:
            Liste_sapwn_tuile = [2, 4]
            Nbr = choice(Liste_sapwn_tuile)
            liste[aleat_x][aleat_y] = Nbr
            xh = (aleat_y)*HEIGHT_CANVAS/N
            yh = aleat_x*HEIGHT_CANVAS/N
            xb = (aleat_y+1)*HEIGHT_CANVAS/N
            yb = (aleat_x+1)*WIDHT_CANVAS/N
            Grille.append(Canvas.create_rectangle(xh, yh, xb, yb,
                                                  fill=rgbtohex(238, 228, 218),
                                                  outline=rgbtohex
                                                  (187, 173, 160),
                                                  width=10))
            Grille.append(Canvas.create_text((xh+xb)//2,
                          (yb+yh)//2, text=str(Nbr),
                          fill=rgbtohex(120, 111, 102),
                          font=("arial black", 30)))
        else:
            print("ERREUR")
    print(liste, 'liste_1')
    return


def Up():
    """"Fonction lier au bouton Haut """
    pass


def Down():
    """"Fonction lier au bouton Bas """
    pass


def Left():
    """"Fonction lier au bouton Gauche """
    pass


def Right():
    """"Fonction lier au bouton Droite """
    pass


def End():
    """"Fonction lier au bouton Exit """
    global Run, Score
    Run = False
    Canvas.itemconfigure(Label_Valeur_Score, text=str(Score))


def Save():
    global liste
    """"Fonction lier au bouton Sauvegarder
    elle permet de sauvgarder un la dernier liste"""
    fic = open("Save", "w")
    for i in range(0, N):
        for j in range(0, N):
            fic.write(str(liste[i][j])+"\n")
    fic.close()
    print(liste, "save")


def Load():
    global liste
    """"Fonction lier au bouton Charger
    elle peurmet de charger la liste sauvgarder dans le fichier save"""
    fic = open("Save", "r")
    Grille_S = []
    for i in range(N):
        Grille_S.append([0]*N)
    for line in fic:
        for i in range(0, N):
            for j in range(0, N):
                Grille_S[i][j] = int(line)
                line = fic.readline()
    fic.close()
    liste = Grille_S
    print(liste, "Load")


def Calcul():
    """"Fonction qui gère les movement sur la grille """
    pass

# ------------------------ Code Principale ------------------------ #


racine = tk.Tk()
# Parrametre de la racine et Canvas
racine.title("2048")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)


# Bouttons
Bouton_Play = tk.Button(text='Play', command=grille)
Bouton_Exit = tk.Button(text="Exit", command=End)
Bouton_Save = tk.Button(text="Sauvegarder", command=Save)
Bouton_Load = tk.Button(text="Charger", command=Load)
Bouton_Up = tk.Button(text="Haut", command=Up)
Bouton_Down = tk.Button(text="Bas", command=Down)
Bouton_Right = tk.Button(text="Droite", command=Right)
Bouton_Left = tk.Button(text="Gauche", command=Left)

# Label
Label_Score = tk.Label(text="Score :", foreground="Black", font="Arial 10")
Label_Valeur_Score = tk.Label(text=str(Score), foreground="Blue",
                              font="Arial 10")


# Placement des éléments
Label_Score.grid(row=0, column=1, columnspan=1)
Label_Valeur_Score.grid(row=0, column=2, columnspan=1)
Canvas.grid(row=1, column=1, columnspan=1, rowspan=5)
Bouton_Play.grid(row=2, column=0)
Bouton_Exit.grid(row=3, column=0)
Bouton_Save.grid(row=4, column=0)
Bouton_Load.grid(row=5, column=0)
Bouton_Up.grid(row=2, column=4)
Bouton_Down.grid(row=3, column=4)
Bouton_Right.grid(row=3, column=3)
Bouton_Left.grid(row=3, column=5)

# mainloop
racine.mainloop()

# ----------------------- Fin du programme  ----------------------- #
