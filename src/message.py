# Stdlib imports
import time

# Local imports
from src import log
from src.config import ALERT

def update_msg(stop_event, detection_event, time_interval):
    # Start alert loop
    while not stop_event.is_set():

        # Check for detection event
        if detection_event.is_set():
            ALERT['msg'] = 'Cat wants to go inside!'
            log.info('Setting new message in alert dictionary.')

        time.sleep(time_interval)

    log.info("Message thread ended.")
    return