from .db_publisher import DBPublisher
from .worker_base import Worker


class UserWorker:
    @staticmethod
    def run(mq_url):
        worker = Worker(UserWorker.payload_handler,
                        DBPublisher(mq_url), 'users', mq_url)
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        return payload


if __name__ == "__main__":
    UserWorker.run("rabbitmq://127.0.0.1:5672")
