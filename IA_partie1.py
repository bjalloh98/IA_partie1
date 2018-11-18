"""
Auteur : Jalloh, Bocar
Date : 18 / 11 / 2018
Matricule : 000474742
Assistant : Ternon, Cédric
Classe : BA_1 Info
"""

import random
def makeMove(M, last, strategy, eps, alpha) :
    eps = random.random()
    alpha = random.random()
    r = random.random()
    k = max(M)[0] # Cherche l'état aprés coupa ssocié à la probabilité maximale
    if r >= eps :
        move = k
    else :
        move = random.random
    return move

def endGame(won, history, strategy, alpha) :
    alpha = random.random()
    won = True or False
    if won == True :
        r = 1
    elif won == False :
        r = 0
    if strategy == "Monte Carlo " :
        c = [] # Initialise une liste C
        for i in history :
            c.append(i[1]) # On ajoute toutes les probabilités de history dans C
        for i in c :
            i = (1 - (alpha ** c.index(i)) * i + (alpha ** c.index(i)) * r)

        s = i
        move = s

    elif strategy == "TD(0)" :
        c = [] # Initialise une liste C
        for i in history :
             c.append(i[1]) # On ajoute toutes les probabilités de history dans C
        for i in c :
            i[c.index(i-1)] = ( 1 - alpha) * i[c.index(i-1)] + alpha * i
        s = i[c.index(i-1)]
        move = s


    elif strategy == "Q-learning" :
        c = [] # Initialise une liste C
        for i in history :
            c.append(i[1]) # On ajoute toutes les probabilités de history dans C
        for i in c:
            i[c.index(i-1)] = ( 1 - alpha) * i[c.index(i-1)] + alpha * i
        s = i[c.index(i-1)]
        move = s
    return move
