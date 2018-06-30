from flask import Flask


def create_app():
    """

    :return: Flask
    """
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    """

    :type app: Flask
    """
    from app.web import web
    app.register_blueprint(web)

