import requests
import json


class Client:
    def __init__(self, host='127.0.0.1',
                 port='5000',
                 reader=None,
                 parser=None):
        """
        Server Class
        Sends the data of the sample file to the server

        :param host: defaults to '127.0.0.1'
        :param port: defaults to '5000'
        :param reader: read the data from sample file
        :param parser: parse the snapshot and leave only the relevant fields
        """
        self.reader = reader
        self.server_add = f'http://{host}:{port}'
        self.server_config = None
        self.update_config()

    def update_config(self):
        """[summary]
        Updates the config of the server
        """
        result = requests.get(f'{self.server_add}/fields')
        if result.status_code != 200:
            return 1
        self.server_config = json.loads(result.json())
        return 0

    def post_snapshot(self, snapshot, user_id):
        """
        Send snapshot data
        """
        ep = f'{self.server_add}/{user_id}/snapshot'
        if self.server_config and self.parser:
            snapshot = self.parser.parse_snapshot(snapshot, self.server_config)
        result = requests.post(ep, snapshot.SerializeToString())
        if result.status_code != 201:
            return 1
        return 0

    def post_user(self, user):
        """
        Send user data
        """
        ep = f'{self.server_add}/users'
        result = requests.post(ep, user.SerializeToString())
        if result.status_code != 201:
            return 1
        return 0

    def upload_sample(self):
        """
        Uploads the sample file
        """
        i = 0
        if not self.reader:
            return i
        with self.reader as reader:
            self.post_user(reader.user)
            for snapshot in reader:
                result = self.post_snapshot(snapshot, reader.user.user_id)
                if result == 0:
                    i = i+1
        return i
