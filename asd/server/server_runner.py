from .flask_server import Server
from .snanpshot_publisher import SnanpshotPublisher
from .snapshot_formater import SnapshotFormater


class ServerRunner():
    @staticmethod
    def run(host, port):
        # datetime in mandatory in every snapshot!
        config = ['datetime', 'pose', 'color_image', 'feelings', 'depth_image']
        server = Server(host=host, port=port)
        datapath = "/home/idos/Desktop/Advenced-System-Design/ASDFP/asd/data"
        server.run_server(config, SnapshotFormater(),
                          SnanpshotPublisher(), datapath)
