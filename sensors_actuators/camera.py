import logging
import frank_manager.bring_to_life

class RecognizedObject:  

  def __init__(self):
    ##somehing
    logging.debug(f"recognized object init")

  def get_recognized_object(self):
    return frank_manager.bring_to_life.recognized_object_queue.pop()