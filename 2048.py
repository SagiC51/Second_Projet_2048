#####################################################################
# Docstring
# groupe MPCI TD1
# CHRISTOPHE Passcal
# CHAKROUN Mohammed
# KALI-A-NGOUELE Gloire
# https://github.com/uvsq21918050/Second_Projet_2048
#########################################

# ------------------------- Bibliothèques ------------------------- #
import numpy as np
import math
from secrets import choice
import tkinter as tk
import random as rd
import copy

def rgb(r,g,b):
     return f'#{r:02x}{g:02x}{b:02x}' 

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 400
N = 4
n = 2
xh = HEIGHT_CANVAS/N
yh = HEIGHT_CANVAS/N
xb = HEIGHT_CANVAS/N
yb =WIDHT_CANVAS/N
Liste_sapwn_tuile = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
Liste_couleur = [rgb(187,173,160), rgb(238,228,218), rgb(231,216,191), rgb(237,173,118), rgb(235,145,94), rgb(240,118,90), 
                 rgb(231,95,67), rgb(231,201,114), rgb(239,204,99), rgb(230,194,64), rgb(230,192,68), rgb(229,190,45)]
liste_nombre = [2**n for n in range(1,15)]
Score = 0
grille = []
grille_tuile = []
grille_nbr = []
nbr_aleat = choice(Liste_sapwn_tuile)
liste_tuile = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
event = True
event_classique = False
event4d = False
grille1 = []  
grille2 = []
grille3 = []
grille4 = []
liste_tuile1 = np.array([[0,0],[0,0]])
liste_tuile2 = np.array([[0,0],[0,0]])
liste_tuile3 = np.array([[0,0],[0,0]])
liste_tuile4 = np.array([[0,0],[0,0]])
liste_tuile4D = [liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4]
eventhard = False
def Classique():
    """
    Initialisation de notre grille.
    """
    global Score, grille, event, grille_tuile, liste_tuile, grille_nbr, nbr_aleat, event_classique, event4d
    event_classique = True
    event4d = False
    if event_classique == True:
        if event == False:
            Bouton_replay.destroy()
            game_over.destroy()
        #Réinitialisation des variables globales 
        Score = 0
        grille = []  # grille
        grille_tuile = []
        grille_nbr = []
        liste_tuile = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        event = True
        nbr_aleat = choice(Liste_sapwn_tuile)
        maj_score()
        #Création de la grille
        grille = []
        for i in range(0, N):
            intermediaire = []
            for j in range(1, N+1):
                intermediaire.append(canvas.create_rectangle((j-1)*xh, i*yh, j*xb, (i+1)*yb,
                                                    fill=rgb(208,193,180), outline=Liste_couleur[0], width=10))
            grille.append(intermediaire)
        #Création de deux tuiles: 2 ou 4 
        for i in range(0,2):
            spawn_tuile()
            maj()
    return

def Secondmode():
    """
    Initialisation de notre grille.
    """
    global Score, grille1, grille2, grille3, grille4, event, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, liste_tuile4D, nbr_aleat, event_classique, event4d
    event_classique = False
    event4d = True
    if event4d == True:
        if event == False:
            Bouton_replay.destroy()
            game_over.destroy()
        #Réinitialisation des variables globales 
        Score = 0
        grille1 = []  
        grille2 = []
        grille3 = []
        grille4 = []
        liste_tuile1 = np.array([[0,0],[0,0]])
        liste_tuile2 = np.array([[0,0],[0,0]])
        liste_tuile3 = np.array([[0,0],[0,0]])
        liste_tuile4 = np.array([[0,0],[0,0]])
        liste_tuile4D = [liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4]
        event = True
        nbr_aleat = choice(Liste_sapwn_tuile)
        #Création de la grille
        #On crée une grille correspondante au second mode de jeu
        #Chaque boucle correspond à une grille
        # 1ere bouvle: coin sup gauche 
        for i in range(0,n):
            intermediaire = []
            for j in range(0,n):
                intermediaire.append(canvas.create_rectangle(i*xh-5, j*yh-5, (i+1)*xh-5, (j+1)*yh-5 , fill=rgb(208,193,180), outline=Liste_couleur[0], width=10))
            grille1.append(intermediaire)
        #2eme boucle: coin sup droit
        for i in range(n,N):
            intermediaire = []
            for j in range(0,n):
                intermediaire.append(canvas.create_rectangle(i*xh+5, j*yh-5, (i+1)*xh+5, (j+1)*yh-5 , fill=rgb(208,193,180), outline=Liste_couleur[0], width=10))    
            grille2.append(intermediaire)
        #3eme boucle: coin inf gauche
        for i in range(0,n):
            intermediaire = []
            for j in range(n,N):
                intermediaire.append(canvas.create_rectangle(i*xh-5, j*yh+5, (i+1)*xh-5, (j+1)*yh+5 , fill=rgb(208,193,180), outline=Liste_couleur[0], width=10))    
            grille3.append(intermediaire)
        #4eme boucle: coin inf droit
        for i in range(n,N):
            intermediaire = []
            for j in range(n,N):
                intermediaire.append(canvas.create_rectangle(i*xh+5, j*yh+5, (i+1)*xh+5, (j+1)*yh+5 , fill=rgb(208,193,180), outline=Liste_couleur[0], width=10))
            grille4.append(intermediaire)
        canvas.create_line(WIDHT_CANVAS//2, 0, WIDHT_CANVAS//2, HEIGHT_CANVAS, fill=Liste_couleur[0], width=20)
        canvas.create_line(0, HEIGHT_CANVAS//2, WIDHT_CANVAS, HEIGHT_CANVAS//2, fill=Liste_couleur[0], width=20)
        spawn_tuile()
        maj()
    return

def tuile(x, y):
    """Création des tuiles : fond + chiffre"""
    global grille_nbr, nbr_aleat, liste_tuile, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4
    if event_classique == True:
        if liste_tuile[x][y] == 2:  
        #Création du fond de la tuile 
            grille_tuile.append(canvas.create_rectangle(y*xh, x*yh, (y+1)*xb, (x+1)*yb,
                                                fill=Liste_couleur[1],
                                                outline=Liste_couleur[0], width=10
                                                ))
        else:
            grille_tuile.append(canvas.create_rectangle(y*xh, x*yh, (y+1)*xb, (x+1)*yb,
                                                fill=Liste_couleur[2],
                                                outline=Liste_couleur[0], width=10
                                                ))
        #Création du chiffre sur la tuile   
        grille_nbr.append(canvas.create_text((y*(xh+xb)+xb)//2, (x*(yb+yh)+yh)//2,
                                            text=str(liste_tuile[x][y]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
    elif event4d == True:
        for tuile in liste_tuile4D:
            if tuile[x][y] == 2:  
            #Création du fond de la tuile 
                grille_tuile.append(canvas.create_rectangle(y*xh, x*yh, (y+1)*xb, (x+1)*yb,
                                                    fill=Liste_couleur[1],
                                                    outline=Liste_couleur[0], width=10
                                                    ))
            else:
                grille_tuile.append(canvas.create_rectangle(y*xh, x*yh, (y+1)*xb, (x+1)*yb,
                                                    fill=Liste_couleur[2],
                                                    outline=Liste_couleur[0], width=10
                                                    ))
            #Création du chiffre sur la tuile   
            grille_nbr.append(canvas.create_text((y*(xh+xb)+xb)//2, (x*(yb+yh)+yh)//2,
                                                text=str(tuile[x][y]), 
                                                fill=rgb(120,111,102), 
                                                font=("arial black", 30))
                                                )
    return

def maj():
    global grille_nbr, grille_tuile, liste_tuile, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event4d, event_classique
    if event_classique == True:
        for elmnt in grille_tuile:
            canvas.delete(elmnt)
        for elmnt in grille_nbr:
            canvas.delete(elmnt)
        grille_tuile=[]
        grille_nbr=[]
        for i in range(0, len(liste_tuile)):
            for j in range(0, len(liste_tuile)):
                for k in range(1, 3):
                    if liste_tuile[i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh, i*yh, (j+1)*xb, (i+1)*yb,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb)+xb)//2, (i*(yb+yh)+yh)//2,
                                            text=str(liste_tuile[i][j]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
                for k in range(3, 20):
                    if liste_tuile[i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh, i*yh, (j+1)*xb, (i+1)*yb,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb)+xb)//2, (i*(yb+yh)+yh)//2,
                                            text=str(liste_tuile[i][j]), 
                                            fill='white', 
                                            font=("arial black", 30))
                                        )
    elif event4d == True:
        for elmnt in grille_tuile:
            canvas.delete(elmnt)
        for elmnt in grille_nbr:
            canvas.delete(elmnt)
        grille_tuile=[]
        grille_nbr=[]
        for i in range(0, n):
            for j in range(0, n):
                for k in range(1, 3):
                    #1ere grille
                    if liste_tuile4D[0][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh-5, i*yh-5, (j+1)*xb-5, (i+1)*yb-5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb-5)+xb-5)//2, (i*(yb+yh-5)+yh-5)//2,
                                            text=str(liste_tuile4D[0][i][j]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
                    #2eme grille
                    if liste_tuile4D[1][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle((j+2)*xh+5, i*yh-5, (j+3)*xb+5, (i+1)*yb-5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text(((j+2)*(xh+xb+5)+xb+5)//2, (i*(yb+yh-5)+yh-5)//2,
                                            text=str(liste_tuile4D[1][i][j]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
                    #3eme grille
                    if liste_tuile4D[2][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh-5, (i+2)*yh+5, (j+1)*xb-5, (i+3)*yb+5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb-5)+xb-5)//2, ((i+2)*(yb+yh+5)+yh+5)//2,
                                            text=str(liste_tuile4D[2][i][j]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
                    #4eme grille
                    if liste_tuile4D[3][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle((j+2)*xh+5, (i+2)*yh+5, (j+3)*xb+5, (i+3)*yb+5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text(((j+2)*(xh+xb+5)+xb+5)//2, ((i+2)*(yb+yh+5)+yh+5)//2,
                                            text=str(liste_tuile4D[3][i][j]), 
                                            fill=rgb(120,111,102), 
                                            font=("arial black", 30))
                                            )
                for k in range(3, 20):
                    #1ere grille
                    if liste_tuile4D[0][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh-5, i*yh-5, (j+1)*xb-5, (i+1)*yb-5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb-5)+xb-5)//2, (i*(yb+yh-5)+yh-5)//2,
                                            text=str(liste_tuile4D[0][i][j]), 
                                            fill='white', 
                                            font=("arial black", 30))
                                            )
                    #2eme grille
                    if liste_tuile4D[1][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle((j+2)*xh+5, i*yh-5, (j+3)*xb+5, (i+1)*yb-5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text(((j+2)*(xh+xb+5)+xb+5)//2, (i*(yb+yh-5)+yh-5)//2,
                                            text=str(liste_tuile4D[1][i][j]), 
                                            fill='white', 
                                            font=("arial black", 30))
                                            )
                    #3eme grille
                    if liste_tuile4D[2][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle(j*xh-5, (i+2)*yh+5, (j+1)*xb-5, (i+3)*yb+5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text((j*(xh+xb-5)+xb-5)//2, ((i+2)*(yb+yh+5)+yh+5)//2,
                                            text=str(liste_tuile4D[2][i][j]), 
                                            fill='white', 
                                            font=("arial black", 30))
                                            )
                    #4eme grille
                    if liste_tuile4D[3][i][j] == 2**k:
                        grille_tuile.append(canvas.create_rectangle((j+2)*xh+5, (i+2)*yh+5, (j+3)*xb+5, (i+3)*yb+5,
                                                fill=Liste_couleur[k],
                                                outline=Liste_couleur[0], width=10
                                                ))
                        grille_nbr.append(canvas.create_text(((j+2)*(xh+xb+5)+xb+5)//2, ((i+2)*(yb+yh+5)+yh+5)//2,
                                            text=str(liste_tuile4D[3][i][j]), 
                                            fill='white', 
                                            font=("arial black", 30))
                                            )
    return

def spawn_tuile():
    """Fait apparaitre les tuiles à des positions aléatoires"""
    global liste_tuile, event, liste_tuile4D, liste_nbr, nbr_aleat, event, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event4d, event_classique
    if event_classique == True:
        if eventhard == False:
            if 0 in liste_tuile and event == True:
                nbr_aleat = choice(Liste_sapwn_tuile)
                #Modification de la liste qui contient la position des tuiles 
                spawnx = rd.randint(0, len(liste_tuile)-1)
                spawny = rd.randint(0, len(liste_tuile)-1)
                pos_aleat = liste_tuile[spawnx][spawny]
                while pos_aleat != 0:
                    spawnx = rd.randint(0, len(liste_tuile)-1)
                    spawny = rd.randint(0, len(liste_tuile)-1)
                    pos_aleat = liste_tuile[spawnx][spawny]
                if liste_tuile[spawnx][spawny] == 0:
                    liste_tuile[spawnx][spawny] += nbr_aleat
        # elif eventhard == True:
        #     for i in range(1, len(liste_tuile)-1):
        #         for j in range(1, len(liste_tuile)-1):
        #             if liste_tuile[i][j] == max(liste_tuile[i]):
        #                 nbr_aleat = choice(Liste_sapwn_tuile)
        #                 if liste_tuile[i-1][j] == 0 :
        #                     liste_tuile[i-1][j] += nbr_aleat
        #                     break
        #                 elif liste_tuile[i+1][j] == 0:
        #                     liste_tuile[i+1][j] += nbr_aleat
        #                     break
        #                 elif liste_tuile[i][j+1] == 0:
        #                     liste_tuile[i][j+1] += nbr_aleat
        #                     break
        #                 elif liste_tuile[i][j-1] == 0:
        #                     liste_tuile[i][j-1] += nbr_aleat
        #                     break
        #                 break
        # elif 0 in liste_tuile and event == True:
        #     nbr_aleat = choice(Liste_sapwn_tuile)
        #     #Modification de la liste qui contient la position des tuiles 
        #     spawnx = rd.randint(0, len(liste_tuile)-1)
        #     spawny = rd.randint(0, len(liste_tuile)-1)
        #     pos_aleat = liste_tuile[spawnx][spawny]
        #     while pos_aleat != 0:
        #         spawnx = rd.randint(0, len(liste_tuile)-1)
        #         spawny = rd.randint(0, len(liste_tuile)-1)
        #         pos_aleat = liste_tuile[spawnx][spawny]
        #     if liste_tuile[spawnx][spawny] == 0:
        #         liste_tuile[spawnx][spawny] += nbr_aleat
    elif event4d == True:
        for tuile in liste_tuile4D:
            if 0 in tuile and event == True:
                nbr_aleat = choice(Liste_sapwn_tuile)
                spawnx = rd.randint(0, len(tuile)-1)
                spawny = rd.randint(0, len(tuile)-1)
                pos_aleat = tuile[spawnx][spawny]
                while pos_aleat != 0:
                    spawnx = rd.randint(0, len(tuile)-1)
                    spawny = rd.randint(0, len(tuile)-1)
                    pos_aleat = tuile[spawnx][spawny]
                if tuile[spawnx][spawny] == 0:
                    tuile[spawnx][spawny] += nbr_aleat
    return

def maj_score():
    global liste_tuile, Score, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event4d, event_classique
    if event_classique == True:
        Score = 0
        for i in range(0, len(liste_tuile)):
            for j in range(0, len(liste_tuile)):
                Score += liste_tuile[i][j]
        Label_Valeur_Score.configure(text=str(Score))
    elif event4d == True:
        Score = 0
        for tuile in liste_tuile4D:
            for i in range(0, len(tuile)):
                for j in range(0, len(tuile)):
                    Score += tuile[i][j]
        Label_Valeur_Score.configure(text=str(Score))
    return Score

def Up():
    """"Fonction lier au bouton Bas """
    global Score, liste_tuile, grille_tuile, grille_nbr, event, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event_classique, event4d
    #On modifie la liste associée aux tuiles
    if event_classique == True:
        #MOVE_TUILE
        if event == True:
            L=copy.deepcopy(liste_tuile)    
            for i in range(0, len(liste_tuile)):
                for j in range(0, len(liste_tuile)):
                    if liste_tuile[i][j] != 0:              
                        val = liste_tuile[i][j]
                        for k in range(0,i):
                            if liste_tuile[k][j] == 0:
                                liste_tuile[i][j] = 0
                                liste_tuile[k][j] = val
                                break
            #FUSION
            for i in range(0,len(liste_tuile)-1):
                for j in range(0, len(liste_tuile)):
                    if liste_tuile[i+1][j] == liste_tuile[i][j] and liste_tuile[i][j] != 0: 
                        if i == 0:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i+1][j] = liste_tuile[i+2][j]
                            liste_tuile[i+2][j] = liste_tuile[i+3][j]
                            liste_tuile[i+3][j] = 0
                            break                                                                                       
                        elif i == 1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i+1][j] = liste_tuile[i+2][j]
                            liste_tuile[i+2][j] = 0
                            break
                        elif i == 2:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i+1][j] = 0
                            break
            #On regarde si l'on peut faire spawn une tuile ou non ie on regarde si la liste finale est égale à la liste initiale ou non
            compteur = 0
            for i in range(0,len(liste_tuile)):
                for j in range(0,len(liste_tuile)):
                    if L[i][j] == liste_tuile[i][j]:
                        compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()

    elif event4d == True:
        if event == True:
            for tuile in liste_tuile4D:
                L=copy.deepcopy(tuile)    
                for i in range(0, len(tuile)):
                    for j in range(0, len(tuile)):
                        if tuile[i][j] != 0:              
                            val = tuile[i][j]
                            for k in range(0,i):
                                if tuile[k][j] == 0:
                                    tuile[i][j] = 0
                                    tuile[k][j] = val
                                    break
                for i in range(0,len(tuile)-1):
                    for j in range(0, len(tuile)):
                        if tuile[i+1][j] == tuile[i][j] and tuile[i][j] != 0: 
                            if i == 0:
                                tuile[i][j] *= 2
                                tuile[i+1][j] = 0
                                break            
                compteur = 0
                for i in range(0,len(tuile)):
                    for j in range(0,len(tuile)):
                        if L[i][j] == tuile[i][j]:
                            compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()

def Down():
    """"Fonction lier au bouton Bas """
    global Score, liste_tuile, grille_tuile, grille_nbr, event, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event_classique, event4d
    if event_classique == True:
        if event == True:
            L=copy.deepcopy(liste_tuile)
            #On modifie la liste associée aux tuiles                   
            for i in range(len(liste_tuile)-1, -1, -1):
                for j in range(0, len(liste_tuile)):
                    if liste_tuile[i][j] != 0:      
                        val = liste_tuile[i][j]
                        for k in range(len(liste_tuile)-1,i,-1):
                                if liste_tuile[k][j] == 0:
                                    liste_tuile[i][j] = 0
                                    liste_tuile[k][j] = val
                                    break
            for i in range(len(liste_tuile)-1, -1,-1):
                for j in range(0, len(liste_tuile)):
                    if liste_tuile[i-1][j] == liste_tuile[i][j] and liste_tuile[i][j] != 0: 
                        if i == len(liste_tuile)-1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i-1][j] = liste_tuile[i-2][j]
                            liste_tuile[i-2][j] = liste_tuile[i-3][j]
                            liste_tuile[i-3][j] = 0
                            break                                                                                       
                        elif i == 2:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i-1][j] = liste_tuile[i-2][j]
                            liste_tuile[i-2][j] = 0
                            break
                        elif i == 1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i-1][j] = 0
                            break
            compteur = 0
            for i in range(0,len(liste_tuile)):
                for j in range(0,len(liste_tuile)):
                    if L[i][j] == liste_tuile[i][j]:
                        compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()

    elif event4d == True:
        if event == True:
            for tuile in liste_tuile4D:
                L=copy.deepcopy(tuile)
                for i in range(len(tuile)-1, -1, -1):
                    for j in range(0, len(tuile)):
                        if tuile[i][j] != 0:      
                            val = tuile[i][j]
                            for k in range(len(tuile)-1,i,-1):
                                    if tuile[k][j] == 0:
                                        tuile[i][j] = 0
                                        tuile[k][j] = val
                                        break
                for i in range(len(tuile)-1, -1,-1):
                    for j in range(0, len(tuile)):
                        if tuile[i-1][j] == tuile[i][j] and tuile[i][j] != 0: 
                            tuile[i][j] *= 2
                            tuile[i-1][j] = 0
                            break                                                                                       
                compteur = 0
                for i in range(0,len(tuile)):
                    for j in range(0,len(tuile)):
                        if L[i][j] == tuile[i][j]:
                            compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()
    return

def Left():
    """"Fonction lier au bouton Gauche """
    global Score, liste_tuile, grille_tuile, grille_nbr, event, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event_classique, event4d
    if event_classique == True:
        if event == True:
            L=copy.deepcopy(liste_tuile)
            #On modifie la liste associée aux tuiles
            for i in range(0, len(liste_tuile)):
                for j in range(0, len(liste_tuile)):
                    if liste_tuile[i][j] != 0:              
                        val = liste_tuile[i][j]
                        for k in range(0,j):
                            if liste_tuile[i][k] == 0:
                                liste_tuile[i][j] = 0
                                liste_tuile[i][k] = val
                                break
            for i in range(0,len(liste_tuile)):
                for j in range(0, len(liste_tuile)-1):
                    if liste_tuile[i][j+1] == liste_tuile[i][j] and liste_tuile[i][j] != 0: 
                        if j == 0:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j+1] = liste_tuile[i][j+2]
                            liste_tuile[i][j+2] = liste_tuile[i][j+3]
                            liste_tuile[i][j+3] = 0
                            break                                                                                       
                        elif j == 1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j+1] = liste_tuile[i][j+2]
                            liste_tuile[i][j+2] = 0
                            break
                        elif j == 2:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j+1] = 0
                            break
            compteur = 0
            for i in range(0,len(liste_tuile)):
                for j in range(0,len(liste_tuile)):
                    if L[i][j] == liste_tuile[i][j]:
                        compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()
    elif event4d == True:
        if event == True:
            for tuile in liste_tuile4D:
                L=copy.deepcopy(tuile)
                for i in range(0, len(tuile)):
                    for j in range(0, len(tuile)):
                        if tuile[i][j] != 0:              
                            val = tuile[i][j]
                            for k in range(0,j):
                                if tuile[i][k] == 0:
                                    tuile[i][j] = 0
                                    tuile[i][k] = val
                                    break
                for i in range(0,len(tuile)):
                    for j in range(0, len(tuile)-1):
                        if tuile[i][j+1] == tuile[i][j] and tuile[i][j] != 0: 
                            if j == 0:
                                tuile[i][j] *= 2
                                tuile[i][j+1] = 0
                                break                                                                                       
                compteur = 0
                for i in range(0,len(tuile)):
                    for j in range(0,len(tuile)):
                        if L[i][j] == tuile[i][j]:
                            compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()
    return

def Right():
    """"Fonction lier au bouton Droite """
    global Score, liste_tuile, grille_tuile, grille_nbr, event, liste_tuile4D, liste_tuile1, liste_tuile2, liste_tuile3, liste_tuile4, event_classique, event4d
    if event_classique == True:
        if event == True:
            L=copy.deepcopy(liste_tuile)
            #On modifie la liste associée aux tuiles
            for i in range(0, len(liste_tuile)):
                for j in range(len(liste_tuile)-1, -1, -1):
                    if liste_tuile[i][j] != 0:        #1 , 0      
                        val = liste_tuile[i][j]
                        for k in range(len(liste_tuile)-1,j,-1):
                                if liste_tuile[i][k] == 0:
                                    liste_tuile[i][j] = 0
                                    liste_tuile[i][k] = val
                                    break
            for i in range(0, len(liste_tuile)):
                for j in range(len(liste_tuile)-1, -1,-1):
                    if liste_tuile[i][j-1] == liste_tuile[i][j] and liste_tuile[i][j] != 0: 
                        if j == len(liste_tuile)-1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j-1] = liste_tuile[i][j-2]
                            liste_tuile[i][j-2] = liste_tuile[i][j-3]
                            liste_tuile[i][j-3] = 0
                            break                                                                                       
                        elif j == 2:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j-1] = liste_tuile[i][j-2]
                            liste_tuile[i][j-2] = 0
                            break
                        elif j == 1:
                            liste_tuile[i][j] *= 2
                            liste_tuile[i][j-1] = 0
                            break
            compteur = 0
            for i in range(0,len(liste_tuile)):
                for j in range(0,len(liste_tuile)):
                    if L[i][j] == liste_tuile[i][j]:
                        compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score()

    elif event4d == True:   
        if event == True:
            for tuile in liste_tuile4D:
                L=copy.deepcopy(tuile)
                for i in range(0, len(tuile)):
                    for j in range(len(tuile)-1, -1, -1):
                        if tuile[i][j] != 0: 
                            val = tuile[i][j]
                            for k in range(len(tuile)-1,j,-1):
                                    if tuile[i][k] == 0:
                                        tuile[i][j] = 0
                                        tuile[i][k] = val
                                        break
                for i in range(0, len(tuile)):
                    for j in range(len(tuile)-1, -1,-1):
                        if tuile[i][j-1] == tuile[i][j] and tuile[i][j] != 0: 
                            if j == len(tuile)-1:
                                tuile[i][j] *= 2
                                tuile[i][j-1] = 0
                compteur = 0
                for i in range(0,len(tuile)):
                    for j in range(0,len(tuile)):
                        if L[i][j] == tuile[i][j]:
                            compteur += 1
            if compteur != 16:
                spawn_tuile()
                maj()
                maj_score() 
    return

def End():
    global event
    """"Fonction lier au bouton Exit """
    event = False
    # Bouton_replay = tk.Button(text="replay", command=play)
    # game_over = tk.Label(text="Fin de la partie", foreground='Black',
    #                            font='Arial 30',)
    game_over.grid(row=3, column=1, columnspan=1)
    Bouton_replay.grid(row=5, column=1)

def Save():
    global liste_tuile, liste_tuile4D, event4d, event_classique
    liste_save = copy.deepcopy(liste_tuile)
    """"Fonction lier au bouton Sauvegarder
    elle permet de sauvgarder un la dernier liste"""
    if event_classique == True:
        fic = open("Save", "w")
        for i in range(0, N):
            for j in range(0, N):
                fic.write(str(liste_save[i][j])+"\n")
        fic.close()
    elif event4d == True:
        for tuile in liste_tuile4D:
            liste_save = copy.deepcopy(tuile)
            fic = open("Save", "w")
            for i in range(0, n):
                for j in range(0, n):
                    fic.write(str(liste_save[i][j])+"\n")
        fic.close()

def Load():
     global liste_tuile
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
     liste_tuile = np.array(Grille_S)
     maj()

def Hard():
    """active l'evenement pour passer le jeu en hard"""
    global eventhard
    eventhard = True
    Classique()

def clavier_up(event):
    Up()
    return
def clavier_down(event):
    Down()
    return
def clavier_right(event):
    Right()
    return
def clavier_left(event):
    Left()
    return

# ------------------------ Code Principale ------------------------ #
racine = tk.Tk()
# Parrametre de la racine et Canvas
racine.title("2048")
canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)

# Bouttons
Bouton_Play = tk.Button(text='Classique', command=Classique)
Bouton_hard = tk.Button(text='hard', command=Hard)
Bouton_Exit = tk.Button(text="Exit", command=End)
Bouton_Save = tk.Button(text="Sauvegarder", command=Save)
Bouton_Load = tk.Button(text="Charger", command=Load)
Bouton_Up = tk.Button(text="Haut", command=Up)
Bouton_Down = tk.Button(text="Bas", command=Down)
Bouton_Left = tk.Button(text="Droite", command=Right)
Bouton_Right = tk.Button(text="Gauche", command=Left)
Bouton_replay = tk.Button(text="replay", command=Classique)
# Bouton_classique = tk.Button(text="classique", command=Classique)
Bouton_4d = tk.Button(text="4D", command=Secondmode)
# Label
Label_Score = tk.Label(text="Score :", foreground="Black", font="Arial, 10")
Label_Valeur_Score = tk.Label(text=str(Score), foreground="Blue",
                               font="Arial 10")
game_over = tk.Label(text="Fin de la partie", foreground='Black',
                               font='Arial 30',)
# Placement des éléments
Label_Score.grid(row=0, column=1, columnspan=1)
Label_Valeur_Score.grid(row=0, column=2, columnspan=1)
canvas.grid(row=1, column=1, columnspan=1, rowspan=7)
Bouton_Play.grid(row=2, column=0)
Bouton_Exit.grid(row=5, column=0)
Bouton_Save.grid(row=6, column=0)
Bouton_Load.grid(row=7, column=0)
Bouton_Up.grid(row=2, column=4)
Bouton_Down.grid(row=3, column=4)
Bouton_Right.grid(row=3, column=3)
Bouton_Left.grid(row=3, column=5)
Bouton_4d.grid(row=3, column=0)
Bouton_hard.grid(row=4, column=0)
#Clavier
racine.bind("<Up>", clavier_up)
racine.bind("<Down>", clavier_down)
racine.bind("<Right>", clavier_right)
racine.bind("<Left>", clavier_left)

# mainloop
racine.mainloop()

# ----------------------- Fin du programme  ----------------------- #