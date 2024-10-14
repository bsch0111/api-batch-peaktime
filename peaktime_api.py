import requests 

class PeaktimeAPI:

    def __init__(self):
        self._set_headers()

    def _set_headers(self):
        self.headers = {
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
    
    def _set_url(self, plane_name : str) -> None:
        if plane_name == 'bietet':
            self.url = 'https://api.basecamp.team/product/list/2528'
        elif plane_name == 'jinair':
            self.url = 'https://api.basecamp.team/product/list/2575'
    
    def set_params(self, params : dict) -> None:
        self.params = params

    def get_response(self) -> dict:
        response = requests.get(self.url, headers=self.headers, params=self.params)
        return response
    
    def find_ticket(self, plane_name : str) -> bool:
        self._set_url(plane_name)
        response = self.get_response()
        response_json = response.json()['list']
        

        if plane_name == 'bietet':
            response = self.get_response()
            response_json = response.json()['list']
            if response_json == []:
                return False
            else:
                return True
        elif plane_name == 'jinair':
            if response_json[0]['status_id'] == '3':
                return False
            else:
                return True


