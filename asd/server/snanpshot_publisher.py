import pika
import pickle
import time
from furl import furl
# todo: loger by mq


class SnanpshotPublisher():
    """
    SnanpshotPublisher Class
    publish the server data to the message queue
    """

    def __init__(self, queues, url='rabbitmq://127.0.0.1:5672'):
        """
        :param queues: queues for the message queue
        :param url: defaults to 'rabbitmq://127.0.0.1:5672'
        """
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
                for queue in self.queues:
                    self.channel.queue_declare(queue=queue, durable=True)
                self.channel.queue_declare(queue="users", durable=True)
                return self
            except Exception:
                time.sleep(10)

    def publish_user(self, user):
        """Publish user info
        """
        self.channel.basic_publish(
            exchange='',
            routing_key="users",
            body=pickle.dumps(
                user),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print("User Sent")

    def publish_snapshot(self, snapshot, user_id):
        """Publish snapshot info
        """
        for field in self.queues:
            attr = snapshot.get(field)
            if attr:
                self.channel.basic_publish(
                    exchange='',
                    routing_key=field,
                    body=pickle.dumps(
                        dict(data=attr,
                             user_id=user_id,
                             datetime=snapshot.get('datetime'))),
                    properties=pika.BasicProperties(
                        delivery_mode=2,  # make message persistent
                    ))
            print(" [x] Sent")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
