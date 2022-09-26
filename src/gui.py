"""module GUI"""

import tkinter as tk
from splitter import *
from tkinter import IntVar, Tk, Entry, Button, Text, Label, Checkbutton


class GUI:
    """GUI class"""

    def __init__(self) -> None:
        self.root: Tk = Tk()

        self.label_chunksize: Label = Label(
            self.root, text="chunksize")
        self.label_chunksize.pack()
        self.input_chunksize = Entry(self.root)
        self.input_chunksize.pack()

        self.checkstate: IntVar = IntVar()
        self.checkbutton: Checkbutton = Checkbutton(
            self.root,
            text='Eingabe-Datei verwenden',
            variable=self.checkstate,
            onvalue=1,
            offvalue=0
        )
        self.checkbutton.pack()

        self.label_filepath: Label = Label(self.root, text="Datei-Pfad")
        self.label_filepath.pack()
        self.input_filepath = Entry(self.root)
        self.input_filepath.pack()

        self.label_input_text = Label(
            self.root, text="Text-Eingabe:"
        )
        self.label_input_text.pack()
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
