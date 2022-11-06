"""PyUnit test for Splitter module"""
from pathlib import Path
from src.splitter import Splitter


def test_split_message() -> None:
    """test_split_message"""
    splitter = Splitter()
    data_path = Path("./src/tests/data")
    it = data_path.absolute() / 'input_text.txt'
    splitted_text = splitter.split_message(100, it.open().read())
    ot = data_path / 'output_text.txt'
    assert splitted_text == ot.open().read()
