from .db_publisher import DBPublisher
from .worker_base import Worker
from .utills import parse_payload


class FeelingsWorker:
    @staticmethod
    def run(mq_url):
        """
        Start consuming and handles the data from the mq

        :param mq_url:
        """
        worker = Worker(FeelingsWorker.payload_handler,
                        DBPublisher(mq_url), 'feelings', mq_url)
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        feelings, user_id, datetime = parse_payload(payload)
        return {"data": feelings,
                "user_id": user_id,
                "datetime": datetime}


if __name__ == "__main__":
    FeelingsWorker.run()
