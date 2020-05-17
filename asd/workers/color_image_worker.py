from PIL import Image as PIL
from .db_publisher import DBPublisher
from .worker_base import Worker
import pathlib
from .utills import parse_payload

db_path = "/home/idos/Desktop/Advenced-System-Design/ASDFP/asd/data"


class ColorImgWorker:
    @staticmethod
    def run():
        worker = Worker(ColorImgWorker.payload_handler,
                        DBPublisher(), 'color_image')
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

        path = pathlib.Path(db_path) / user_id / 'color_images'
        path.mkdir(parents=True, exist_ok=True)
        path = path / f'{datetime}.jpg'

        with open(data_path, "rb") as f:
            img_data = f.read()

        image = PIL.frombytes(data=img_data, mode='RGB', size=size)
        image.save(path)

        return str(path)


if __name__ == "__main__":
    ColorImgWorker.run()
