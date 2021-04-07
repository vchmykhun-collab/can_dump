import time
import re

from dump import dump, CanFrame

# dump({'Time': 1, 'ID': 1, 'DLC': 2, 'Data': ['00 11 22']})
# dump({'Time': 1, 'ID': 2, 'DLC': 2, 'Data': ['00 11 22']})
# exit()

DISPLAY_COLS = 4
STEP_TIMEOUT = 50
DIMM_TIMEOUT = 1000
fname = "e60_pdc.trc.txt"
# fname = "bmw x5 F15 copy.txt"
with open(fname) as f:
    heading = f.readline()
    columns = re.split(r"\s+", heading)

    while True:
        line = f.readline()
        line = line[:41]
        if not line:
            break
        row = re.split(r"\s+", line)
        
        if not row[-1:][0]:
            row = row[:-1]

        # data = [row[0], row[1], row[2], row[3:]]
        # can_frame = dict(zip(columns, data))
        
        frame = CanFrame(time=row[0], id=row[1], dlc=row[2], data=row[3:])

        dump(frame, cols=DISPLAY_COLS, dimming_time=DIMM_TIMEOUT)
        time.sleep(STEP_TIMEOUT/1000)

