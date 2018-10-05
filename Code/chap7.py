# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:46:11 2018

@author: Cyril GENISSON
"""
from math import pi

# Exercice 7.2
def ligneCar(n , ca):
    l = ""
    for k in range(n):
        l += ca
    return l

# Exercice 7.3
def surfCercle(R):
    return pi * R**2

# Exercice 7.4
def volBoite(x1, x2, x3):
    return x1 * x2 * x3

# Exercice 7.5
def maximum(n1, n2, n3):
    if n1 >= n2:
        if n1 >= n3:
            return n1
        else:
            return n3
    elif n2 >= n3:
        return n2
    else:
        return n3

# Exercice 7.9
def compteCar(ca, ch):
    n = 0
    for k in range(len(ch)):
        if ch[k] == ca:
            n += 1
    return n

# Exercice 7.10
def indexMax(liste):
    max , index= liste[0], 0
    for k in range(len(liste)):
        if max < liste[k]:
            max, index = liste[k], k
    return index

# Exercice 7.11
def nomMois(n):
    t = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
         'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return t[n-1]

# Exercice 7.12
def inverse(ch):
    reverse = ""
    for k in range(len(ch)):
        reverse += ch[len(ch)-1-k]
    return reverse

# Exercice 7.13
# L'idée ici est de compter la différence etre les espaces. Pour avoir un mot
# il suffit que la distance entre 2 espaces soit supérieure à 1
def compteMots(ph):
    p = ' ' + ph + ' '
    t = []
    for k in range(len(p)):
        if p[k] == ' ':
            t.append(k)

    cpt = 0
    for k  in range(len(t)-1):
        if t[k+1] - t[k] > 1:
            cpt += 1

    return cpt

# Exercice 7.14
def volBoite2(x1=10, x2=10, x3=10):
    return x1 * x2 * x3

# Exercice 7.15
def volBoite3(x1, x2, x3):
    if x1:
        if x2:
            if x3:
                return x1 * x2 * x3
            else:
                return (x2 * x1 ** 2) / 3
        else:
            return x1 ** 3
    else:
        return -1

# Exercice 7.16
def changeCar(ch, ca1, ca2, debut=0, fin=0):
    new = ""
    if not fin:
        fin = len(ch) - 1
    for k in range(len(ch)):
        if k <= fin and k >= debut and ch[k] == ca1:
            new += ca2
        else:
            new += ch[k]
    return new

# Exercice 7.17
def eleMax(liste, debut=0 , fin=0):
    if not fin:
        fin = len(liste) + 1
    return liste[indexMax(liste[debut:fin])]
