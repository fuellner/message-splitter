"""main.py module"""
from sys import argv
import customtkinter as ctk
import src.widgets as w
from src.cli import CLI


class Application(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode(mode_string="dark")
        self.geometry(geometry_string="500x800")
        self.title(string="Message Splitter")

        # layout
        self.rowconfigure(index=0, weight=3)
        self.rowconfigure(index=1, weight=5)
        self.rowconfigure(index=2, weight=5)
        self.columnconfigure(index=0, weight=1, uniform="a")

        # data
        self.chunk_size = ctk.IntVar()

        # widgets
        w.OptionsFrame(
            parent=self,
            chunk_size=self.chunk_size
        ).grid(row=0, column=0)

        w.ConvertFrame(
            parent=self,
            chunk_size=self.chunk_size
        ).grid(row=1, column=0)


if __name__ == "__main__":
    if argv[1:]:
        CLI().run()
    else:
        Application().mainloop()
