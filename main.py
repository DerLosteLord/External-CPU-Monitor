import os
import psutil
import time
import serial
import struct



serialcom = serial.Serial('/dev/ttyACM0', 115200)
serialcom.timeout = 0

time.sleep(3)

while True:
    CPULOARD = psutil.cpu_percent()
    print(CPULOARD)
    my_str = str(CPULOARD)
    serialcom.write(bytes(my_str, 'ascii'))
    time.sleep(1)
