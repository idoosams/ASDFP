import click
from .db_runner import DbRunner
import configparser


config = configparser.ConfigParser()
config.read('../config.ini')

@click.group()
def cli_client():
    pass


@cli_client.command('run')
@click.option('-h', 'host', default="")
@click.option('-p', 'port', default="")
def run_server(host, port):
    DbRunner.run(host=host, port=port)


def run_cli_api():
    cli_client(prog_name='dbclient')