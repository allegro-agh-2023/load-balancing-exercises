import random
import string
import time
from datetime import datetime
from flask import Flask, request, jsonify
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
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)


def generate_request_id():
    length = 5
    available_chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(available_chars) for _ in range(length))


@app.route("/job", methods=["POST"])
def create_job():
    request_id = generate_request_id()
    app.logger.info("[%s] Got request", request_id)
    time.sleep(2)  # doing some job!
    app.logger.info("[%s] Serving response", request_id)
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
