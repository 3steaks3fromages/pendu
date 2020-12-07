#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:07:58 2020

@author: timothee
"""
from tkinter import Tk,Label,Button

def popup(texte):
    fenetre=Tk()
    fenetre.title("Jeu du pendu")
    fenetre.resizable(False, False)
    
    label=Label(fenetre, text=texte)
    label.grid(row=1)
    
    button=Button(fenetre, text="Ok", command=fenetre.destroy())
    button.grid(row=2)
    fenetre.mainloop()