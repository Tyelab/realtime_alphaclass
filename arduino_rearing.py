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
        link = txfer.SerialTransfer('COM12', 115200, debug=True) ############# REPLACE COM PORT
        # Open the link
        link.open()

        # While expeirment is running
        while True:
            # List for transmission is the rearing_list
            list_ = rearing_list
            # Create transmission object; size refers to packet size
            list_size = link.tx_obj(list_)
            # Send packet
            link.send(list_size)
            # Print what was sent to the Arduino
            print("Sent:\t\t{}".format(list_))

            # If transmission becomes unavailable, pass
            # Shouldn't happen in this use case, at least I don't think so...
            while not link.available():
                pass

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
