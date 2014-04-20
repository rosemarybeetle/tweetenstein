#include <StepperMotor.h>

// 4 pins of the stepper motor board
#define _PIN1 19
#define _PIN2 18
#define _PIN3 17
#define _PIN4 16

// Interruption on PIN2, push-button connected to pull-up
#define ITR_PIN 2
#define ITR_NB 0

volatile boolean forward = false;
volatile boolean start = false;
volatile boolean first = true;

StepperMotor stepper(_PIN1, _PIN2, _PIN3, _PIN4);

/**
 * This method is called on the interruption raised on the falling front of the PIN2
 * The start flag is used to avoid rebound front. Interruptions are disabled inside the 
 * interrupt vector method.
 * start is reset once it has been processed in the main loop() 
 */
void buttonPressed()
{
  if (!first)
  {
    if (!start)
    {
      forward = !forward;
      start = true;
    }
  }
  else
  {
    first = false;
  }
}

void setup()
{
  cli();
  stepper.setPeriod(5);
  pinMode(ITR_PIN, INPUT_PULLUP);
  attachInterrupt(0, buttonPressed, FALL);
  sei();
}

void loop()
{
  if (start)
  {
    if (forward)
    {
      stepper.move(2048);
      stepper.stop();
    }
    else
    {
      stepper.move(-2048);
      stepper.stop();
    }
    start = false;
  }
}
