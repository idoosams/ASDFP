import connection
import socket
 
 
class Listener:
    def __init__(self, port, host='0.0.0.0', backlog=1000, reuseaddr=True):
        self.sever = None
        self.port = port
        self.host = host
        self.backlog = backlog
        self.reuseaddr = reuseaddr
 
    def __repr__(self):
        return f"Listener(port={self.port}, host='{self.host}', backlog={self.backlog}, reuseaddr={self.reuseaddr})"
 
    def __enter__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.reuseaddr:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.host, self.port))
        server.listen(self.backlog)
        self.sever = server
 
    def __exit__(self, type, value, traceback):
        self.sever.close()
 
    def accept(self):
        try:
            conn, address = self.sever.accept()
            return connection.Connection(conn)
        except Exception as e:
            return e
 

