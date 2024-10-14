# Api Call to Peaktime
import time
import logging
from peaktime_api import PeaktimeAPI
from kakao_api import KakaoMessageAPI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

while True:
    peaktime_api = PeaktimeAPI()
    peaktime_api.set_params({
        'start_date': '20250125',
        'end_date': '20250125',
    })
    plane_name ='jinair'
    if peaktime_api.find_ticket(plane_name) == False:
        logger.info(f"{plane_name} 구매할 수 있는 티켓이 없습니다")
        time.sleep(600)
        continue
    else:
        logger.info("구매할 수 있는 티켓이 있습니다")
        kakao_api = KakaoMessageAPI()
        kakao_api.send_message("구매할 수 있는 티켓이 있습니다")
        break

