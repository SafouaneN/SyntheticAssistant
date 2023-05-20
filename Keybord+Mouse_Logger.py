import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse


def generate_csv_filename():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f'events_{timestamp}.csv'


current_event = ''  # Variable to store the current event
csv_filename = generate_csv_filename()


def on_move(x, y):
    event_type = 'Move'
    print(f'{event_type} to ({x}, {y})')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv([event_type, '', x, y, 0, elapsed_time])


def on_click(x, y, button, pressed):
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
    write_event_to_csv([time.time(), event_type, button.name if button else '', x, y, 0, elapsed_time])


on_click.last_click = None


def on_scroll(x, y, dx, dy):
    event_type = 'Scroll'
    print(f'{event_type} {(dx, dy)} at ({x}, {y})')

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv([event_type, '', x, y, dy, elapsed_time])


def on_press(key):
    global current_event

    try:
        # Print the pressed key
        print(f'Key pressed: {key}')

        # Check if Space or Backspace is pressed
        if key == keyboard.Key.space or key == keyboard.Key.backspace:
            # Write the current event to the CSV file
            if current_event:
                write_event_to_csv(current_event)
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
    write_event_to_csv(['KeyPress', str(key), '', '', 0, elapsed_time])

    # Check if the F12 key is pressed to exit and save the program
    if key == keyboard.Key.f12:
        exit_listener()


def on_release(key):
    # Stop the listener if the 'Esc' key is pressed
    if key == keyboard.Key.esc:
        # Write the current event to the CSV file before stopping
        if current_event != '':
            write_event_to_csv(current_event)
        return False

    # Calculate the elapsed time
    elapsed_time = timeit.default_timer() - start_time

    # Write the event data to the CSV file
    write_event_to_csv(['KeyRelease', str(key), '', '', 0, elapsed_time])


def write_event_to_csv(event):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow( event)


def start_listener():
    global start_time

    # Create the CSV file if it doesn't exist
    if not os.path.exists(csv_filename):
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Event Type', 'Button', 'X', 'Y', 'Scroll Amount', 'Elapsed Time'])

    print('Listening to mouse and keyboard events. Press ESC to stop and save the CSV file.')

    # Create mouse and keyboard listeners
    mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

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
