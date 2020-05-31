
from pymongo import MongoClient


class AsdMongoClient:
    def __init__(self, mongo_url="mongodb://127.0.0.1:27017"):
        client = MongoClient(mongo_url)
        self.db = client.mind_db

    def save(self, payload):
        data, table_name = parse_payload(payload)
        table = self.db[table_name]
        if table_name == "users":
            mongo_doc = {
                'user_id': data["user_id"],
                'value': data,
            }
            table.update({"user_id": data["user_id"]},
                         mongo_doc, upsert=True)
        else:
            mongo_doc = {
                'user_id': data["user_id"],
                'datetime': data["datetime"],
                'value': data["data"],
            }
            table.update({"user_id": data["user_id"],
                          "datetime": data["datetime"]},
                         mongo_doc, upsert=True)
        print(f'new {table_name} entry')

    def get_data(self, query, table_name):
        table = self.db[table_name]
        return [x for x in table.find(query)]

    def get_user(self, user_id):
        return self.get_data({"user_id": user_id}, "users")

    def get_users(self, query={}):
        return self.get_data(query, "users")

    def get_data_by_user_id(self, user_id, table_name):
        return self.get_data({"user_id": user_id}, table_name)


def parse_payload(payload):
    return payload['data'],\
        payload['table_name']
