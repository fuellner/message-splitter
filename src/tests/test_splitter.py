"""PyUnit test for Splitter module"""
from pathlib import Path
from src.splitter import Splitter


def test_split_message() -> None:
    """test_split_message pytest unit test method"""
    splitter = Splitter()
    data_path = Path("./src/tests/data")
    input_file = data_path.absolute() / 'input_text.txt'
    splitted_text = splitter.split_message(100, input_file.open().read())
    output = data_path / 'output_text.txt'
    assert splitted_text == output.open().read()


def test_load_input_string() -> None:
    """test_load_input_string pytest unit test method"""
    splitter = Splitter()
    data_path = Path("./src/tests/data")
    input_file = data_path.absolute() / 'input_text.txt'
    assert splitter.load_input_string(
        str(input_file)) == input_file.open().read()
