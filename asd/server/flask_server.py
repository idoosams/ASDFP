from flask import Flask, request
from flask_restful import Resource, Api
import json


class Server():
    """
    Server Class
    Handels the connection with POST and GET endpoints

    avaliable EPs:
        - /fields/
        - /users/
        - /<user_id>/snapshot/
    """
    def __init__(self, host="127.0.0.1", port="5000"):
        """[summary]

        :param host: defaults to "127.0.0.1"
        :param port: defaults to "5000"
        """
        self.app = None
        self.api = None
        self.host = host
        self.port = port

    def run_server(self, fields, snapshot_formater,
                   snanpshot_publisher, data_path):
        class fields_callback(Resource):
            def get(self):
                return json.dumps(fields), 200

        class users_callback(Resource):
            def post(self):
                user_dict = snapshot_formater.format_user(request.data)
                with snanpshot_publisher as publisher:
                    publisher.publish_user(user_dict)

        class snapshot_callback(Resource):
            def post(self, user_id):
                snapshot_dict = snapshot_formater.format_snapshot(
                    request.data, user_id, data_path)
                with snanpshot_publisher as publisher:
                    publisher.publish_snapshot(snapshot_dict, user_id)

        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(fields_callback, '/fields/')
        self.api.add_resource(users_callback, '/users/')
        self.api.add_resource(snapshot_callback, '/<user_id>/snapshot')
        self.app.run(host=self.host, port=self.port)
