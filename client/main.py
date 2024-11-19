import requests
import time
import json
import datetime
from backup_screen_ocr_data import backup_screen_ocr_data
from PIL import ImageGrab
from ocrmac import ocrmac

# function to query the local screen-pipe operation.

sp_url = "http://localhost:3030"
backend_url = "http://localhost:8000"



def capture_and_read_text():
    screenshot = ImageGrab.grab()
    annotations = ocrmac.OCR(screenshot).recognize()
    result = " ".join([a[0] for a in annotations])

    return result

def main():
    """Run query on an interval"""

    interval = 90  # seconds

    time.sleep(5)

    while True:
        ocr_text = capture_and_read_text()
        res = {
            "source": "desktop",
            "content": ocr_text
        }
        # send OCR info to server
        print(f"posting request with OCR data: {res}")
        try:
            requests.post(f"{backend_url}/handle_activity", json=res)
            print("request posted")
        except requests.exceptions.Timeout:
            print("Request timed out. Retrying...")
            continue

        print(f"snoozing for {interval} seconds")
        time.sleep(interval)


main()
