FROM ubuntu

RUN apt-get update && apt-get install -y python3

COPY . /app

WORKDIR /app

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]