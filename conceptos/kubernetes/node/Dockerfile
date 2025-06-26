# FROM node:22.10
FROM node

COPY . /app

WORKDIR /app

RUN npm install && chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]