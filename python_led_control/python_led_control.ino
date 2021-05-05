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
const int rearing_led_pin = 12; // LED control for rearing behavior
const int walking_led_pin = 8; // LED control for walking behavior
const int sitting_led_pin = 7; // LED control for sitting behavior
const int grooming_led_pin = 4; // LED control for grooming behavior

// Use a list to receive classified behavior
// Create the trigger_value with a size of 1
int32_t trigger_list[1];

//// SETUP ////
void setup() {
  // -- DEFINE BITRATE -- //
  // If using pySerialTransfer on Arduino UNO, Serial cannot be monitored.
  // Serial transfer of data through USB connection
  // Arduino UNO has Serial ONLY
  Serial.begin(115200);
  myTransfer.begin(Serial, true);

  // -- DEFINE PIN MODES -- //
  // input, as in input to the Arduino from some kind of sensor
  // None
  // output
  pinMode(rearing_led_pin, OUTPUT);
  pinMode(walking_led_pin, OUTPUT);
  pinMode(sitting_led_pin, OUTPUT);
  pinMode(grooming_led_pin, OUTPUT);
}

//// TRIGGER FUNCTIONS ////
// If the serial port is available:
//    receive a signal from python
//    if a 0 is sent, rearing is happening!
//    if a 1 is sent, walking is happening!
//    if a 2 is sent, sitting is happening!
//    if a 3 is sent, grooming is happening!
void behavior_trigger() {
  if (myTransfer.available())
  {
    myTransfer.rxObj(trigger_list);
    if (trigger_list[0] == 0) {
      // Rearing!
      digitalWrite(rearing_led_pin, HIGH);
      digitalWrite(walking_led_pin, LOW);
      digitalWrite(sitting_led_pin, LOW);
      digitalWrite(grooming_led_pin, LOW);
    }
    else if (trigger_list[0] == 1) {
      // Walking!
      digitalWrite(rearing_led_pin, LOW);
      digitalWrite(walking_led_pin, HIGH);
      
      digitalWrite(sitting_led_pin, LOW);
      digitalWrite(grooming_led_pin, LOW);
    }
    else if (trigger_list[0] == 2) {
      // Sitting!
      digitalWrite(rearing_led_pin, LOW);
      digitalWrite(walking_led_pin, LOW);
      digitalWrite(sitting_led_pin, HIGH);
      digitalWrite(grooming_led_pin, LOW);
    }
    else {
      // Grooming!
      digitalWrite(rearing_led_pin, LOW);
      digitalWrite(walking_led_pin, LOW);
      digitalWrite(sitting_led_pin, LOW);
      digitalWrite(grooming_led_pin, HIGH);
    }
  }
}

// loop
void loop() {
  behavior_trigger();
}
