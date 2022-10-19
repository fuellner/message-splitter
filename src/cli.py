"""cli.py"""

import getopt
import sys
from typing import Tuple


class CLI:
    """CLI class"""

    def __init__(self) -> None:
        self.arguments: list[Tuple[str, str]]
        self.ueberhang: list[str]
        self.output_filename: str = ""
        self.input_file: str = ""
        self.chunk_size: int = 0

    def process_arguments(self) -> bool:
        """process_arguments method"""
        for current_argument, current_value in self.arguments:
            if current_argument in ("-h", "--help"):
                print("displaying help")
            if current_argument in ("-f", "--file"):
                self.input_file = current_value
            if current_argument in ("-o", "--output"):
                self.output_filename = current_value
            if current_argument in ("-n", "--chunksize"):
                self.chunk_size = int(current_value)
        return self.check_params()

    def check_params(self) -> bool:
        """check_params method"""
        result: bool = True
        if not bool(self.chunk_size):
            print("chunksize not given but required")
            result = False
        if not bool(self.output_filename):
            print("output filename not given but required")
            result = False
        if not bool(self.input_file):
            print("input file not given but required")
            result = False
        return result

    def count_cli_params(self) -> int:
        """count_cli_params method"""
        return len(sys.argv)

    def read_arguments(self) -> None:
        """read arguments from command line"""
        try:
            self.arguments, self.ueberhang = getopt.getopt(
                sys.argv[1:],
                "hf:o:n:",
                ["help", "file=", "output=", "chunksize="]
            )
        except getopt.error as err:
            print(str(err))
