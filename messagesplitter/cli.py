# cli.py

import getopt
import sys
import os
import time
from typing import Tuple

class CLI:
    def __init__(self) -> None:
        self.arg_length: int = len(sys.argv)
        self.argument_list: list[str]  = sys.argv[1:]
        self.options: str = "hf:o:n:"
        self.long_options: list[str] = ["help", "file=", "output=", "chunkSize="]
        self.arguments: list[Tuple[str, str]]
        self.ueberhang:list[str]

    def process_arguments(self) -> None:
        """process_arguments method"""
        try:
            self.arguments, self.ueberhang = getopt.getopt(self.argument_list, self.options, self.long_options)
            print(self.arguments)
            return
            
            for currentArgument, currentValue in self.arguments:
                if currentArgument in ("-h", "--help"):
                    print ("displaying help")
                if currentArgument in ("-f", "--file"):
                    if os.path.exists(currentValue):
                        with open(currentValue, "r") as file:
                            self.inputFile = file.read()
                if currentArgument in ("-o", "--output"):
                    self.outputFileName = currentValue
                if currentArgument in ("-n", "--chunkSize"):
                    self.chunkSize = int(currentValue)
        except getopt.error as err:
            print (str(err))