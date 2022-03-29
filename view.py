from sre_constants import CATEGORY_UNI_LINEBREAK
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    
    PAD = 10
    button_names = ["C", "+/-", "%", "/", 7, 8, 9, "*", 4, 5, 6, "-", 1, 2, 3, "+", 0, ".", "="]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Calculator")
        # self.maxsize(300,420)
        self.minsize(300,420)

        self.value = tk.StringVar()
        self.value2 = tk.StringVar()

        self._frame_create()

        #Rows and Cols
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        
        
        self.iconbitmap('calculator_icon.ico')
        # self._create_entry()
        # self._create_label()

        for button in self.button_names:
            self._create_button(name=button, row=1, column=0)

    def main(self):
        self.mainloop()
    
    def _frame_create(self):
        self.frame = ttk.Frame(self)
        self.frame.grid(padx=self.PAD, pady=self.PAD)

    def _create_entry(self):
        entry = ttk.Entry(self.frame, textvariable=self.value)
        entry.grid()
    
    def _create_label(self):
        label1 = ttk.Label(self.frame, textvariable=self.value)
        label1.grid()
    
    def _create_button(self,name,row,column):
        button = ttk.Button(text=name, command=lambda button=name: self.controller.onClick(button))
        button.grid(row=row, column=column, sticky="nsew")
