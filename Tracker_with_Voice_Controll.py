# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 23:42:04 2018

@author: Jinson Wu
"""

import speech_recognition
import io
import pyautogui
import threading
x=[]
y=[]
i=0
spl=[]
sets=[]
print(pyautogui.size())
print('instruction')
print('click,right click,enter,scroll up/down,screenshot,drag right/down,copy,paste,typing')
def Voice_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text = r.recognize_google(audio,language='en-US')
        return text
def rec():
    while True:
        text = Voice_To_Text()
        outfile = 'C:\Users\Jinson Wu\.spyder\Voice.txt'
        f1 = io.open(outfile,"w",encoding="CP950")
        f1.write(text+'\n')
        f1.close
        if text == 'click':
            pyautogui.click()
        elif text == 'right click':
            pyautogui.rightClick()
        elif text == 'enter':
            pyautogui.press('enter')
        elif text =='scroll up':
            pyautogui.scroll(-200)
        elif text == 'scroll down':
            pyautogui.scroll(200)
        elif text == 'screenshot':
            pyautogui.screenshot()
        elif text == 'drag right':
            pyautogui.dragRel(100,0)
        elif text == 'drag down':
            pyautogui.dragRel(0,100)
        elif text == 'copy':
            pyautogui.hotkey('crtl','c')
        elif text == 'paste':
            pyautogui.hotkey('ctrl','v')
            
        else:
            pyautogui.typewrite(text)
t = threading.Thread(target=Voice_To_Text)
s = threading.Thread(target=rec)
t.start()
s.start()
while True:
    data = open('def.txt')
    sets = data.read().split('\n')  
    spl.append(sets[i].split(" "))
    x.append(spl[i][0])
    y.append(spl[i][1])
    if i==0:
        pyautogui.moveTo(1000,500)
        i=i+1
    else:
        pyautogui.moveRel(float(x[i]),float(y[i]),duration=0.05)
        i=i+1    





