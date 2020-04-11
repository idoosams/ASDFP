# based on:
# https://dev.to/duomly/how-to-create-a-simple-rest-api-with-python-/and-flask-in-5-minutes-3edg

from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()


class Config(Resource):
    def get(self):
        pass


class Snapshot(Resource):
    def post(self, user_id):
        pass


api.add_resource(Config, '/config/')
api.add_resource(Snapshot, '/snapshot/<user_id>')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8000')
