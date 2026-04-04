# main.py

import speech_recognition as sr
import datetime
import win32com.client
import logging
from config import ASSISTANT_NAME, USER_NAME
from commands import (get_time, get_date, tell_joke, get_weather, search_web,
                      open_app, close_app, play_music, greet_user, about_jarvis,
                      get_battery, take_screenshot, get_news, what_can_i_do)

# ── Logging ───────────────────────────────────────────────────
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ── Setup TTS ─────────────────────────────────────────────────
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def speak(text):
    print(f"{ASSISTANT_NAME}: {text}")
    logging.info(f"Jarvis: {text}")
    speaker.Speak(text)

# ── Listen to Mic ─────────────────────────────────────────────
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"You: {query}")
        logging.info(f"You: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that. Please say it again.")
        return ""

# ── Process Commands ──────────────────────────────────────────
def process_command(command):
    speak("One second!")
    speak("Here we go!")

    if "time" in command:
        speak(get_time())
    elif "date" in command:
        speak(get_date())
    elif "joke" in command:
        speak(tell_joke())
    elif "weather" in command:
        speak(get_weather())
    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query:
            speak(search_web(query))
    elif "close" in command:
        speak(close_app(command))
    elif "open" in command:
        speak(open_app(command))
    elif "play music" in command or "play song" in command:
        speak(play_music())
    elif "hello" in command or "hi" in command or "hey" in command:
        speak(greet_user())
    elif "who are you" in command or "about you" in command or "introduce yourself" in command:
        speak(about_jarvis())
    elif "what can you do" in command or "help" in command or "what can i do" in command:
        speak(what_can_i_do())
    elif "battery" in command:
        speak(get_battery())
    elif "screenshot" in command:
        speak(take_screenshot())
    elif "news" in command:
        headlines = get_news()
        speak("Here are the top 5 news headlines.")
        for headline in headlines:
            speak(headline)
    elif "stop" in command or "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")

# ── Main Loop ─────────────────────────────────────────────────
if __name__ == "__main__":
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    speak(f"{greeting}, {USER_NAME}! I am {ASSISTANT_NAME}, your voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)