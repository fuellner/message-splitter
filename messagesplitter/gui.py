"""module GUI"""

import tkinter as tk
from splitter import Splitter
from tkinter import IntVar, StringVar, Tk, Entry, Button, Text, Label


class GUI:
    def __init__(self) -> None:
        self.root: Tk = Tk()

        self.label_chunksize: Label = Label(
            self.root, text="chunksize")
        self.label_chunksize.pack()
        chunksize_var = StringVar(self.root)
        self.input_chunksize = Entry(
            self.root, textvariable=chunksize_var)
        self.input_chunksize.pack()

        self.input_text: Text = Text(self.root)
        self.input_text.pack()
        self.output_text: Text = Text(self.root)
        self.output_text.pack()

        self.convert_button: Button = Button(
            self.root, text="convert", command=self.split_message)
        self.convert_button.pack()

        self.delete_button: Button = Button(
            self.root, text="delete", command=self.delete_input)
        self.delete_button.pack()

        self.quit_button: Button = Button(
            self.root, text="quit", command=self.quit_app)
        self.quit_button.pack()

    def delete_input(self) -> None:
        """method delete_input"""
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def run_mainloop(self) -> None:
        """method run_mainloop"""
        self.root.mainloop()

    def quit_app(self) -> None:
        """method quit_app"""
        print("Bye!")
        self.root.destroy()

    def split_message(self) -> None:
        """method split_message"""
        if self.input_chunksize.get() == "":
            return None
        splitter = Splitter(
            int(self.input_chunksize.get()),
            self.input_text.get("1.0", tk.END)
        )
        splitted_message = splitter.split_message()
        self.output_text.insert("1.0", splitted_message)
