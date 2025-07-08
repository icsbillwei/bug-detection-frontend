# YOLO-based Bug Detector App
An app that allows you to see if there are insects in your household, through a video stream.

This is the frontend portion of the App, backend is at [https://github.com/icsbillwei/bug-detection-frontend](https://github.com/icsbillwei/bug-detection-backend/)

## Description
As we go deeper into the summer (As of July 2025), bugs are becoming a more common occurence in households. To study the time period in which they appear and more importantly, to take notice of pests such as cockroaches so you can take action as early as possible, I created this app that detects and summerizes bug occurences into a dashboard on a website.

This app utilizes a custom trained model based on YOLOv8 medium to detect occurences of insects through an internet video stream. The dataset used for the training is https://universe.roboflow.com/maximilian-sittinger/insect_detect_detection/dataset/3 . When the backend detects any occurences of an insect, it updates a list of detections. The Flask frontend periodically fetches data and updates it and display the bug occurences on the website. 

## How To Use
### Step 1: Set up a live video stream of the bug camera

The bug detector app takes in a video stream from an URL, so any method that streams a video feed of the area that you want to detect bugs would work. I used a Raspberry Pi Connected to a GoPro camera, then created a stream using the Motion camera app running on the Pi (https://www.motioncamapp.com/). There should also be a large variety of apps that allows you to use a smartphone camera for this.

Place the camera relatively close to the area you are monitoring, to make the insects identifiable on the camera.

### Step 2: Set up the backend

Follow the instructions at [https://github.com/icsbillwei/bug-detection-frontend](https://github.com/icsbillwei/bug-detection-backend/)

### Step 3: Set up the frontend

- Clone/Download this repo
- Set up and activate a Python venv
- Set up the dependencies by running `pip install flask flask-cors`
- Start the Flask server by running `python server.py`. Ctrl+clicking the URL that is shown to you to access the website
Whenever the camera catches a bug, the image and timestamp should appear on the website.
