# Stdlib imports
import threading
import queue
import atexit

# Local imports
from src import log
from src.config import *
from src.capture import capture_thread
from src.model import prediction_thread
from src.message import update_msg

# Create list for holding active threads
threads = []

def create_threads():
    # Initialize thread components
    image_queue = queue.Queue()
    detection_event = threading.Event()
    stop_event = threading.Event()

    # Initialize capture thread
    capture = threading.Thread(name='capture-thread',
                               target=capture_thread,
                               args=(stop_event,
                                     image_queue,
                                     FRAME_TIME_INTERVAL,
                                     CAPTURE_SOURCE))
    threads.append(capture)
    
    # Initialize prediction thread 
    predict = threading.Thread(name='predict-thread',
                               target=prediction_thread,
                               args=(stop_event,
                                     detection_event, 
                                     image_queue,
                                     MODEL_NAME,
                                     CLASS_ID_LIST,
                                     CONFIDENCE_THRESHOLD,
                                     THREAD_INTERVAL,
                                     ANNOTATES_FRAMES_DIR))
    threads.append(predict)
    
    update = threading.Thread(name='alert-thread',
                             target=update_msg,
                             args=(stop_event,
                                   detection_event,
                                   THREAD_INTERVAL))
    threads.append(update)
    
    for t in threads:
        log.info(f"Starting {t.getName()}.")
        t.start()

@atexit.register
def cleanup():
    log.info("Cleaning up")
    for t in threads:
        if t.is_alive():
            t.join()