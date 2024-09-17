import logging
import requests
import frank_manager.bring_to_life

class Engine:
    def __init__(self, api_url="http://192.168.1.12:8000/engine"):
        self.api_url = api_url
        self.d = 0.6
        logging.debug(f"Engine class initialization")

    def _send_post_request(self, duty_cicle_lx: int, duty_cicle_rx: int):
        payload = {
            "duty_cicle_lx": duty_cicle_lx,
            "duty_cicle_rx": duty_cicle_rx
        }
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"POST request sent successfully: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error sending POST request: {e}")

    def start_left(self, power_percentage: int):
        duty_to_send = int(power_percentage * self.d)
        frank_manager.bring_to_life.engine_left_queue.append(duty_to_send)
        self._send_post_request(duty_cicle_lx=duty_to_send, duty_cicle_rx=self.get_right_duty())

    def start_right(self, power_percentage: int):
        duty_to_send = int(power_percentage * self.d)
        frank_manager.bring_to_life.engine_right_queue.append(duty_to_send)
        self._send_post_request(duty_cicle_lx=self.get_left_duty(), duty_cicle_rx=duty_to_send)

    def stop_left(self):
        frank_manager.bring_to_life.engine_left_queue.append(0)
        self._send_post_request(duty_cicle_lx=0, duty_cicle_rx=self.get_right_duty())

    def stop_right(self):
        frank_manager.bring_to_life.engine_right_queue.append(0)
        self._send_post_request(duty_cicle_lx=self.get_left_duty(), duty_cicle_rx=0)

    def get_left_duty(self):
        # Returns the current duty cycle for the left motor
        return frank_manager.bring_to_life.engine_left_queue[-1] if frank_manager.bring_to_life.engine_left_queue else 0

    def get_right_duty(self):
        # Returns the current duty cycle for the right motor
        return frank_manager.bring_to_life.engine_right_queue[-1] if frank_manager.bring_to_life.engine_right_queue else 0
