#include <RawPrint.h>

RawPrint raw(Serial);

double sumfink = 456.234;
int bla = 0;  

void setup()
{
  Serial.begin(115200);
  while (!Serial);
  Serial.println("\r\n\r\nOK");
}

void loop()
{
  raw.print(sumfink);
  raw.print(bla++);
}
