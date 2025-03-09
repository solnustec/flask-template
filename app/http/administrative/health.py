import logging

from flask import Blueprint, jsonify

healthRouter = Blueprint("health", __name__)
logger = logging.getLogger(__name__)


@healthRouter.route("/")
def index():
    return jsonify({"status": "healthy"}), 200
