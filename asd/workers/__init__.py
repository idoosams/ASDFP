# flake8: noqa
""" 
This is the Workers module.
The workers consume the data sent by the server to the mq, handle then and publish the results to the DB queue.


In order to add a worker write a new payload handler and pass it to the Worker class(base_worker.py) and add the worker to the factory.
"""
from .depth_image_worker import DepthImgWorker
from .feelings_worker import FeelingsWorker
from .pose_worker import PoseWorker
from .color_image_worker import ColorImgWorker
