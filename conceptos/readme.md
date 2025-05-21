# Docker

Tecnología de contenedores que permite empaquetar aplicaciones y sus dependencias en un solo objeto llamado contenedor.

Technology of containers that allows you to package applications and their dependencies into a single object called a container.

Son ligeros, portables y se pueden ejecutar en cualquier entorno que soporte Docker.

Docker only works on Linux, but it can run on Windows and MacOS using a lightweight virtual machine.

## Basics Concepts

- **Dockerfile**: Text file with instructions to build a Docker image. It contains the commands to assemble the image, not have a file extension.

- **Docker Image**: Read-only template used to create containers. Compiled version of the Dockerfile. Image are built from Dockerfiles and can be shared via Docker Hub or other registries.

- **Docker Container**: Running instance of a Docker image. Final object that runs in Docker. Through the image you can create multiple containers

- **Docker Hub**: Public repository for Docker images. It allows you to share and download images

- **Docker Daemon**: Background service that manages Docker containers. It is responsible for building, running, and managing containers. It listens for API requests and can communicate with the Docker CLI or other tools.

**Docker CLI**: Command-line interface for interacting with Docker. It allows you to run commands to manage containers, images, and other Docker resources.

**Docker Compose**: Tool for defining and running multi-container Docker applications. It uses a YAML file to configure the services, networks, and volumes needed for the application. With Docker Compose, you can start and stop all the containers in your application with a single command.

**Docker Swarm**: Native clustering and orchestration tool for Docker. It allows you to manage a cluster of Docker nodes as a single virtual system. With Docker Swarm, you can deploy and manage services across multiple Docker hosts.

**Docker Registry**: Service for storing and distributing Docker images. It can be public (like Docker Hub) or private (self-hosted). A registry allows you to push and pull images to and from it.

**Docker Volume**: Persistent storage for Docker containers. Volumes are used to store data that needs to persist even if the container is removed. They can be shared between containers and are managed by Docker.

**Docker Network**: Virtual network that allows containers to communicate with each other. Docker provides several network drivers (bridge, host, overlay) to create different types of networks for your containers.

**Docker Compose File**: YAML file used to define and configure multi-container Docker applications. It specifies the services, networks, and volumes needed for the application. The file is typically named `docker-compose.yml` and can be used with the `docker-compose` command to manage the application.

**Docker Stack**: Collection of services that make up an application in Docker Swarm. A stack is defined by a `docker-compose.yml` file and can be deployed to a Swarm cluster. It allows you to manage multiple services as a single unit.

**Docker Context**: A named set of parameters that define a Docker environment. It allows you to switch between different Docker environments (local, remote, cloud) easily. You can create, list, and manage contexts using the `docker context` command.

**Docker Secrets**: Secure storage for sensitive data (like passwords, API keys) used by Docker services. Secrets are encrypted and can be accessed only by the services that need them. They are managed by Docker Swarm and can be created, listed, and removed using the `docker secret` command.

**Docker Configs**: Configuration files used by Docker services. They allow you to store non-sensitive data (like configuration files, scripts) that can be shared between services. Configs are managed by Docker Swarm and can be created, listed, and removed using the `docker config` command.

**Docker Healthcheck**: Mechanism to check the health of a running container. It allows you to define a command that Docker will run periodically to determine if the container is healthy or not. If the command fails, Docker can take action (like restarting the container) based on the health status.

**Docker BuildKit**: Advanced build subsystem for Docker that improves the performance and capabilities of the `docker build` command. It allows for parallel builds, better caching, and support for new features like build secrets and build contexts. BuildKit can be enabled by setting the `DOCKER_BUILDKIT=1` environment variable.

**Docker Compose Override File**: A file used to override or extend the configuration of a Docker Compose file. It allows you to define additional settings or modifications without changing the original `docker-compose.yml` file. The override file is typically named `docker-compose.override.yml` and is automatically used by Docker Compose when running commands.

**Dockerfile Best Practices**: Guidelines for writing efficient and maintainable Dockerfiles. Some best practices include:

- Use a .dockerignore file to exclude unnecessary files from the build context.
- Minimize the number of layers in the image by combining commands.
- Use official base images from Docker Hub when possible.
- Keep images small by removing unnecessary packages and files.
- Use multi-stage builds to separate build and runtime dependencies.

## Docker Commands

```bash
docker --version
```

[Docker hub Httpd](https://hub.docker.com/_/httpd)

- Docker pull

```bash
docker pull httpd
```

**docker**: Command-line tool for interacting with Docker.

**pull**: Command to download a Docker image from a registry (like Docker Hub) to your local machine.

**httpd**: The name of the Docker image to download. In this case, it is the official Apache HTTP server image.

**latest**: The tag of the image to download. If not specified, Docker will pull the `latest` tag by default. The `latest` tag usually refers to the most recent stable version of the image.

**docker pull httpd:2.4**: Command to download a specific version (2.4) of the Apache HTTP server image. If you want to download a different version, you can specify the desired tag.

- Docker run

```bash
docker run -p 8080:80 -d httpd
```

**docker**: Command-line tool for interacting with Docker.
**run**: Command to create and start a new container from an image
**-p 8080:80**: Maps port 8080 on the host to port 80 in the container. This allows you to access the web server running in the container from your host machine. 8080 is the host port and 80 is the container port.
**-d**: Runs the container in detached mode, meaning it runs in the background and does not block the terminal.
**httpd**: The name of the Docker image to use. In this case, it is the official Apache HTTP server image. If the image is not available locally, Docker will pull it from Docker Hub.

```bash
docker run -p 8080:80 -d --name my-httpd httpd:2.4
```

**--name my-httpd**: Assigns a name (my-httpd) to the container. This makes it easier to manage the container later, as you can refer to it by name instead of its container ID.

- Docker ps: Command to list all running containers

```bash
docker ps
```

**docker ps**: Command to list all running containers. It shows the container ID, image name, command, creation time, status, ports, and names of the running containers.

**docker ps -a**: Command to list all containers, including stopped ones. It shows the same information as `docker ps`, but includes containers that are not currently running.

**docker ps -q**: Command to list only the container IDs of all running containers. It is useful for scripting and automation.

**docker ps -aq**: Command to list only the container IDs of all containers, including stopped ones. It is useful for scripting and automation.

**docker ps -l**: Command to show the most recently created container. It shows the same information as `docker ps`, but only for the last created container.

**docker ps -n 5**: Command to show the last 5 created containers. It shows the same information as `docker ps`, but only for the last 5 created containers.

**docker ps -n 5 -q**: Command to show the last 5 created containers, but only their IDs. It is useful for scripting and automation.

**docker ps -s**: Command to show the size of each container. It shows the same information as `docker ps`, but includes the size of each container.

**docker ps -s -q**: Command to show the size of each container, but only their IDs. It is useful for scripting and automation.

**docker ps -s -l**: Command to show the size of the most recently created container. It shows the same information as `docker ps`, but only for the last created container.

**docker ps -s -n 5**: Command to show the size of the last 5 created containers. It shows the same information as `docker ps`, but only for the last 5 created containers.

**docker ps -s -n 5 -q**: Command to show the size of the last 5 created containers, but only their IDs. It is useful for scripting and automation.

**docker ps -s -n 5 -l**: Command to show the size of the last 5 created containers, but only for the last created container. It shows the same information as `docker ps`, but only for the last created container.

- nginx

```bash
docker run -p 8080:80 -d nginx
```

- Docker container

**Docker container ls**: List all running containers

```bash
docker container ls
```

**docker container ls -a**: List all containers, including stopped ones

```bash
docker container --help
```

```bash
docker container inspect <container_id>
docker inspect <container_id>
```

**inspect**: Command to get detailed information about a container. It shows the container's configuration, state, network settings, and more.

**<container_id>**: The ID or name of the container you want to inspect. You can find the container ID or name using the `docker ps` command. Can be also a name, for example `db-db-1`.

```bash
docker inspect <container_id> | grep -i env
docker container inspect <container_id> | grep -i env
```

**grep -i env**: Filters the output of the `docker inspect` command to show only lines containing the word "env" (case-insensitive). This is useful for finding environment variables set in the container.

```bash
docker rm <container_id or name>
docker container rm <container_id or name>
```

**rm**: Command to remove a container. It deletes the container from your local machine. You can only remove stopped containers, so make sure to stop the container first if it is running.
**<container_id or name>**: The ID or name of the container you want to remove. You can find the container ID or name using the `docker ps` command.

Módulo 2
|
8 clases
Contenedores
expand_more
done_all
Clase 1

Comandos Básicos

done_all
Clase 2

Contenedores en Segundo Plano

done_all
Clase 3

Modo Interactivo

done_all
Clase 4

Puertos

done_all
Clase 5

Logs

done_all
Clase 6

Inspeccionar Contenedores

done_all
Clase 7

Variables de Entorno

done_all
Clase 8

Contenedores sin servicios

Módulo 3
|
7 clases
Redes y Volúmenes
expand_more
done_all
Clase 1

Qué son los Volúmenes

done_all
Clase 2

Volúmenes de Docker

done_all
Clase 3

Compartir Archivos entre Contenedores

done_all
Clase 4

Volúmenes Manuales

done_all
Clase 5

Redes

done_all
Clase 6

Conectando Contenedor a Red

done_all
Clase 7

Red hosts

Módulo 4
|
9 clases
Imágenes
expand_more
done_all
Clase 1

Qué son las Imágenes

done_all
Clase 2

Primer Imagen

done_all
Clase 3

Copiando Archivos

done_all
Clase 4

Variables de Entono

done_all
Clase 5

Ejecutar Servicios

done_all
Clase 6

Entrypoint vs CMD

done_all
Clase 7

Dokerizar script python

done_all
Clase 8

docker hub

done_all
Clase 9

Dockerizar script node

check_circle_outline
Módulo 5
|
7 clases

|
7 clases
Docker Compose
expand_more
done_all
Clase 1

Qué es Docker Compose

done_all
Clase 2

Servicios

done_all
Clase 3

Redes

done_all
Clase 4

Volúmenes

done_all
Clase 5

Variables de Entorno

done_all
Clase 6

Stack Local

done_all
Clase 7

Docker Compose Build

Módulo 6
|
8 clases
Introducción Kubernetes
expand_more
done_all
Clase 1

Qué son los Orquestadores

done_all
Clase 2

Conceptos Básicos

done_all
Clase 3

Instalación

done_all
Clase 4

Primer Pod

done_all
Clase 5

Port Forwad

done_all
Clase 6

Terminal Interactiva

done_all
Clase 7

Eliminar pods

done_all
Clase 8

Logs en pods

Módulo 7
|
4 clases
Extras
expand_more
done_all
Clase 1

Consumir API Docker

done_all
Clase 2

Docker Portainer

done_all
Clase 3

Docker Aplicaciones Gráficas

done_all
Clase 4

Entorno VSCode
