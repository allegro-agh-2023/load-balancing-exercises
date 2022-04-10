from flask import Flask

loadbalancer = Flask(__name__)


@loadbalancer.route("/")
def balance_load():
    return "I will balance your load!"
