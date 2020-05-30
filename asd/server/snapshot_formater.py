import pathlib
from .asd_pb2 import Snapshot, User
import json


class SnapshotFormater:
    def format_snapshot(self, snapshot, user_id, data_path):
        snapshot_obj = Snapshot.FromString(snapshot)
        json_snapshot = {
            "datetime": snapshot_obj.datetime,
            "depth_image": self._depth_image_handler(snapshot_obj, user_id,
                                                     data_path),
            "color_image": self._color_image_handler(snapshot_obj, user_id,
                                                     data_path),
            "feelings": self._feeling_handler(snapshot_obj),
            "pose": self._pose_handler(snapshot_obj),
        }
        return json_snapshot

    def format_user(self, user):
        user_obj = User.FromString(user)
        return {
            "username": user_obj.username,
            "gender": user_obj.gender,
            "birthday": user_obj.birthday,
            "user_id": user_obj.user_id,
        }

    def _color_image_handler(self, snapshot, user_id, data_path):
        color_image, datetime = snapshot.color_image, snapshot.datetime

        path = pathlib.Path(data_path) / user_id / str(datetime)
        path.mkdir(parents=True, exist_ok=True)
        path = path / 'color_image_data'
        with open(path, 'wb') as f:
            f.write(color_image.data)

        return {'data_path': path,
                "width": color_image.width,
                "height": color_image.height}

    def _depth_image_handler(self, snapshot, user_id, data_path):
        depth_image, datetime = snapshot.depth_image, snapshot.datetime

        path = pathlib.Path(data_path) / user_id / str(datetime)
        path.mkdir(parents=True, exist_ok=True)
        path = path / 'depth_image_data'
        with open(path, 'w') as f:
            data_array = [float(num) for num in depth_image.data]
            json.dump(data_array, f)

        return {'data_path': path,
                "width": depth_image.width,
                "height": depth_image.height}

    def _feeling_handler(self, snapshot):
        return {
            "hunger": snapshot.feelings.hunger,
            "thirst": snapshot.feelings.thirst,
            "exhaustion": snapshot.feelings.exhaustion,
            "happiness": snapshot.feelings.happiness
        }

    def _pose_handler(self, snapshot):
        return {
            "translation": {
                "x": snapshot.pose.translation.x,
                "y": snapshot.pose.translation.y,
                "z": snapshot.pose.translation.z,
            },
            "rotation": {
                "x": snapshot.pose.rotation.x,
                "y": snapshot.pose.rotation.y,
                "z": snapshot.pose.rotation.z,
                "w": snapshot.pose.rotation.w,
            }}
