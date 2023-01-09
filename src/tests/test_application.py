"""PyUnit test for application module"""
from src.application import Application
from src.cli import CLI


def test_get_cli() -> None:
    """test cli method"""
    app: Application = Application()
    method_return_value: CLI = app.get_cli()
    assert isinstance(method_return_value, CLI)
