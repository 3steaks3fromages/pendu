#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:28:51 2020

@author: timothee
"""

import random

def mot_aleatoire():
    #On choisit un mot aléatoirement dans la liste
    f=open("mots.txt","r")
    lignes=0
    liste_mots=[]
    for ligne in f:
        if ligne !="\n":
            lignes+=1
            liste_mots.append(ligne)
    n=random.randint(0,lignes)
    mot=liste_mots[n-1]
    f.close()
    return mot
    