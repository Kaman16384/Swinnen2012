# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:16:49 2018

@author: Cyril GENISSON
"""
# Petites corrections par rapport au programme donné dans le livre
import tkinter as tk
from random import randrange

def drawline():
    " Tracé d'une ligne dans le canvas 1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1, y1, x2, y2, width=2, fill=coul)

    # Modification des coordonnées de la ligne suivante
    y2, y1 = y2 + 10, y1 - 10

def changecolor():
    " Change aléatoirement la couleur du tracé"
    global coul
    pal = ['purple', 'cyan', 'maroon', 'green', 'red',
           'blue', 'yellow', 'orange']
    coul = pal[randrange(len(pal))]

x1, y1, x2, y2 = 0, 200, 200, 0
coul = 'green'

fen1 = tk.Tk(screenName='Ray Tracing')

can1 = tk.Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side='left')

bou1 = tk.Button(fen1, text='Quitter', command=fen1.quit)
bou1.pack(side='bottom')

bou2 = tk.Button(fen1, text='Nouvelle ligne', command=drawline)
bou2.pack()

bou3 = tk.Button(fen1, text='Couleur', command=changecolor)
bou3.pack()

fen1.mainloop()
fen1.destroy()

# Exercice 8.1
# On peut modifier la liste pal en enlevant les couleurs cyan, maroon et green

# Exercice 8.2
# x1, y1, x2, y2 = 10, 190, 190, 190    initialisation des variables
# y2, y1 = y2 - 10, y1 - 10     changement des variables dans drawline()

# Exercice 8.3
# can1 = tk.Canvas(fen1, bg='dark grey', height=650, width=500)