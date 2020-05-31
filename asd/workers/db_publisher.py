import pika
import pickle
from furl import furl
# todo: loger by mq


class DBPublisher():
    """
    DBPublisher class
    Publish the results of the workers to the DB queue
    """
    def __init__(self,  url='rabbitmq://127.0.0.1:5672'):
        self.url = furl(url)

    def __enter__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.url.host, self.url.port))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="db_feed", durable=True)
        return self

    def publish(self, data, table_name):
        """
        Publish the data to the table

        :param data:
        :param table_name:
        """
        self.channel.basic_publish(
            exchange='',
            routing_key="db_feed",
            body=pickle.dumps(
                dict(data=data,
                     table_name=table_name)),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
