# cli.py

import getopt
import sys
import os
from typing import Tuple
from splitter import Splitter

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
        try:
            self.arguments, self.ueberhang = getopt.getopt(
                sys.argv[1:],
                "hf:o:n:",
                ["help", "file=", "output=", "chunksize="]
            )
            for current_argument, current_value in self.arguments:
                if current_argument in ("-h", "--help"):
                    print ("displaying help")
                if current_argument in ("-f", "--file"):
                    self.input_file = current_value
                if current_argument in ("-o", "--output"):
                    self.output_filename = current_value
                if current_argument in ("-n", "--chunksize"):
                    self.chunk_size = int(current_value)
        except getopt.error as err:
            print (str(err))
        return self.check_params()

    def check_params(self) -> bool:
        """check_params method """
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

    def split_message(self) -> str:
        """split_message method in CLI class"""
        splitter = Splitter(
            self.chunk_size,
            "",
            self.input_file,
            self.output_filename
        )
        return splitter.split_message()
