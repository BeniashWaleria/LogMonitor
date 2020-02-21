import threading
import re
import json
import logging
import datetime as dt

lock = threading.Lock()
headers = ['Container', 'Date', 'Time', 'FPS']
logs_arr = []

class LogMonitor:

    def __init__(self, docker_client):
        self.docker_client = docker_client

    def get_containers(self):
        containers = self.docker_client.containers.list()
        return containers

    def get_cont_logs(self, container, f):
        logs_dict = {}
        logging.info("getting logs")
        logs = container.logs(stream=True)
        for line in logs:
            parts = line.decode().split()
            sep = ' '
            time = parts[1].split(',')
            datetime = sep.join([parts[0], time[0]])
            fps = re.search(r'FPS = \d+(\.\d{1,2})?', line.decode()).group().split('=')[1]
            logs_dict['Container'] = container.attrs['Name']
            logs_dict['Date'] = str(dt.datetime.strptime(datetime.strip(), '%Y-%m-%d %H:%M:%S').date())
            logs_dict['Time'] = str(dt.datetime.strptime(datetime.strip(), '%Y-%m-%d %H:%M:%S').time())
            logs_dict['FPS'] = fps
            lock.acquire()
            logs_arr.append(logs_dict)
            with open(f,'a') as file:
                 json.dump(logs_arr, file)
            lock.release()

    def get_logs(self, frequency, container_, file):
        t = threading.Timer(frequency, self.get_cont_logs, (container_, file))
        t.start()
