from pymongo import MongoClient
from pprint import pprint
from utills import parse_payload


class MongoSaver:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.mind_db
        # Issue the serverStatus command and print the results
        serverStatusResult = self.db.command("serverStatus")
        # pprint(serverStatusResult)

    def save(self, payload):
        data, user_id, date_time, queue_name = parse_payload(payload)
        mongo_doc = {
            'user_id': user_id,
            'datetime': date_time,
            'value': data
        }
        table = self.db[queue_name]
        table.insert_one(mongo_doc)
        print(f'new {queue_name}')
