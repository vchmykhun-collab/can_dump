CAN Dump
===

A simple console sniffer for CAN bus traffic using cheap components Arduino Nano and MCP2515.
New messages are appended at the end of a list, repeated messages highlighted.

![alt text](https://github.com/vchmykhun-collab/can_dump/blob/master/assets/sniffer.png?raw=true)

Arduino circuit
===
![alt text](https://github.com/vchmykhun-collab/can_dump/blob/master/assets/can%20dump%20arduino.png.png?raw=true)

Usage
===

Configured with `DISPLAY_COLS` and `DIMM_IMEOUT` variables.

`python3 test_dump.py` - process stored dumps

`python3 can_sniff.py` - display CAN traffic in real-time from a serial connection
