# Stdlib imports
import os
from queue import Empty

# External imports
from ultralytics import YOLO
from numpy import array
from cv2 import imwrite

# Local imports
from src import log

class Model:
    """
    A class used to represent a detection model

    ...

    Attributes
    ----------
    model : YOLO object
        the detection model YOLO object
    class_id : list
        list of class IDs for prediction filter
    conf : str
        confidence threshold for preciction filter
    res : list | default = None
        predcition result
    detection_count: int
        counter for detections
    """
     
    def __init__(self, model_name, class_id, confidence_threshold):
        # Initializes the model object
        self.model = YOLO(model_name)
        self.class_id = class_id
        self.conf = confidence_threshold
        self.res = None
        self.detection_count = 0

    def predict(self, frame):
        # Performs prediction and sets the res attribute
        self.res = self.model(frame, 
                        verbose=False, 
                        conf=self.conf,
                        classes=self.class_id)
    
    def get_annotated_frame(self):
        # Returns annotated frame from res attribute
        return self.res[0].plot()
    
    def get_detection_array(self):
        # Returns list of detections from result attribute
        return array(self.res[0].boxes.conf.cpu())
    


def prediction_thread(stop_event, 
                      detection_event, 
                      image_queue, 
                      model_name, 
                      class_id,
                      confidence_threshold, 
                      time_interval,
                      annotated_frames_dir):
    
    # Initialize model object
    model = Model(model_name, class_id, confidence_threshold)

    # Create directory
    os.makedirs(annotated_frames_dir, exist_ok=True)

    # Start prediction loop
    while not stop_event.is_set():
        try:
            # Waits 0.1 second for queue item
            frame = image_queue.get(timeout=time_interval)

            # Run prediction
            model.predict(frame)

            # Check for valid predictions
            if len(model.get_detection_array()) > 0 and not detection_event.is_set():
                log.info("Detected object, setting event.")
                # Update detection event
                detection_event.set()

                # Save image with annotations
                model.detection_count += 1
                imwrite(f'{annotated_frames_dir}/detection{model.detection_count}.jpg', 
                        model.get_annotated_frame())

            else:
                log.info("No detections, clearing event.")
                # Clear detection event
                detection_event.clear()
            
            # Remove item from queue
            image_queue.task_done()

        # continues if queue is empty
        except Empty:
            continue

    log.info("Prediction thread ended.")
    return