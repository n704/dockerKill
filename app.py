import sys
import signal
import time
import logging

def signal_handler(signal, frame):
    """Signal handler for the interrupt
    
    Arguments:
        signal {int} -- Signal id, eg 15 SIGTERM
        frame {object} -- Frame object for interrupt
    """

    for i in range(5, 0, -1):
        ##* Printing time to exist
        logging.error("Process will be terminated in {0}".format(i))
        time.sleep(1)
    sys.exit()

# # Registering Signal with function handler
signal.signal(signal.SIGTERM, signal_handler)
while True:
    ##? Something to do here 
    ##? Just printing for eg
    logging.warn("Running infinite Loop")
    time.sleep(1)
