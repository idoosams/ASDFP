import click
from .saver import MongoSaver as Saver
from .db_consumer import DbConsumer
import configparser


@click.group()
def cli_client():
    pass


@click.option('--mq_url', 'mq_url', default="rabbitmq://127.0.0.1:5672")
@click.option('--db_url', 'db_url', default="mongodb://127.0.0.1:27017")
@click.option('--config_path', 'config_path')
@cli_client.command('run')
def run(mq_url, db_url, config_path):
    """Runs the dbclient
    :param mq_url:
    :param db_url: 
    :param config_path:
    """
    if config_path:
        config = configparser.ConfigParser()
        config.read(config_path)
        mq_url = config['mq']['url']
        db_url = config['db']['url']
        click.echo(
            f'''config file has loaded, all the explict flags overrides config file.
            the config path is: {config_path}''')
    DbConsumer(Saver(db_url), mq_url).start_consuming()


def run_cli_api():
    cli_client(prog_name='dbclient')
