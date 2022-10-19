"""module app"""

import os
import subprocess
import sys
import tkinter as tk
from tkinter import Canvas, filedialog, Text

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="select file", filetypes=(("textfiles", ".txt"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        lable = tk.Label(frame, text=app)
        lable.pack()


def runApps():
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    for app in apps:
        subprocess.call([opener, app])


canvas = tk.Canvas(root, height=700, width=700, bg="#243545")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(
    root,
    text="open file",
    padx=10, pady=5,
    fg="white", bg="#243545",
    command=addApp
)
openFile.pack()

runApps = tk.Button(root, text="run apps", padx=10, pady=5,
                    fg="white", bg="#243545", command=runApps)
runApps.pack()


for app in apps:
    lable = tk.Label(frame, text=app)
    lable.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
