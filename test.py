# Api Call to Peaktime
import time
import logging
from peaktime_api import PeaktimeAPI
from make_com_api import MakeComApi

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ticket_available = False
SLEEP_TIME = 600

while ticket_available == False:
    
    peaktime_api = PeaktimeAPI()
    peaktime_api.set_params({
        'start_date': '20250125',
        'end_date': '20250125',
    })
    plane_list = ['jinair', 'vietjet']

    for plane_name in plane_list:
        ticket_available = peaktime_api.find_ticket(plane_name)
        if ticket_available == False:
            logger.info(f"{plane_name} 구매할 수 있는 티켓이 없습니다")
            continue
        elif ticket_available == True:
            logger.info(f"{plane_name} 구매할 수 있는 티켓이 있습니다")
            make_com_api = MakeComApi()
            make_com_api.send_notification({
                "plane" : plane_name,
                "message" : f"{plane_name} 구매할 수 있는 티켓이 있습니다"
            })

    time.sleep(SLEEP_TIME)

