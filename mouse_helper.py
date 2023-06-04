import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse
from csv_helper import write_event_to_csv 
#start_time = timeit.default_timer()


def on_move(x, y,csv_filename,Id,start_time):
    event_type = 'Move'
    print(f'{event_type} to ({x}, {y})')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv([event_type, '', x, y, 0, elapsed_time],csv_filename,Id)
def on_click(x, y, button, pressed,csv_filename,Id,start_time):
    if pressed:
        action = 'Pressed'
        if button == mouse.Button.left:
            if on_click.last_click and (time.time() - on_click.last_click) < 0.3:
                event_type = 'Double Click'
                print(f'{event_type} at ({x}, {y}) with {button}')
            else:
                event_type = 'Click'
                print(f'{event_type} at ({x}, {y}) with {button}')
            on_click.last_click = time.time()
        else:
            event_type = 'Click'
            print(f'{event_type} at ({x}, {y}) with {button}')
            on_click.last_click = None
    else:
        event_type = 'Release'
        print(f'{event_type} at ({x}, {y}) with {button}')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv([ event_type, button.name if button else '', x, y, 0, elapsed_time],csv_filename,Id)

def on_scroll(x, y, dx, dy,csv_filename,Id,start_time):
    event_type = 'Scroll'
    print(f'{event_type} {(dx, dy)} at ({x}, {y})')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv([event_type, '', x, y, dy, elapsed_time],csv_filename,Id)
