import time
import PIL.ImageGrab
from utility import tempfile
from execute_actions import execute_action
from config import sequence
from roboflow_actions import get_model

def execute_main_sequence():
    model = get_model()
    for email_step in sequence:
        time.sleep(2)
        screenshot = PIL.ImageGrab.grab()
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        screenshot.save(temp_file.name)
        # Adjust prediction confidence for unread_email check
        if email_step["target_object"] == "unread_email":
            prediction_confidence = 0.6  # or whichever value you prefer
        else:
            prediction_confidence = 0 # default confidence level
        
        prediction_result = model.predict(temp_file.name, confidence=prediction_confidence, overlap=30).json()
        found_match = False
        for prediction in prediction_result['predictions']:
            if prediction['class'] == email_step["target_object"]:
                found_match = True
                execute_action(email_step, prediction)
                break

        # Specifically for the first step, if its target_object is "unread_email" and it's not found, return False
        if email_step["target_object"] == "unread_email" and not found_match:
            temp_file.close()
            return False

        temp_file.close()

    # If we reached the end of the loop_sequence without returning early, return True
    return True