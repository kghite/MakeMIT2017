#include <Servo.h> 

// Servo objects
Servo emotion;
Servo age;
Servo swag;

int incoming[2];

int pos = 90;
String p = "Not available";

void setup()  {
  Serial.begin(9600);

  emotion.attach(9);
  age.attach(10);
  swag.attach(11);

  pinMode(LED_BUILTIN, OUTPUT);

  emotion.write(90);
  age.write(200);
  swag.write(20);
}

void loop()   
{
  if (Serial.available() >= 3)
  {  
    for (int i = 0; i < 3; i++) {
      incoming[i] = Serial.read();
    }

    emotion.write(incoming[0]);
    age.write(incoming[1]);
    swag.write(incoming[2]);
  } 
}
