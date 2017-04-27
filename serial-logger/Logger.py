#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from ArduinoSerial import ArduinoSerial
import time

if len(sys.argv) < 4:
    sys.stderr.write("Usage: %s <serial-port> <format-string> <log-file>\n"%sys.argv[0])
    sys.exit(1)

serial_port = sys.argv[1]
format_string = sys.argv[2]
log_filename = sys.argv[3]
start_time = int(time.time())

s = ArduinoSerial(serial_port, baudrate=9600, timeout=50)

while True:
    line = s.readline()
    if line.strip() == "OK":
        break

log_file = open(log_filename, "w")

def gettimestamp():
    global start_time
    return int(time.time())-start_time

token_types = {
    "s" : s.read_uint8_t,
    "i" : s.read_uint16_t,
    "d" : s.read_uint16_t,
    "l" : s.read_uint32_t,
    "f" : s.read_double,
    "t" : gettimestamp
}

def tee(file_handle, output):
    sys.stdout.write(output)
    file_handle.write(output)
    file_handle.flush()


tee(log_file, "Start-time: %s"%time.strftime("%Y-%m-%d %H:%M:%S"))



try:
    token_match = False
    while True:
        for c in format_string:
            if c == "%":
                token_match = True
            elif token_match:
                value = str(token_types[c]())
                if value:
                    tee(log_file, value)
                token_match = False
            else:
                tee(log_file, c)
        tee(log_file, os.linesep)
except KeyboardInterrupt:
    pass

s.flush()
s.close()
log_file.close()
