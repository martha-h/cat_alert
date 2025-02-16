# Cat Alert Application
When my cat wants to go inside she has a habit of popping up in one of the windows in the kicthen. If I am not in the kicthen, I will have no idea that my cat wants to go inside, and she must remain ouside in the cold. That is a recipe for a grumpy cat! So I thought, how can I be alerted when my cat wants to go inside, regardless of where I am inside the house? <br />

The solution I present is a camera pointed towards her favourite pop up spot, a default YOLOv8 model, trained on COCO dataset running object detection with a filter for the class ID representing cats, and a Flask application sending alerts out on the local WiFi Network. The camera will stream video, and read frames based on an interval. The detection algorithm will then run a prediction on said frames and check if any cat detections are registered. If the model has indeed detected a cat, an alert will be sent to a message updater, which again will updated the message which will be visible in a Flask web application. Since the flask application runs on the local WiFi network, anyone with accsess to this network may actually let the cat inside! My cat will never be grumpy again! Or maybe not, since she is a cat after all....

## Getting started
- Create python virtual environment: `python -m venv venv`
- Activate the virtual environment (Windows): `.\venv\Scripts\activate`
- Install the required libraries: `pip install -r requirements.txt`

## Before Running the Application
Ensure you have a camera connected to the machine running the SW with USB. <br />
Alternatively you may run the code with a video .mp4 file. Simply change the value of the video stream variable in src/config.py to be your video file location. <br />
Current state of the program will only allow video files, or live camera feedback for a maximum of 60 seconds. This will be improved in future updates of the code. <br />

## Running the Application
- Run the code using the following command: `python main.py` <br />
- Go to the IP specified in the code and refresh the web page to get the updated messages (default is localhost/loopback address).

To end the Flask application run the Ctrl+C command in the terminal where you run the code. 

You will also find some saved annotated frames, if you get any detections with your input data, in a folder called 'data', which will be created when you start the code. 