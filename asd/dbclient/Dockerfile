FROM python:3

COPY dbclient /dbclient
COPY requirements.txt requirements.txt
COPY config.ini config.ini
RUN pip install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python", "-m", "dbclient"]