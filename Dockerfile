FROM centos:centos7

COPY . /tmp/

RUN yum -y install net-tools wget

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN python get-pip.py

RUN pip install --no-cache-dir -r /tmp/requirements.txt

cmd python flask_test.py

