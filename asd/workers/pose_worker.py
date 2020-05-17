import json
from .db_publisher import DBPublisher
from .worker_base import Worker


class PoseWorker:
    @staticmethod
    def run():
        worker = Worker(PoseWorker.payload_handler,
                        DBPublisher(), 'pose')
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        data = payload['data']
        translation = data["translation"]
        rotation = data["rotation"]
        return json.dumps({"translation": translation, "rotation": rotation})


if __name__ == "__main__":
    PoseWorker.run()
