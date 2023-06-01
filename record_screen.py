import cv2
import pyautogui
from PIL import Image
import datetime
import numpy as np
import csv
import uuid
import os
import threading
#os.chdir(r"C:\Users\LENOVO\Documents\Studium\SoSe23\Computer vision project\secret_capture")

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{time_stamp}.mp4'



# Set the screen recording parameters

def record_video():
    #define screen dimensions
    screen_width, screen_height = pyautogui.size()
    #define timestamp
    output_file = filename
    fps = 20.0
    
    # Load custom mouse pointer image with transparent background
    custom_pointer_image = Image.open("icons8-3d-pointer-50.png").convert("RGBA")
    
    # Define the video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (screen_width,screen_height))


    while True:
        # Capture the screen frame
        img = pyautogui.screenshot()

        # Convert the image to RGBA format
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2RGBA)

        # Get the mouse position
        mouse_position = pyautogui.position()

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Overlay the custom mouse pointer image on the frame
        frame_pil = Image.fromarray(frame)
        frame_pil.paste(custom_pointer_image, (mouse_position[0], mouse_position[1]), custom_pointer_image)

        # Convert the frame back to BGR format
        frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGBA2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow("Screen Recording", frame)

        # Stop recording when 'q' is pressed
        if cv2.waitKey(1) == 27:
            break
    
        # Release the video writer and close windows
    out.release()
    cv2.destroyAllWindows()

    
def generate_csv_file_video(Id):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = "Timestamp_video.csv"
    with open(filename, 'w', newline='') as file:
        # Create a CSV writer object
        print("yo")
        writer = csv.writer(file)
        writer.writerow(['Timestamp_video',"id" ])
        writer.writerow([timestamp, Id])

""" if __name__ == '__main__':
    record_video()
    generate_csv_file_video() """






