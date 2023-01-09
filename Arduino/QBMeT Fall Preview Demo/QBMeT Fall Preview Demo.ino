/*
This code was developed by William Quigley for the Queens Biomechatronics Teams Fall Preview for potential upcoming Queens engineers.  This code 
has a rover use its arm to pick up a flag, wave the flag, and the put it back down on a loop.
*/

//-----------------------------------------------------------------------------Servo Initialization-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Use this library to command servomotors
#include <Servo.h>

// Create a servo object to control a servo
Servo hs422servo;
Servo arm;
Servo rotator;
//----------------------------------------------------------------------------Setup Non-Constant Variables------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Arduino analog input pin to which the Sharp sensor is connected
const byte SHARP_PIN_L = 1;
const byte SHARP_PIN_F = 0;
const byte SHARP_PIN_R = 2;

// Variable to store the proximity measurement
int sharp_val_L = 0;
int sharp_val_F = 0;
int sharp_val_R = 0;

long distance_L = 0.0;
long distance_F = 0.0;
long distance_R = 0.0;

//Time variables
double driveTime;
double revTime;
double currentTime;

// Variable to store the servo position [degrees]
int angle = 0;
int angleArm = 0;

//---------------------------------------------------------------------------Motor Initialization----------------------------------------------------------------------------------------------------------------------
// Motor driver PWM pins
const byte E1 = 3;
const byte E2 = 5;

// Motor driver direction pins
const byte M1 = 2;
const byte M2 = 4;

// Left wheel encoder digital pins
const byte SIGNAL_AL = 6;
const byte SIGNAL_BL = 7;

// Right wheel encoder digital pins
const byte SIGNAL_AR = 8;
const byte SIGNAL_BR = 9;

// Motor PWM command variables [0-255]
short u_L = 0;
short u_R = 0;

byte u = 122;





//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------Methods------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
float find_distance(double sharp_val){
  double distance;
  distance = -0.000006 * pow(sharp_val, 3) + 0.0023 * pow(sharp_val, 2) - 0.5174 * sharp_val + 58.473;
  if (distance < 0){
    distance = 0;
  }
  distance = distance * 2.54;
  return distance;
}

void grabFlag(){
  // 1)Open gripper 
  for (angleArm = 180; angleArm >= 0; angleArm -= 1)
  {
      // Tell servo to go to position "angle"
      arm.write(angleArm);

      // Wait a specified time [ms]
      delay(5);
  }

  // 2)Close gripper
  for (angleArm = 0; angleArm <= 180; angleArm += 1)
  {
      // Tell servo to go to position "angle"
      arm.write(angleArm);

      // Wait a specified time [ms]
      delay(5);
  }

  // 3)Set rover arm to 180 deg
  for (angle = 90; angle <= 180; angle += 1)
  {
      Serial.println(angle);
      // Tell servo to go to position "angle"
      hs422servo.write(angle);

      // Wait a specified time [ms]
      delay(50);
  }
}

void wave(){
  int waves = 0;

  hs422servo.write(180);
  delay(1000);

  // 1)Open gripper 
  for (angleArm = 180; angleArm >= 0; angleArm -= 1)
  {
      // Tell servo to go to position "angle"
      arm.write(angleArm);

      // Wait a specified time [ms]
      delay(5);
  }

  hs422servo.write(90);
  delay(1000);

  // 2)Close gripper
  for (angleArm = 0; angleArm <= 180; angleArm += 1)
  {
      // Tell servo to go to position "angle"
      arm.write(angleArm);

      // Wait a specified time [ms]
      delay(5);
  }

  // 3)Set rover arm to 160 deg
  for (angle = 90; angle <= 180; angle += 1)
  {
      //Serial.println(angle);
      // Tell servo to go to position "angle"
      hs422servo.write(angle);

      // Wait a specified time [ms]
      delay(50);
  }

  rotator.write(90);

  // 4) Wave the flag
  while (waves <= 3){
    for (int i = 0; i<180; i++){
      rotator.write(i);
      delay(10);
    }
    for (int i = 180; i>0; i--){
      rotator.write(i);
      delay(10);
    }
    waves++;
  }

  rotator.write(90);

  // 5)Set rover arm to 90 deg
  for (angle = 180; angle >= 90; angle -= 1)
  {
      Serial.println(angle);
      // Tell servo to go to position "angle"
      hs422servo.write(angle);

      // Wait a specified time [ms]
      delay(50);
  }

  // 6)Open gripper 
  for (angleArm = 180; angleArm >= 0; angleArm -= 1)
  {
      // Tell servo to go to position "angle"
      arm.write(angleArm);

      // Wait a specified time [ms]
      delay(5);
  }
}
//------------------------------------------------------------------------------Start of Code-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------Start of Setup-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void setup()
{
    // Open the serial port at 9600 bps
    Serial.begin(9600);

    // Set the pin modes for the motor driver
    pinMode(M1, OUTPUT);
    pinMode(M2, OUTPUT);
    
    // Attach the servo on pin 12 to the Servo object
    hs422servo.attach(12);
    arm.attach(11);
    rotator.attach(13);
}

//------------------------------------------------------------------------------Start of Loop-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void loop()
{
  delay(1000);
  //Read the time
  currentTime = millis();
  
  // Read the sensor output (0-1023, or 10 bits)
  sharp_val_L = analogRead(SHARP_PIN_L);
  sharp_val_F = analogRead(SHARP_PIN_F);
  sharp_val_R = analogRead(SHARP_PIN_R);

  distance_L = find_distance(sharp_val_L);
  distance_F = find_distance(sharp_val_F);
  distance_R = find_distance(sharp_val_R);

  //Serial.println(state);
  //Serial.println(sharp_val_F);

  hs422servo.write(90);
  arm.write(0);
  rotator.write(90);

  delay(5000);
  wave();
}
