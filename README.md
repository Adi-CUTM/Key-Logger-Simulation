# 🔐 Keylogger Surveillance Simulation

A lightweight, multi-threaded Python project simulating basic surveillance tools including:

- ⌨️ Keylogging
- 📸 Webcam video capture
- 🖥️ Full-screen recording

Designed **strictly for ethical testing**, development, and cybersecurity education inside virtualized environments.

---

## 📁 Folder Structure


keylogger_surveillance_sim/
├── main.py # 🧠 Launches keylogger + webcam + screen recorder
├── keylogger.py # ⌨️ Captures all keystrokes
├── video_capture.py # 📸 Records webcam (30s duration)
├── screen_capture.py # 🖥️ Records full screen continuously
├── requirements.txt # 📦 Python dependencies
├── README.md # 📘 This documentation
├── logs/ # 🗂️ Output folder (auto-created)
│ ├── key_log.txt # Keystrokes log
│ ├── capture.avi # Webcam capture (30s)
│ └── screen_record.avi # Full-screen video recording  


---

## 🚀 Features

| Module          | Description                              |
|-----------------|------------------------------------------|
| `keylogger.py`  | Logs all keystrokes to `logs/key_log.txt` |
| `video_capture.py` | Records 30s webcam feed to `logs/capture.avi` |
| `screen_capture.py` | Records entire screen to `logs/screen_record.avi` |
| `main.py`       | Runs all modules simultaneously using threading |

---

## 🛠️ Installation

### ✅ Requirements

Python 3.8+ is recommended.

Install required packages:

```bash
pip install -r requirements.txt

Dependencies include:

pynput

opencv-python

numpy

mss



💻 Usage
From the project directory:

"python main.py"

This will:

Start logging keystrokes immediately

Capture 30 seconds of webcam video

Begin continuous screen recording (press Ctrl + C to stop)

All logs are saved in the logs/ folder

⚠️ Disclaimer
This project is intended only for:

🧪 Local testing

🖥️ Virtual environments

🧑‍💻 Cybersecurity learning

❌ Never use this outside of legal, controlled, and consensual environments.
Unauthorized use may violate privacy laws, terms of service, and ethical guidelines.

📘 Author Note
If you're a student, researcher, or security analyst — this project is designed to help you understand how surveillance tools work from a defensive perspective.

Stay ethical. Stay curious. 💻🔐
