#install base python image
FROM python:3.6-alpine

# Install postgressql linux library config packages
RUN apk update && apk add build-base postgresql-dev python3-dev libffi-dev

#set default user to tram
RUN adduser -D tram

#copy all contents in present directory to specified directory on container
COPY . /home/tram

#set working directory
WORKDIR /home/tram

#install all app dependicies and packages
RUN pip install -r requirements.txt

RUN pip install -U flask-cors

#set flask env variable within container
ENV FLASK_APP run.py

#create entry points for running app
ENTRYPOINT ["python"]

#create command to run app
CMD ["run.py"]