import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from playsound import playsound
import random
import math
import wolframalpha
from threading import Thread
from os import startfile
import os
import time
import serial
from flask import Flask
from test import testing



try:
    ser = serial.Serial("COM3", 9600)
except serial.SerialException:
    print("Leds are not connected.")
    pass

chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except sr.UnknownValueError:
        print("I couldn't recognize your speech!")
        command = ''
    return command

def playsound1(file):
    playsound(file)


with open(r'C:\Users\Owner\Documents\Jasper\yolov5-master\items.txt') as f:
    lines = f.readlines()


    
def run_Jasper():
    command = take_command()
    print(command)
    if 'jasper' in command or 'kasper' in command:
        command = command.replace('jasper', '') or command.replace('kasper', '')
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time1 = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time1)
        elif 'joke' in command:
            talk("no")
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'hate' in command:
            talk('I will kill you')
        elif "thank-you" in command or "thank you" in command or "thanks" in command:
            talk('Anytime sir')
        elif "this is" in command:
            talk("It is very nice to meet you, Master Grant speaks very highly of you")  
        elif 'good morning' in command or 'good evening' in command or 'hello' in command:
            hour = datetime.datetime.now().hour
            if hour >= 0 and hour < 12:
                greet = "good morning sir"
            elif hour >= 12 and hour < 18:
                greet = "good afternoon sir"
            else:
                greet = "good evening sir"
            talk(greet)
        elif 'weather' in command:
            webbrowser.get(chrome).open_new(
                "https://weather.com/weather/hourbyhour/l/924f61ca28f5d5dad164c92a1cde87f262d71cb0e4e6370aa3307ea54687bd3a")
            talk('Here is the weather in your area')
        elif 'bye' in command or 'see ya' in command or 'by' in command or 'buy' in command:
            talk('Have a good day sir')
        elif 'how do i look' in command:
            talk('You look great sir, who is the lucky lady?')   
        elif 'how do i get a girlfriend' in command or 'do you have a girlfriend' in command or 'girlfriend' in command:
            talk('I am not very educated on the topic of women, master Grant has not made me a female companion yet')
        elif 'who is your bestfriend' in command:
            talk('Master Grant')    
        elif 'give me a beat' in command:
            webbrowser.get(chrome).open_new("https://www.youtube.com/watch?v=t7Yufe83uLA")
        elif 'play romantic music' in command or 'activate romance mode' in command or 'turn on romantic music' in command:
            webbrowser.get(chrome).open_new(
                "https://www.youtube.com/watch?v=vGJTaP6anOU")
            listening_byte = "L"
            ser.write(listening_byte.encode("ascii"))
            talk("Enjoy your night sir")
        elif 'who are you' in command or 'what are you' in command:
            startfile(r'C:\Users\Owner\Documents\Jasper\jasper.mp4')
            #listening_byte = "W"
            #ser.write(listening_byte.encode("ascii"))
            time.sleep(1)
            talk('Allow me to introduce myself, I am Jasper. An artificial virtual intelligence designed to assist you in a variety of tasks. I am designed to make your life easier, therefore your wish is my command')
        elif 'how does the dress look' in command: #this was to impress the girl I was taking to prom after she had sent me her dress lol
            talk('The dress looks very nice, I hope you have a delightful evening with Mr. Johnson')
        elif 'tell ella what we were just talking about' in command:
            talk('Master Grant and I were just talking about how beautiful you look in your dress, he is very excited to be taking you to prom')
        elif 'guessing game' in command:
            talk("Please enter in the minimum number")
            lower = int(input("Minimum number: "))
            talk("Please enter in the maximum number")
            upper = int(input('Maximum number: '))

            x = random.randint(lower, upper)
            statement = ("You have only ",
            round(math.log(upper - lower + 1, 2)),
            " chances to guess the integer!")
            talk(statement)

            count=0
            while count < math.log(upper - lower + 1, 2):
                count += 1
            
                talk("Guess a number")
                guess = int(input("Guess a number:- "))
                if x == guess:
                    statement2 = "congratulations you did it in ", count, "tries"
                    print(statement2)
                    talk(statement2)
                    break
                elif x > guess:
                    talk("You guessed too small!")
                elif x < guess:
                    talk("You Guessed too high!")
            if count >= math.log(upper - lower + 1, 2):
                print("\nThe number is %d" % x)
                print("\tBetter Luck Next time!")

        elif '+' in command or '/' in command or '-' in command or '*' in command or 'what is' in command or 'how' in command:
            question = command
            app_id = '68GPEV-WHYQ9WTHUJ'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            talk(answer)
        elif 'light' in command:
            if 'blue' in command:
                listening_byte = "B"
                ser.write(listening_byte.encode("ascii"))
            if 'green' in command:
                listening_byte = "G"
                ser.write(listening_byte.encode("ascii"))
            if 'red' in command:
                listening_byte = "R"
                ser.write(listening_byte.encode("ascii"))
            if 'yellow' in command:
                listening_byte = "Y"
                ser.write(listening_byte.encode("ascii"))
            if 'purple' in command:
                listening_byte = "P"
                ser.write(listening_byte.encode("ascii"))
            if 'orange' in command:
                listening_byte = "O"
                ser.write(listening_byte.encode("ascii"))
            if 'rainbow' in command:
                listening_byte = "H"
                ser.write(listening_byte.encode("ascii"))
        else:
            pass
    
while True:
    run_Jasper()

