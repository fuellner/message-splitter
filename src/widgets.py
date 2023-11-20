"""
widget classes module
"""

import customtkinter as ctk
import tkinter as tk
import src.splitter as s
from tkinter import filedialog


class OptionsFrame(ctk.CTkFrame):
    """frame widget class for all potential options"""

    def __init__(self, parent, chunk_size: ctk.IntVar) -> None:
        super().__init__(master=parent)

        self.chunk_size: ctk.IntVar = chunk_size

        ctk.CTkLabel(master=self, text="chunk size:").pack(fill="x")
        ctk.CTkEntry(
            master=self,
            placeholder_text="chunk size as numeric value",
            textvariable=self.chunk_size
        ).pack()

        ctk.CTkButton(master=self, text="Twitter/X default length",
                      command=lambda: self.click(value=280)).pack(side="left", padx=10, pady=10)
        ctk.CTkButton(master=self, text="GETTR default length",
                      command=lambda: self.click(value=777)).pack(side="left", padx=10, pady=10)

    def click(self, value) -> None:
        self.chunk_size.set(value=value)


class ConvertFrame(ctk.CTkFrame):
    """
    widget with input and output fields aswell as buttons for triggering the splitting conversion and clearing the
    fields
    """

    def __init__(self, parent, chunk_size: ctk.IntVar) -> None:
        super().__init__(master=parent)

        self.chunk_size: ctk.IntVar = chunk_size

        # input field
        ctk.CTkLabel(master=self, text="input:").pack()
        self.input_textbox = ctk.CTkTextbox(master=self, height=200, width=450)
        self.input_textbox.pack(expand=True, fill="x")

        # output field
        ctk.CTkLabel(master=self, text="output:").pack()
        self.output_textbox = ctk.CTkTextbox(
            master=self, height=200, width=450)
        self.output_textbox.pack(expand=True, fill="x")

        frame1 = ctk.CTkFrame(master=self)

        # convert button
        ctk.CTkButton(
            master=frame1,
            text="convert",
            command=self.convert
        ).pack(
            side="left",
            padx=10,
            pady=10,
            fill="x"
        )

        # clear button
        ctk.CTkButton(
            master=frame1,
            text="clear",
            command=self.clear
        ).pack(
            side="right",
            padx=10,
            pady=10,
            fill="x"
        )

        frame1.pack()

        frame2 = ctk.CTkFrame(master=self)

        # open file button
        ctk.CTkButton(
            master=frame2,
            text="open",
            command=self.open_file
        ).pack(
            side="left",
            padx=10,
            pady=10,
            fill="x"
        )

        # save button
        ctk.CTkButton(
            master=frame2,
            text="save",
            command=self.save_to_file
        ).pack(
            side="left",
            padx=10,
            pady=10,
            fill="x"
        )

        frame2.pack()

    def convert(self) -> None:
        """wrapper function for using the actual logic of the splitter class"""
        splitter = s.Splitter(
            chunk_size=int(self.chunk_size.get()),
            # input_text=self.input_text.get()
            input_text=self.input_textbox.get(index1="0.0", index2="end")
        )
        self.output_textbox.insert(index="0.0", text=splitter.split_message())

    def clear(self) -> None:
        self.input_textbox.delete(index1="0.0", index2="end")
        self.output_textbox.delete(index1="0.0", index2="end")

    def save_to_file(self) -> None:
        file: IO[Incomplete] | None = filedialog.asksaveasfile()
        file.write(self.output_textbox.get(index1="0.0", index2="end"))
        file.close()

    def open_file(self) -> None:
        file: IO[Incomplete] | None = filedialog.askopenfile()
        self.input_textbox.insert(index="0.0", text=file.read())
        file.close()
