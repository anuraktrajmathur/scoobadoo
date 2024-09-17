from collections import deque
import time
import logging
import random


def hovering_main(config, proximity_sensor_front_queue: deque, proximity_sensor_btm_queue: deque):
    
    while True:
        if  config.frank.ultrasonic_sensor_front and len(proximity_sensor_front_queue) != 0:
            logging.info(f"main hovering front:  {proximity_sensor_front_queue.pop()}")
        
        if config.frank.ultrasonic_sensor_btm and len(proximity_sensor_btm_queue) != 0:
            logging.info(f"main hovering btm:  {proximity_sensor_btm_queue.pop()}")

        time.sleep(2)