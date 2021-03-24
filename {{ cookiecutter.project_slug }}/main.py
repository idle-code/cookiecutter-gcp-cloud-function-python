from typing import Callable

import yaml
from flask import Flask, Request, request
from pydantic import BaseSettings


class CloudFunctionSettings(BaseSettings):
    # Enable debug output (logging, additional messages, etc)
    DEBUG: bool = False


def {{ cookiecutter.code_entry_point }}(req: Request) -> str:
    return "ok"


def serve_flask_endpoint(endpoint: Callable) -> None:
    app = Flask(__name__)
    app.debug = True
    app.route("/")(lambda: endpoint(request))
    app.run()


def load_settings_from_environment() -> CloudFunctionSettings:
    return CloudFunctionSettings()


def load_settings_from_yaml(yaml_path: str) -> CloudFunctionSettings:
    with open(yaml_path) as yaml_file:
        yaml_env = yaml.safe_load(yaml_file)
        return CloudFunctionSettings(**yaml_env)


if __name__ == "__main__":
    # TODO: check arguments to see if `.env.yaml.template` should be generated
    settings = load_settings_from_yaml(".env.yaml")
    serve_flask_endpoint({{ cookiecutter.code_entry_point }})
else:
    settings = load_settings_from_environment()
