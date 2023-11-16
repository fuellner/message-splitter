"""cli.py"""

from src.splitter import Splitter
from argparse import ArgumentParser, Namespace


class CLI:
    def __init__(self) -> None:
        # initialize propterties
        self.file_content: str = ""

        # build actual CLI
        self.parser = ArgumentParser()
        self.parser.add_argument(
            "-i", "--input", help="Defines the input file with content to split.", required=True)
        self.parser.add_argument(
            "-o", "--output", help="Defines the output file for writing splitted content to.", required=False)
        self.parser.add_argument(
            "-c", "--chunksize", help="character size of chunks in which the given text shall be splitted.", required=True)

    def run(self) -> None:
        self.args: Namespace = self.parser.parse_args()
        self._open_file()
        self._split_content()
        self._handle_output()

    def _open_file(self) -> None:
        with open(file=self.args.input) as file:
            self.file_content: str = file.read()

    def _split_content(self) -> None:
        self.splitted_text: str = Splitter(
            chunk_size=int(self.args.chunksize), input_text=self.file_content).split_message()

    def _handle_output(self) -> None:
        if self.args.output:
            try:
                with open(file=self.args.output, mode="w") as file:
                    file.write(self.splitted_text)
            except:
                raise IOError("file could not be written")
        else:
            print(self.splitted_text)
