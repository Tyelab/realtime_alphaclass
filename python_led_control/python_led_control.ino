// Control code for Arduino management of rearing experiment LEDs
// Jeremy Delahanty, Aneesh Bal Apr. 2021
// SerialTransfer.h written by PowerBroker2
// https://github.com/PowerBroker2/SerialTransfer

// Include Serital Transfer package
#include "SerialTransfer.h"

// Rename SerialTransfer to myTransfer
SerialTransfer myTransfer;

//// PIN ASSIGNMENT: LEDs ////
// output
const int left_led_pin = 12; // LED control for mouse on left side
const int right_led_pin = 8; // LED control for mouse on right side

// Use a list to determine which animal is rearing
// 0-th index = Left, 1st index = Right
// Create the trigger_list with a size of 2 integers
int32_t trigger_list[2];

//// SETUP ////
void setup() {
  // -- DEFINE BITRATE -- //
  // Serial debugging on COM13, use Ctrl+Shift+M to open in Arduino IDE
  // If using pySerialTransfer on Arduino UNO, Serial cannot be monitored.
  // Serial transfer of data through USB connection
  // Arduino UNO has Serial ONLY
  Serial.begin(115200);
  myTransfer.begin(Serial, true);


  // -- DEFINE PIN MODES -- //
  // input, as in input to the Arduino from some kind of sensor
  // None
  // output
  pinMode(left_led_pin, OUTPUT);
  pinMode(right_led_pin, OUTPUT);
}

//// TRIGGER FUNCTIONS ////
// If the serial port is available:
//    receive a signal from python
//    if a 1 is sent, print in the monitor that rearing is happening!
//    otherwise, print that the animal is not rearing and turn LED off
void rearing_trigger() {
  if (myTransfer.available())
  {
    myTransfer.rxObj(trigger_list);
    if ((trigger_list[0]== 1) && (trigger_list[1] == 0)) {
      // L Rearing!
      digitalWrite(left_led_pin, HIGH);
      digitalWrite(right_led_pin, LOW);
    }
    else if ((trigger_list[0] == 0) && (trigger_list[1] == 1)) {
      // R Rearing!
      digitalWrite(left_led_pin, LOW);
      digitalWrite(right_led_pin, HIGH);
    }
    else if ((trigger_list[0] == 1) && (trigger_list[1] == 1)) {
      // Both Rearing!
      digitalWrite(left_led_pin, HIGH);
      digitalWrite(right_led_pin, HIGH);
    }
    else {
      // "Neither Rearing!
      digitalWrite(left_led_pin, LOW);
      digitalWrite(right_led_pin, LOW);
    }
  }
}

// loop
void loop() {
  rearing_trigger();
}
