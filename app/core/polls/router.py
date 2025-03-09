from flask import Blueprint, jsonify, request

from app.core.polls.handlers import handle_polls_error
from app.core.polls.services import PollService

pollsRouter = Blueprint("polls", __name__)


@pollsRouter.route("/")
def index():
    try:
        q = request.args.get("q", None)
        value = PollService.create(q)

        return jsonify({"msg": value}), 200
    except Exception as e:
        return handle_polls_error(e)
