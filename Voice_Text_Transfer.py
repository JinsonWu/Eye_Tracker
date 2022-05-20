# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 21:55:08 2018

@author: Jinson Wu
"""

import speech_recognition
import io
def Voice_To_Text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print ("please say sth")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio,language='en-US')
    except r.UnknownValueError:
        text = 'cant transfer'
    except r.RequestError as e:
        text = 'cant transfer{0}'.format(e)
    return text
outfile = 'C:\Users\Jinson Wu\.spyder\Voice.txt'
f1 = io.open(outfile,"w",encoding="CP950")
text = Voice_To_Text()
print text
f1.write(text+'\n')
f1.close
