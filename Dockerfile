FROM python:3.6.6
ENV PYTHONUNBUFFERED 1
#RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD ./test_nekidaem /code/
