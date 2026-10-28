import logging

from flask import Blueprint, jsonify

healthRouter = Blueprint("health", __name__)
logger = logging.getLogger(__name__)


# strict_slashes=False: the cluster probes call /health, without a trailing slash
@healthRouter.route("/", strict_slashes=False)
def index():
    return jsonify({"status": "healthy"}), 200
