import requests
from multiprocessing.pool import ThreadPool
import time
from flask import Flask
from functools import partial
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

benchmark = Flask(__name__)


@benchmark.route("/benchmark", methods=["GET"])
def run_benchmark():
    benchmark.logger.info('Starting benchmark')

    load_balancers = [
        ('java', 'http://load-balancer-java:8080'),
        ('python', 'http://load-balancer-python:5000'),
        ('nginx', 'http://load-balancer-nginx:80'),
    ]

    results = [benchmark_results_for(load_balancer_name, load_balancer_url) for (load_balancer_name, load_balancer_url)
               in load_balancers]

    benchmark.logger.info('Benchmark finished')
    return {
        "load_balancers": results
    }


def benchmark_results_for(load_balancer_name, load_balancer_url):
    expected_time = 2.5
    time_elapsed, responses_successful = benchmark_load_balancer(load_balancer_url)

    return {
        "load_balancer": load_balancer_name,
        "measured_time": time_elapsed,
        "expected_time": expected_time,
        "errors_in_responses": not responses_successful,
        "result": "SUCCESS" if time_elapsed < expected_time and responses_successful else "FAIL"
    }


def benchmark_load_balancer(load_balancer):
    benchmark_subject = partial(execute_benchmarked_endpoint, load_balancer)
    time_elapsed, responses_successful = benchmark_function(benchmark_subject)
    return time_elapsed, responses_successful


def benchmark_function(benchmark_subject, threads=2):
    pool = ThreadPool(threads)
    start = time.time()
    results_async = [pool.apply_async(benchmark_subject) for _ in range(threads)]
    results = [result_async.get() for result_async in results_async]
    end = time.time()
    time_elapsed = end - start
    return time_elapsed, all(results)


def execute_benchmarked_endpoint(load_balancer):
    response = requests.post(url=f'{load_balancer}/job',
                             json={
                                 "some_data": "benchmarking"
                             })
    return response.status_code == 200
