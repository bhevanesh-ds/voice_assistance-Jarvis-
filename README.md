# 🤖 Jarvis - Voice Controlled Desktop Assistant

A fully functional AI-powered voice assistant built with Python by **Bhevanesh**.
Jarvis listens to your voice commands and responds intelligently using text-to-speech.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Features

| Feature | Command |
|---|---|
| 🕐 Tell Time | "What is the time" |
| 📅 Tell Date | "What is the date" |
| 🌤️ Weather Update | "What is the weather" |
| 😂 Tell Jokes | "Tell me a joke" |
| 🔍 Web Search | "Search" |
| 🖥️ Open Apps | "Open Notepad / VS Code" |
| 🌐 Open Websites | "Open YouTube / Google" |
| ❌ Close Apps | "Close Chrome" |
| 🎵 Play Music | "Play music" |
| 🔋 Battery Status | "Battery" |
| 📸 Screenshot | "Take a screenshot" |
| 📰 News Headlines | "Tell me the news" |
| 🤖 About Jarvis | "Who are you" |
| ❓ Help | "What can you do" |
| 👋 Exit | "Bye / Stop / Exit" |

---

## 🛠️ Technologies Used

- **Python 3.13**
- **SpeechRecognition** — voice input from microphone
- **Windows SAPI** — text to speech engine
- **OpenWeatherMap API** — live weather data
- **NewsAPI** — latest news headlines
- **JokeAPI** — random jokes
- **psutil** — battery status
- **pyautogui** — screenshots
- **requests** — API calls
- **subprocess / os** — app launching and closing

---

## ⚙️ Installation

**1. Clone the repository**
```
git clone https://github.com/bhevanesh-ds/voice_assistance-Jarvis-
cd voice_assistance-Jarvis-
```

**2. Install dependencies**
```
pip install speechrecognition pywin32 requests psutil pyautogui pillow
```

**3. Configure API keys**

Open `config.py` and update the following:
```python
CITY = "Your City"
WEATHER_API_KEY = "your_openweathermap_key"
NEWS_API_KEY = "your_newsapi_key"
ASSISTANT_NAME = "Jarvis"
USER_NAME = "Your Name"
MUSIC_FOLDER = r"C:\Path\To\Your\Music"
```

Get free API keys from:
- 🌤️ Weather: [openweathermap.org](https://openweathermap.org)
- 📰 News: [newsapi.org](https://newsapi.org)

**4. Run Jarvis**
```
python main.py
```

---

## 📁 Project Structure
```
voice_assistance-Jarvis-/
├── config.py       # Settings and API keys
├── commands.py     # All feature functions
├── main.py         # Core loop and voice engine
└── README.md       # Project documentation
```

---

## 🚀 How It Works

1. **Startup** — Jarvis greets you by name based on time of day
2. **Listening** — Microphone activates and adjusts for background noise
3. **Recognition** — Audio sent to Google Speech Recognition API
4. **Processing** — Command matched to the right feature function
5. **Response** — Result spoken aloud using Windows SAPI voice engine
6. **Logging** — All conversations saved to `log.txt` with timestamps
7. **Loop** — Jarvis keeps listening until you say "Bye"

---

## 🖥️ Supported Apps

| Voice Command | Opens |
|---|---|
| "Open Notepad" | Notepad |
| "Open Calculator" | Calculator |
| "Open Paint" | MS Paint |
| "Open File Explorer" | File Explorer |
| "Open VS Code" | Visual Studio Code |
| "Open YouTube" | YouTube in browser |
| "Open Google" | Google in browser |
| "Open GitHub" | GitHub in browser |
| "Open WhatsApp" | WhatsApp Web |

---

## ❌ Closing Apps

| Voice Command | Closes |
|---|---|
| "Close Chrome" | Google Chrome |
| "Close Edge" | Microsoft Edge |
| "Close Firefox" | Firefox |
| "Close Notepad" | Notepad |
| "Close VS Code" | Visual Studio Code |

---

## 📋 Requirements

- Windows 10 or 11
- Python 3.13
- Working microphone
- Internet connection
- Free API keys from OpenWeatherMap and NewsAPI

---

## 👨‍💻 Developer

**Bhevanesh**
- GitHub: [@bhevanesh-ds](https://github.com/bhevanesh-ds)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub!
