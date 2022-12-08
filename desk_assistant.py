import pyttsx3  #text to speech conversion library
import datetime
import pyaudio
import webbrowser
import os
import speech_recognition as sr
import wikipedia
import pyautogui
import tkinter
from tkinter import *
from PIL import ImageTk,Image


engine=pyttsx3.init('sapi5')  # sapi5 to take voices from windows api
voices=engine.getProperty('voices')
# print(voices)   #to check voices avb on pc
engine.setProperty('voice',voices[0].id)    #male [0] and female[1] voices


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")

    # speak("I am your desktop assistant alex,Please tell me how may i help you?")

def takeCommand():


     #it takes microphone ip from user and returns string op

    r =sr.Recognizer() #helps to recognize voice
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=2     #will wait for 3 sec
        r.energy_threshold = 200
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:

         # print(e)

        print("Say that again please...")
        return "None"
    return query

class Widget:
    def __init__(self):
        root = Tk()  # root instance of cls tk ,there should be one instance in every tk

        root.title('Alex')
        root.geometry('520x420')

        img = ImageTk.PhotoImage(Image.open('virt.png'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        # frame
        userText = StringVar()

        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Alex', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=('Century Gothic', 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        btn = tkinter.Button(root, text='Start', font=('railways', 10, 'bold'), bg='cyan', fg='white',command=self.clicked).pack(fill='x',
                                                                                                            expand='no')
        btn2 = tkinter.Button(root, text='Close', font=('railways', 10,
                                                        'bold'), bg='yellow', fg='black', command=root.destroy).pack(
            fill='x', expand='no')
        speak("I am your desktop assistant alex,Please tell me how may i help you?")

        root.mainloop()

    def clicked(self):
        # BUTTON CALLING
        print("working...")

if __name__ == '__main__':
    widget=Widget()
    # speak("Nishat is a good girl")    #checking
    wishMe()    #dont put it in while loop
    # if 1:
    while 1:
        query=takeCommand().lower()

    #logic for executing the task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'who are you ' in query:
            speak('i am alex The Smart Assistant of nishaat, Developed to help her around with her work and makes her life easier with her machine')

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'google ' in query:   #
            speak("opening google")
            webbrowser.open('google.com')

        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open('instagram.com')

        elif 'find location' in query:
            location= speak('what location ')   #
            url = ( 'https://google.nl/maps/place/' + location + '/&amp;')
            webbrowser.get().open(url)


        elif 'play movie' in query:
            speak("playing movie")
            # mov='C:\\Users\\shaik\\Videos\\movies'
            os.startfile('C:\\Users\\shaik\\Videos\\movies')

        elif 'the time' in query:
            timeNow= datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'the time is {timeNow}')

        elif 'netflix' in query:
            os.startfile('C:\\Users\\shaik\\Desktop')

        elif 'search' in query:
            search=speak('what do you want to search for')
            url=('https://google.com/search?q=') +search
            webbrowser.get().open(url)


        elif 'screenshot' in query:
            img = pyautogui.screenshot()
            img.save('C:\Users\shaik\Pictures\Screenshots\screenshot.png')

        elif 'close' in query:
            speak('thank you have a good day')
            exit()

        # elif 'send email' in query:

