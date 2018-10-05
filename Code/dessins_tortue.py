# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:16:49 2018

@author: Cyril GENISSON
"""
from turtle import *
from math import pi, sqrt

# Exercice 7.*
# Création de différentes fonctions de dessins
skin = ['blue', 'brown', 'black', 'red', 'yellow', 'green', 'purple']

def equilateral(s, c, a=1):
    ''' Méthode pour dessiner un triangle équilatéral:
        s: taille en pixels
        c: couleur
        a: angle direct 1 ou indirect 0
    '''
    color(c)
    down()
    for k in range(3):
        forward(s)
        if a:
            left(120)
        else:
            right(120)
    up()
    forward(s)

def etoile6(s, c):
# Voir pour améliorer la fonction avec le moins d'instructions possibles
    equilateral(s, c)
    left(90)
    forward(s / sqrt(3))
    left(90)
    equilateral(s, c)
    left(90)
    forward(s / sqrt(3))
    left(90)
    forward(s)

def carre(s, c):
    ''' Méthode pour dessiner un carré:
        c: couleur
        s: taille en pixels
    '''
    color(c)
    down()
    for k in range(4):
        forward(s)
        left(90)
    up()

def etoile5(s, c):
    color(c)
    down()
    for k in range(5):
        forward(s)
        right(144)
    forward(s)

	
