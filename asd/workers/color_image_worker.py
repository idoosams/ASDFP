from PIL import Image as PIL
from .db_publisher import DBPublisher
from .worker_base import Worker
import pathlib
from .utills import parse_payload


class ColorImgWorker:
    """
    ColorImgWorker Class
    """
    data_path = "../data"  # defualt value

    @staticmethod
    def run(mq_url):
        """
        Start consuming and handles the data from the mq

        :param mq_url:
        """
        worker = Worker(ColorImgWorker.payload_handler,
                        DBPublisher(mq_url), 'color_image', mq_url)
        worker.start_consuming()

    @staticmethod
    def payload_handler(payload):
        path = ColorImgWorker.get_color_image_path(payload)
        print("ColorImgWorker finish prossesing")
        return path

    @staticmethod
    def get_color_image_path(payload):
        color_image, user_id, datetime = parse_payload(payload)
        size = (color_image['width'], color_image['height'])
        data_path = color_image['data_path']

        path = pathlib.Path(ColorImgWorker.data_path) / \
            user_id / 'color_images'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{datetime}.jpg'

        with open(data_path, "rb") as f:
            img_data = f.read()

        image = PIL.frombytes(data=img_data, mode='RGB', size=size)
        image.save(path)

        return {"data": str(path),
                "user_id": user_id,
                "datetime": datetime}


if __name__ == "__main__":
    ColorImgWorker.run()
