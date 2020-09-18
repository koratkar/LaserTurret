
#include <Servo.h>

Servo serX;
Servo serY;

int xPos = 0;
int yPos = 0;

void setup() {
  // put your setup code here, to run once:
  serX.attach(9);
  serY.attach(10);

  serX.write(0);
  serY.write(0);
  
}

void loop() {
  //yeet
}
