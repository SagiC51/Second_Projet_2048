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
import tkinter as tk

# --------------------------- Constante --------------------------- #
HEIGHT_CANVAS = WIDHT_CANVAS = 400

# ----------------------- Varaibles Globale ----------------------- #

# ------------------------ Partie Fonction ------------------------ #

# ------------------------ Code Principale ------------------------ #

# Parrametre de la racine et Canvas
racine = tk.Tk()
racine.title("2048")
Canvas = tk.Canvas(bg='white', height=HEIGHT_CANVAS, width=WIDHT_CANVAS)
# Placement des éléments
Canvas.grid(row=1, column=2, columnspan=1, rowspan=7)
# mainloop
racine.mainloop()

# ----------------------- Fin du programme  ----------------------- #
