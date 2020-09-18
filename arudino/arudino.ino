
#include <Servo.h>

Servo serX;
Servo serY;

String serialData;

void setup() {
  // put your setup code here, to run once:
  serX.attach(9);
  serY.attach(10);

  serX.write(90);
  serY.write(90);

  Serial.begin(9600);
  Serial.setTimeout(10);

}

void loop() {

}

void serialEvent() {
  serialData = Serial.readString();
  
  serX.write(parsedX(serialData));
  serY.write(parsedY(serialData));
}

int parsedX (String data) {
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);

  return data.toInt();
}

int parsedY (String data) {
  data.remove(0, data.indexOf("Y") + 1);

  return data.toInt();
}
