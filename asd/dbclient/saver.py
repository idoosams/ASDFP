from pymongo import MongoClient
from .utills import parse_payload


class MongoSaver:
    def __init__(self, mongo_url="mongodb://127.0.0.1:27017"):
        client = MongoClient(mongo_url)
        self.db = client.mind_db

    def save(self, payload):
        data, table_name = parse_payload(payload)
        if table_name == "users":
            mongo_doc = {
                'user_id': data["user_id"],
                'value': data,
            }
        else:
            mongo_doc = {
                'user_id': data["user_id"],
                'datetime': data["datetime"],
                'value': data["data"],
            }
        table = self.db[table_name]
        table.insert_one(mongo_doc)
        print(f'new {table_name}')
