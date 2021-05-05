# Arduino Serial Communication for Rearing Experiment
# Jeremy Delahanty, Aneesh Bal Apr. 2021
# pySerialTransfer written by PowerBroker2
# https://github.com/PowerBroker2/pySerialTransfer

# -----------------------------------------------------------------------------
# Import Packages
# -----------------------------------------------------------------------------
# Import pySerialTransfer for serial comms with Arduino
from pySerialTransfer import pySerialTransfer as txfer
# Import sys for exiting program safely
import sys
# Import random for generating random numbers
from random import randint
# import time for sleep given demo
import time

# -----------------------------------------------------------------------------
# Main Function; can become function called during experiment
# -----------------------------------------------------------------------------

# 4 behaviors are getting tracked: rearing, walking, sitting, grooming
# Key:
# 0 = Rearing
# 1 = Walking
# 2 = Sitting
# 3 = Grooming
behavior_dictionary = {
    0 : "Rearing!", 1 : "Walking!",
    2 : "Sitting!", 3 : "Grooming!"
}


if __name__ == '__main__':
    try:
        # Establish link to the Arduino
        # SerialTransfer() takes:
        # COM Port of UART converter
        # BAUD rate, or communication rate: 115200 is faster than 9600
        # debug for if you want debug outputs when something fails
        link = txfer.SerialTransfer('COM3', 115200, debug=True) ############# REPLACE COM PORT
        # Open the link
        link.open()

        # While experiment is running for the number of samples:
        while True:
            behavior = randint(0,3)
            print(behavior_dictionary[behavior])

            time.sleep(1)
            # Create transmission object; size refers to packet size
            behavior_size = link.tx_obj(behavior)
            # Send packet
            link.send(behavior_size)
            # Print what was sent to the Arduino
            print("Sent:\t\t{}".format(behavior))

            # Although the documentation/previous experience dictates to use
            # this while statement, including it doesn't allow for continous
            # sending of data for some reason... need to investigate further
            # For now, do NOT uncomment this statement
            # while not link.available():
            #     pass

    except KeyboardInterrupt:
        try:
            link.close()
            print("Done")
            print("Exiting...")
            sys.exit()
        except:
            pass

    except:
        import traceback
        traceback.print_exc()

        try:
            link.close()
            print("Exiting")
            sys.exit()
        except:
            pass
