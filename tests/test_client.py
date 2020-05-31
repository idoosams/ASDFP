from asd.server.snapshot_formater import SnapshotFormater
from asd.client import Reader, Parser, Client
from werkzeug.wrappers.response import Response
import pathlib
from furl import furl


import pytest


@pytest.fixture
def mock_respone():
    return {
        'datetime': "2019-12-04_08:08:07.339000",
        'depth_image': {
            'data_path': "",
            'width': 224,
            'height': 172
        },
        'color_image': {
            'data_path': "",
            'width': 1920,
            'height': 1080
        },
        'feelings': {
            'hunger': 0.0,
            'thirst': 0.0,
            'exhaustion': 0.0,
            'happiness': 0.0
        },
        'pose': {
            'translation':
            {
                'x': 0.4873843491077423,
                'y': 0.007090016733855009,
                'z': -1.1306129693984985
            },
            'rotation':
            {
                'x': -0.10888676356214629,
                'y': -0.26755994585035286,
                'z': -0.021271118915446748,
                'w': 0.9571326384559261
            }
        }
    }


def get_fields():
    return


def post_snapshot():
    pass


def test_client_e2e(httpserver, tmp_path, mock_respone):

    def validate(req):
        data = req.data
        snapshot_dict = SnapshotFormater().format_snapshot(data, '42',
                                                           tmp_path)
        snapshot_dict["color_image"]["data_path"] = ""
        snapshot_dict["depth_image"]["data_path"] = ""
        assert mock_respone == snapshot_dict
        return Response(response='OK', content_type='text/plain', status=201,)

    httpserver.expect_request(
        "/fields").respond_with_json(
            '["datetime", "pose", "color_image", "feelings", "depth_image"]')
    httpserver.expect_request(
        "/42/snapshot").respond_with_handler(validate)
    url = furl(httpserver.url_for("/"))
    sample_path = str(pathlib.Path(
        'tests/data_mocks/mock_sample.mind.gz').absolute())
    client = Client(host=url.host, port=url.port)
    client.reader = Reader(sample_path)
    client.parser = Parser()
    number_of_snapshots = client.upload_sample()

    assert number_of_snapshots == 1


