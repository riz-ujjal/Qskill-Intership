# Personal Python Voice Assistant 🎙️🤖

A modular, multi-threaded voice assistant built in Python. This assistant is designed to actively listen to voice commands, manage a persistent task list, and run a background clock to trigger custom time-based reminders without freezing the main listening loop.

## ✨ Features
* **Speech-to-Text (STT):** Uses Google's speech recognition to translate voice commands into text.
* **Text-to-Speech (TTS):** Provides real-time audio feedback using the `pyttsx3` engine.
* **Task Management:** Parses commands (e.g., "add milk") and permanently saves them to a local text file (`Demo.txt`).
* **Multi-Threaded Reminders:** Runs a continuous background clock that watches for specific alarm times and speaks reminders, all while the main thread continues to listen for new commands.

## 🗂️ Project Architecture
This project follows a strict "Manager/Worker" architecture to ensure Separation of Concerns. 

* **`main.py` (The Manager):** The core entry point of the app. It handles the infinite loops, spins up the background threads, and passes data between the hardware and the task workers.
* **`Listening_to_user.py` (The Ears):** A dedicated, standalone module containing the `Listen()` function. It opens the microphone, calibrates for ambient noise, and returns a clean string of text.
* **`Speaking_to_user.py` (The Mouth):** A dedicated module containing the `Speak()` function. 
* **`Task_setting.py` (The Worker):** Pure text-processing logic. It takes incoming strings from `main.py`, searches for trigger words (like "add"), writes to `Demo.txt`, and returns a success/error message.

## 🛠️ Prerequisites & Installation

You will need Python 3 installed on your system, along with a few external audio libraries.

**1. Open your terminal and install the required modules:**
```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio