import random
import string
import time
from datetime import datetime
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

app = Flask(__name__)


def generate_request_id():
    length = 5
    available_chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(available_chars) for _ in range(length))


@app.before_request
def log_request_info():
    app.logger.debug('Request logging:\n'
                     f'{request.method} {request.path}\n'
                     f'{request.headers}'
                     f'{request.get_data()}\n')


@app.after_request
def log_response_info(response):
    app.logger.debug('Response logging:\n'
                     f'{response.status}\n'
                     f'{response.headers}'
                     f'{response.get_data()}\n')
    return response


@app.route("/job", methods=["POST"])
def create_job():
    request_id = generate_request_id()
    app.logger.info("[%s] Job started", request_id)
    time.sleep(2)  # doing some job!
    app.logger.info("[%s] Job finished", request_id)
    return {
        "request_id": request_id,
        "job_data": request.get_json()
    }


@app.route("/status", methods=["GET"])
def post_job():
    return {
        "status": "OK",
        "current_time": datetime.now().isoformat()
    }
