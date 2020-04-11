import requests
import click


class Client:
    def __init__(self, host, port, reader):
        self.reader = reader
        self.server_add = f'http://{host}:{port}'

    def get_config(self):
        self.server_config = requests.get(f'{self.server_add}/config')

    def post_snap_shot(self, snapshot, user_id):
        pass

    def run(self):
        click.echo('hi')


@click.command('run')
def main():
    Client(host='127.0.0.1', port='8000', reader=None).run()


if __name__ == "__main__":
    main()
