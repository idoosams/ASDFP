import pika
import pickle
import time
from furl import furl
# todo: loger by mq


class SnanpshotPublisher():
    def __init__(self, queues, url='rabbitmq://127.0.0.1:5672'):
        self.url = furl(url)
        self.queues = queues[:]
        self.queues.remove('datetime')  # passed in every queue

    def __enter__(self):
        # on docker usually fails on the first time since mq didn't start
        # to run
        for i in range(5):
            try:
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(self.url.host, self.url.port))
                self.channel = self.connection.channel()
                for field in self.queues:
                    self.channel.queue_declare(queue=field, durable=True)
                return self
            except Exception:
                time.sleep(10)

    def publish(self, snapshot, user_id, datetime):
        for field in self.queues:
            attr = snapshot.get(field)
            if attr:
                self.channel.basic_publish(
                    exchange='',
                    routing_key=field,
                    body=pickle.dumps(
                        dict(data=attr,
                             user_id=user_id,
                             datetime=datetime)),
                    properties=pika.BasicProperties(
                        delivery_mode=2,  # make message persistent
                    ))
            print(" [x] Sent")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
