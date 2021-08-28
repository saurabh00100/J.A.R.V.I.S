import sys
import cv2
import pyttsx3
import speech_recognition as sr
import datetime,time
import os
import numpy as np
import pyautogui as auto
import random
import wikipedia
from requests import  get
import webbrowser
import pywhatkit as kit
from smtplib import SMTP
from time import sleep



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



#text to speach
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To conver voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=100,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en')
        q=query.lower()
        print(f"user said: {q}")

    except Exception as e:
        #speak("Sir,do you have any other work.....")
        return "none"
    query=query.lower()
    return query

# To wish
def wish():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    speak("wait a second ,Jarvis is waking up.... ")
    sleep(4)
    speak("Jarvis is now ready for your help......")
    #speak("How can i help you sir ???????")


def TaskExecution():
    wish()
    while True:
        query = takecommand() 
        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            global os
            os.startfile(npath)

        elif "close notepad" in query:
            speak("Ok sir,I am closing notepad")
            os.system("taskkill /f /im notepad.exe ")

        elif "volume" in query:
            speak("What I do with volume increase or decrease")
            while True:
                query=takecommand()
                if "increase" in query:
                    speak("how much level I increase")
                    while True:
                        query=takecommand()
                        if "full" in query :
                            for i in range(1,101):
                                auto.press("f3")
                            speak("volume increased.")
                            break;
                        elif "fifty" in query:
                            for i in range(1,51):
                                auto.press("f3")
                            speak("volume increased.")
                            break;
                elif "decrease" in query:
                    auto.keyDown("f2")
                    speak("volume decreased.")
                    break;
        
        elif "change screen" in query:
            auto.keyDown('alt')
            auto.press('Tab')
            auto.keyUp('alt')
        
        
        elif "open cmd" in query:
            os.system("start cmd")
        
        elif "close cmd" in query:
            speak("Ok sir,I am closing cmd")
            os.system("taskkill /f /im cmd.exe")

        elif "open camera" in query:
            global cv2
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "take a screenshot" in query:
            global np
            image = auto.screenshot()
            image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
            speak("give me the name of your screenshot image")
            query=takecommand()
            cv=f"<YOUR EMAIL ID>"
            cv2.imwrite(cv,image)
            f=open('img_name.txt','w')
            f.write(cv)
            f.close()
        
        elif "show me the screenshot" in query:
            f=open('img_name.txt','r')
            g=f.read()
            os.startfile(g)
            print(g)
            print(type(g))
            f.close()
            
            
                        
        elif "open browser" in query:
            pathb = "<YOUR EMAIL ID>"
            os.startfile(pathb)
        
        elif "close browser" in query:
            speak("Ok Sir ,I am closing browser.")
            os.system("taskkill /f /im brave.exe")

        elif "play music" in query: 
            music_dir = "<YOUR EMAIL ID>"
            songs = os.listdir(music_dir)
            #rd=random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))

        elif "stop music" in query:
            speak("music is stoped.")
        
        elif "close music" in query:
            speak("Ok Sir ,I am closing music.")
            os.system("taskkill /f /im vlc.exe")

        elif "send text message" in query:
            import requests
            import json
          
            url = "https://www.fast2sms.com/dev/bulk"
            speak("Sir,enter your message here")
            mes=input("Enter your message: \n ")
            speak("Enter phone number whom you want to send message")
            num=input("Enter phone number whom you want to send message :\n")
            my_data = {'sender_id': 'FSTSMS','message': mes,'language': 'english','route': 'p','numbers': num}

            headers = {
                'authorization': '<ENTER YOUR AUTH KEY>',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
                        
                }

            response = requests.request("POST",url,data = my_data,headers = headers)

            returned_msg = json.loads(response.text)

            speak(returned_msg['message'])

                        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "tell me a joke" in query:
            import pyjokes
            inpu = pyjokes.get_joke()
            translate = inpu
            speak(translate)

        elif "wikipedia" in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            res =  wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            speak(res)
            print(res)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open instagram" in query:
            webbrowser.open("www.instgram.com")

        elif "open github" in query:
            webbrowser.open("www.github.com")

        elif "open heroku" in query:
            webbrowser.open("https://dashboard.heroku.com/apps")

        elif "open google" in query:
            speak("Sir,what shoul I search on google")
            cm = takecommand()
            webbrowser.open(f"{cm}")

        elif "send whats app message" in query:
            speak("Sir,what you want to send")
            #mzt = time.strftime("%I:%M %p")
            sen = takecommand()
            kit.sendwhatmsg("<ENTER NUMBER HERE>", (f"{sen}"),7,20)
            speak("message sent")

        elif "play on youtube" in query:
            speak("Sir ,what i play on youtube")
            c = takecommand()
            kit.playonyt(f"{c}")

        elif "send email" in query:
            import smtplib
            def sendEmail(to, content):
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("<YOUR EMAIL ID>", 'python=<YOUR PASSWORD>')
                server.sendmail('<YOUR EMAIL ID>', to, content)
                server.close()
            speak("I am listening you speak")
            try:
                speak("what should I say ?")
                content = takecommand()
                to = "<YOUR FRIEND EMAIL>"
                sendEmail(to, content)
                speak(f"Email have been sent to {to}")
            except Exception as e:
                print(e)
                speak("Sorry Sir,I am not able to send email,I am going back to taskexecution.")
                break

        elif "open sub text" in query:
            speak("opening sublime text editor")
            spath = "<ENTER PATH>"
            TaskExecution(os.startfile(spath))

        elif "internet speed" in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed .")
            print(f"downloadin = {dl}  and  uploading = {up} ")

        elif "open mobile camera" in query:
            import urllib.request
            import cv2
            import numpy as np
            import time
            URL = "http://192.168.100.19:8080/shot.jpg"
            while True:

                img_s = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_s, -1)
                cv2.imshow("IPWebcam", img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;
            cv2.destroyAllWindows()


        elif "sleep mode on" in query:
            speak("I am going to sleep mode .")
            break;
        
        elif "good bye" in query :
            speak("thank for using me sir, have a good day")

if __name__=="__main__":
    while True:
        permission = takecommand()
        if"ok start" in permission:
            TaskExecution()
        elif "good bye" in permission :
            speak("Thank You Sir ,for using me if you need me again then activate me,have anice day.")
            sys.exit()
        elif "close system" in permission:
            speak("Starting to shutdown your laptop")
            os.system("shutdown /s /t 1")


