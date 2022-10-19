"""test_gui"""

from tkinter import Button, Checkbutton, Entry, IntVar, Label, Text, Tk
import tkinter as tk
from src.gui import GUI


def test_gui_init_positive() -> None:
    """test_gui_init_positive"""
    gui: GUI = GUI()
    assert isinstance(gui, GUI) is True
    assert isinstance(gui.root, Tk) is True
    assert isinstance(gui.label_chunksize, Label) is True
    assert isinstance(gui.input_chunksize, Entry) is True
    assert isinstance(gui.checkstate, IntVar) is True
    assert isinstance(gui.checkbutton, Checkbutton) is True
    assert isinstance(gui.label_filepath, Label) is True
    assert isinstance(gui.input_filepath, Entry) is True
    assert isinstance(gui.label_input_text, Label) is True
    assert isinstance(gui.input_text, Text) is True
    assert isinstance(gui.output_text, Text) is True
    assert isinstance(gui.convert_button, Button) is True
    assert isinstance(gui.delete_button, Button) is True
    assert isinstance(gui.quit_button, Button) is True


def test_delete_input() -> None:
    """test_delete_input method"""
    gui: GUI = GUI()
    content = "TEST string"
    gui.input_text.insert("1.0", content)
    assert gui.input_text.get("1.0", tk.END) == 'TEST string\n'
    gui.delete_input()
    assert gui.input_text.get("1.0", tk.END) == "\n"
