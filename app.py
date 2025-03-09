from flask import Flask
from flask_cors import CORS

from app.config.settings import settings
from app.http.administrative.health import healthRouter
from app.http.administrative.info import infoRouter
from app.http.routes import apiRouter


def create_server():
    server = Flask(__name__)
    server.config["ENV"] = settings.ENVIRONMENT
    server.config["DEBUG"] = settings.DEBUG

    # Configuration CORS according to the environment variables
    CORS(server, resources={r"/*": {"origins": settings.CORS_ORIGINS}})

    server.register_blueprint(infoRouter, url_prefix="/")
    server.register_blueprint(healthRouter, url_prefix="/health")
    server.register_blueprint(apiRouter, url_prefix="/api")
    return server


httpServer = create_server()

if __name__ == "__main__":
    httpServer.run(host="0.0.0.0", port=5000, debug=httpServer.config["DEBUG"])
