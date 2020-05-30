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
        result = requests.get(f'{self.server_add}/fields')
        if result.status_code != 200:
            return 1
        self.server_config = json.loads(result.json())
        return 0

    def post_snapshot(self, snapshot, user_id):
        ep = f'{self.server_add}/{user_id}/snapshot'
        if self.server_config and self.parser:
            snapshot = self.parser.parse_snapshot(snapshot, self.server_config)
        result = requests.post(ep, snapshot.SerializeToString())
        if result.status_code != 201:
            return 1
        return 0

    def post_user(self, user):
        ep = f'{self.server_add}/users/{user.user_id}'
        result = requests.post(ep, user.SerializeToString())
        if result.status_code != 200:
            return 1
        return 0

    def upload_sample(self):
        i = 0
        if not self.reader:
            return i
        with self.reader as reader:
            for snapshot in reader:
                result = self.post_snapshot(snapshot, reader.user.user_id)
                if result == 0:
                    i = i+1
        return i
