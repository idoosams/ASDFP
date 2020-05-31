FROM python:3

COPY api /api
COPY requirements.txt requirements.txt
COPY config.ini config.ini
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "-m", "api"]