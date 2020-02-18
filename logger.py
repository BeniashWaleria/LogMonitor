import logging
import random
import time


def outFPS(length):

    logging.basicConfig(level=logging.INFO)
    for i in range(length):
        fps = random.randrange(20)
        logging.info("FPS = {}".format(fps))

outFPS(5)
