FROM python:3

COPY server /server
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python", "-m", "server", "run_server"]