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


def generate_csv_filename():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'events_{timestamp}.csv'


current_event = ''  # Variable to store the current event
csv_filename = generate_csv_filename()

on_click.last_click = None
def start_listener():
    global start_time

    # Create the CSV file if it doesn't exist
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Event Type', 'Button', 'X', 'Y', 'Scroll Amount', 'Elapsed Time'])

    print('Listening to mouse and keyboard events. Press ESC to stop and save the CSV file.')

    # Create mouse and keyboard listeners
    mouse_listener = mouse.Listener(on_move=lambda x, y: on_move(x, y, csv_filename), on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, csv_filename), on_scroll=lambda x, y, dx, dy: on_scroll(x, y, dx, dy,csv_filename))
    keyboard_listener = keyboard.Listener(on_press=lambda key: on_press(key, csv_filename), on_release=lambda key: on_release(key, csv_filename))

    # Start the listeners
    mouse_listener.start()
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


if __name__ == '__main__':
    start_listener()
