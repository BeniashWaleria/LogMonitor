import logging
import random
from time import sleep

logging.basicConfig(level=logging.INFO, format='%(asctime)s   %(message)s')


def out_fps():
    while True:
        fps = random.randrange(20)
        logging.info("FPS = {}".format(fps))
        sleep(1)


out_fps()
