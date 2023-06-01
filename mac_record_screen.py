import numpy as np
import cv2
from mss import mss
import datetime
import csv
import time
import pyautogui

def record_video():
    #SCREEN_SIZE = (2880, 1800)
    screen_width, screen_height = pyautogui.size()
    
    SCREEN_SIZE = (2*screen_width,2*screen_height)

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    out = cv2.VideoWriter('output.mp4', fourcc, 60, SCREEN_SIZE)

    with mss() as sct:
        monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}

        while True:
            last_time = time.time()

            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            out.write(img)

            print("fps: {}".format(1 / (time.time() - last_time)))

            if cv2.waitKey(2) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    out.release()

# Call the function to start recording
#record_video()
def generate_csv_file_video(Id):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = "Timestamp_video.csv"
    with open(filename, 'w', newline='') as file:
        # Create a CSV writer object
        print("yo")
        writer = csv.writer(file)
        writer.writerow(['Timestamp_video',"id" ])
        writer.writerow([timestamp, Id])