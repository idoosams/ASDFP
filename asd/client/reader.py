

import gzip
import struct
from .asd_pb2 import User, Snapshot


class Reader():
    def __init__(self, path):
        self._path = path
        self._fd = None
        self.user = None

    def __repr__(self):
        return f"Reader(path = {self.path}, user = {self.user}"

    def __enter__(self):
        self._fd = gzip.open(self._path)
        # self._fd2 = gzip.open("/home/idos/Desktop/ASDFP/tests/data_mocks/mock_sample.mind.gz", mode='wb')
        self.user = self._get_user()
        return self

    def __exit__(self, type, value, traceback):
        self._fd.close()
        self.user = None

    def _get_user(self):
        buf = self._fd.read(4)
        msg_size = struct.unpack("I", buf)[0]
        # self._fd2.write(buf)
        msg_bytes = self._fd.read(msg_size)
        # self._fd2.write(msg_bytes)
        return User.FromString(msg_bytes)

    def __iter__(self):
        while True:
            buf = self._fd.read(4)
            if len(buf) == 4:
                msg_size = struct.unpack("I", buf)[0]
                # self._fd2.write(buf)
                msg_bytes = self._fd.read(msg_size)
                # self._fd2.write(msg_bytes)
                # self._fd2.close()
                snapshot = Snapshot.FromString(msg_bytes)
            else:
                if (buf != ''):  # todo: handel errors
                    pass
                break

            yield snapshot
