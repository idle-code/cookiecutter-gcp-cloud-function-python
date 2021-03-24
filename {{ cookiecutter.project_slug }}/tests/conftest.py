import pytest
from flask import Flask, request

from main import {{ cookiecutter.code_entry_point }}


@pytest.fixture
def test_app():
    def post_handler() -> str:
        return {{ cookiecutter.code_entry_point }}(request)

    app = Flask(__name__)
    app.config["TESTING"] = True
    app.route("/", methods=["POST"])(post_handler)
    with app.app_context():
        yield app


@pytest.fixture
def client(test_app):
    with test_app.test_client() as client:
        yield client
