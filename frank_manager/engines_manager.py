from collections import deque
import time
import logging
import RPi.GPIO as GPIO


def forward(pin1, pin2):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    logging.info("forward")


def backward(pin1, pin2):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    logging.info("backward")


def stop(pin1, pin2):
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.LOW)
    logging.info("stop")


def engines_main(config, engine_left_queue: deque, engine_right_queue: deque):
    #set pin enumeration
    GPIO.setmode(GPIO.BCM)
    if config.frank.engine_lx_enable:
        GPIO.setup(config.pinout.l298n_engine_lx_in1, GPIO.OUT)
        GPIO.setup(config.pinout.l298n_engine_lx_in2, GPIO.OUT)
        GPIO.setup(config.pinout.l298n_engine_lx_ena, GPIO.OUT)
        #turn off engines
        GPIO.output(config.pinout.l298n_engine_lx_in1, GPIO.LOW)
        GPIO.output(config.pinout.l298n_engine_lx_in2, GPIO.LOW)
        pwm_control_lx = GPIO.PWM(config.pinout.l298n_engine_lx_ena, config.engines_param.l298n_engine_lx_ena_pwm_frequency)
        pwm_control_lx.start(0)
    
    if config.frank.engine_rx_enable:
        GPIO.setup(config.pinout.l298n_engine_rx_in3, GPIO.OUT)
        GPIO.setup(config.pinout.l298n_engine_rx_in4, GPIO.OUT)
        GPIO.setup(config.pinout.l298n_engine_rx_enb, GPIO.OUT)
        #turn off engines
        GPIO.output(config.pinout.l298n_engine_rx_in3, GPIO.LOW)
        GPIO.output(config.pinout.l298n_engine_rx_in4, GPIO.LOW)
        pwm_control_rx = GPIO.PWM(config.pinout.l298n_engine_rx_enb, config.engines_param.l298n_engine_rx_enb_pwm_frequency)
        pwm_control_rx.start(0)
        
    logging.info('engines main')

    while True:

        if config.frank.engine_lx_enable and len(engine_left_queue) != 0:
            duty = engine_left_queue.pop()
            logging.info(f"main engine left: {duty/0.6}")
            
            #at moment we consider only positive value for duty
            duty = abs(duty)

            if duty == 0:
                stop(config.pinout.l298n_engine_lx_in1, config.pinout.l298n_engine_lx_in2)
                pwm_control_lx.ChangeDutyCycle(0)
            elif duty > 0:
                forward(config.pinout.l298n_engine_lx_in1, config.pinout.l298n_engine_lx_in2)
                pwm_control_lx.ChangeDutyCycle(duty)
            else:
                backward(config.pinout.l298n_engine_lx_in1, config.pinout.l298n_engine_lx_in2)
                pwm_control_lx.ChangeDutyCycle(abs(duty))

        if config.frank.engine_rx_enable and len(engine_right_queue) != 0:
            duty = engine_right_queue.pop()
            logging.info(f"main engine right: {duty/0.6}")

            #at moment we consider only positive value for duty
            duty = abs(duty)

            if duty == 0:
                stop(config.pinout.l298n_engine_rx_in3, config.pinout.l298n_engine_rx_in4)
                pwm_control_rx.ChangeDutyCycle(0)
            elif duty > 0:
                forward(config.pinout.l298n_engine_rx_in3, config.pinout.l298n_engine_rx_in4)
                pwm_control_rx.ChangeDutyCycle(duty)
            else:
                backward(config.pinout.l298n_engine_rx_in3, config.pinout.l298n_engine_rx_in4)
                pwm_control_rx.ChangeDutyCycle(abs(duty))

        time.sleep(0.3)
