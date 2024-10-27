import logging

def set_logging(level=logging.INFO):
    logging.basicConfig(                                                      
        level=logging.INFO, format="%(name)s - %(asctime)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(level)