FROM ubuntu

# Install Python 3 and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install --break-system-packages docker

COPY . /app

WORKDIR /app

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]