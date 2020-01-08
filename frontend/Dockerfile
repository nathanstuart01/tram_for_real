# use docker hub node.js image for react
FROM node:8.15.0-alpine

#set default user to tram
RUN adduser -D tram

#set working directory
WORKDIR /home/frontend

#copy all contents in present directory to workdir on container
COPY . .

#install react
RUN npm install

#install react-router-for-web
RUN npm install --save react-router-dom
#install bootstrap for css styling
RUN npm install react-bootstrap bootstrap

CMD npm start

