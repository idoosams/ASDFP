import flask
import pathlib
from asd.dbclient.mongo_client import AsdMongoClient

from flask import send_file

app = flask.Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    return flask.jsonify(app.config['db'].)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):

    return flask.jsonify(app.config['db'].get_user(user_id))


@app.route('/users/<user_id>/snapshots', methods=['GET'])
def get_snapshots(user_id):

    return flask.jsonify(app.config['db'].get_snapshots(user_id))


@app.route('/users/<user_id>/snapshots/<snapshot_id>', methods=['GET'])
def get_snapshot(user_id, snapshot_id):
    return flask.jsonify(app.config['db'].get_snapshot(user_id, snapshot_id))


@app.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>', methods=['GET'])
def get_result(user_id, snapshot_id, result_name):
    r = app.config['db'].get_result(user_id, snapshot_id, result_name)

    if 'data' in r:
        result_file = pathlib.Path(r['data'])
        if result_file.exists():
            r['data'] = f'/users/{user_id}/snapshots/{snapshot_id}/{result_name}/data'
    return flask.jsonify(r)


@app.route('/users/<user_id>/snapshots/<snapshot_id>/<result_name>/data', methods=['GET'])
def get_result_data(user_id, snapshot_id, result_name):
    r = app.config['db'].get_result(user_id, snapshot_id, result_name)
    s = result_name.split('_')[0]
    result_file = pathlib.Path(r['data']) / f'{s}.jpg'
    if result_file.exists():
        return send_file(str(result_file), mimetype='image/jpg')
    return flask.jsonify(r)


def run_api_server(host, port, db_url):
    app.config['db'] = AsdMongoClient(db_url)
    app.run(host=host, port=port, threaded=True)
