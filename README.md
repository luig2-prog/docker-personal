# Docker

Repository for commands to run docker containers.

## MySQL

[docker-compose-mysql.yml](db/docker-compose-mysql.yml)

docker-compose-mysql.yml is a docker-compose file for a MySQL container

Execute the following command to start the MySQL container:

Linux:
```bash
docker compose -f db/docker-compose-mysql.yml up -d
```

Windows:
```bash
docker-compose -f db/docker-compose-mysql.yml up -d
```
`docker compose` is used to run the container with docker compose on Linux.

`docker-compose` is used to run the container with docker compose on Windows and Mac.

`-f` is used to specify the path to the docker-compose file.

`up` is used to start the container.

`-d` is used to run the container in detached mode.

Execute the following command to stop the MySQL container:

Linux:
```bash
docker compose -f db/docker-compose-mysql.yml down
```

Windows:
```bash
docker-compose -f db/docker-compose-mysql.yml down
```

`down` is used to stop the container.
