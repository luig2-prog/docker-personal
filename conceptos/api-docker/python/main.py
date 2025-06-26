import docker

# client = docker.from_env()

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

client.containers.run("ubuntu", "echo hello world 2!")

images = client.images.list()

print(images)