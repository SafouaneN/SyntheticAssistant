import numpy as np
import cv2
from mss import mss
from PIL import Image
import datetime
import csv
import time
import pyautogui

def mac_record_video():
    #SCREEN_SIZE = (2880, 1800)
    screen_width, screen_height = pyautogui.size()
    
    SCREEN_SIZE = (2*screen_width,2*screen_height)

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    out = cv2.VideoWriter(f'{time_stamp}.mp4', fourcc, 20, SCREEN_SIZE)
    # Load custom mouse pointer image with transparent background
    custom_pointer_image = Image.open("icons8-3d-pointer-50.png").convert("RGBA")

    with mss() as sct:
        monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}

        while True:
            last_time = time.time()

            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Overlay the custom mouse pointer image on the frame
            mouse_position = pyautogui.position()
            frame_pil = Image.fromarray(img)
            frame_pil.paste(custom_pointer_image, (mouse_position[0], mouse_position[1]), custom_pointer_image)
            # Convert the frame back to BGR format
            img = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGBA2BGR)
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