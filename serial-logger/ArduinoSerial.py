import serial
import struct

class ArduinoSerial(serial.Serial):

    def read_int(self):
        raw_data = self.read(2)
        int_value = int(struct.unpack("<h", raw_data)[0])
        return int_value

    def read_double(self):
        raw_data = self.read(4)
        double_value = float(struct.unpack("<f", raw_data)[0])
        return double_value


if __name__ == "__main__":
    s = ArduinoSerial("/dev/ttyUSB0", baudrate=115200)

    try:
        print s.read_double()
        print s.read_int()
    except KeyboardInterrupt:
        pass
    s.flush()
    s.close()
