import click
from .server_runner import ServerRunner
import configparser


config = configparser.ConfigParser()
config.read('../config.ini')


@click.group()
def cli_client():
    pass


@cli_client.command('run_server')
@click.option('-h', 'host', default=config['server']['host'])
@click.option('-p', 'port', default=config['server']['port'])
def run_server(host, port):
    ServerRunner.run(host=host, port=port)


def run_cli_api():
    cli_client(prog_name='asd-client')
