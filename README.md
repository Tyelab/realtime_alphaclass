# Realtime Arduino Behavior Classification
## Use case
This is meant to control an Arduino using Python triggers for an experiment Aneesh Bal is going to run.
A behavior box will be divided in the middle by a wall that will only allow the animals to rear so they can see one another.
If both animals rear at the same time at this wall, a reward will be delivered to the mice.
## Basic procedure
AlphaTracker will be used to monitor the two animals. When the animal(s) rear, a signal will be sent to the Arduino that will turn on an LED and deliver a reward, likely sucrose.
### TODO
As of 4/30/21:

~~The code has yet to be tested in either language.~~

Code is tested and functional for demonstration.

Standard computing environment for Anaconda should be made. Jeremy to export conda environment and upload here.

Code must be integrated with a script running real time AlphaTracker.

Control of a solenoid or other gating mechanism must be introduced to release reward.

Update as of 5/5/21: This is not necessary for using the Arduino UNO. If we want more outputs, we might need an Arduino MEGA in which case buying one would be helpful. The're cheaply available on Amazon.

~~To use the package, we need to purchase a UART converter. They're cheaply available on Amazon.~~

Link: https://www.amazon.com/gp/product/B07TXVRQ7V/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
