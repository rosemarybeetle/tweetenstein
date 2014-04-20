#include "Ultrasonic.h"

Ultrasonic ultrasonicR(12,13);
Ultrasonic ultrasonicL (10,11);

void setup() {

delay(1000);
Serial.begin(9600);       // use the serial port
int rng_diff=0;
}

void loop()
{
  int rng_diff=0;
  Serial.println();
  Serial.println("Left = ");
  Serial.println(ultrasonicR.Ranging(CM));
   Serial.println("Right = ");
   
  Serial.println(ultrasonicL.Ranging(CM));
  rng_diff=(ultrasonicR.Ranging(CM)-ultrasonicL.Ranging(CM));
  
  Serial.println("Range difference = ");
  Serial.println(rng_diff);
  delay(1000);
}




