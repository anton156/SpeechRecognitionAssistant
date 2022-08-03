import speech_recognition as sr
import pyttsx3
import time
import os
import pydirectinput
from sys import exit


r=sr.Recognizer()

def saysentence(sentence):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(sentence)
    engine.runAndWait()
    
    time.sleep(0.4)
    
def record_audio(ask=False):
  with sr.Microphone() as source:
    if ask:
        print(ask)
    
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)
    voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Repeat')
    except sr.RequestError:
        print('Error')
    print(f">> {voice_data.lower()}")
    return voice_data

def respond(voice_data):
    if 'up' in voice_data:
        pydirectinput.press('w')
    if 'down' in voice_data:
        pydirectinput.press('s')
    if 'left' in voice_data:
        pydirectinput.press('a')
    if 'right' in voice_data:
        pydirectinput.press('d')
    if 'start' in voice_data:
        pydirectinput.press('enter')
    if 'back' in voice_data or 'beck' in voice_data:
        pydirectinput.press('k')
    if 'ok' in voice_data:
        pydirectinput.press('l')
    if 'option' in voice_data:
        pydirectinput.press('o')
    if 'return' in voice_data:
        pydirectinput.press('i')
    if 'select' in voice_data:
        pydirectinput.press('back')
    if 'exit' in voice_data:
        exit()



time.sleep(1)

while(1):
 voice_data = record_audio()
 respond(voice_data)