import requests
from flask import Flask

loadbalancer = Flask(__name__)


@loadbalancer.route("/")
def balance_load():
    return requests.get("http://load-balancing-exercises-server-1-1:5000/").text
