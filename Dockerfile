FROM node:slim
ADD ./app /app
WORKDIR /app
RUN npm install
CMD npm start