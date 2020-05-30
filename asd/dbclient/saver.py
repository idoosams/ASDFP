from pymongo import MongoClient
from .utills import parse_payload


class MongoSaver:
    def __init__(self, mongo_url="mongodb://127.0.0.1:27017"):
        client = MongoClient(mongo_url)
        self.db = client.mind_db

    def save(self, payload):
        data, user_id, date_time, table_name = parse_payload(payload)
        mongo_doc = {
            'user_id': user_id,
            'datetime': date_time,
            'value': data
        }
        table = self.db[table_name]
        table.insert_one(mongo_doc)
        print(f'new {table_name}')
