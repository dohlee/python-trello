import os
import pytrello
import yaml

import board as board_api
import pytrello.request_wrapper as request


def get_api_info(api_name):
    package_dir = os.path.dirname(pytrello.__path__[0])
    api_yaml = os.path.join(package_dir, 'pytrello', 'api', 'api.yaml')
    api_info = yaml.load(open(api_yaml))
    return api_info[api_name]


def run_api(api_name, **kwargs):
    api_info = get_api_info(api_name)
    uri = api_info['uri']
    request_type = api_info['request_type']
    if request_type == 'GET':
        r = request.get(uri, **kwargs)
    elif request_type == 'POST':
        r = request.post(uri, **kwargs)
    elif request_type == 'PUT':
        r = request.put(uri, **kwargs)
    elif request_type == 'DELETE':
        r = request.delete(uri, **kwargs)

    return r


if __name__ == '__main__':
    board_id = board_api.get_board_id('pytrello')
    print(run_api('get_board', board_id=board_id))
    # print(board_api.get_board(board_id=board_id))
