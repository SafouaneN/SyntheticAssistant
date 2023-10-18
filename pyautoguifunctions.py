# docker_helper.py
import requests
import tempfile

def get_screenshot_from_host():
    response = requests.get("http://130.149.93.81:5005/screenshot")
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    with open(temp_file.name, "wb") as f:
        f.write(response.content)
    return temp_file

def move_click_on_host(x, y):
    payload = {"x": x, "y": y}
    response = requests.post("http://130.149.93.81:5005/moveclick", json=payload)
    return response.json()

def click_on_host(x, y):
    payload = {"x": x, "y": y}
    response = requests.post("http://130.149.93.81:5005/click", json=payload)
    return response.json()

def typewrite_on_host(text):
    payload = {"text": text}
    response = requests.post("http://130.149.93.81:5005/typewrite", json=payload)
    return response.json()

def press_on_host(key):
    payload = {"key": key}
    response = requests.post("http://130.149.93.81:5005/press", json=payload)
    return response.json()

def hotkey_on_host(keys):
    payload = {"keys": keys}  # `keys` should be a list
    response = requests.post("http://130.149.93.81:5005/hotkey", json=payload)
    return response.json()

def get_screenshot_sizes_from_host():
    # Making a GET request to retrieve sizes
    response = requests.get("http://130.149.93.81:5005/screenshot-sizes")

    # Ensure the response is successful and return the parsed JSON data
    response.raise_for_status()
    return response.json()