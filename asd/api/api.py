import flask
import asd.api.templates as temp
from asd.dbclient.mongo_client import AsdMongoClient

from flask import send_file

app = flask.Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    response = ""
    users_list = app.config['db'].get_users()
    for user in users_list:
        response += temp.UserTemplate(user["value"])
    return response


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    res = app.config['db'].get_user(user_id)
    if len(res) >= 1:
        return temp.UserTemplate(res[0]["value"])
    return "no such user"


@app.route('/users/<user_id>/feelings', methods=['GET'])
def get_feelings(user_id):
    res = app.config['db'].get_data_by_user_id(user_id,
                                               "feelings")
    if len(res) >= 1:
        x = temp.MultiFeelingsTemplate(res)
        return temp.MultiFeelingsTemplate(res)
    return "no such user"


@ app.route('/users/<user_id>/pose', methods=['GET'])
def get_pose(user_id):
    return flask.jsonify(app.config['db'].get_data_by_user_id(user_id),
                         "pose")


def run_api_server(host, port, db_url):
    app.config['db'] = AsdMongoClient(db_url)
    app.run(host=host, port=port, threaded=True)


run_api_server("127.0.0.1", 8000, "mongodb://127.0.0.1:27017")
