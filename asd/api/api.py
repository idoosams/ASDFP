import flask
from .templates import UserTemplate, MultiFeelingsTemplate, MultiPoseTemplate
from .mongo_client import AsdMongoClient
import pathlib
from flask import send_file


app = flask.Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    response = ""
    users_list = app.config['db'].get_users()
    for user in users_list:
        response += UserTemplate(user["value"])
    return response


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    res = app.config['db'].get_user(user_id)
    if len(res) >= 1:
        return UserTemplate(res[0]["value"])
    return "no such user"


@app.route('/users/<user_id>/feelings', methods=['GET'])
def get_feelings(user_id):
    res = app.config['db'].get_data_by_user_id(user_id,
                                               "feelings")
    if len(res) >= 1:
        return MultiFeelingsTemplate(res)
    return "no such user"


@ app.route('/users/<user_id>/poses', methods=['GET'])
def get_pose(user_id):
    res = app.config['db'].get_data_by_user_id(user_id,
                                               "pose")
    if len(res) >= 1:
        return MultiPoseTemplate(res)
    return "no such user"


@ app.route('/users/<user_id>/<img_kind>/<datetime>', methods=['GET'])
def get_color_image(user_id, img_kind, datetime):
    res = app.config['db'].get_data({"user_id": user_id,
                                     "datetime": datetime}, img_kind)
    if len(res) >= 1:
        image_path = pathlib.Path(res[0]['value'])
        if image_path.exists():
            return send_file(str(image_path), mimetype='image/jpg')
    return f"no such {img_kind.split('_')}"


def run_api_server(host, port, db_url):
    app.config['db'] = AsdMongoClient(db_url)
    app.run(host=host, port=port, threaded=True)
