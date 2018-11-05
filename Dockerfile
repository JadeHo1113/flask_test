FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8888
ENTRYPOINT ["python"]

#CMD ["flask_test.py"]
CMD python flask_test.py
