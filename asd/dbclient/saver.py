from pymongo import MongoClient
from pprint import pprint
from .utills import parse_payload
from furl import furl
import click


class MongoSaver:
    def __init__(self,  host, port):
        x = furl("mongodb://mongo-asd:27017")
        click.echo(f"{x.host}, {x.port}")
        client = MongoClient('mongodb://mongo-asd:27017')
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
