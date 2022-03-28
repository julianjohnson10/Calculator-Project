import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 10
    button_names = ["C", "+/-", "%", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "0", ".", "="]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Calculator")
        self.minsize(400,150)

        self.value = tk.StringVar()

        self._frame_create()
        self._create_entry()
        for button in self.button_names:
            self._create_button(button)

    def main(self):
        self.mainloop()
    
    def _frame_create(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_entry(self):
        entry = ttk.Entry(self.frame, textvariable=self.value)
        entry.pack()
    
    def _create_button(self, name):
        button = ttk.Button(self.frame, text=name)
        button.pack()