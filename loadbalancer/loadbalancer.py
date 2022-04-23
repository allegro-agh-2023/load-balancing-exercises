import requests
from flask import Flask, request
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'DEBUG',
        'handlers': ['wsgi']
    }
})

loadbalancer = Flask(__name__)


@loadbalancer.before_request
def log_request_info():
    loadbalancer.logger.debug('Request logging:\n'
                              f'{request.method} {request.path}\n'
                              f'{request.headers}'
                              f'{request.get_data()}')


@loadbalancer.route('/', defaults={'u_path': ''})
@loadbalancer.route("/<path:u_path>")
def balance_load(u_path):
    # TODO
    loadbalancer.logger.info(f"Proxying path: '{u_path}'")
    return requests.get(f'http://app-instance-1:5000/{u_path}').text
