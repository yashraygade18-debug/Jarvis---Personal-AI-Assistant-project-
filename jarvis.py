from gtts import gTTS
import speech_recognition as sr
import webbrowser
import musicLibrary
import requests
import os
import playsound
import datetime
import pyjokes

# recognizer
recognizer = sr.Recognizer()

# ---- SPEAK FUNCTION ----
def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    playsound.playsound("temp.mp3")
    os.remove("temp.mp3")

# ---- WEATHER ----
def get_weather(city):
    api_key = "669f1fe4bf0ee3e3df7cfc61180eee4a"
   # 🔑 Put your OpenWeatherMap API key here
    url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric"

    response = requests.get(url).json()
    if response["cod"] != "404":
        weather = response["main"]
        temp = weather["temp"]
        desc = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {desc}."
    else:
        return "Sorry, I could not find the weather for that city."

# ---- TIME, DATE, JOKE ----
def get_time():
    now = datetime.datetime.now()
    return now.strftime("The time is %I:%M %p")

def get_date():
    today = datetime.date.today()
    return today.strftime("Today is %B %d, %Y")

def tell_joke():
    return pyjokes.get_joke()

# ---- COMMAND HANDLER ----
def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = c.split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in your library.")

    elif "weather" in c:
        speak("Sure, which city?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)
            city = recognizer.recognize_google(audio)
            report = get_weather(city)
            speak(report)

    elif "time" in c:
        speak(get_time())

    elif "date" in c:
        speak(get_date())

    elif "joke" in c:
        speak(tell_joke())

# ---- MAIN LOOP ----
if __name__ == "__main__":
    speak("Hello yash, I am Jarvis. What can I do for you?")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)

            if "jarvis" in word.lower():
                speak("Yes, I'm listening...")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error:", e)

