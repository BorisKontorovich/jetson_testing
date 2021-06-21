import board
from digitalio import DigitalInOut, Direction, Pull
import busio
import adafruit_vl53l0x

import time


led = DigitalInOut(board.D4)
led.direction = Direction.OUTPUT

led_state = False

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:

    if led_state == False:
        led_state = True
    elif led_state == True:
        print(f"Range {vl53.range}")
        led_state = False

    led.value = led_state
        
    time.sleep(1)
