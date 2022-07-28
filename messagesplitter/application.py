"""app.py module"""

from cli import CLI
from gui import GUI


class Application:
    """class Application"""

    def __init__(self, cli: CLI) -> None:
        self.cli: CLI = cli
        self.gui: GUI = GUI()

    def run(self) -> None:
        """method run"""
        self.gui.run_mainloop()

    def get_cli(self) -> CLI:
        """method get_cli"""
        return self.cli

    def get_gui(self) -> GUI:
        """method get_gui"""
        return self.gui
