from .db_consumer import DbConsumer


class DbRunner():
    @staticmethod
    def run(host, port):
        DbConsumer(host, port).start_consuming()