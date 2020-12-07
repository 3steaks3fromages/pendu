#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:54:29 2020

@author: timothee
"""

#Fonctions pour la fenêtre du pendu
# 1- Initialiser la fenêtre
# 2- Boutons
# 3- Image

from tkinter import Tk, Label, Entry, Button, PhotoImage, StringVar
from pendu_v2_jeu import jeu
from pendu_v2_choix_mot import mot_aleatoire

def main():
    lettres_deja_entrees=[]
    fenetre=Tk()
    
    f=open("high_score.txt","r")
    high_score=f.read()
    f.close
    
    fenetre.title("Jeu du pendu (Record: {err} erreurs)".format(err=high_score))
    fenetre.resizable(False, False)
    
    mot=mot_aleatoire()
    print(mot)
    #On crée le premier string qui contient la première lettre du mot et les _
    
    erreurs=0
    
    liste_lettres=list(mot)
    liste_lettres.remove("\n")
    k=len(liste_lettres)
    
    premiere_lettre=liste_lettres[0]
    underscore="_ "*(k-1)
    
    mot_incomplet="Le mot est: {l1} {_}".format(l1=premiere_lettre, _=underscore)
    
    #
    
    fenetre.geometry('800x400+400+200')
    bonhomme= PhotoImage(file='bonhomme1.gif')
    label0=Label(fenetre)
    label0.configure(image=bonhomme)
    label0.image=bonhomme
    
    label1=Label(fenetre, text=mot_incomplet)
    
    label2= Label(fenetre, text="Proposez une lettre")
    
    label3= Label(fenetre, text="Timothée Levilly", fg='gray')
    
    
    propos=StringVar()
    entry= Entry(fenetre, textvariable=propos)
    
    def proposer():
        jeu(entry,fenetre,label0,label1,mot,erreurs,liste_lettres,lettres_deja_entrees,propos)
    
    button = Button(fenetre, text="Proposer", command=proposer)
    
    
    label1.grid(row=1)
    label2.grid(row=2)
    entry.grid(row=2, column=2)
    button.grid(row=3)
    label3.grid(row=4)
    label0.grid(row=1, column=3, rowspan=3, padx=10, pady=10, sticky='nesw')
    
    fenetre.mainloop()

main()