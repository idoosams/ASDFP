from .depth_image_worker import DepthImgWorker
from .feelings_worker import FeelingsWorker
from .pose_worker import PoseWorker
from .color_image_worker import ColorImgWorker

config = ['pose', 'color_image', 'feelings', 'depth_image']


class WorkersFactory:
    @staticmethod
    def create_worker(name):
        if name == 'pose':
            return PoseWorker()
        elif name == 'color_image':
            return ColorImgWorker()
        elif name == 'feelings':
            return FeelingsWorker()
        elif name == 'depth_image':
            return DepthImgWorker
