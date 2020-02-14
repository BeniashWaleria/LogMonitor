import logging
import random
import time


def outFPS(length):

    logging.basicConfig(level=logging.INFO)
    for i in range(length):
        start = time.time()
        fps = random.randrange(20)
        logging.info("FPS = {}".format(fps))
        time.sleep(5.0)

outFPS(5)
