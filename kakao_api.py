import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

KAKAO_TOKEN = os.getenv('KAKAO_TOKEN')

class KakaoMessageAPI:
    def __init__(self):
        self.url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    def send_message(self, text: str):
        headers = {
            'Authorization': f'Bearer {KAKAO_TOKEN}'
        }

        data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":text,
            "link":{
                "web_url":"www.naver.com"
            }
        })
        }

        response = requests.post(self.url, headers=headers, data=data)
        breakpoint()
        if response.status_code == 200:
            print('메시지 전송 성공!')
        else:
            print('메시지 전송 실패!')