from .db_publisher import DBPublisher
from .worker_base import Worker
import pathlib
from matplotlib import cm
from matplotlib.pyplot import imshow, savefig
import numpy
import json

db_path = "../data"


class DepthImgWorker:
    @staticmethod
    def run():
        worker = Worker(DepthImgWorker.payload_handler,
                        DBPublisher(), 'depth_image')
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        path = DepthImgWorker.save_img_get_path(payload)
        print("DepthImgWorker finish prossesing")
        return path

    @staticmethod
    def save_img_get_path(payload):
        depth_image, user_id, datetime = payload['data'], \
            payload['user_id'], \
            payload['datetime']

        path = pathlib.Path(db_path) / user_id / 'depth_images'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{datetime}.jpg'

        with open(depth_image["data_path"], "r") as f:
            data_array = json.load(f)

        try:
            imshow(numpy.reshape(data_array,
                                 (depth_image["width"],
                                  depth_image["height"])),
                   cmap=cm.RdYlGn)
        except Exception as e:
            print(str(e))
        savefig(path)

        return str(path)


if __name__ == "__main__":
    DepthImgWorker.run()
