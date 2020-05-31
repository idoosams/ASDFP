from .depth_image_worker import DepthImgWorker
from .feelings_worker import FeelingsWorker
from .pose_worker import PoseWorker
from .color_image_worker import ColorImgWorker
from .users_worker import UserWorker

config = ['pose', 'color_image', 'feelings', 'depth_image']


class WorkersFactory:
    """
    WorkersFactory Class
    Creates instanse of a worker by name.
    """
    @staticmethod
    def create_worker(name, data_path):
        if name == 'pose':
            return PoseWorker()
        elif name == 'color_image':
            w = ColorImgWorker()
            w.data_path = data_path
            return w
        elif name == 'feelings':
            w = FeelingsWorker()
            w.data_path = data_path
            return w
        elif name == 'depth_image':
            return DepthImgWorker()
        elif name == 'users':
            return UserWorker()
