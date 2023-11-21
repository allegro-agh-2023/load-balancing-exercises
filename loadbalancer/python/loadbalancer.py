import requests
from flask import Flask, request, Response
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


@loadbalancer.after_request
def log_response_info(response):
    loadbalancer.logger.debug('Response logging:\n'
                              f'{response.status}\n'
                              f'{response.headers}'
                              f'{response.get_data()}\n')
    return response


ALL_HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@loadbalancer.route('/', defaults={'u_path': ''}, methods=ALL_HTTP_METHODS)
@loadbalancer.route("/<path:u_path>", methods=ALL_HTTP_METHODS)
def balance_load(u_path):
    first_instance_url = 'http://app-instance-1:5000'
    second_instance_url = 'http://app-instance-2:5000'

    ####
    # TODO: Start your implementation here
    #
    # Currently, all requests are forwarded to app-instance-1. Try to implement round-robin!
    # Every second request should be routed to app-instance-2.
    # You can test your load balancer with benchmark on GET http://localhost:8082/benchmark
    # ###

    proxy_response = requests.request(method=request.method,
                                      url=f'{first_instance_url}/{u_path}',
                                      headers=request.headers,
                                      data=request.get_data())

    return Response(response=proxy_response.text,
                    status=proxy_response.status_code,
                    headers=proxy_response.headers.items())
