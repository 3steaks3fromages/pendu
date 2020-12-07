#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:56:41 2020

@author: timothee
"""


from pendu_v2_chgt_image import changement_image
from pendu_v2_popup import popup
from pendu_v2_rejouer import popup_rejouer


def jeu(entry,fenetre,label0,label1,mot,erreurs,liste_lettres,lettres_deja_entrees,propos):
    
    #3eme etape: On crée maintenant une boucle dans laquelle le joueur rentrera des lettres jusqu'a gagner/perdre
    lettre=propos.get()
    
    if lettre == "":
        popup("Veuillez entrer une lettre")
        return
    
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    lettre_trouvee=[liste_lettres[0]]
    mot_trouve=False
    liste_sans_premiere_lettre=liste_lettres[:]
    liste_sans_premiere_lettre.remove(liste_lettres[0])
    
    propos.set("")
    
    cas_particulier=False
    if (lettre in alphabet):
        #Cas particulier le joueur rentre une lettre qui est aussi la premiere lettre du mot
        print(liste_lettres[0])
        if (lettre == liste_lettres[0]) and (lettre in liste_sans_premiere_lettre)==False:
            cas_particulier=True
            lettres_deja_entrees.append(lettre)
            erreurs+=1
            if erreurs<8:
                popup("Malheureusement, cette lettre ne fait pas partie du mot, {err} erreurs sur 8".format(err=erreurs))
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
            label1.setvar(mot_partiel)
        elif lettre in lettres_deja_entrees and cas_particulier==False:
            popup("Vous avez déjà essayé cette lettre")
        else:
            lettres_deja_entrees.append(lettre)
            erreurs+=1
            changement_image(erreurs,fenetre,label0)
            if erreurs<8:
                popup("Malheureusement, cette lettre ne fait pas partie du mot, {err} erreurs sur 8".format(err=erreurs))
            return
    else:
        popup("Ce n'est pas une lettre")
        return
    if mot_trouve:
        popup_rejouer("Bien joué, partie terminée avec {err} erreur(s)".format(err=erreurs),fenetre)
    else:
        popup_rejouer("Game over, vous n'avez pas réussi à trouver le mot à temps :(",fenetre)
    
    #Score
    f=open("high_score.txt","r")
    high_score=f.read()
    high_score=int(list(high_score)[0])
    if high_score>erreurs:
        f.close()
        f=open("high_score.txt","w")
        f.seek(0)
        f.truncate
        f.write(str(erreurs))
    f.close()
    return