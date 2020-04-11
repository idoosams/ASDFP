import asd.connection as connection
import socket


class Listener:
    def __init__(self, port, host='0.0.0.0', backlog=1000, reuseaddr=True):
        self.server = None
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuseaddr = reuseaddr

    def __repr__(self):
        return f"Listener(port={self.port}, host='{self.host}', "\
            f"backlog={self.backlog}, reuseaddr={self.reuseaddr})"

    def __enter__(self):
        _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.reuseaddr:
            _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        _socket.bind((self.host, self.port))
        _socket.listen(self.backlog)
        self.server = _socket

    def __exit__(self, type, value, traceback):
        self.server.close()

    def accept(self):
        try:
            conn, address = self.server.accept()
            return connection.Connection(conn)
        except Exception as e:
            return e
