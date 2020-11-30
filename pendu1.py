#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:56:41 2020

@author: timothee
"""

import random

#Pendu
while True:
    print("Jeu du pendu")
    f=open("high_score.txt","r")
    print("Record actuel (nombre d'erreurs): {err}".format(err=f.read()))
    f.close()
    #1ere etape: On choisit un mot aléatoirement dans la liste
    f=open("mots.txt","r")
    lignes=0
    liste_mots=[]
    for ligne in f:
        if ligne !="\n":
            lignes+=1
            liste_mots.append(ligne)
    n=random.randint(0,lignes)
    mot=liste_mots[n-1]
    print(mot)
    f.close()
    #2eme etape: On affiche le mot et sa premiere lettre
    
    liste_lettres=list(mot)
    liste_lettres.remove("\n")
    k=len(liste_lettres)
    
    premiere_lettre=liste_lettres[0]
    underscore="_ "*(len(liste_lettres)-1)
    
    print("Le mot est: {l1} {_}".format(l1=premiere_lettre, _=underscore))
    
    #3eme etape: On crée maintenant une boucle dans laquelle le joueur rentrera des lettres jusqu'a gagner/perdre
    
    erreurs=0
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lettres_deja_entrees=[]
    lettre_trouvee=[liste_lettres[0]]
    doublon=len(liste_lettres)-len(set(liste_lettres))
    mot_trouve=False
    liste_sans_premiere_lettre=liste_lettres[:]
    liste_sans_premiere_lettre.remove(liste_lettres[0])
    
    
    while erreurs<8 and mot_trouve==False:
        lettre=raw_input("Veuillez entrer une lettre: ")
        cas_particulier=False
        if (lettre in alphabet):
            #Cas particulier le joueur rentre une lettre qui est aussi la premiere lettre du mot
            print(liste_lettres[0])
            if (lettre == liste_lettres[0]) and (lettre in liste_sans_premiere_lettre)==False:
                cas_particulier=True
                print("Malheureusement, cette lettre ne fait pas partie du mot ")
                lettres_deja_entrees.append(lettre)
                erreurs+=1
                if erreurs<8:
                    print("{err} erreurs sur 8".format(err=erreurs))
            if(lettre in liste_lettres) and (lettre in lettres_deja_entrees)==False:
                print("Correct!")
                lettres_deja_entrees.append(lettre)
                lettre_trouvee.append(lettre)
                #Constitution de la chaine de caractères
                mot_partiel=""
                mot_trouve=True
                for i in range(len(liste_lettres)):
                    if i==0:
                        mot_partiel=mot_partiel+liste_lettres[0]+" "
                    else:
                        if liste_lettres[i] in lettre_trouvee:
                            mot_partiel=mot_partiel+liste_lettres[i]+" "
                        else:
                            mot_trouve=False
                            mot_partiel=mot_partiel+"_ "
                print(mot_partiel)
            elif lettre in lettres_deja_entrees and cas_particulier==False:
                print("Vous avez déjà essayé cette lettre")
            else:
                print("Malheureusement, cette lettre ne fait pas partie du mot ")
                lettres_deja_entrees.append(lettre)
                erreurs+=1
                if erreurs<8:
                    print("{err} erreurs sur 8".format(err=erreurs))
        else:
            print("Ce n'est pas une lettre")
    
    if mot_trouve:
        print("Bien joué, partie terminée avec {err} erreur(s)".format(err=erreurs))
    else:
        print("Game over, vous n'avez pas réussi à trouver le mot à temps :(")
    
    #Score
    f=open("high_score.txt","r")
    high_score=f.read()
    high_score=int(list(high_score)[0])
    if high_score>erreurs:
        print("Nouveau record!")
        f.close()
        f=open("high_score.txt","w")
        f.seek(0)
        f.truncate
        f.write(str(erreurs))
    f.close()
    reponse=raw_input("Rejouer? (o/n): ")
    if reponse=="o":
        continue
    else:
        break


