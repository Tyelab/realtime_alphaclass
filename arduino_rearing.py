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
# Import numpy random for generating random lists
# Use default_rng per documentation
from numpy.random import default_rng
# import time for sleep given demo
import time

# -----------------------------------------------------------------------------
# Main Function; can become function called during experiment
# -----------------------------------------------------------------------------

# Create a rearing list that's updated depending on animal behavior
# 0-th index = L side, 1st index = R side
# Key:
# [0,0] = neither rearing
# [1,0] = left side rearing
# [0,1] = right side rearing
# [1,1] = both rearing
rearing_list = [0,0]

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

        # While expeirment is running for the number of samples:
        while True:
            rng = default_rng()
            rearing_value = rng.uniform(low=0, high=1, size=1)
            print(rearing_value)
            if rearing_value <= 0.50:
                rearing_list = [0,1]
            else:
                rearing_list = [1,0]
            time.sleep(.1)
            # List for transmission is the rearing_list
            list_ = rearing_list
            # Create transmission object; size refers to packet size
            list_size = link.tx_obj(list_)
            # Send packet
            link.send(list_size)
            # Print what was sent to the Arduino
            print("Sent:\t\t{}".format(list_))

            # Although the documentation/previous experience dictates to use
            # this while statement, including it doesn't allow for continous
            # sending of data for some reason... need to investigate further
            # For now, do NOT uncomment this statement
            # while not link.available():
            #     pass
        link.close()
        print("Done")
        sys.exit()

    except KeyboardInterrupt:
        try:
            link.close()
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
