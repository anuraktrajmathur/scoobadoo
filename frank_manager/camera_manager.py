from collections import deque
import time
import cv2
from neural_network.cameraManager import CameraManager

from neural_network.detectedBlock import DetectedBlock

def camera_main(config, camera_queue: deque):
    # initialize the camera
    myCamHandler = CameraManager()
    myCamHandler.setup()

    freq = cv2.getTickFrequency()
    
    # Let camera warm up
    time.sleep(0.3)

    running = True
    while running:
        start=time.time()

        # Capture frame
        frame = myCamHandler._camera.capture_array()
        camera_queue.append(frame)

        time.sleep(abs(1/config.camera.fps-(time.time()-start)))

        # Exit on 'q' key
        key = cv2.waitKey(1)
        if key == ord("q"):
            print("Quitting")
            break

def object_recognition(config, camera_queue: deque, recognized_object_queue: deque):
    
    # write your code for code recognition
    
    print()