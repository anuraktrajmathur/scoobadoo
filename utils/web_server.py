from collections import deque
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
import time
import re
import logging
from urllib.parse import urlparse
from sensors_actuators.engine import Engine


class WebRequestHandler(BaseHTTPRequestHandler):

    engine_left_queue = None
    engine_right_queue = None  
    pump_queue = None
    valve_queue = None
    proximity_sensor_front_queue = None
    proximity_sensor_btm_queue = None
    camera_queue = None
    
    def do_GET(self):
        if re.search('/engine', self.path):
            parsed_path = urlparse(self.path)
            logging.info(f"path: {parsed_path.path}")
            logging.info(f"parsed path: {parsed_path.query}")

        if re.search('/proximity_sensor_btm', self.path):
            value = self.proximity_sensor_btm_queue.pop()
            logging.info(f"web client proximity_sensor_btm: {value}")

        self.wfile.write(self.get_response(value).encode("utf-8"))

    def do_POST(self):
        if re.search('/engine', self.path):
            content_lenght=int(self.headers['Content-Length'])
            data=json.loads(self.rfile.read(content_lenght))
            logging.info(f"web client engine data: {data}")
            
            engine = Engine()
            engine.start_left(int(data['duty_cicle_lx']))
            engine.start_right(int(data['duty_cicle_rx']))
            
            #self.engine_left_queue.append(int(data['duty_cicle_lx'])) OLD VERSION WITHOUT LIMIT
            #self.engine_right_queue.append(int(data['duty_cicle_rx']))

        if re.search('/pump', self.path):
            content_lenght=int(self.headers['Content-Length'])
            data=json.loads(self.rfile.read(content_lenght))
            logging.info(f"web client pump data: {data}")
            
            self.pump_queue.append(int(data['duty_cicle']))

        if re.search('/proximity_sensor', self.path):
            content_lenght=int(self.headers['Content-Length'])
            data=json.loads(self.rfile.read(content_lenght))
            logging.info(f"web client pump data: {data}")
            
            self.proximity_sensor_front_queue.append(int(data['proximity_sensor_front']))
            

        self.wfile.write(self.get_response().encode("utf-8"))
            

    
    def get_response(self,val):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        return json.dumps(
            {
                "msg": val,              
            }
        )