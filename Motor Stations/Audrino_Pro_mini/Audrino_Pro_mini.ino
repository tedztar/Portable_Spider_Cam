/*
 * This is code for the motor startions
 * IMPORTANT:
 * make sure the motor indicator is changed to the correct flag for the spesified motor.
 */
#include <Stepper.h>

const int stepsPerRevolution = 200;// change this to fit the number of steps per revolution
// for your motor
const int step_angle = 1.8;
// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

//sets up the varuables used in the code
char motor = '1';
char delim[]= " "; //this is the charater that splits the data when transmited from the main controller
int current_pos = 0;
int go_to_pos = 0;
int num_of_steps = 0;
char *flag = "hello"; //this is NOT the definition for what motor this controlls only a place hoder for later use
char inString[] = "this is a test that has no merrit";
int inint = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //starts the serial comunication
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 1){
    int inint = Serial.read();
    if (inint != "run command"){
      inString = char(inint)
      char *ptr = strtok(inString, delim);
      flag = strtok(NULL, delim);
      if (flag == motor + "r" or flag == motor + "s"){
        myStepper.setSpeed(atoi(strtok(NULL, delim)));
        go_to_pos = atoi(strtok(NULL, delim));
        if (flag == motor + "r"){//code that is run when the module get the run signal
          num_of_steps = ((go_to_pos-current_pos)/step_angle);
         }
        if (flag == motor + "s"){//code that is run when the module get the setup signal
          current_pos = go_to_pos;
        }
      }
    }
    if (inint != "run command"){
      myStepper.step(num_of_steps);
      current_pos = go_to_pos;
    }
  }
}
