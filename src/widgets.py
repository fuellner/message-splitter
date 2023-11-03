"""
widget classes module
"""

import customtkinter as ctk
import src.splitter as s


class OptionsFrame(ctk.CTkFrame):
    """frame widget class for all potential options"""

    def __init__(self, parent, chunk_size: ctk.IntVar) -> None:
        super().__init__(master=parent)

        self.chunk_size: ctk.IntVar = chunk_size

        ctk.CTkLabel(master=self, text="Teilgröße:").pack(fill="x")
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
    def __init__(self,
                 parent,
                 input_text: ctk.StringVar,
                 chunk_size: ctk.IntVar
                 ) -> None:
        super().__init__(master=parent)

        self.input_text: ctk.StringVar = input_text
        self.chunk_size: ctk.IntVar = chunk_size

        # input field
        ctk.CTkLabel(master=self, text="Eingabe:").pack()
        ctk.CTkEntry(master=self, height=200, width=450,
                     textvariable=self.input_text).pack(expand=True, fill="x")

        # output field
        ctk.CTkLabel(master=self, text="Ausgabe:").pack()
        self.output = ctk.CTkTextbox(master=self, height=300, width=450)
        self.output.pack(expand=True, fill="x")

        ctk.CTkButton(master=self, text="Convert",
                      command=self.convert).pack(side="left", padx=10, pady=10, fill="x")

        ctk.CTkButton(master=self, text="Clear",
                      command=self.clear).pack(side="right", padx=10, pady=10, fill="x")

    def convert(self) -> None:
        """wrapper function for using the actual logic of the splitter class"""
        splitter = s.Splitter(
            chunk_size=int(self.chunk_size.get()),
            input_text=self.input_text.get()
        )
        self.output.insert(index="0.0", text=splitter.split_message())

    def clear(self) -> None:
        self.input_text.set(value="")
        self.output.delete(index1="0.0", index2="end")
