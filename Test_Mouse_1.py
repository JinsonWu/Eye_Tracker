# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 02:14:41 2018

@author: Jinson Wu
"""
x=[]
y=[]
i=0
spl=[]
sets=[]
import pyautogui
print(pyautogui.size())
while True:
    data = open('')
    sets = data.read().split('\n')    
    spl.append(sets[0].split(" "))
    x.append(spl[i][0])
    y.append(spl[i][1])
    pyautogui.moveTo(float(x[i]),float(y[i]),duration=0.05)