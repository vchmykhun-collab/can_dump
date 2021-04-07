import sys
import time
# from collections import deque

RELOAD_TIMEOUT = 50

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def timeMillis():
  return int(round(time.time() * 1000))


class CanFrame:
  def __init__(self, time, id, dlc, data):
    self.time = time
    self.id = id
    self.dlc = dlc
    self.data = data 

    self.prev_data = []
    self.highlight_expiration = None

  def __str__(self):
    _data = self.data
    _highlight = False
    if self.prev_data and self.highlight_expiration > timeMillis():
        _highlight = True
        highlight = lambda a, b: f"{bcolors.WARNING}" + a + f"{bcolors.ENDC}" if a!=b else a
        _prev_data = self.prev_data
        if len(_prev_data) < len(self.data): #@workaround
          _prev_data = _prev_data + ['  '] * (len(self.data) - len(_prev_data))
          
        _data = [highlight(_prev_data[i], xx) for i, xx in enumerate(self.data)]
    
    _data_str = ' '.join(_data + ['  '] * (8 - len(self.data)))
    
    highlight_row = lambda x: f"\x1b[0;30;43m{x}\x1b[0m" if _highlight else f"{bcolors.OKBLUE}{x}{bcolors.ENDC}"
    _time = f"{bcolors.BOLD}{self.time}{bcolors.ENDC}"

    return f"{_time} {highlight_row(self.id)}: {self.dlc} {_data_str}"
    
  __repr__ = __str__

queue = []
ids = {}

prev_time = 0

def dump(obj: CanFrame, cols=3, dimming_time=1000):
    canid = obj.id
    global prev_time
    
    reload_screen = timeMillis()-prev_time > RELOAD_TIMEOUT
    if reload_screen:
      prev_time = timeMillis()

    if reload_screen:
      # move up cursor and delete whole line
      # for _ in range(len(queue)):
      for _ in range(0, len(queue), cols):
          sys.stdout.write("\x1b[1A\x1b[2K") 

    if ids.get(canid, -1) != -1:
        prev_frame: CanFrame = queue[ids[canid]]
        obj.prev_data = prev_frame.data
        obj.highlight_expiration = timeMillis() + dimming_time
        queue[ids[canid]] = obj
    else:
        queue.append(obj)
        ids[canid] = len(queue)-1

    if reload_screen:
      # reprint the lines
      # for i in range(len(queue)):
      #     line_str = str(queue[i])
      #     sys.stdout.write(line_str + "\n")

      for row_offset in range(0, len(queue), cols):
          sys.stdout.write(' | '.join(str(x) for x in queue[row_offset: row_offset+cols]))
          sys.stdout.write("\n")
