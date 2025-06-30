import cv2
import os

def start_video_recording(filename=r'E:\Saved Games\key-logger-simulation\logs\capture.avi', duration=30):
    os.makedirs(r"E:\Saved Games\key-logger-simulation\logs", exist_ok=True)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[!] Webcam not accessible")
        return

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

    frame_count = 0
    max_frames = duration * 20  # 20 fps

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            frame_count += 1
        else:
            break

    cap.release()
    out.release()
