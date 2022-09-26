"""test_cli"""

import sys
from src.cli import CLI
from pytest import MonkeyPatch

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

def test_count_cli_params_positive() -> None:
    """test_count_cli_params_pos"""
    cli: CLI = CLI()
    assert cli.count_cli_params() == len(sys.argv)

def test_process_arguments_positive(monkey_patch: MonkeyPatch) -> None:
    """test_count_cli_params_pos"""
    
    monkey_patch.setattr('sys.argv', args)
    cli: CLI = CLI()
    assert cli.process_arguments() is False