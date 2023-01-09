"""module GUI"""

import tkinter as tk
from tkinter import IntVar, Tk, Entry, Button, Text, Label, Checkbutton
from src.splitter import Splitter


class GUI:
    """GUI class"""

    def __init__(self) -> None:
        self.root: Tk = Tk()
        # label chunksize
        self.label_chunksize: Label = Label(self.root, text="chunksize:")
        self.label_chunksize.grid(row=0, column=0)
        # input field chunksize
        self.input_chunksize = Entry(self.root)
        self.input_chunksize.grid(row=1, column=0)
        # label filepath
        self.label_filepath: Label = Label(self.root, text="file path:")
        self.label_filepath.grid(row=2, column=0)
        # input field file path
        self.input_filepath = Entry(self.root)
        self.input_filepath.grid(row=3, column=0)
        # checkbox for input file (path) option
        self.checkstate: IntVar = IntVar()
        self.checkbox: Checkbutton = Checkbutton(
            self.root,
            text='use input file',
            variable=self.checkstate,
            onvalue=1,
            offvalue=0
        )
        self.checkbox.grid(row=3, column=1)
        # label input text
        self.label_input_text = Label(self.root, text="input text:")
        self.label_input_text.grid(row=4, column=0)
        # input text field
        self.input_text: Text = Text(self.root)
        self.input_text.grid(row=5, column=0)
        # label output text
        self.label_output_text = Label(
            self.root, text="splitted output:"
        )
        self.label_output_text.grid(row=6, column=0)
        # output text field
        self.output_text: Text = Text(self.root)
        self.output_text.grid(row=7, column=0)
        # convert button
        self.convert_button: Button = Button(
            self.root, text="split!", command=self.split_message
        )
        self.convert_button.grid(row=8, column=0)
        # delete button
        self.delete_button: Button = Button(
            self.root, text="clear all fields", command=self.delete_input
        )
        self.delete_button.grid(row=8, column=1)
        # quit button
        self.quit_button: Button = Button(
            self.root, text="quit", command=self.quit_app)
        self.quit_button.grid(row=8, column=2)

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
        splitter: Splitter = Splitter()
        if not self.check_input():
            return
        if self.checkstate.get() == 1:
            content: str = splitter.load_input_string(
                self.input_filepath.get()
            )
            self.input_text.insert("1.0", content)

        splitted_message: str = splitter.split_message(
            int(self.input_chunksize.get()),
            self.input_text.get("1.0", tk.END),
        )
        self.output_text.insert("1.0", splitted_message)

    def check_input(self) -> bool:
        """method for checking input"""
        validation: bool = True

        if self.input_text.compare('end-1c', '==', '1.0') and self.checkstate.get() == 0:
            self.label_input_text.config(fg="red")
            validation = False
        else:
            self.label_input_text.config(fg="black")

        if self.input_chunksize.get() == "":
            self.label_chunksize.config(fg="red")
            validation = False
        else:
            self.label_chunksize.config(fg="black")

        if self.checkstate.get() == 1 and self.input_filepath.get() == "":
            self.label_filepath.config(fg="red")
            validation = False

        return validation
