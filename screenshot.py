import PIL.ImageGrab
import tempfile
import pyautogui
import shutil
import os

def capture_and_save():
    # Capture the screenshot
    screenshot = PIL.ImageGrab.grab()

    # Save it to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        screenshot.save(temp_file.name)

        # Path where you want to save the screenshot
        path_to_save = "prediction.jpg"

        # Copy from the temporary file to the desired location
        shutil.copy(temp_file.name, path_to_save)

        # Remove the temporary file
        os.remove(temp_file.name)
#capture_and_save()
def movetest():
    pyautogui.moveTo(1242,1221.5)
    x,y=pyautogui.size()
    z= PIL.ImageGrab.grab()

    print(x,y,z.width,z.height)

movetest()