MODEL_NAME              = 'models/yolov8l.pt'               # YOLO model file name
CLASS_ID_LIST           = [15]                              # COCO Dataset class ID for class filter
CONFIDENCE_THRESHOLD    = 0.2                               # Confidence threshold for confidence filter
FRAME_TIME_INTERVAL     = 3                                 # Time interval between frames [sec]
CAPTURE_SOURCE          = 'videos/video_with_cat.mp4'       # Source for frame capture
ALERT                   = {'msg': 'No alert.'}              # Alert message
HOST_IP                 = '127.0.0.1'                       # Host IP address
HOST_PORT               = 5000                              # Host port
THREAD_INTERVAL         = 0.1                               # Thread sleep interval [sec]
ANNOTATES_FRAMES_DIR    = 'data'                            # Directory for annotated frames                 