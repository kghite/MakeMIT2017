 //control servo motor with serial monitering window - by ujash patel
  //for more go to www.uu-machinetool.blogspot.com
#include <Servo.h> 

// Servo objects
Servo emotion;
Servo age;
Servo swag;

int info;
int pos;

void setup()  {
  Serial.begin(9600);  

  emotion.attach(9);
  age.attach(10);
  swag.attach(11);
}

void loop()   
{
  writePos;
}

void writePos() {
  if (Serial.available() > 0)
  {
    info = Serial.read();

    // EMOTION
    if(info % 10 == '1')
    {
      Serial.println("1"); // Confirm recieved
  
      // Get the sent position: 0-360 
      pos = info / 10;
      
      emotion.write(pos);
    }

    // AGE
    if(info % 10 == '1')
    {
      Serial.println("1"); // Confirm recieved
  
      // Get the sent position: 0-360
      pos = info / 10;

      age.write(pos);
    }

    // SWAG
    if(info % 10 == '1')
    {
      Serial.println("1"); // Confirm recieved
  
      // Get the sent position: 0-360 
      pos = info / 10;

      swag.write(pos);
    }

    else {
      Serial.println("0"); // Failed write
    }
  }  
}

