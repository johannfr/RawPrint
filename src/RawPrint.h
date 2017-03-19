#pragma once

#include <HardwareSerial.h>

class RawPrint
{
    public:
        RawPrint(HardwareSerial& serialPort_) : serialPort(serialPort_) {};

        template<typename T>
        void print(const T& v)
        {
            char *charPtrV = (char*)&v;
            for (int i = 0 ; i < sizeof(T) ; i++)
            {
                this->serialPort.write(*(charPtrV++));
            }
        }

    private:
        HardwareSerial& serialPort;
};
