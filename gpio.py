import board
from digitalio import DigitalInOut, Direction, Pull
import busio
from adafruit_vl53l0x import VL53L0X

import time



led = DigitalInOut(board.D4)
led.direction = Direction.OUTPUT

i2c_bus = busio.I2C(board.SCL, board.SDA)
vl53 = []

sensor_settings = [ [29, DigitalInOut(board.D20)],
                    [30, DigitalInOut(board.D21)]]


for i in range(len(sensor_settings)):
    print(f"Settings for sensor 1: {sensor_settings[i][0]} {sensor_settings[i][1].}")

for i in range(len(sensor_settings)):
    print(f"Switching pin {i} to output")
    sensor_settings[i][1].switch_to_output(value=False)

    print(f"Adding VL53 #{i} to list")
    vl53.append(VL53L0X(i2c_bus))

    print(f"Setting line for VL53 #{i} to HIGH")
    sensor_settings[i][1].value = True
    
    print(f"Sensor {i} address: {sensor_settings[i][0]}")
    vl53[-1].set_address(sensor_settings[i][0])

led_state = False
time.sleep(5)
print(f"Setup done, entering blinking loop")

while True:

    if led_state == False:
        led_state = True
    elif led_state == True:
        # print(f"Range {vl53.range}")
        led_state = False

    led.value = led_state

    for i in range(len(vl53)):
        print(f"Range {i} is {vl53[i].range}")
        
    #time.sleep(1)
