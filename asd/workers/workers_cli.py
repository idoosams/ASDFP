import click
import configparser
from .workers_factory import WorkersFactory


@click.command()
@click.option('--w', 'worker_name', default="", required=True)
@click.option('--mq_url', 'mq_url', default="rabbitmq://127.0.0.1:5672")
@click.option('--data_path', 'data_path', default="../data")
@click.option('--config_path', 'config_path')
def cli_client(worker_name, mq_url, data_path, config_path):
    """
    Start the worker

    :param worker_name:
    :param mq_url:
    :param data_path:
    :param config_path:
    """
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)
        mq_url = config['mq']['url']
        data_path = config['data']['path']
        click.echo(
            f'''config file has loaded, all the explict flags overrides config file.
            the config path is: {config_path}''')
    worker = WorkersFactory.create_worker(worker_name, data_path)
    if worker:
        worker.run(mq_url)
    else:
        click.echo("wrong worker name")


def run_cli_api():
    cli_client(prog_name='asd-client')
