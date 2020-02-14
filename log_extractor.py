import docker
client = docker.from_env()
containers = client.containers.list()
print(containers)

