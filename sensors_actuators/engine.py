import logging
import frank_manager.bring_to_life

class Engine:
  

  def __init__(self):
    ##somehing
    logging.debug(f"Engine class initialization")
    self.d = 0.6

  def start_left(self, power_percentage: int):
    duty_to_send = power_percentage*self.d
    frank_manager.bring_to_life.engine_left_queue.append(duty_to_send)

  def start_right(self, power_percentage: int):
    duty_to_send = power_percentage*self.d
    frank_manager.bring_to_life.engine_right_queue.append(duty_to_send)

  def stop_left(self):
    frank_manager.bring_to_life.engine_left_queue.append(0)

  def stop_right(self):
    frank_manager.bring_to_life.engine_right_queue.append(0)