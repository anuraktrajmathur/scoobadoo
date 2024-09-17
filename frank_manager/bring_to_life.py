from http.server import HTTPServer
import os
from pathlib import Path
import threading
import logging
from collections import deque
from frank_manager import pump_valve_manager, proximity_manager, hovering_manager, turn_manager, plot_manager, engines_manager, camera_manager
from utils import config, web_server

file_dir = os.path.dirname(os.path.realpath(__file__))
config_path = Path(file_dir + '/../config/configuration.yml')
configuration = config.extract_from_yml(config_path)

proximity_sensor_front_queue = deque([], maxlen=configuration.queue_size.proximity_sensor_front)
proximity_sensor_btm_queue = deque([], maxlen=configuration.queue_size.proximity_sensor_btm)
engine_left_queue = deque([], maxlen=configuration.queue_size.engine_left)
engine_right_queue = deque([], maxlen=configuration.queue_size.engine_right)
pump_queue = deque([], maxlen=configuration.queue_size.pump)
valve_queue = deque([], maxlen=configuration.queue_size.valve)
camera_queue = deque([], maxlen=configuration.queue_size.camera)
recognized_object_queue = deque([], maxlen=configuration.queue_size.recognized_object)

def init():

    #init thread with proximity sensor
    if configuration.frank.ultrasonic_sensor_btm or configuration.frank.ultrasonic_sensor_front:
        proximityThread = threading.Thread(target=proximity_manager.proximity_main, args = (configuration, proximity_sensor_front_queue,proximity_sensor_btm_queue), name="proximityThread")
        proximityThread.daemon=True
        proximityThread.start()
        logging.info("FrankProcess - Starting proximity manager thread")

        #hoveringThread = threading.Thread(target=hovering_manager.hovering_main, args = (configuration, proximity_sensor_front_queue,proximity_sensor_btm_queue), name="hoveringThread")
        #hoveringThread.daemon=True
        #hoveringThread.start()
        #logging.info("FrankProcess - Starting hovering manager thread")

    #init thread with engines
    if configuration.frank.engine_lx_enable or configuration.frank.engine_rx_enable:
        enginesThread = threading.Thread(target=engines_manager.engines_main, args = (configuration, engine_left_queue, engine_right_queue), name="enginesThread")
        enginesThread.daemon=True
        enginesThread.start()
        logging.info("FrankProcess - Starting engines manager thread")

        #turnThread = threading.Thread(target=turn_manager.turn_main, args = (engine_left_queue, engine_right_queue), name="turnThreadThread")
        #turnThread.daemon=True
        #turnThread.start()
        #logging.info("FrankProcess - Starting turnThread manager thread")

    #init thread with pump and valve
    if configuration.frank.pump_enable or configuration.frank.valve_enable:
        pumpValveThread = threading.Thread(target=pump_valve_manager.pump_valve_main, args = (pump_queue, valve_queue), name="pumpValveThread")
        pumpValveThread.daemon=True
        pumpValveThread.start()
        logging.info("FrankProcess - Starting pump valve manager thread")
          

    #init thread with camera
    if configuration.frank.camera_enable:
        cameraThread = threading.Thread(target=camera_manager.camera_main, args = (configuration, camera_queue), name="cameraThreadThread")
        cameraThread.daemon=True
        cameraThread.start()
        logging.info("FrankProcess - Starting cameraThread manager thread")

        ''' cameraDisplayThread = threading.Thread(target=camera_manager.camera_display_frame, args = (configuration, camera_queue), name="cameraDisplayThread")
        cameraDisplayThread.daemon=True
        cameraDisplayThread.start()
        logging.info("FrankProcess - Starting cameraDisplayThread manager thread") '''

        objectRecognitionThread = threading.Thread(target=camera_manager.object_recognition, args = (configuration, camera_queue, recognized_object_queue), name="objectRecognitionThread")
        objectRecognitionThread.daemon=True
        objectRecognitionThread.start()
        logging.info("FrankProcess - Starting objectRecognitionThread manager thread")

    #plotThread = threading.Thread(target=plot_manager.plot_main, args = (proximity_sensor_front_queue,proximity_sensor_btm_queue, config), name="plotThread")
    #plotThread.daemon=True
    #plotThread.start()
    #logging.info("FrankProcess - Starting plot manager thread")



    #setup web server for http req to write directly in the controller queues
    if configuration.frank.web_api_enable:
        wrh=web_server.WebRequestHandler
        wrh.engine_right_queue=engine_right_queue
        wrh.engine_left_queue=engine_left_queue
        wrh.pump_queue=engine_left_queue
        wrh.valve_queue=engine_left_queue
        wrh.proximity_sensor_front_queue = proximity_sensor_front_queue
        wrh.proximity_sensor_btm_queue = proximity_sensor_btm_queue
        wrh.camera_queue = camera_queue

        server = HTTPServer(("0.0.0.0", 8000), wrh)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.socket.close()

    return True