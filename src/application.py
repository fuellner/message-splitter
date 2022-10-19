"""app.py module"""

from cli import CLI
from gui import GUI
from splitter import Splitter


class Application:
    """class Application"""

    def __init__(self) -> None:
        self.cli: CLI = CLI()
        self.gui: GUI = GUI()

    def run(self) -> None:
        """method run"""
        self.cli.read_arguments()
        if self.cli.count_cli_params() > 1 and self.cli.process_arguments():
            splitter: Splitter = Splitter()
            splitter.split_message(
                self.cli.chunk_size,
                splitter.load_input_string(self.cli.input_file),
                True,
                self.cli.output_filename
            )
        elif self.cli.count_cli_params() == 1:
            self.gui.run_mainloop()

    def get_cli(self) -> CLI:
        """method get_cli"""
        return self.cli

    def get_gui(self) -> GUI:
        """method get_gui"""
        return self.gui
