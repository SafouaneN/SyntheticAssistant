import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse
from csv_helper import write_event_to_csv 
start_time = timeit.default_timer()
current_event = '' 
def on_press(key, csv_filename,Id):
    global current_event

    try:
        # Print the pressed key
        print(f'Key pressed: {key}')

        # Check if Space or Backspace is pressed
        if key == keyboard.Key.space or key == keyboard.Key.backspace:
            # Write the current event to the CSV file
            if current_event:
                write_event_to_csv(current_event,csv_filename,Id)
            current_event = []
        else:
            # Concatenate the pressed key to the current event
            if key.char is not None:
                current_event.append(key.char)
            else:
                current_event.append(f'<{key.value}>')  # Handle non-character keys

    except AttributeError:
        # Handle special keys like 'Ctrl', 'Shift', etc.
        print(f'Special Key pressed: {key}')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv(['KeyPress', str(key), '', '', 0, elapsed_time],csv_filename,Id)

def on_release(key,csv_filename,Id):
    # Stop the listener if the 'Esc' key is pressed
    if key == keyboard.Key.esc:
        # Write the current event to the CSV file before stopping
        if current_event != '':
            write_event_to_csv(current_event,csv_filename,Id)
        return False

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv(['KeyRelease', str(key), '', '', 0, elapsed_time],csv_filename,Id)