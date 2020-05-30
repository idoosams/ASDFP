import json
from .db_publisher import DBPublisher
from .worker_base import Worker


class FeelingsWorker:
    @staticmethod
    def run(mq_url):
        worker = Worker(FeelingsWorker.payload_handler,
                        DBPublisher(mq_url), 'feelings', mq_url)
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        data = payload['data']
        return json.dumps(data)


if __name__ == "__main__":
    FeelingsWorker.run()
