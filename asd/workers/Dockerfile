FROM python:3

COPY workers /workers
COPY requirements.txt requirements.txt
COPY config.ini config.ini
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "workers"]