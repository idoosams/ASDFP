import click
from .client_module import Client
from .reader import Reader
from .proto_parser import Parser


@click.group()
@click.pass_obj
@click.option('-h', 'host', default='127.0.0.1')
@click.option('-p', 'port', default='5000')
def cli_client(obj, host, port):
    obj['Client'] = Client(host, port)


@cli_client.command('upload_sample')
@click.argument('path')
@click.pass_obj
def upload_sample(obj, path):
    client = obj['Client']
    client.reader = Reader(path)
    client.parser = Parser()
    client.upload_sample()


@cli_client.command('get_config')
@click.pass_obj
def get_config(obj):
    client = obj['Client']
    click.echo(client.server_config)


def run_cli_api():
    cli_client(prog_name='asd-client', obj={})
