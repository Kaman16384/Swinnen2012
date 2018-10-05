# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 10:15:07 2018

@author: Cyril GENISSON
"""
from math import sqrt, pi

# Exercice 6.1
# Converti une vitesse en milles / heures en km/h et m/s
vitesse = 10
conv = vitesse * 1609 / 3600
print("Vitesse en m/s: ", conv)
print("Vitesse en km/h: ", conv*3.6)

# Exercice 6.2
# Calcul le périmètre et l'aire d'un triangle quelconque
a, b, c = 1, 4, 3
d = (a + b + c) / 2
print("Périmètre: ", d*2)
print("Aire: ", sqrt(d*(d-a)*(d-b)*(d-c)))

# Exercice 6.3
# Calcul la période d'un pendule simple
l, g = 1, 9.81
print("Période du pendule en seconde: ", 2*pi*sqrt(l/g))

# Exercice 6.4
# Crée une liste d'entiers saisie par un utilisateur
liste =[]

while True:
    ent = input("Veuillez entrer une valeur: ")
    if ent:
        liste.append(int(ent))
    else:
        break

print(liste)

# Exercice 6.4 (bis)
# Version modifiée avec utilisation de fonctions que l'on verra au chapitre 7
def aff(liste):
    print(liste)

def creeliste():
    liste = []

    while True:
        ent = input("Veuillez entrer une valeur: ")
        if ent :
            liste.append(int(ent))
        else:
            break

    return liste

aff(creeliste())

# Exercice 6.5
# Pour a = 2 affiche gagné sinon affiche tout le temps perdu

# Exercice 6.6
# a) ne fait rien puisque la condition n'est pas vérifiée
# b) affiche presque gagné
# c) affiche perdu

# Exercice 6.7
# c) si a = 0 alors not a sera évalué comme True et le programme affichera
# gagné

# Exercice 6.8
# Additionne les multiples de 3 et de 5 des nombres compris entre 2 bornes
a, b, somme = 0, 32, 0

for k in range(a, b+1):
    if not (k%3) and not (k%5):
        somme += k
print(somme)

# Exercice 6.8 (bis)
# Additionne les multiples de 3 ou de 5 des nombres comrpis entre 2 bornes
a, b, somme = 0, 32, 0

for k in range(a, b+1):
    if not (k%3) or not (k%5):
        somme += k
print(somme)

# Exercice 6.9
# Détermine si une année saisie par l'utilisateur est bissextile ou non
an = int(input("Donnée une année: "))

if (not an%4 and an%100) or not an%400:
    print("Année bissextille")
else:
    print("Année non bissextile")

# Exercice 6.10
# Demande le sexe et le nom d'une personne pour une réponse appropriée
nom = input("Votre nom de famille: ")
sexe = input("Votre sexe M/F: ")

if str.lower(sexe) == 'm':
    print("Cher Monsieur ", nom)
else:
    print("Chère Mademoiselle ", nom)

# Exercice 6.11
# Demande à l'utilisateur trois longueur et détermine les propriétes du
# triangle ainsi formé si il existe.
tr = (0., 0., 0.)

# Saisie utilisateur des trois longueurs
for k in range(len(tr)):
    tr[k] = float(input("donnée une valeur numérique: "))

# Recherche du maximum dans le tuple et création d'une liste pour les 2 autres
# côtés
max = tr[0]
tr2 = []
for k in range(1,len(tr)):
    if max < tr[k]:
        tr2.append(max)
        max = tr[k]
    else:
        tr2.append(tr[k])

if max > tr2[0]+ tr2[1]:
    print("Le triangle n'existe pas.")
else:
    if max**2 == tr2[0] ** 2 + tr2[1] ** 2:
        if tr2[0] == tr2[1]:
            print("Le triangle est rectangle isocèle.")
        else:
            print("Le triangle est rectangle.")
    elif tr2[0] == tr2[1]:
        if max == tr2[0]:
            print("Le triangle est équilatéral.")
        else:
            print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")

# Exercice 6.12
# Affiche la racine carrée d'un nombre si elle existe.
a = float(input("Saisir un nombre: "))
if a >= 0:
    print(sqrt(a))
else:
    print("la racine carrée de", a, "n'existe pas.")

# Exercice 6.13
nb_points = 85
note = 27
val = note / nb_points
if val < 0.4 :
    print("E")
elif val < 0.5 :
    print("D")
elif val < 60 :
    print("C")
elif val < 80 :
    print("B")
else:
    print("A")

# Exercice 6.14
# Affiche les noms d'une liste avec le nombre de caractères le compose.
l=['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
       'Alexandre-benoît', 'Louise']
for k in range(len(l)):
    print(l[k], len(l[k]))

#  Exercice 6.15
notes = []

def moyenne(liste):
    somme = 0.
    for k in range(len(liste)):
        somme += liste[k]
    return somme / len(liste)

while True:
    a = float(input("Saisir une note ou -1 pour sortir: "))
    if a<0 :
        break
    else:
        notes.append(a)
        print("note la plus élevée: ", max(note))
        print("note la plus basse:", min(notes))
        print("moyenne des notes: ", moyenne(notes))

# Exercice 6.16
d = 0.05
m = 10000
G = 6.67*10**(-11)

for k in range(0, 20):
    F = G * m**2 / (d * 2**k)**2
    print("d = ", d * 2**k, "m : la force vaut ", F, "N")