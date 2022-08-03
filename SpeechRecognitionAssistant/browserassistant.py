import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import os
import pyautogui
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
    if 'search' in voice_data:
        saysentence('Search for')
        search = record_audio("Search")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('I found this for ' + search)
        time.sleep(5)
        pyautogui.press('tab', presses=18)
    if 'video' in voice_data:
        saysentence('Search for')
        search = record_audio("Search")
        url = 'https://www.youtube.com/results?search_query=' + search
        webbrowser.get().open(url)
        print('I found this for ' + search)                                                                     
    if 'close' in voice_data:
        pyautogui.hotkey('ctrl', 'w')
    if 'home' in voice_data:
        pyautogui.hotkey('alt','home')
    if 'right' in voice_data:
        pyautogui.hotkey('ctrl','pgdn')
    if 'left' in voice_data:
        pyautogui.hotkey('ctrl','pgup')
    if 'refresh' in voice_data:
        pyautogui.hotkey('ctrl','r')
    if 'top' in voice_data:
        pyautogui.press('home')
    if 'bottom' in voice_data:
        pyautogui.press('end')
    if 'up' in voice_data:
        pyautogui.hotkey('shift','space')
    if 'down' in voice_data:
        pyautogui.press('space')
    if 'bookmark' in voice_data:
        pyautogui.hotkey('ctrl','d')
    if 'previous' in voice_data:
        pyautogui.hotkey('alt','left')
    if 'forward' in voice_data:
        pyautogui.hotkey('alt','right')
    if 'next' in voice_data:
        pyautogui.press('tab')
    if 'back' in voice_data or 'beck'in voice_data:
        pyautogui.hotkey('shift','tab')
    if 'print' in voice_data:
        pyautogui.hotkey('ctrl','p')
    if 'pencil' in voice_data or 'cancel' in voice_data or 'put down' in voice_data:
        saysentence('Writing')
        write = record_audio("Write")
        pyautogui.write(write)
    if '5' in voice_data:
        pyautogui.press('tab', presses=5)
    if 'ok' in voice_data or 'enter' in voice_data:
        pyautogui.press('enter')
    if 'download' in voice_data:
        pyautogui.hotkey('crtl','j')
    if 'manager' in voice_data:
        pyautogui.hotkey('crtl','b')
    if 'menu' in voice_data:
        pyautogui.hotkey('alt','f')
    if 'find' in voice_data:
        pyautogui.hotkey('crtl','f')
    if 'content' in voice_data:
        pyautogui.hotkey('crtl','f6')
    if 'help' in voice_data:
        pyautogui.press('f1')
    if 'save' in voice_data:
        pyautogui.hotkey('crtl','s')
    if 'history' in voice_data:
        pyautogui.hotkey('ctrl','h')
    if 'full' in voice_data:
        pyautogui.press('f11')
    if 'default size' in voice_data:
        pyautogui.hotkey('ctrl','0')
    if 'developer' in voice_data:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.keyDown('j')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('j')
    if 'delete' in voice_data:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.keyDown('delete')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('delete')
    if 'last' in voice_data or 'lost' in voice_data:
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        time.sleep(1)
        pyautogui.keyDown('t')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('t')
    if 'wait' in voice_data:
        time.sleep(60)
    if 'stop' in voice_data:
        time.sleep(300)
    if 'hold' in voice_data or 'cold' in voice_data:
        time.sleep(600)
    if 'time out' in voice_data or 'time' in voice_data or 'out' in voice_data:
        out = 'stop'
        while(out != 'start'):
            out = record_audio()
    if 'exit' in voice_data:
        exit()



time.sleep(1)

webbrowser.get().open('https://google.com')
time.sleep(2)
while(1):
 saysentence('How can i help')
 voice_data = record_audio()
 respond(voice_data)
