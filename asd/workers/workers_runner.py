from .workers_factory import WorkersFactory
from multiprocessing import Process
import click


class WorkersRunner():
    @staticmethod
    def run(workers_list):
        for worker_name in workers_list:
            click.echo("aaaaaaa")
            worker = WorkersFactory.create_worker(worker_name)
            if worker:
                worker.run()
                # process = Process(target=worker.run)
                # process.start()
                # print(f'{worker_name} had started')
