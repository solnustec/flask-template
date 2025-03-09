from flask import jsonify

from app.core.polls.errors import PollsBadRequestError, PollsNotFoundError


def handle_polls_error(error: Exception):

    if isinstance(error, PollsBadRequestError):
        return jsonify({"err": str(error)}), 400

    if isinstance(error, PollsNotFoundError):
        return jsonify({"err": str(error)}), 404

    return jsonify({"err": str(error)}), 500
