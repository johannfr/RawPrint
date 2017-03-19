#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from ArduinoSerial import ArduinoSerial

if len(sys.argv) < 4:
    sys.stderr.write("Usage: %s <serial-port> <format-string> <log-file>\n"%sys.argv[0])
    sys.exit(1)

serial_port = sys.argv[1]
format_string = sys.argv[2]
log_filename = sys.argv[3]

s = ArduinoSerial(serial_port, baudrate=115200)
log_file = open(log_filename, "w")

token_types = {
    "d" : s.read_int,
    "f" : s.read_double
}

def tee(file_handle, output):
    sys.stdout.write(output)
    file_handle.write(output)

try:
    token_match = False
    while True:
        for c in format_string:
            if c == "%":
                token_match = True
            elif token_match:
                tee(log_file, str(token_types[c]()))
                token_match = False
            else:
                tee(log_file, c)
        tee(log_file, os.linesep)
except KeyboardInterrupt:
    pass

s.close()
log_file.close()
