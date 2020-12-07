#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:18:24 2020

@author: timothee
"""

from tkinter import PhotoImage

def changement_image(fenetre,erreurs,label0):
    bonhomme= PhotoImage(file='bonhomme{n}.gif'.format(n=erreurs))
    label0.configure(image=bonhomme)
    label0.image=bonhomme
    return()