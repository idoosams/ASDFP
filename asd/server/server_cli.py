import click
from .flask_server import Server
from .snanpshot_publisher import SnanpshotPublisher
from .snapshot_formater import SnapshotFormater
import configparser


@click.group()
def cli_client():
    pass


@cli_client.command('run_server')
@click.option('--h', 'host', default="127.0.0.1")
@click.option('--p', 'port', default="5000")
@click.option('--fields', 'fields',
              default="datetime,pose,color_image,feelings,depth_image")
@click.option('--data_path', 'data_path', default="../data")
@click.option('--mq_url', 'mq_url', default="rabbitmq://127.0.0.1:5672")
@click.option('--config_path', 'config_path')
def run_server(host, port, fields, data_path, mq_url, config_path):
    """ start the server

    :param host: host addresss
    :param port: port number
    :param fields: the fields of the snapshots the server can handel, datetime is mandatory. example: "datetime,pose,color_image,feelings,depth_image".
    :param data_path: path to the server data
    :param mq_url: massage queue url
    :param config_path: path to a config file

    """
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)
        host = config['server']['host']
        port = config['server']['port']
        fields = config['server']['fields']
        mq_url = config['mq']['url']
        data_path = config['data']['path']
        click.echo(
            f'''config file has loaded, all the explict flags overrides config file.
            the config path is: {config_path}''')
    fields = fields.split(',')
    server = Server(host=host, port=port)
    server.run_server(fields, SnapshotFormater(),
                      SnanpshotPublisher(fields, mq_url), data_path)


def run_cli_api():
    cli_client(prog_name='asd-client')
