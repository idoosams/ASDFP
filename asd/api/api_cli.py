import click
from .api import run_api_server
from .mongo_client import AsdMongoClient
import configparser


@click.group()
def cli_client():
    pass


@cli_client.command('run')
@click.option('--h', 'host', default="127.0.0.1")
@click.option('--p', 'port', default="8000")
@click.option('--db_url', 'db_url', default="mongodb://127.0.0.1:27017")
@click.option('--config_path', 'config_path')
def run(host, port, db_url, config_path):
    """
    Starts the api

    :param host: host addresss
    :param port: port number
    :param db_url: db url
    :param config_path: path to a config file
    """
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)
        host = config['api']['host']
        port = config['api']['port']
        db_url = config['db']['url']
        click.echo(
            f'''config file has loaded, all the explict flags overrides config file.
            the config path is: {config_path}''')
    run_api_server(host, port, db_url)


@cli_client.command('get_data')
@click.option('--db_url', 'db_url', default="mongodb://127.0.0.1:27017")
@click.argument('user_id', required=True)
@click.argument('table_name', required=True)
def get_data(db_url, user_id, table_name):
    """
    gets the data from the DB client

    :param db_url: db url
    :param user_id:
    :param table_name:
    """
    dbclient = AsdMongoClient(db_url)
    res = dbclient.get_data_by_user_id(user_id, table_name)
    if res:
        click.echo(res)
        return res


def run_cli_api():
    cli_client(prog_name='asd-client')
