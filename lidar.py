#   This script requires tty port access.
#   $ usermod -a -G dialout username 

#   Python=3.9.0

#   Adfruits repo is not working: https://github.com/dastels/adafruit_rplidar/blob/master/code/rplidar.py
#   This is working: https://github.com/Roboticia/RPLidar

from math import floor
from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0', baudrate=115200)

scan_data=[0]*360

info = lidar.get_info()
print(info)

health = lidar.get_health()
print(health)

try:

    while True:

        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                scan_data[min([359, floor(angle)])] = distance
                if (floor(angle) > 0 and floor(angle) < 10):
                    print(f"andle: {floor(angle)}, distance: {floor(distance)}")
   
    # for i, scan in enumerate(lidar.iter_scans()):
    #     print('%d: Got %d measurments' % (i, len(scan)))
    #     if i > 10:
    #         break

except KeyboardInterrupt:
    print("Stopping")


lidar.stop()
lidar.stop_motor()
lidar.disconnect()

