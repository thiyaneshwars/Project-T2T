
# 🗣️ PhonoKit - Voice-Based Pronunciation Trainer

PhonoKit is a Raspberry Pi-compatible educational tool designed to help users improve pronunciation using speech recognition and feedback in Tamil. It fetches words from a server, checks spoken words using VOSK + Levenshtein Distance, and gives encouraging responses in Tamil.

---

## 🎯 Features

- ✅ Wake word detection using VOSK (`"hello"`)
- ✅ Fetches word list from a Flask backend server
- ✅ Pronunciation checking using string similarity
- ✅ Real-time Tamil feedback using Google Text-to-Speech (`gTTS`)
- ✅ Server integration for result storage and retrieval
- ✅ Cross-platform and deployable on Raspberry Pi

---

## 🗂️ Project Structure

```

PhonoKit/
├── server.py              # Flask backend for word handling
├── client.py              # Main voice recognition script
├── vosk-model/            # Downloaded VOSK model directory
├── requirements.txt       # Python dependencies
└── README.md              # You're here!

````

---

## 🚀 How to Run

### 1. 🧠 Install Dependencies

```bash
pip install vosk pyaudio gtts playsound requests flask flask-cors python-Levenshtein
````

> ⚠️ On some systems, `pyaudio` may need `portaudio`:

```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

### 2. 📦 Download VOSK Model

* Download a VOSK model (e.g. [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models))
* Extract and place inside your project folder

### 3. 🔊 Run the Flask Backend

```bash
python server.py
```

This will host endpoints like:

* `GET /get-words`
* `POST /post-result`
* `GET /get-results`

### 4. 🧏‍♂️ Start the Voice Interface

```bash
python client.py
```

* Wait for wake word: **"hello"**
* Say each word from the server
* Receive pronunciation feedback

---

## 🌐 API Endpoints

| Method | Endpoint       | Description             |
| ------ | -------------- | ----------------------- |
| GET    | `/get-words`   | Get current word list   |
| POST   | `/post-result` | Post result (if needed) |
| GET    | `/get-results` | View posted results     |

---

## 📋 Sample Configuration

Change this URL in `client.py` to point to your server:

```python
SERVER_URL = "https://<your-ngrok-or-server-url>"
```

---

## 🤖 Technologies Used

* [VOSK](https://github.com/alphacep/vosk-api) – Offline speech recognition
* [gTTS](https://pypi.org/project/gTTS/) – Google Text-to-Speech
* [Flask](https://flask.palletsprojects.com/) – Backend server
* [Levenshtein](https://pypi.org/project/python-Levenshtein/) – String similarity
* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) – Audio stream input

---

## 🧪 Future Improvements

* ✅ Word list upload from UI
* ✅ Store user scores in DB
* ✅ Graphical frontend for users
* ✅ Multiple language support

---

## ✍️ Author

* **Thiyaneshwar S** 
* Email: [sthiyaneshwar94@gmail.com]

---

## 📄 License

This project is for educational use only.

```

