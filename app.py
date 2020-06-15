from flask import Flask, request, make_response, redirect, render_template, Blueprint
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_filename)
    from apps.Farmacias.views import farmacia_bp
    app.register_blueprint(farmacia_bp, url_prefix='/')

    return app.run("0.0.0.0", port=80 , debug=True)


if __name__ == "__main__":
	create_app()
