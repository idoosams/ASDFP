import pika
import pickle
# todo: loger by mq


class DBPublisher():
    def __init__(self, host='localhost'):
        self.host = host

    def __enter__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="db_feed", durable=True)
        return self

    def publish(self, data, user_id, datetime):
        self.channel.basic_publish(
            exchange='',
            routing_key="db_feed",
            body=pickle.dumps(
                dict(data=data,
                     user_id=user_id,
                     datetime=datetime)),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
