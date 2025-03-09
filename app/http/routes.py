from flask import Blueprint

from app.core.polls.router import pollsRouter

apiRouter = Blueprint("api", __name__)


apiRouter.register_blueprint(pollsRouter, url_prefix="/polls")
