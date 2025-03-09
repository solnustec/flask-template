from flask import Blueprint, jsonify

from app.config.settings import settings

infoRouter = Blueprint("info", __name__)


@infoRouter.route("/")
def index():
    return (
        jsonify(
            {
                "name": settings.NAME,
                "description": settings.DESCRIPTION,
                "version": settings.VERSION,
                "author": settings.AUTHOR,
                "keywords": settings.KEYWORDS,
                "environment": settings.ENVIRONMENT,
            }
        ),
        200,
    )
