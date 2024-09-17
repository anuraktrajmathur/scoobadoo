import logging
import time
from frank_manager import bring_to_life
import sys
from sensors_actuators.engine import Engine
from sensors_actuators.proximity import Proximity
from sensors_actuators.camera import RecognizedObject

def main():
    
    logging.warning("init frank")
    bring_to_life.init()

    #---Engine Example---#
    engine = Engine()        # Instantiate the class
    engine.start_left(30)    # Function to manage the left motor
    engine.start_right(30)   # Function to manage the right motor
    engine.stop_left()       # Function to stop the left motor
    engine.stop_right()      # Function to stop the right motor

    #---Proximity Sensor Example---#
    # proximity = Proximity()
    # distance = proximity.get_btm_distance()  # Only the bottom sensor is usable. No front sensors are available

    # recognized_object = RecognizedObject()
    # block = recognized_object.get_recognized_object()
    # control the engines

    while True:
        logging.debug("main do somethings")
        time.sleep(10)

if __name__ == '__main__':

    # logger = logging.getLogger(__name__)
    # logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
