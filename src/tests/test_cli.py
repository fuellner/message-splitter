"""test_cli"""

import sys
from src.cli import CLI


def test_check_params_all_fail() -> None:
    """test_check_params_all_fail"""
    cli: CLI = CLI()
    assert cli.check_params() is False


def test_check_params_all_pass() -> None:
    """test_check_params_all_pass"""
    cli: CLI = CLI()
    cli.chunk_size = 100
    cli.output_filename = 'test.txt'
    cli.input_file = 'test.txt'
    assert cli.check_params() is True


def test_count_cli_params() -> None:
    """test_count_cli_params_pos"""
    cli: CLI = CLI()
    assert cli.count_cli_params() == len(sys.argv)


def test_process_arguments_positive() -> None:
    """test_count_cli_params_pos"""
    cli: CLI = CLI()
    cli.arguments = [('-n', '100'), ('-o', 'test.txt'), ('-f', 'README.md')]
    assert cli.process_arguments() is True


def test_process_arguments_negative() -> None:
    """test_count_cli_params_pos"""
    cli: CLI = CLI()
    cli.arguments = [('-n', '100'), ('-f', 'README.md')]
    assert cli.process_arguments() is False
