import click
from .server_runner import ServerRunner


@click.group()
def cli_client():
    pass


@cli_client.command('run_server')
@click.option('-h', 'host', default='127.0.0.1')
@click.option('-p', 'port', default='5000')
def run_server(host, port):
    ServerRunner.run(host=host, port=port)


def run_cli_api():
    cli_client(prog_name='asd-client')
