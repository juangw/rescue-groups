# our base image
FROM python:3.6.6

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get install python3-dev
RUN apt-get install libevent-dev
RUN pip3 install -r requirements.txt
RUN python setup.py develop

# specify the port number the container should expose
EXPOSE 8080

# run the application
ENTRYPOINT ["uwsgi"]
CMD ["uwsgi.ini"]
