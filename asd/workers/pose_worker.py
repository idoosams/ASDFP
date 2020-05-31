from .db_publisher import DBPublisher
from .worker_base import Worker
from .utills import parse_payload


class PoseWorker:
    @staticmethod
    def run(mq_url):
        """
        Start consuming and handles the data from the mq

        :param mq_url:
        """
        worker = Worker(PoseWorker.payload_handler,
                        DBPublisher(mq_url), 'pose', mq_url)
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        pose, user_id, datetime = parse_payload(payload)
        return {"data": pose,
                "user_id": user_id,
                "datetime": datetime}


if __name__ == "__main__":
    PoseWorker.run("rabbitmq://127.0.0.1:5672")
