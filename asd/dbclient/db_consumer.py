import pika
import pickle
from furl import furl
import time
import click
from .saver import MongoSaver as Saver


class DbConsumer():
    def __init__(self, host, port):
        click.echo("enter to init")
        self.host = host
        self.port = port
        self.channel = None
        for i in range(5):
            try:
                click.echo("start to init")
                x = furl("rabbitmq://mq-asd:5672")
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(x.host, x.port))
                # self.connection = pika.BlockingConnection(
                #     pika.ConnectionParameters('localhost'))
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue='db_feed', durable=True)
                click.echo("succssed to init")
                return
            except Exception as e:
                if i==4:
                    raise e
                time.sleep(10)

    def callback(self, ch, method, properties, body):
        payload = pickle.loads(body)
        Saver(self.host, self.port).save(payload)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue="db_feed",
                                   on_message_callback=self.callback)
        self.channel.start_consuming()
