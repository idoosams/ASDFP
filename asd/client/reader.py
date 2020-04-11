

import gzip
import struct
from . import asd_pb2 as pb


class Reader():
    def __init__(self, path):
        self._path = path
        self._fd = None
        self.user = None

    def __repr__(self):
        return f"Reader(path = {self.path}, user = {self.user}"

    def __enter__(self):
        self._fd = gzip.open(self._path)
        self.user = self._get_user()

    def __exit__(self, type, value, traceback):
        self._fd.close()

    def _get_user(self):
        msg_size = struct.unpack("I", self._fd.read(4))[0]
        msg_bytes = self._fd.read(msg_size)
        return pb.User.FromString(msg_bytes)

    def __iter__(self):
        while True:
            buf = self._fd.read(4)
            if len(buf) == 4:
                msg_size = struct.unpack("I", buf)[0]
                msg_bytes = self._fd.read(msg_size)
                snapshot = pb.Snapshot.FromString(msg_bytes)
            else:
                if (buf != ''):  # todo: handel errors
                    pass
                break

            yield snapshot
