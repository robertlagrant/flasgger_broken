from flask import Flask
from flasgger import Swagger

from .blueprint import b


swagger_config = {
    'title': 'Flasgger validation?',
    'uiversion': 2,
    'basePath':''
}

swagger_definition = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}


def create_app():

    app = Flask(__name__)
    app.config['SWAGGER'] = swagger_config
    Swagger(app, config=swagger_definition, template_file='swagger.yaml')

    app.register_blueprint(b)

    return app
