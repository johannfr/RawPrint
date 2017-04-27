import serial
import struct

class ArduinoSerial(serial.Serial):

    def read_uint8_t(self):
        raw_data = self.read(1)
        try:
            int_value = int(struct.unpack("<B", raw_data)[0])
        except struct.error:
            return None
        return int_value

    def read_uint16_t(self):
        raw_data = self.read(2)
        try:
            int_value = int(struct.unpack("<H", raw_data)[0])
        except struct.error:
            return None
        return int_value

    def read_uint32_t(self):
        raw_data = self.read(2)
        try:
            int_value = int(struct.unpack("<I", raw_data)[0])
        except struct.error:
            return None
        return int_value


    def read_double(self):
        raw_data = self.read(4)
        try:
            double_value = float(struct.unpack("<f", raw_data)[0])
        except struct.error:
            return None
        return double_value


if __name__ == "__main__":
    s = ArduinoSerial("/dev/ttyUSB0", baudrate=9600, timeout=1)

    try:
        print s.read_double()
        print s.read_uint16_t()
    except KeyboardInterrupt:
        pass
    s.flush()
    s.close()
