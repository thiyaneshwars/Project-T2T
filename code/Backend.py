from vosk import Model, KaldiRecognizer
import pyaudio
import json
import time
import Levenshtein
import requests
from gtts import gTTS
from playsound import playsound
import os
import tempfile

# ------------------ CONFIG -------------------
SERVER_URL = "https://16b0-103-78-167-218.ngrok-free.app"  # ✅ Replace with your actual ngrok URL

# ------------------ TTS USING GTTS -------------------
def speak(text, lang='ta'):
    print(text)
    with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
        tts = gTTS(text=text, lang=lang)
        playsound("test.mp3")

# ------------------ LOAD VOSK MODEL -------------------
model = Model(r"H:\project T2T\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")

def listen_for_text():
    rec = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1,
                      rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result.get("text", "").strip().lower()

# ------------------ WAKE WORD DETECTION -------------------
def listen_for_wake_word(wake_word="hello"):
    speak("PhonoKit-le ungalai varaverkirom! Wake word kekumpoathu sollunga.", lang='ta')
    speak("sollunga 'hello'")
    while True:
        spoken = listen_for_text()
        print(f"Ketta varthai: {spoken}")
        if wake_word in spoken:
            speak("Wake word kidaichiduchu!")
            return True

# ------------------ SIMILARITY CALCULATION -------------------
def similarity_percentage(word1, word2):
    if not word1 or not word2:
        return 0
    distance = Levenshtein.distance(word1, word2)
    max_len = max(len(word1), len(word2))
    similarity = (1 - distance / max_len) * 100
    return round(similarity, 2)

# ------------------ PRONUNCIATION CHECK -------------------
def check_pronunciation(expected_word):
    while True:
        speak(f"{expected_word} nu sollunga", lang='ta')
        spoken = listen_for_text()
        print(f"Neenga sonnadhu: {spoken}")

        percent = similarity_percentage(spoken, expected_word)
        speak(f"Neenga {percent} percent correct-a sonneenga", lang='ta')

        if spoken == expected_word.lower():
            speak("Super! Correct-a sonnenga!", lang='ta')
            return True
        elif percent > 80:
            speak("Nalla try. Konjam improve pannu!", lang='ta')
        else:
            speak("Konjam wrong iruku. Marubadi sollunga.", lang='ta')

# ------------------ SERVER WORD FETCH -------------------
def fetch_words_from_server():
    try:
        response = requests.get(f"{SERVER_URL}/get-words")
        if response.status_code == 200:
            return response.json()
        else:
            speak("Server response error", lang='ta')
            return []
    except Exception as e:
        speak(f"Server connect panna mudiyala: {str(e)}", lang='ta')
        return []

# ------------------ MAIN ENTRY -------------------
def main():
    if listen_for_wake_word():
        speak("PhonoKit-le ungalai varaverkirom!", lang='ta')
        words = fetch_words_from_server()

        if not words:
            speak("Word list empty or server error.", lang='ta')
            return

        for word in words:
            check_pronunciation(word)

        speak("Ella words-um correct-a sonnenga. Nandri!", lang='ta')

if __name__ == "__main__":
    main()
