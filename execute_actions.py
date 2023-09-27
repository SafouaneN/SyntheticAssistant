import pyautogui
import time
import PIL.ImageGrab

def execute_action(step, prediction):
    global screenshot
    x = prediction['x']
    y = prediction['y']
    width = prediction['width']
    height = prediction['height']
    screenshot = PIL.ImageGrab.grab()
    screen_width, screen_height = pyautogui.size()
    x_factor = screen_width / screenshot.width
    y_factor = screen_height / screenshot.height
    screen_x = int(x * x_factor)
    screen_y = int(y * y_factor)
    middle_x = screen_x + int(width * x_factor / 2)
    middle_y = screen_y + int(height * y_factor / 2)

    current_action = step["action"]
    current_target = step["target_object"]
            
    if current_action == "click":
        if current_target == "unread_email":
            pyautogui.moveTo(middle_x - 200, middle_y)
            pyautogui.click()
            # Wait for the meeting window to open (adjust the delay as needed)
            time.sleep(2)
            # Press Command+A (select all)
            pyautogui.hotkey('command', 'a')
            time.sleep(2)
            # Press Command+C (copy)
            pyautogui.hotkey('command', 'c')

        else:
            pyautogui.moveTo(middle_x, middle_y)
            time.sleep(1)
            pyautogui.click()

    elif current_action == "click_then_type":
        pyautogui.moveTo(middle_x, middle_y)
        pyautogui.click()
        time.sleep(2)
        pyautogui.typewrite(step["text"])
        time.sleep(2)
        pyautogui.press('enter')
    
    elif current_action == "copy_gpt":
        pyautogui.moveTo(middle_x, middle_y)
        pyautogui.click()
        time.sleep(2)
        pyautogui.typewrite(step["text"])
        time.sleep(2)
        pyautogui.press('enter')

    elif current_action == "click_then_paste":
        pyautogui.moveTo(middle_x, middle_y)
        pyautogui.click()
        time.sleep(1)  
        pyautogui.hotkey('command', 'v')  

    elif current_action == "click_type":
        pyautogui.moveTo(middle_x, middle_y - 20)
        pyautogui.click()
        time.sleep(2) 
        pyautogui.typewrite(step["text"])
        time.sleep(3)
        pyautogui.hotkey('command', 'v')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.hotkey('command', 'shift', 'c')
        time.sleep(1)
