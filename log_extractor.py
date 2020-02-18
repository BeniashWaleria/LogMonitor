import docker
import re
client = docker.from_env()

container = client.containers.get('log_tracker')
logs = container.logs(stream =True)

for line in logs:
    value = [int(v) for v in (re.findall(r'\d+', str(line)))]
    print(value)