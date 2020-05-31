import click
from .api import run_api_server
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


def run_cli_api():
    cli_client(prog_name='asd-client')
