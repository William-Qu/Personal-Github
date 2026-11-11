/*
This code was developed in an Educational Labratory setting to have a autonomous rover drive forward until it detected a flag within reach,
stop, pick up the flag with the rovers arm, and then bring the flag back to the rovers starting postion.
Credits to Joshua Marshall for creating the shell of the labratory code.  The rest of the code was developed by William Quigley and Jacob O'Neil
*/

//-----------------------------------------------------------------------------Servo Initialization-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
// Use this library to command servomotors
#include <Servo.h>

// Create a servo object to control a servo
Servo hs422servo;
Servo arm;
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

//State of object avoidance
int state = 0;

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
    arm.attach(13);
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

  Serial.println(state);
  Serial.println(sharp_val_F);

  if (state == 0){
    distance_F = 100;
    arm.write(0);
    delay(1000);
    state = 1;
  }
  
  if (state == 1){
    // Write to the output pins
    digitalWrite(M1, LOW); // Drive forward (left wheels)
    analogWrite(E1, u);    // Write left motors command
    digitalWrite(M2, HIGH); // Drive forward (right wheels)
    analogWrite(E2, u);    // Write right motors command
    if (sharp_val_F >= 500){
      state = 2;
      driveTime = millis();
      analogWrite(E1, 0);    // Write left motors command
      analogWrite(E2, 0);    // Write right motors command
    }
  }
  
  else if(state == 2){
    grabFlag();
    state = 3;
    revTime = millis();
  }

  else if(state == 3 ){//&& (currentTime-revTime-driveTime) <= driveTime){
    digitalWrite(M1, HIGH); // Drive forward (left wheels)
    analogWrite(E1, u);    // Write left motors command
    digitalWrite(M2, LOW); // Drive backwards (right wheels)
    analogWrite(E2, u);    // Write right motors command
    Serial.print("The time we have is: ");
    Serial.println(currentTime-revTime-driveTime);
    Serial.print("Drive time is: ");
    Serial.println(driveTime);
  }

  if (state == 3 &&(currentTime-revTime-driveTime+20000) >= driveTime){
    state = 4;
    Serial.println("Initial Position Detected");
    analogWrite(E1, 0);    // Write left motors command
    analogWrite(E2, 0);    // Write right motors command
    
  }

  if (state == 4){
    hs422servo.write(90);
    delay(100);
    arm.write(180);
    delay(100);
  }
}
