from collections import deque
import time
import logging


def pump_valve_main(pump_queue : deque, valve_queue: deque):

    while True:
        logging.info('pump valve main')
        time.sleep(3)