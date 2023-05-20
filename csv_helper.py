import csv
import os
import signal
import time
import timeit
from datetime import datetime
from pynput import keyboard, mouse
def write_event_to_csv(event,csv_filename):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow( event)