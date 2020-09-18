
#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  // put your setup code here, to run once:

  servoX.attach(9);
  servoY.attach(9);

  servoX.write(0);
  servoY.write(0);
}

void loop() {
  

}
