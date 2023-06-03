import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse
from csv_helper import write_event_to_csv 
from mouse_helper import on_move,on_click,on_scroll
from keyboard_helper import on_press,on_release
from mac_record_screen import mac_record_video
from mac_record_screen import generate_csv_file_video
from record_screen import record_video
import threading
import multiprocessing
import uuid

#Id=uuid.uuid4()

def generate_id():
    # Generate a timestamp-based unique Id
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'id_{timestamp}'

def save_id_to_file(id):
    # Save the Id to a file
    with open('id.txt', 'w') as file:
        file.write(id)
def load_id_from_file():
    # Load the Id from the file
    if os.path.exists('id.txt'):
        with open('id.txt', 'r') as file:
            return file.read().strip()
    else:
        return None
def generate_csv_filename():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'events_{timestamp}.csv'


current_event = ''  # Variable to store the current event
csv_filename = generate_csv_filename()
# Threading event for synchronization
# Threading lock for synchronization

on_click.last_click = None
def start_listener(Id):
    global start_time

    # Create the CSV file if it doesn't exist
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Event Type', 'Button', 'X', 'Y', 'Scroll Amount', 'Elapsed Time','Id'])

    print('Listening to mouse and keyboard events. Press ESC to stop and save the CSV file.')

    # Create mouse and keyboard listeners
    mouse_listener = mouse.Listener(on_move=lambda x, y: on_move(x, y, csv_filename,Id), on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, csv_filename,Id), on_scroll=lambda x, y, dx, dy: on_scroll(x, y, dx, dy,csv_filename,Id))
    keyboard_listener = keyboard.Listener(on_press=lambda key: on_press(key, csv_filename,Id), on_release=lambda key: on_release(key, csv_filename,Id))
    # start recording the video

    # Start the listeners
    mouse_listener.start()
    time.sleep(1)
    keyboard_listener.start()

    # Record the start time
    start_time = timeit.default_timer()

    # Wait for the 'Esc' key to stop the listeners
    keyboard_listener.join()

    # Stop the mouse listener
    mouse_listener.stop()

    # Save the CSV file
    print('Saving the CSV file...')
    mouse_listener.join()  # Wait for the mouse listener to stop before saving the file

    print('CSV file saved.')

def start_video_recording():
    if os.name == 'posix':
        mac_record_video()  # For Unix or MacOS
    else:
        record_video()  # For other operating systems

def generate_csv_and_start_recording(Id):
    generate_csv_file_video(Id)

if __name__ == '__main__':
    # Load the Id from the file or generate a new one
    Id = load_id_from_file()
    if Id is None:
        Id = generate_id()
        save_id_to_file(Id)
    # Create a process for event handling
    process1 = multiprocessing.Process(target=start_listener, args=(Id,))
    process1.start()

    # Wait for process1 to complete initialization
    #time.sleep(1)

    # Create a process for screen recording
    process2 = multiprocessing.Process(target=start_video_recording)
    process2.start()

    # Create a process for CSV generation
    process3 = multiprocessing.Process(target=generate_csv_and_start_recording, args=(Id,))
    process3.start()

    # Wait for process1, process2, and process3 to complete
    process1.join()
    process2.join()
    process3.join()


