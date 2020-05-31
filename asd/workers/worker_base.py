import pika
import pickle
from furl import furl
import time
import click


class Worker():
    """
    The base class of the workers
    """
    def __init__(self, payload_handler, db_publisher, queue_name,
                 mq_url='rabbitmq://127.0.0.1:5672'):
        """
        :param payload_handler:
        :param db_publisher:
        :param queue_name: queue to listen to
        :param mq_url: [description], defaults to 'rabbitmq://127.0.0.1:5672'
        """
        self.queue_name = queue_name
        self.db_publisher = db_publisher
        self.payload_handler = payload_handler
        self.channel = None
        for i in range(5):
            try:
                click.echo(f"{mq_url}")
                x = furl(mq_url)
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(x.host, x.port))
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue=queue_name, durable=True)
                click.echo("succssed to init")
                return
            except Exception as e:
                if i == 4:
                    raise e
                time.sleep(10)
        click.echo(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(self, ch, method, properties, body):
        payload = pickle.loads(body)
        db_payload = self.payload_handler(payload)
        with self.db_publisher as publisher:
            publisher.publish(
                db_payload,
                self.queue_name)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback)
        self.channel.start_consuming()
