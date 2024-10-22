import requests
from dotenv import load_dotenv
import os

load_dotenv()

MAKE_COM_WEBHOOK_URL = os.getenv("MAKE_COM_WEBHOOK_URL")


class MakeComApi:
    def __init__(self):
        self.url = MAKE_COM_WEBHOOK_URL
        self.headers = {"Content-Type": "application/json"}

    def send_notification(self, data: dict):

        response = requests.post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print(f"Failed to send notification. Status code: {response.status_code}")
