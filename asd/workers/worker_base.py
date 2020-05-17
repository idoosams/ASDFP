import pika
import pickle


class Worker():
    def __init__(self, payload_handler, db_publisher, queue_name):
        self.queue_name = queue_name
        self.db_publisher = db_publisher
        self.payload_handler = payload_handler
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(self, ch, method, properties, body):
        payload = pickle.loads(body)
        db_payload = self.payload_handler(payload)
        with self.db_publisher as publisher:
            publisher.publish(
                db_payload,
                payload['user_id'],
                payload['datetime'],
                self.queue_name)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=self.callback)
        self.channel.start_consuming()
