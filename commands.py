# commands.py

import datetime
import webbrowser
import os
import subprocess
import requests
import random
import psutil
import pyautogui
pyautogui.FAILSAFE = False
from config import CITY, WEATHER_API_KEY, MUSIC_FOLDER, NEWS_API_KEY

def get_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {time}"

def get_date():
    date = datetime.datetime.now().strftime("%A, %d %B %Y")
    return f"Today is {date}"

def tell_joke():
    try:
        url = "https://v2.jokeapi.dev/joke/Any?type=single&blacklistFlags=nsfw,racist,sexist"
        response = requests.get(url).json()
        return response["joke"]
    except:
        return "Sorry, I couldn't fetch a joke right now."

def get_weather():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url).json()
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"The weather in {CITY} is {desc} with a temperature of {temp}°C"
    except:
        return "Sorry, I couldn't fetch the weather right now."

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching for {query}"

def open_app(command):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "file explorer": "explorer.exe",
        "vs code": r"C:\Users\bhava\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "netflix": r"C:\Users\bhava\AppData\Local\Microsoft\WindowsApps\Netflix.exe",
    }
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "whatsapp": "https://web.whatsapp.com",
    }
    for app, path in apps.items():
        if app in command:
            subprocess.Popen(path)
            return f"Opening {app}"
    for site, url in sites.items():
        if site in command:
            webbrowser.open(url)
            return f"Opening {site}"
    return "Sorry, I don't know how to open that."
                
    for app, path in apps.items():
        if app in command:
            subprocess.Popen(path)
            return f"Opening {app}"
    for site, url in sites.items():
        if site in command:
            webbrowser.open(url)
            return f"Opening {site}"
    return "Sorry, I don't know how to open that."

def close_app(command):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "firefox": "firefox.exe",
    }
    for app, process in apps.items():
        if app in command:
            os.system(f"taskkill /f /im {process}")
            return f"Closing {app}"
    return "Sorry, I don't know how to close that."

def play_music():
    try:
        songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
        if not songs:
            return "No MP3 files found in your music folder."
        song = random.choice(songs)
        os.startfile(os.path.join(MUSIC_FOLDER, song))
        return f"Playing {song}"
    except:
        return "Sorry, I couldn't play music right now."

def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning! How can I help you?"
    elif hour < 18:
        return "Good afternoon! How can I help you?"
    else:
        return "Good evening! How can I help you?"

def about_jarvis():
    return ("I am Jarvis, your personal voice assistant built by Bhevanesh. "
            "I can tell you the time, date, weather, play music, search the web, "
            "open apps and websites, tell jokes, and much more. How can I help you?")

def what_can_i_do():
    return ("I can help you with the following. "
            "Tell the time and date. "
            "Check the weather. "
            "Tell jokes. "
            "Search the web. "
            "Open and close apps and websites. "
            "Play music. "
            "Check battery. "
            "Take a screenshot. "
            "Read the latest news.")

def get_battery():
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = "and is plugged in" if battery.power_plugged else "and is not plugged in"
        return f"Battery is at {percent}% {plugged}"
    except:
        return "Sorry, I couldn't check the battery status."

def take_screenshot():
    try:
        screenshot = pyautogui.screenshot()
        path = os.path.join(os.path.expanduser("~"), "Desktop", "screenshot.png")
        screenshot.save(path)
        return "Screenshot taken and saved to your Desktop!"
    except Exception as e:
        return f"Screenshot failed because {str(e)}"

def get_news():
    try:
        api_key = "c211081b65b44c758e2dadcfe549ab5f"
        url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}"
        response = requests.get(url)
        print("Status code:", response.status_code)
        data = response.json()
        print("Keys:", data.keys())
        print("Status:", data.get("status"))
        articles = data["articles"][:5]
        headlines = []
        for i, article in enumerate(articles, 1):
            title = article['title'].encode('ascii', 'ignore').decode('ascii')
            title = title.split('-')[0].strip()
            headlines.append(f"Headline {i}. {title}")
        return headlines
    except Exception as e:
        print("Full error:", str(e))
        return [f"News failed because {str(e)}"]