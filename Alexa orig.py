
import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
from PIL import Image
#import subprocesspip
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import requests


import psutil
import urllib
from urllib.request import urlopen
import urllib.error

import speech_recognition
import pyttsx3
import datetime
import wikipedia
import pyjokes
import turtle as t
from turtle import Turtle, Screen
import time
import random

FONT = ("Times New Roman", 30, "bold")
p = ['red', 'green', 'blue', 'purple', 'black', 'orange', 'cyan', 'pink', 'brown', 'magenta', 'maroon', 'salmon']
color = (random.choice(p))

h = ['red', 'green', 'blue', 'purple', 'black', 'orange', 'cyan', 'pink', 'brown', 'magenta', 'maroon', 'salmon']
paint = (random.choice(h))

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print(' **listening**...')

            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=100.0)
            command = listener.recognize_google(voice)
            command = command.lower()
    except sr.WaitTimeoutError:
        pass
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    except ReferenceError:
        pass
    except RuntimeError:
        pass
    except TimeoutError:
        pass
    except UnboundLocalError:
        pass
    return command.lower()








def check_power():
    battery = psutil.sensors_battery()
    plugged_in = battery.power_plugged
    percent = str(battery.percent)



def run_alexa():

    command = take_command()
    print(command)
    try:

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            url = "https://www.youtube.com/refsults?search_query=" + song
            webbrowser.get().open(url)
            talk("Here is what i found on youtube")

        elif 'time' in command:
            _time = datetime.datetime.now().strftime('%I:%M %p')
            tess = t.Turtle()
            wn = t.Screen()
            wn.setup(width=400, height=300)
            t.penup()
            t.pencolor(paint)
            t.goto(-172, 90)
            t.write(command)
            t.pencolor(color)
            t.goto(7, -60)
            t.write('current time is ' + _time)
            t.hideturtle()
            talk('Current time is ' + _time)
            t.done()


        elif 'who is' in command:
            try:
                per = command.replace('who is', '')
                info = wikipedia.summary(per, 1)
                print(info)
                talk(info)
            except RuntimeError:
                pass
            except ReferenceError:
                pass
            except UnboundLocalError:
                pass
            t.reset()
            c = "couldn't find the required infor, try searching manually. may i open web browser for u"
            t.pencolor(color)
            t.goto(7, -60)
            t.write(c[0:30])
            t.goto(7, -75)
            t.write(c[30:60])
            t.goto(7, -90)
            t.write(c[60:90])
            t.goto(7, -105)
            t.write(c[90:120])
            t.goto(7, -120)
            t.write(c[120:150])
            t.goto(7, 135)
            t.write(c[150:])
            t.hideturtle()
            t.hideturtle()
            t.done()
            talk("couldn't find the required infor, try searching manually,may i open web browser for u?")
            command = take_command()
            choice = command
            if choice == 'yes' or choice == 'yeah':
                url = f"https://google.com"
                webbrowser.get().open(url)
                talk('there u go sir')
            elif choice == 'no':
                t.reset()
                t.write('as u wish sir')
                t.hideturtle()
                t.done()
            else:
                pass


        elif 'what is the battery status' in command:
            try:
                if 'battery' in command:
                    plugged_in = 'we are on battery power'
                    talk(plugged_in + '\n' + 'you have' + percent + '% of your battery power remaining.')
                    print(plugged_in + '\n' + 'you have' + percent + '% of your battery power remaining.')
                else:
                    plugged_in = 'we are on AC power.'
                    talk(plugged_in)
                    print(plugged_in)
            except:
                pass


        elif 'read' in command:
            b = r'C:\Users\wamda\PycharmProjects\mouse\2.txt'
            with open(b, 'r') as f:
                f.read()
                t.write(b)
                talk(b)
                f.close()

        elif 'game' in command:
            talk('what game would you like to play')
            command = take_command()
            try:
                if 'rock' or 'scissors' or 'paper' in command:

                    talk("choose among rock paper or scissor")
                    command = take_command()
                    moves = ["rock", "paper", "scissor"]
                    cmove = random.choice(moves)
                    pmove = command
                    talk("The computer chose" + cmove)
                    talk("You chose " + pmove)

                    if pmove == cmove:
                        talk("the match is draw")
                    elif pmove == "rock" and cmove == "scissor":
                        talk("Player wins")
                    elif pmove == "rock" and cmove == "paper":
                        talk('computer wins')
                    elif pmove == "paper" and cmove == "rock":
                        talk('player wins')
                    elif pmove == "paper" and cmove == "scissor":
                        talk("Computer wins")
                    elif pmove == "scissor" and cmove == "paper":
                        talk("Player wins")
                    elif pmove == "scissor" and cmove == "rock":
                        talk("Computer wins")
                    else:
                        t.reset()
                        t.write('try again')
                        t.hideturtle()
                        t.done()
                else:
                    pass
                t.reset()
                t.write('come again')
                t.hideturtle()
                t.done()
                print('come again')

            except AttributeError:
                pass

        elif 'where am i' in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            talk("You must be somewhere near here, as per Google maps")

        elif 'google' in command:
            f = command.replace('google', '')
            url = f"https://google.com/search?q=" + f
            webbrowser.get().open(url)
            talk('Here is what i found for' + f + 'on google')
        elif 'hope' in command:
            im = Image.open(r"C:\Users\wamda\Desktop\image\IMG_20220619_175936.jpg")
            im.show()
            talk('this is all i can help as per now')

        elif 'remember my name is' in command:
            person_name = command.replace('remember my name is', '')
            div = r'C:\Users\wamda\PycharmProjects\mouse\names.txt'
            with open(div, 'w') as ti:
                ti.write(person_name)
                ti.close()
                talk("okay, i will remember that your name is" + person_name)

        elif 'what is my name' in command:
            tol = r'C:\Users\wamda\PycharmProjects\mouse\names.txt'
            with open(tol, 'r') as y:
                y.read()
                talk(tol)
                y.close()

        elif 'your name should be' in command:
            asis_name = command.split("be")[-1].strip()
            shane_name = r'C:\Users\wamda\PycharmProjects\mouse\shane name.txt'
            with open(shane_name, 'w') as ef:
                ef.write(asis_name)
                ef.close()
                talk(' i will remember that my name is' + asis_name)

        elif 'what is your name' in command:
            df = r'C:\Users\wamda\PycharmProjects\mouse\shane name.txt'
            with open(df, 'r') as xc:
                xc.read()
                xc.close()
                talk('my name is' + df)

        elif 'screenshot' in command:
            myscreenshot = pyautogui.screenshot()
            myscreenshot.save(r'C:\Users\wamda\PycharmProjects\mouse\screen.jpg')
            t.reset()
            t.write('screenshot saved', font=FONT)
            t.hideturtle()
            t.done()

        elif 'write a note' in command:
            t.reset()
            t.goto(-172,90)
            t.write('what would you like to write', font=FONT)
            t.hideturtle()
            t.done()
            talk('what would you like to write')
            command = take_command()
            f = command
            print(f[0:108])
            print(f[108:216])
            print(f[216:324])
            print(f[324:432])
            print(f[432:540])
            print(f[648:756])
            print(f[756:864])
            print(f[864:972])
            print(f[972:1080])
            print(f[1188:1296])
            print(f[1296:1512])
            print(f[1512:1620])
            print(f[1620:1728])
            print(f[1728:1836])
            print(f[1836:1944])
            print(f[1944:2052])
            print(f[2052:])

            fd = r'C:\Users\wamda\PycharmProjects\mouse\dfile.txt'
            with open(fd, 'a') as v:
                v.write('\n' + f + '\n')
                v.close()
                t.reset()
                t.pencolor(color)
                t.write('successfully written..... check in dfile.txt ')
                t.hideturtle()
                t.done()
        elif 'logout' in command:
            os.system('logout /l')

        elif 'restart' in command:
            os.system('restart /r')

        elif 'shutdown' in command:
            t.reset()
            t.write('Are you sure you want to power off the computer', font=FONT)
            t.hideturtle()
            t.done()
            talk('are you sure you want to power off the computer')
            command = take_command()
            choice = command
            if choice == 'yes' or choice == 'yeah':
                os.system('shutdown /s')

            elif choice == 'no':
                t.reset()
                t.write('as u wish sir')
                t.hideturtle()
                t.done()
                talk('as u wish sir')
            else:
                t.reset()
                t.write('try again')
                t.hideturtle()
                t.done()
                print('try again')
        elif 'exit' in command:
            t.reset()
            t.write('going offline')
            time.sleep(4)
            t.hideturtle()
            t.done()
            exit()

        elif 'assistant' in command:
            def ass():
                t.reset()
                t.write(''' Hello there am your friendly bot, ready to help you with anything
                lets start with the basics. what is your name''', font=FONT)
                t.hideturtle()
                t.done()

                talk('hello there. am your friendly bot. ready to help you with anything.')
                talk('lets start with the basics. what is your name')
                command = take_command()
                if 'my name is' in command:

                    q = command.replace('my name is', '')
                    t.reset()
                    t.write(q + 'how are u doing')
                    t.hideturtle()
                    t.done()
                elif 'i am' in command:
                    tv = command.replace('i am', '')
                    t.reset()
                    t.write(tv + 'how are you doing')
                    t.hideturtle()
                    t.done()
                elif 'my name' in command:
                    ut = command.replace('my name', '')
                    t.reset()
                    t.write(ut + 'how are you doing')
                    t.hideturtle()
                    t.done()

                    command = take_command()
                    if 'am fine' or 'am good' or 'fine' or 'good' in command:
                        talk('if you are good am good.That being said how can i help you')
                        command = take_command()
                        if 'search for' in command:
                            j = command.replace('search for', '')
                            ud = f"https://google.com/search?q=" + j
                            webbrowser.get().open(ud)
                            talk('Here is what i found for' + j + 'on google')

                        elif 'i wanted' in command:
                            s = command.replace('i wanted', '')
                            uv = f"https://google.com/search?q=" + s
                            webbrowser.get().open(uv)
                            talk('Here is what i found for' + s + 'on google')
                        elif 'what' in command:
                            a = command.replace('what', '')
                            rl = f"https://google.com/search?q=" + a
                            webbrowser.get().open(rl)
                            talk('Here is what i found for' + a + 'on google')
                        elif 'is' in command:
                            c = command.replace('is', '')
                            ul = f"https://google.com/search?q=" + c
                            webbrowser.get().open(ul)
                            talk('Here is what i found for' + c + 'on google')

                        elif 'where' in command:
                            ve = command.replace('where', '')
                            ur = f"https://google.com/search?q=" + ve
                            webbrowser.get().open(ur)
                            talk('Here is what i found for' + ve + 'on google')

                        else:
                            t.reset()
                            t.write('''command not in the database, to help with the development
                                                           of the bot, say add features command''', font=FONT)
                            t.hideturtle()
                            t.done()
                            print(
                                'command not in the database. to help with development of the bot.say add features command.to add new features')
                    else:
                        pass

                elif 'add feature' or 'add' in command:
                    t.reset()
                    t.write('what would you like to write', font=FONT)
                    t.hideturtle()
                    t.done()
                    talk('what would you like to write')
                    command = take_command()
                    d = r'C:\Users\wamda\PycharmProjects\mouse\add features.txt'
                    with open(d, 'a') as k:
                        k.write('add >>' + command)
                        k.close()

                elif 'exit' in command:
                    exit()
                else:
                    pass

            while True:
                ass()

        else:
            t.reset()
            t.pencolor(color)
            t.write('please say the command again', font=FONT)
            t.hideturtle()
            t.exitonclick()
            time.sleep(4)
            t.done()
            talk('Please say the command again.')

    except TypeError:
        pass
    except RuntimeError:
        pass
    except ResourceWarning:
        pass
    except ReferenceError:
        pass
    except MemoryError:
        pass
    except AttributeError:
        pass
    except UnboundLocalError:
        pass
    except TimeoutError:
        pass

check_power()


while True:
    run_alexa()
