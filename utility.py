import tempfile

def temp_file():
    return tempfile.NamedTemporaryFile(suffix=".png", delete=False)
