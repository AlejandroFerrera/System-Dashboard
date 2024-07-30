from flask import Flask
from metrics import Metrics
from flask import jsonify
from flask import render_template

app = Flask(__name__)


@app.route("/metrics", methods=["GET"])
def metrics() -> dict:
    """
    Endpoint to get system metrics.
    :return: Dictionary with CPU usage, CPU usage by core, and memory info.
    """

    cpu_usage = Metrics.get_cpu_usage()
    cpu_usage_by_core = Metrics.get_cpu_usage_by_core()
    memory_info = Metrics.get_memory_info()

    return jsonify(
        {
            "cpu_usage": cpu_usage,
            "cpu_usage_by_core": cpu_usage_by_core,
            "memory_info": memory_info,
        }
    )


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")
