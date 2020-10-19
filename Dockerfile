FROM python:2.7

RUN mkdir /python && pip install flask
COPY server.py /python
COPY run.sh /python
WORKDIR /python

CMD ["/bin/bash", "run.sh"]