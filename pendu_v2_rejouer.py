#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:13:37 2020

@author: timothee
"""
from tkinter import Tk,Label,Button
#from pendu_v2_main import main

def popup_rejouer(texte,fenetre_principale):
    fenetre=Tk()
    fenetre.title("Jeu du pendu")
    fenetre.resizable(False, False)
    
    label=Label(fenetre, text=texte)
    label.grid(row=1)
    
    '''
    def rejouer():
        fenetre_principale.destroy()
        fenetre.destroy()
        main()
    
    button1=Button(fenetre, text="Rejouer", command=rejouer)
    button1.grid(row=2,column=1)
    
    Ce bout de code ne fonctionne pas et je n'ai pas eu le temps de trouver une solution 
    '''
    button2=Button(fenetre, text="Quitter", command=fenetre.destroy)
    button2.grid(row=2,column=1)
    
    fenetre.mainloop()
    
