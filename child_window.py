from tkinter import *

class ChildWindow:
    def __init__(self, parent, width, height, title="My app", resizable=(False, False), a=0, b=0):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{a}+{b}")
        self.root.resizable(resizable[0], resizable[1])

    #     self.grab_focus()
    # def grab_focus(self):
    #     self.root.grab_set()
    #     self.root.focus_set()
    #     self.root.wait_window()