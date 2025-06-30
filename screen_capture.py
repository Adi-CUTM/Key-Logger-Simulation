import cv2
import numpy as np
import mss
import os
from datetime import datetime

def start_screen_record():
    # Define logs directory
    log_dir = r'E:\Saved Games\key-logger-simulation\logs'
    os.makedirs(log_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = os.path.join(log_dir, f'screen_record_{timestamp}.avi')

    # Get screen dimensions
    sct = mss.mss()
    monitor = sct.monitors[1]  # Primary screen (monitor[0] is full virtual screen)
    width, height = monitor["width"], monitor["height"]

    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 10.0, (width, height))

    print("[*] Screen recording started. Press Ctrl + C to stop.")

    try:
        while True:
            img = np.array(sct.grab(monitor))
            frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
            out.write(frame)
    except KeyboardInterrupt:
        print("[!] Screen recording manually stopped.")
    except Exception as e:
        print(f"[!] Unexpected error during screen capture: {e}")
    finally:
        out.release()
        cv2.destroyAllWindows()
        print(f"[*] Screen recording saved to: {filename}")
