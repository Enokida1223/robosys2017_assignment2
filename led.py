#!/usr/bin/env python

import rospy
import time
import pigpio
from time import sleep

PIN = 25
FREQ = 50
RANGE = 100

pi = pigpio.pi()

pi.set_mode(PIN, pigpio.OUTPUT)
pi.set_PWM_frequency(PIN, FREQ)
pi.set_PWM_range(PIN, RANGE)


try:
    a = 0
    b = 20
    while True:
        pi.set_PWM_dutycycle(PIN, a)
        sleep(0.01)
        a += b
        if a >= RANGE or a <= 0:
            b *= -1

except KeyboardInterrupt:
    pass

pi.set_mode(PIN, pigpio.INPUT)
pi.stop()
