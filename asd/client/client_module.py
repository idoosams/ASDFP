import requests
import json


class Client:
    def __init__(self, host='127.0.0.1',
                 port='5000',
                 reader=None,
                 parser=None):
        self.reader = reader
        self.server_add = f'http://{host}:{port}'
        self.server_config = None
        self.update_config()

    def update_config(self):
        result = requests.get(f'{self.server_add}/config')
        if result.status_code != 200:
            return
        self.server_config = json.loads(result.json())

    def post_snapshot(self, snapshot, user_id):
        ep = f'{self.server_add}/{user_id}/snapshot'
        if self.server_config and self.parser:
            snapshot = self.parser.parse_snapshot(snapshot, self.server_config)
        result = requests.post(ep, snapshot.SerializeToString())
        if result.status_code != 201:
            return

    def post_user(self, user):
        ep = f'{self.server_add}/users/{user.user_id}'
        result = requests.post(ep, user.SerializeToString())
        if result.status_code != 200:
            return

    def upload_sample(self):
        if not self.reader:
            return
        with self.reader as reader:
            for snapshot in reader:
                self.post_snapshot(snapshot, reader.user.user_id)

