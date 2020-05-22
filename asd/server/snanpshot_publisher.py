import pika
import pickle
# todo: loger by mq

config = ['datetime', 'pose', 'color_image', 'feelings', 'depth_image']


class SnanpshotPublisher():
    def __init__(self, host='0.0.0.0'):
        self.host = host

    def __enter__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        for field in config:
            self.channel.queue_declare(queue=field, durable=True)
        return self

    def publish(self, snapshot, user_id, datetime):
        for field in config:
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
