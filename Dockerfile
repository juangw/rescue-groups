FROM python:3.8.5

RUN mkdir -p /usr/src/app
COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt
RUN python setup.py develop

# specify the port number the container should expose
EXPOSE 8080

# run the application
ENTRYPOINT ["uwsgi"]
CMD ["uwsgi.ini"]
