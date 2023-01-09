//Hackathon Arduino Project
/*
This code was created for the Next Generation Medical Simulation Hackathon as a part of a dentistry training simulator.  For the purposes of the 
hackathon only the teeth cleaning simulation was created, however the full simulator, if properly developed, would be used to train dentists for 
multiple procedures to reduce costs of having multiple medical simulators.  Augmented Reality(AR) would also have been added to the project to 
create a further sense of realism in the training modules.

The code was designed for use with a physical model of a human jaw that contained a pressure sensor, a red, yellow and green light, and a buzzer. The
dentist trainee would practice cleaning the model, with plaque simulated on the teeth in AR, and if too much pressure was applied then the red light
would turn on and the buzzer would sound to alert the dentist that they had applied too much force.  The yellow light would be turned on when
slightly more pressure than required was added.

This project was created by William Quigley, Lucas Krayacich, Wade Goren, and Matthew MacEachern and placed 2nd in the Hackathon.
*/

//Set Pins
const byte g_pressure = 12;
const byte y_pressure = 8;
const byte r_pressure = 13;
const byte flexiforce = A5;

//Initialize variables
double pressure;
float current_time;
float start_time;
float prev_time;
byte c_pressure = 2;
byte p_pressure = 1;
bool red = false;
bool change = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(flexiforce, INPUT);
  pinMode(g_pressure, OUTPUT);
  pinMode(y_pressure, OUTPUT);
  pinMode(r_pressure, OUTPUT);

  //Initialize the Serial Monitor
  Serial.begin(9600);

  //Set initial pin values
  digitalWrite(g_pressure, LOW);
  digitalWrite(g_pressure, LOW);
  digitalWrite(r_pressure, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Readings will be done here
  current_time = millis();
  if (red == true && change == true){
    start_time = current_time;
    change = false;
  }
  
  //Calculations will be done here
  pressure = analogRead(flexiforce);
  
  if (pressure == 0){
    //Sets the board to red
    digitalWrite(g_pressure, LOW);
    digitalWrite(y_pressure, LOW);
    digitalWrite(r_pressure, HIGH);
    delay(100);
    red = true;
  }
  else if (pressure > 0 && pressure <= 60) {
    //Sets the board to yellow
    digitalWrite(g_pressure, LOW);
    digitalWrite(y_pressure, HIGH);
    digitalWrite(r_pressure, LOW);
    delay(100);
    //Prints the time
    if (red = true && change == false) {
      prev_time = current_time;
      Serial.print("The start time was ");
      Serial.print(start_time/1000);
      Serial.print(" seconds, and the end time is ");
      Serial.println(prev_time/1000);
      Serial.print(" seconds, for a total of ");
      Serial.print((prev_time - start_time)/1000);
      Serial.println(" seconds.");
      change = true;
    }
    red = false;
  }
  else if (pressure > 60){
    //Sets the board to Green
    digitalWrite(g_pressure, HIGH);
    digitalWrite(y_pressure, LOW);
    digitalWrite(r_pressure, LOW);
    delay(100);
    //Prints the time
    if (red = true && change == false) {
      Serial.println(red);
      prev_time = current_time;
      Serial.print("The start time was ");
      Serial.print(start_time/1000);
      Serial.print(" seconds, and the end time is ");
      Serial.print(prev_time/1000);
      Serial.print(" seconds, for a total of ");
      Serial.print((prev_time - start_time)/1000);
      Serial.println(" seconds.");
      change = true;
    }
    red = false;
  }
  
  //Checks the different values
  //Serial.print("The pressure is: ");
  //Serial.println(pressure);
  //Serial.print("The time difference is: ");
  //Serial.println(current_time - prev_time);
  //Serial.print("Pressure is: ");
  //Serial.println(c_pressure);
}
