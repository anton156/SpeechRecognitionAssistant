import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import os
import pyautogui
import winshell
from random import seed
from random import randint
import subprocess
import psutil
import pyjokes
import datetime
import ecapture as ec
from sys import exit



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

r=sr.Recognizer()

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
 
    return cipher
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
    if 'recycle' in voice_data:
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        saysentence("Recycle Bin Recycled")
    if 'screenshot' in voice_data:
        username = '\\' + os.getlogin()
        name = '\screenshot' + str(randint(0,1000)) +'.png'       
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'C:\Users' + username + '\Desktop' + name)
        saysentence("Saved")
    if 'encrypt' in voice_data:
        saysentence("Say message")
        message = record_audio("Say message")
        result = encrypt(message.upper())
        print(result)
        saysentence("Encrypted")
    if 'memory' in voice_data:
        saysentence('RAM usage')
        saysentence(psutil.virtual_memory().percent)
        saysentence('CPU usage')
        saysentence(psutil.cpu_percent())
    if 'computer number' in voice_data:
        saysentence('Number of CPU')
        saysentence(psutil.cpu_count())
    if 'battery' in voice_data:
        battery = psutil.sensors_battery()
        saysentence(battery.percent)
    if 'create' in voice_data:
        username = '\\' + os.getlogin()
        saysentence('Name folder')
        directory = record_audio("Folder")
        parent_dir = "C:\\Users" + username + "\\Desktop"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        print("Folder '% s' created" % directory)
    if 'time' in voice_data:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        saysentence(f"the time is {strTime}") 
    if 'text' in voice_data:
        saysentence('Name text file')
        text = record_audio("Text file name")
        f= open("C:\\Users" + username + "\\Desktop\\"+ text +".txt","w+")
        saysentence('Say what to write')
        writing = record_audio("Writing")
        f.write(f"{writing.lower()}")
        print("Writen")
        saysentence('Finished')
    if 'joke' in voice_data:
        saysentence(pyjokes.get_joke())
    if "camera" in voice_data or "take a photo" in voice_data:
        ec.capture(0, "User Camera ", "camera.jpg")
    if 'command' in voice_data:
        saysentence('Say command')
        comm = record_audio('Command')
        os.system(f"start /wait cmd /c {comm}")
    if 'down' in voice_data:
        pyautogui.press('volumedown', presses=5)
    if 'up' in voice_data:
        pyautogui.press('volumeup', presses=5)
    if 'windows' in voice_data:
        pyautogui.press('win')
    if 'shut down' in voice_data:
        saysentence("PC will shut down")
        subprocess.call(["shutdown", "/p /f"])
    if "restart" in voice_data:
        subprocess.call(["shutdown", "/r"])
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

while(1):
 saysentence('How can i help')
 voice_data = record_audio()
 respond(voice_data)