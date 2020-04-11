import socket
import contextlib


class Connection():
    def __init__(self, socket):
        self.socket = socket

    def __repr__(self):
        from_address, from_port = self.socket.getsockname()
        to_address, to_port = self.socket.getpeername()
        return f"<Connection from {from_address}:{from_port} to " \
            f"{to_address}:{to_port}>"

    def send(self, data):
        self.socket.sendall(data)

    @classmethod
    @contextlib.contextmanager
    def connect(cls, ip, port):
        try:
            sock = socket.socket()
            sock.connect((ip, port))
            yield Connection(sock)
        finally:
            pass

    def __enter__(self):
        pass

    def receive(self, size):
        data = []
        # Receive the data in small chunks and retransmit it
        while True:
            buffer = self.socket.recv(size)
            recv_len = len(buffer)
            data.append(buffer)
            if recv_len >= size:
                break
            if not buffer:
                raise Exception
            size = size - recv_len

        return b"".join(data)

    def __exit__(self, type, value, traceback):
        self.socket.close()
