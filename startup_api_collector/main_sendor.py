import requests
import json
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv

# What time is now?
# TODO: 수집 시간 출력하기
load_dotenv()
Bearer = os.getenv("Bearer")

import requests

total_data = []

for page in range(1, 24+1):
    headers = {
        'accept': 'application/json',
        'accept-language': 'ko,ko-KR;q=0.9,en-HK;q=0.8,en;q=0.7',
        'authorization': f'Bearer {Bearer}',
        'origin': 'https://www.innoforest.co.kr',
        'priority': 'u=1, i',
        'referer': 'https://www.innoforest.co.kr/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'withcredentials': 'true',
    }

    params = {
        'page': page,
        'limit': '20',
        'keyword': '',
        'orderByField': '',
        'bizArray': '',
        'invstCdArray': '',
        'tagArray': '',
        'tagText': '',
        'userCd': 'S',
        'invstCdFrom': '',
        'invstCdTo': '',
        'invstWholeValFrom': '',
        'invstWholeValTo': '',
        'invstFrom': '',
        'invstTo': '',
        'empFrom': '',
        'empTo': '',
        'salesFrom': '',
        'salesTo': '',
        'provinceArray': '',
        'isHiring': '',
        'isRecommendHiring': '1',
    }

    response = requests.get('https://liveapi.innoforest.co.kr/seed/corp/v1/findseedcorpsummary', params=params, headers=headers)
    print(response.status_code)
    data = response.json()
    for item in data['data']:
        headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko,ko-KR;q=0.9,en-HK;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'ch-veil-id=653b51f6-d31d-46ef-af61-5a95737f62b2; _fbp=fb.2.1727949011796.972566983740072597; _gcl_au=1.1.774798477.1727949012.1563420254.1731859224.1731859457; _gid=GA1.3.1968521037.1732431690; mp_3c8e1b624161b16b50fc050786126000_mixpanel=%7B%22distinct_id%22%3A%20%2219251c97473bcc-0c59db4ce203a-10462c6f-1fa400-19251c974742b2%22%2C%22%24device_id%22%3A%20%2219251c97473bcc-0c59db4ce203a-10462c6f-1fa400-19251c974742b2%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22__alias%22%3A%20%22US00080406%22%2C%22%24user_id%22%3A%20%22US00080406%22%7D; _ga=GA1.3.14185573.1727949012; _ga_Y5PFR0B8JJ=GS1.3.1732431690.12.1.1732433429.60.0.0; _ga_QHNBKM5GY1=GS1.1.1732458647.15.1.1732458654.53.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
        response = requests.get(
    f'https://www.innoforest.co.kr/company/{item["corpId"]}',
    headers=headers,
)       
        print(response.status_code)
        parm_text = response.text
        korea_addr = parm_text.split('corpAddrKr":"')[1].split('"')[0]
        item.update({'korea_addr': korea_addr})
    print(data['data'])
    total_data.extend(data['data'])


pd.DataFrame(total_data).to_csv("test.csv")
