FROM node

COPY . /app

WORKDIR /app

RUN npm install

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]