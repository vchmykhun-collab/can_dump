import serial
import time
import re
import sys

from dump import dump, CanFrame

port = '/dev/tty.usbserial-14430'
baud = 115200

DISPLAY_COLS = 3
DIMM_TIMEOUT = 50

if __name__ == '__main__':
    try:
        s = serial.Serial(port, baud, timeout=1)
        s.flush()
        # start_time = time.time()
        while True:
            if s.in_waiting > 0:
                line = s.readline().decode('utf-8').rstrip()
                # if not line:
                #     continue
                time_delta = time.time()
                line = f"{int(time_delta*10)}"[-5:] +" " + str(line)
                row = re.split(r"\s+", line)
                
                #cut string if there are tailing spaces
                # if not row[-1:][0]:
                #     row = row[:-1]
                
                frame = CanFrame(time=row[0], id=row[1], dlc=row[2], data=row[3:])
                dump(frame, cols=DISPLAY_COLS, dimming_time=DIMM_TIMEOUT)

    except IOError as e:
        print(e)
    except KeyboardInterrupt:
        # quit
        s.close()
        sys.exit()
