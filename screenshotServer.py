# screenshot_server.py
import platform
from flask import Flask, send_from_directory, request, jsonify
import PIL.ImageGrab
import pyautogui
pyautogui.FAILSAFE = False



app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def take_screenshot():
    screenshot = PIL.ImageGrab.grab()
    screenshot_path = "/home/hellwich/hellwich/lehre/ProjectSelfSupervised/repo2/htcv_ss23project_syntheticassistant/screenshot.png"  # Corrected the folder name
    screenshot.save(screenshot_path)
    return send_from_directory("/home/hellwich/hellwich/lehre/ProjectSelfSupervised/repo2/htcv_ss23project_syntheticassistant", "screenshot.png")
@app.route('/screenshot-sizes', methods=['GET'])
def screenshot_sizes():
    # Taking the screenshot
    screenshot = PIL.ImageGrab.grab()

    # Getting the image size
    image_width, image_height = screenshot.size

    # Getting the screen size using pyautogui
    screen_width, screen_height = pyautogui.size()

    # Return sizes as JSON response
    return jsonify({
        "image_size": {"width": image_width, "height": image_height},
        "screen_size": {"width": screen_width, "height": screen_height}
    })
@app.route('/moveclick', methods=['POST'])
def move_click():
    x = request.json.get('x', 0)
    y = request.json.get('y', 0)
    pyautogui.moveTo(x, y)
    return jsonify({"message": "Moved to ({}, {})".format(x, y)})

@app.route('/click', methods=['POST'])
def click():
    x = request.json.get('x', 0)
    y = request.json.get('y', 0)
    pyautogui.click()
    return jsonify({"message": "Clicked at ({}, {})".format(x, y)})

@app.route('/typewrite', methods=['POST'])
def typewrite():
    text = request.json.get('text', "")
    pyautogui.typewrite(text)
    return jsonify({"message": "Typed '{}'".format(text)})

@app.route('/press', methods=['POST'])
def press():
    key = request.json.get('key', "")
    pyautogui.press(key)
    return jsonify({"message": "Pressed '{}' key".format(key)})

@app.route('/hotkey', methods=['POST'])
def hotkey():
    keys = request.json.get('keys', [])

    # Check the operating system
    if platform.system() == "Linux":
        # Replace "command" with "strg" (Ctrl) if "command" is in the keys
        if "command" in keys:
            keys[keys.index("command")] = "strg"

    pyautogui.hotkey(*keys)
    return jsonify({"message": "Executed hotkey with keys: {}".format(', '.join(keys))})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
