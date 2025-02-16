# Stdlib imports
import time

# External imports
import cv2

# Local imports
from src import log

def capture_thread(stop_event, queue, frame_interval, source, max_time):
    # Initialize a video capture object for a given video source
    cap = cv2.VideoCapture(source) 

    # Get frames per second of video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate number of frames for a given time interval
    frame_interval = int(fps * frame_interval)

    # Initialize frame count
    current_frame = 0

    # Set start time
    start_time = time.time()

    # Checking capture object validity
    if not cap.isOpened():
        log.warning("Could not open capture object, setting stop event.")

    else:
        # Start capture frames loop
        while not stop_event.is_set():

            # Check if maximum time reached
            elapsed_time = time.time() - start_time 
            if elapsed_time >= max_time:
                log.warning(f"Max time {max_time} [sec] exceeded, setting stop event.")
                stop_event.set()
                break

            # Read frame
            ret, frame = cap.read()
            if not ret:
                log.warning("Could not read frame, setting stop event.")
                stop_event.set()
                break

            # Check if interval is triggered
            if current_frame % frame_interval == 0:
                log.info("Interval triggered, putting frame in queue.")

                # Update queue
                queue.put(frame)

            # Increase frame count
            current_frame += 1

    log.info("Releasing capture object and setting stop event.")
    
    # Release the video capture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Set event
    stop_event.set()

    log.info("Capture thread ended.")
    return