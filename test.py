
# Api Call to Peaktime
import requests
import time

while True:
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko,ko-KR;q=0.9,en-HK;q=0.8,en;q=0.7',
    'origin': 'https://www.pieceofcreative.com',
    'priority': 'u=1, i',
    'referer': 'https://www.pieceofcreative.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'travel_agent_url': 'www.pieceofcreative.com',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
}

    params = {
        'start_date': '20250125',
        'end_date': '20250125',
    }

    response = requests.get('https://api.basecamp.team/product/list/2528', params=params, headers=headers)

    response_json = response.json()['list']
    if response_json == []:
        time.sleep(600)
        continue
    import json

    # 카카오톡 API 토큰 정보
    from token import KAKAO_TOKEN
    KAKAO_API_URL = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    # 메시지 전송 함수
    def send_kakao_message():
        headers = {
            'Authorization': f'Bearer {KAKAO_TOKEN}'
        }

        data={
        "template_object": json.dumps({
            "object_type":"text",
            "text":"비엣젯 항공 PeakTime 예약 가능합니다",
            "link":{
                "web_url":"www.naver.com"
            }
        })
    }

        response = requests.post(KAKAO_API_URL, headers=headers, data=data)
        if response.status_code == 200:
            print('메시지 전송 성공!')
        else:
            print(f'메시지 전송 실패: {response.status_code} {response.text}')
    send_kakao_message()

    breakpoint()


    # Parse Data

    # 2025-01-25 bietet
