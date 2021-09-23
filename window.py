from tkinter import  *
from child_window import ChildWindow

class Window:
    def __init__(self, width, height, title="My app", resizable=(False, False), a=0, b=0):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{a}+{b}")
        self.root.resizable(resizable[0], resizable[1])

    def run(self):
        self.root.mainloop()

    def create_child(self, width, height, title="Child", resizable = (False, False), a = 0, b = 0):
        ChildWindow(self.root, width, height, title, resizable, a, b)