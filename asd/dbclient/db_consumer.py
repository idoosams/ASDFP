import pika
import pickle
from saver import MongoSaver as Saver


class DbConsumer():
    def __init__(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='db_feed', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(self, ch, method, properties, body):
        payload = pickle.loads(body)
        Saver().save(payload)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue="db_feed",
                                   on_message_callback=self.callback)
        self.channel.start_consuming()


DbConsumer().start_consuming()
