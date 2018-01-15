#!/usr/bin/env python

import pigpio
from time import sleep

PIN = 25

pi = pigpio.pi()
pi.set_mode(PIN, pigpio.OUTPUT)

try:
    while True:
        pi.write(PIN, 1)
        sleep(0.5)
        pi.write(PIN, 0)
        sleep(0.5)

except KeyboardInterrupt:
    pass

pi.set_mode(PIN, pigpio.INPUT)
pi.stop()
