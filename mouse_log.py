from pynput.mouse import Button, Controller, Listener
from pynput.keyboard import Key, Listener as KeyboardListener
import time
import csv
import signal
import os

mouse = Controller()


# Define the CSV file header
csv_header = ['Time', 'Event Type', 'Button', 'X', 'Y', 'Scroll Amount']
# Define the CSV file name and path
csv_filename = 'mouse_events.csv'

def on_move(x, y):
# This function is called when the mouse is moved
    event_type = 'Move'
    print(f'{event_type} to ({x}, {y})')

    # Write the event data to the CSV file
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time.time(), event_type, '', x, y,0])

def on_click(x, y, button, pressed):
# This function is called when a mouse button is clicked or released


    if pressed:
        action = 'Pressed'
        if button == Button.left:
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
        
    # Write the event data to the CSV file
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time.time(), event_type, button.name, x, y,0])

on_click.last_click = None

def on_scroll(x, y, dx, dy):
# This function is called when the mouse wheel is scrolled

    event_type = 'Scroll'
    print(f'{event_type} {(dx, dy)} at ({x}, {y})')
    
    # Write the event data to the CSV file
    with open(csv_filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([time.time(), event_type,'', x, y, dy])

def on_press(key):
# This function is called when a esc key is pressed

    if key == Key.esc:
        print('Stopping listener and saving the CSV file.')
        os.kill(os.getpid(), signal.SIGINT)
        return False
    else:
        on_press.count = 0

on_press.count = 0

def start_listener():
    # Write the header to the CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_header)

    print('Listening to mouse events. Press ESC to stop and save the CSV file.')

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener, \
            KeyboardListener(on_press=on_press) as k_listener:
        listener.join()
        k_listener.join()

if __name__ == '__main__':
    start_listener()
