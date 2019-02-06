# use docker hub node.js image for react
FROM node:8.15.0-alpine

#set default user to tram
RUN adduser -D tram

#set working directory
WORKDIR /home/frontend

#install react
RUN npx create-react-app frontend

#install react-router-for-web
RUN npm install --save react-router-dom

#copy all contents in present directory to specified directory on container
COPY . /home/frontend

CMD npm start

