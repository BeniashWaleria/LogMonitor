from monitor import LogMonitor
import docker
import json

file = 'logs.json'
headers = ['Container', 'Date', 'Time', 'FPS']
break_program = False


def extract_logs():
    client = docker.from_env()
    frequency = 5.0
    monitor = LogMonitor(client)
    containers = monitor.get_containers()
    for container in containers:
        monitor.get_logs(frequency, container, file)


def stat(file_):
    df = pd.read()
    print(jsons)

stat(file)