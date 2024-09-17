import logging
import frank_manager.bring_to_life

class Proximity:  

  def __init__(self):
    ##somehing
    logging.debug(f"class proximity init")

  def get_btm_distance(self):
    return frank_manager.bring_to_life.proximity_sensor_btm_queue.pop()

  def get_front_distance(self):
    return frank_manager.bring_to_life.proximity_sensor_front_queue.pop()
