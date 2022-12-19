import pyttsx3 # Importing a python module to convert text into speech (pip install pyttsx3).
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import os
import cv2 # pip install opencv
from requests import get # pip install request
import wikipedia #pip install wikipedia
import webbrowser # pip install pycopy-webbrowser
from matplotlib import pyplot as plt # pip install matplotlib
import sounddevice as sd # pip3 install sounddevice
import soundfile as sf # pip3 install soundfile or pip install soundfile
from scipy.io.wavfile import write # pip3 install scipy


engine = pyttsx3.init("sapi5") #
voices = engine.getProperty("voices") # Getting the property of voice from pyttsx3
engine.setProperty("voices",voices[0].id) # Getting particular voice from the voice property.

def speak(audio): # Text to Speech
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand(): # Converts voice to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=10)
    try:
        print("Recognizing... ")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{ query }")
    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

def wish():
    speak("initializing my components")
    speak("3")
    speak("2")
    speak("1")
    speak("data reading is complete")
    speak("seting up my environment is complete")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good Morning sir!")
    elif hour>12 and hour<18:
        speak("good Afternoon sir!")
    else:
        speak("Good Evening sir!")
def record():
    speak("Setting up to record voice...")
    speak("Sir specify the duration of recording..")
    freq= 44100
    duration = 10
    speak("i received no input sir, so i was assuming the default value from my commands...")
    speak("Preparing to record voice...")
    speak("3")
    speak("2")
    speak("1") 
    # Start recorder with the given values of duration and sample frequency
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    # Record audio for the given number of seconds
    sd.wait()
    write("recording0.wav", freq, recording)
    speak("Saved the audio file.. preparing to play the file....")
    filename = 'recording0.wav'
    os.startfile("I'M ALONE - Gym Motivation 😔.mp3")

    print("next step")
    
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    
def Project():
    import face_recognition 
    speak("Importing the required modules")
    speak("Setting up the environment")
    speak("3")
    speak("2")
    speak('1')
    img1 = face_recognition.load_image_file("D:\\MYWORLD\\my academics related\\5th sem related\\PHN-313 (Siganals and Systems) related\\Project Related\\2. Attendance\\imgs\\Elon.jpg")
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    imgTest = face_recognition.load_image_file("D:\\MYWORLD\\my academics related\\5th sem related\\PHN-313 (Siganals and Systems) related\\Project Related\\2. Attendance\\Test_imgs\\Elon_Test.jpg")
    imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

    faceLoc = face_recognition.face_locations(img1)[0]
    encodeimg = face_recognition.face_encodings(img1)[0]
    cv2.rectangle(img1,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

    faceLocTest = face_recognition.face_locations(imgTest)[0]
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

    results = face_recognition.compare_faces([encodeimg],encodeTest)
    faceDis = face_recognition.face_distance([encodeimg],encodeTest)
    print(results,faceDis)
    cv2.putText(imgTest, f"{results} {round(faceDis[0],2)}",(0,0),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

    cv2.imshow("Elon Musk", img1)
    cv2.imshow("Elon Test", imgTest)
    #cv2.waitKey(0)
    speak("from my results....")
    speak("It's a match....")

if __name__ == "__main__":
    wish()
    speak("How can i help you sir?")
    while True:
        query = takecommand().lower()
        #logic building for tasks
        if "open chrome" in query:
            npath = ""
            os.startfile(npath)
        elif "terminate" in query or "shutdown" in query or "stop" in query or "sleep" in query:
            speak("Received command to stop!")
            speak("shutting down all the systems...")
            speak("Saving and Closing all the files....")
            speak("Preparing to shutdown!")
            speak("3")
            speak("2")
            speak("1")
            speak("shuttingdown....")
            break
        elif "record audio" in query:
            record()
        elif "introduce yourself" in query:
            npath = "D:\\MYWORLD\\my academics related\\5th sem related\\PHN-313 (Siganals and Systems) related\\Project Related\\Jarvis\\Jarvis Version-1. O\\Javis logo.jpg"
            os.startfile(npath)
            speak("Let me Introduce my self!")
            speak("I am Jarvis, an Artificial Intelligence, version: 1 point O Level-1 with memory 1Tera Byte, processor level-1 point O Advanced multiprocessor!")
            speak("I am here to assist you, Tell me how can i help you ?")
        elif "open command prompt" in query:
            npath = ""
            os.system("start cmd") 
        elif "facial recognization" in query or "facial recognition" in query:
            Project()

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if k==27:
                    break 
            cap.release()
            cv2.destroyAllWindows()     
        elif "play music" in query:
            speak("Opening Music player")
            music_dir = "C:\\Users\\HITESH\\Music\\I'M ALONE - Gym Motivation 😔.mp3"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, songs[0]))
        elif "ip address" in query:
            ip = get("https://api.ipify.org").text 
            speak(f"my IP address is {ip}")
        elif "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2 )
            speak("according to wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open mail" in query:
            webbrowser.open("www.gmail.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("Opening Google")
            speak("Sir, what should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")





