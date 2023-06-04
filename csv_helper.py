import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse
def write_event_to_csv(event,csv_filename,Id):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        event.append(str(Id))
        writer.writerow( event)
