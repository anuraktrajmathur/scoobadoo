from collections import deque
import time
import logging
import random
import RPi.GPIO as GPIO


def proximity_main(config, proximity_sensor_front_queue: deque, proximity_sensor_btm_queue: deque):
    GPIO.setmode(GPIO.BCM)
    if config.frank.ultrasonic_sensor_btm:
        GPIO.setup(config.pinout.ultrasonic_sensor_btm_trig, GPIO.OUT)
        GPIO.setup(config.pinout.ultrasonic_sensor_btm_echo, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    if config.frank.ultrasonic_sensor_front:
        GPIO.setup(config.pinout.ultrasonic_sensor_front_trig, GPIO.OUT)
        GPIO.setup(config.pinout.ultrasonic_sensor_front_echo, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        #if the queue is full automatically is poped left element
        if config.frank.ultrasonic_sensor_btm:
            try:
                distance_btm = get_distance(config.pinout.ultrasonic_sensor_btm_trig, config.pinout.ultrasonic_sensor_btm_echo, config.physics_parameter.sound_speed_in_air)
                proximity_sensor_btm_queue.append(distance_btm)
            except TimeoutError as e:
                logging.error(f"Btm sensor error (e)")
        if config.frank.ultrasonic_sensor_front:
            try:
                distance_front = get_distance(config.pinout.ultrasonic_sensor_front_trig, config.pinout.ultrasonic_sensor_front_echo, config.physics_parameter.sound_speed_in_air)
                proximity_sensor_front_queue.append(distance_front)
            except TimeoutError as e:
                logging.error(f"Front sensor error (e)")
        time.sleep(0.1)

#//!
#//!This routine measures the distance from the sensors to the obstacole.
#//!@param[in] trigger_pin, pin number used to send the signal
#//!@param[in] echo_pin, pin number used to receive the feedback from the obstacole
#//!@param[in] speed_of_sound, costant value related to the speed of sound in air or in water
#//!@param[in] timeout, timeout (in second) used to be sure that an obstacole is near the sensor
#//!@param[out] distance, calculated distance usefull externally
#//!
def get_distance(trigger_pin, echo_pin, speed_of_sound, timeout=1.0):
    
    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.000005)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001) 
    GPIO.output(trigger_pin, GPIO.LOW)
    
    start_time = time.time()
    timeout_time = start_time + timeout
    
    while GPIO.input(echo_pin) == GPIO.LOW:
        if time.time() > timeout_time:
            logging.error("Echo signal not received")
    start_time = time.time()
    while GPIO.input(echo_pin) == GPIO.HIGH:
        if time.time() > timeout_time:
            logging.error("Echo signal did not end")
    end_time = time.time()
    
    duration = end_time - start_time
    duration_us = duration * 1000000
    
    distance = (duration_us * speed_of_sound) / 2
    
    return distance