# cli.py

import getopt
import sys
import os
import time

class CLI:
    def __init__(self) -> None:
        self.arg_length = len(sys.argv)
        self.argumentList = sys.argv[1:]
        self.options = "hf:o:n:"
        self.long_options = ["help", "file=", "output=", "chunkSize="]

    def process_arguments(self) -> None:
        try:
            self.arguments, self.ueberhang = getopt.getopt(self.argumentList, self.options, self.long_options)
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