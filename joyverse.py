import cv2
import mediapipe as mp
import time
import numpy as np
import csv
import os
import argparse

# Command-line argument parsing
parser = argparse.ArgumentParser(description='Facial Landmark Capture')
parser.add_argument('--capture_interval', type=int, default=3, help='Interval in seconds to capture landmarks')
parser.add_argument('--csv_file', type=str, default='landmarks_data.csv', help='Output CSV file name')
args = parser.parse_args()

# Initialize MediaPipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Create CSV file to store landmark data
csv_file = os.path.join('landmarks_csv', f"{time.strftime('%Y%m%d_%H%M%S')}_{args.csv_file}")


file_exists = os.path.isfile(csv_file)
os.makedirs('landmarks_csv', exist_ok=True)


# Open CSV file once for better performance
with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        header = ["Timestamp"] + [f"x_{i}, y_{i}, z_{i}" for i in range(468)]
        writer.writerow(header)

try:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)

    last_capture_time = time.monotonic()
    capture_interval = args.capture_interval

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Failed to capture image")
            break

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = face_mesh.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                current_time = time.monotonic()
                if current_time - last_capture_time >= capture_interval:
                    landmarks_flattened = [lm.x for lm in face_landmarks.landmark] + \
                                          [lm.y for lm in face_landmarks.landmark] + \
                                          [lm.z for lm in face_landmarks.landmark]

                    # Save to CSV with timestamp
                    with open(csv_file, mode="a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S")] + landmarks_flattened)

                    print("Saved landmark data at:", time.strftime("%Y-%m-%d %H:%M:%S"))
                    last_capture_time = current_time

        cv2.imshow("Face Mesh Landmark Detection", image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

except KeyboardInterrupt:
    print("\nProcess interrupted. Exiting...")
finally:
    cap.release()
    cv2.destroyAllWindows()