import datetime
import time
import logging

class Logger:
    def __init__(self):
        logging.basicConfig(filename='log.txt', level=logging.INFO)

    def log(self, msg):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print(" ".join([timestamp, msg]))
        logging.info(" ".join([timestamp, msg]))
