# Redis

```bash
docker compose -f docker-compose-redis.yml up
```

To access to the Redis DB

```bash
docker compose exec -it redis redis-cli
# or
docker exec -it mi-redis-server redis-cli
```

1. CREATE
SET
```bash
SET user:1 "Luis Hernadez"
```

2. READ

GET
```bash
GET user:1
```

3. UPDATE

SET
```bash
SET user:1 "Luis Actualizado"
```

4. DELETE

DEL

```bash
DEL user:1
```

¡Claro! Aquí te presento un Dockerfile para un servidor de Redis y las instrucciones detalladas para realizar pruebas de operaciones CRUD (Crear, Leer, Actualizar, Borrar) utilizando la interfaz de línea de comandos de Redis (redis-cli).
Dockerfile para un servidor de Redis

Este Dockerfile es simple y utiliza la imagen oficial de Redis, que es la mejor práctica para iniciar.
Dockerfile

# Usa la imagen oficial de Redis como base
FROM redis:latest

# El puerto por defecto de Redis
EXPOSE 6379

# Comando por defecto para iniciar el servidor de Redis
CMD ["redis-server"]

Cómo construir y ejecutar la imagen de Docker

    Guarda el código anterior en un archivo llamado Dockerfile.
    Abre una terminal en el mismo directorio donde guardaste el archivo.
    Construye la imagen de Docker con un nombre de tu elección (por ejemplo, mi-redis-server):
    Bash

docker build -t mi-redis-server .

Ejecuta el contenedor de Docker y expón el puerto 6379 para que puedas acceder a él desde tu máquina local:
Bash

    docker run --name mi-redis-container -p 6379:6379 -d mi-redis-server

        --name mi-redis-container: Asigna un nombre al contenedor para que sea fácil de identificar.
        -p 6379:6379: Mapea el puerto 6379 del contenedor al puerto 6379 de tu máquina local.
        -d: Ejecuta el contenedor en modo "detached" (en segundo plano).

Instrucciones para pruebas de CRUD con redis-cli

Una vez que tu contenedor de Redis esté funcionando, puedes interactuar con él usando redis-cli. Puedes acceder al redis-cli directamente dentro del contenedor.

    Abre otra terminal.
    Ejecuta redis-cli dentro del contenedor:
    Bash

    docker exec -it mi-redis-container redis-cli

    Esto te conectará a la instancia de Redis que está corriendo dentro del contenedor. Ahora puedes ejecutar los siguientes comandos para probar las operaciones CRUD.

1. CREATE (Crear)

Usa el comando SET para crear un par de clave-valor.

    Comando: SET <clave> <valor>
    Ejemplo:
    Fragmento de código

    SET usuario:1 "Juan Perez"

        Resultado: OK
        Esto crea una clave llamada usuario:1 con el valor "Juan Perez".

2. READ (Leer)

Usa el comando GET para leer el valor asociado a una clave.

    Comando: GET <clave>
    Ejemplo:
    Fragmento de código

    GET usuario:1

        Resultado: "Juan Perez"
        Esto recupera el valor almacenado en la clave usuario:1.

3. UPDATE (Actualizar)

Para actualizar un valor, simplemente usa el comando SET de nuevo con la misma clave.

    Comando: SET <clave> <nuevo_valor>
    Ejemplo:
    Fragmento de código

    SET usuario:1 "Juan Perez (Actualizado)"

        Resultado: OK
        El valor de la clave usuario:1 ahora ha sido sobrescrito. Si vuelves a usar GET usuario:1, el resultado será "Juan Perez (Actualizado)".

4. DELETE (Borrar)

Usa el comando DEL para eliminar una o varias claves.

    Comando: DEL <clave1> [<clave2> ...]

    Ejemplo:
    Fragmento de código

DEL usuario:1

    Resultado: (integer) 1 (indica que se eliminó 1 clave)
    Ahora, si intentas leer la clave, obtendrás (nil), lo que significa que la clave no existe.

<!-- end list -->
Fragmento de código

    GET usuario:1

        Resultado: (nil)

Comandos útiles adicionales para verificar

KEYS *: Lista todas las claves en la base de datos.
PING: Verifica si el servidor de Redis está activo. La respuesta esperada es PONG.
FLUSHALL: Elimina todas las claves de todas las bases de datos. ¡Úsalo con precaución!
