import serial
import time
import re

from dump import dump, CanFrame

port = '/dev/tty.usbserial-14640'
baud = 115200

DISPLAY_COLS = 2
STEP_TIMEOUT = 50
DIMM_TIMEOUT = 1000


try:
    s = serial.Serial(port, baud, timeout=0.1)
except IOError as e:
    print (e)

s.flushInput()
while True:
    
    line = s.readline().decode('UTF-8')
    if not line:
        continue
    
    line = "TTT " + str(line)
    row = re.split(r"\s+", line)
    
    #cut string if there are tailing spaces
    if not row[-1:][0]:
        row = row[:-1]
    
    frame = CanFrame(time=row[0], id=row[1], dlc=row[2], data=row[3:])

    dump(frame, cols=DISPLAY_COLS, dimming_time=DIMM_TIMEOUT)