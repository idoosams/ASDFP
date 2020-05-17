import click
from .workers_runner import WorkersRunner


@click.command()
@click.option('-w', 'workers_names', default="")
def cli_client(workers_names):
    workers_list = workers_names.split(',')
    WorkersRunner.run(workers_list)


def run_cli_api():
    cli_client(prog_name='asd-client')
