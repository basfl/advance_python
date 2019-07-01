FROM python:3.7.0
MAINTAINER babak soltanifar
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . /src
CMD ["python","app.py"]