from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main import main
    from app.builder import builder

    app.register_blueprint(main)
    app.register_blueprint(builder)

    return app