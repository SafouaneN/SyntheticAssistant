import time
from pyautoguifunctions import get_screenshot_from_host
from pyautoguifunctions import move_click_on_host
from pyautoguifunctions import click_on_host
from pyautoguifunctions import typewrite_on_host
from pyautoguifunctions import press_on_host
from pyautoguifunctions import hotkey_on_host
from pyautoguifunctions import get_screenshot_sizes_from_host

def execute_action(step, prediction):
    #global screenshot
    sizes=get_screenshot_sizes_from_host()
    image_width = sizes['image_size']['width']
    image_height = sizes['image_size']['height']
    x = prediction['x']
    y = prediction['y']
    width = prediction['width']
    height = prediction['height']
    screen_width = sizes['screen_size']['width']
    screen_height = sizes['screen_size']['height']
    x_factor = screen_width / image_width
    y_factor = screen_height / image_height
    screen_x = int(x * x_factor)
    screen_y = int(y * y_factor)
    middle_x = screen_x + int(width * x_factor / 2)
    middle_y = screen_y + int(height * y_factor / 2)


    current_action = step["action"]
    current_target = step["target_object"]
            
    if current_action == "click":
        if current_target == "unread_email":
            move_click_on_host(middle_x - 200, middle_y)
            click_on_host(middle_x - 200, middle_y)
            # Wait for the meeting window to open (adjust the delay as needed)
            time.sleep(2)
            # Press Command+A (select all)
            hotkey_on_host(['ctrl', 'a'])
            time.sleep(2)
            # Press Command+C (copy)
            hotkey_on_host(['ctrl', 'c'])

        else:
            move_click_on_host(middle_x, middle_y)
            time.sleep(1)
            click_on_host(middle_x,middle_y)

    elif current_action == "click_then_type":
        move_click_on_host(middle_x, middle_y)
        click_on_host(middle_x,middle_y)
        time.sleep(2)
        typewrite_on_host(step["text"])
        time.sleep(2)
        press_on_host('enter')
    
    elif current_action == "copy_gpt":
        move_click_on_host(middle_x, middle_y)
        click_on_host(middle_x,middle_y)
        time.sleep(2)
        typewrite_on_host(step["text"])
        time.sleep(2)
        press_on_host('enter')

    elif current_action == "click_then_paste":
        move_click_on_host(middle_x, middle_y)
        click_on_host(middle_x,middle_y)
        time.sleep(1)  
        hotkey_on_host(['ctrl', 'v'])  

    elif current_action == "click_type":
        move_click_on_host(middle_x, middle_y - 20)
        click_on_host(middle_x,middle_y)
        time.sleep(2) 
        typewrite_on_host(step["text"])
        typewrite_on_host(step["text"])
        time.sleep(3)
        hotkey_on_host(['ctrl', 'v'])
        time.sleep(2)
        press_on_host('enter')
        time.sleep(10)
        hotkey_on_host(['ctrl', 'shift', 'c'])
        time.sleep(1)
