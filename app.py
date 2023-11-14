﻿"""main.py module"""
import customtkinter as ctk
import src.widgets as w

# TODO: implement CLI
# TODO: Option menu; first option is switch between light and dark mode


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
        self.input_text = ctk.StringVar()
        self.output_text = ctk.StringVar()

        # widgets
        w.OptionsFrame(
            parent=self,
            chunk_size=self.chunk_size

        ).grid(row=0, column=0)

        w.ConvertFrame(
            parent=self,
            input_text=self.input_text,
            chunk_size=self.chunk_size
        ).grid(row=1, column=0)


if __name__ == "__main__":
    Application().mainloop()
