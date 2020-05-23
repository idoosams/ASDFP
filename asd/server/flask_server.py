# based on:
# https://dev.to/duomly/how-to-create-a-simple-rest-api-with-python-/and-flask-in-5-minutes-3edg

from flask import Flask, request
from flask_restful import Resource, Api
import json


class Server():
    def __init__(self, host="127.0.0.1", port="5000"):
        self.app = None
        self.api = None
        self.host = host
        self.port = port

    def run_server(self, config, snapshot_formater,
                   snanpshot_publisher, data_path):
        class config_callback(Resource):
            def get(self):
                return json.dumps(config), 200

        class snapshot_callback(Resource):
            def post(self, user_id):
                snapshot_dict = snapshot_formater.format_snapshot(
                    request.data, user_id, data_path)
                with snanpshot_publisher as publisher:
                    publisher.publish(snapshot_dict, user_id,
                                      snapshot_dict["datetime"])

        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(config_callback, '/config/')
        self.api.add_resource(snapshot_callback, '/<user_id>/snapshot')
        self.app.run(host=self.host, port=self.port)


# if __name__ == "__main__":
#     from .snanpshot_publisher import SnanpshotPublisher
#     from .snapshot_formater import SnapshotFormater
#     # datetime in mandatory in every snapshot!
#     config = ['datetime', 'pose', 'color_image', 'feelings', 'depth_image']
#     server = Server()
#     datapath = "/home/idos/Desktop/Advenced-System-Design/ASDFP/asd/data"
#     server.run_server(config, SnapshotFormater(),
#                       SnanpshotPublisher(), datapath)
#     app = server.app
