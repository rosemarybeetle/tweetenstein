#include "Ultrasonic.h"

Ultrasonic ultrasonicR(12,13);
Ultrasonic ultrasonicL (10,11);

void setup() {

delay(1000);
Serial.begin(9600);       // use the serial port

}

void loop()
{
  
  Serial.println("Right = ");
  Serial.println(ultrasonicR.Ranging(CM));
  Serial.println("Left = ");
  Serial.println(ultrasonicL.Ranging(CM));
  delay(100);
}




