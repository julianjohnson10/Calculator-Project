import tkinter as tk
from tkinter import W, ttk
import math
class View(tk.Tk):
    
    PAD = 10
    button_names = ["%", "1/x", 7, 4, 1, "+/-", "CE", "x²", 8, 5, 2, 0, "C", "√", 9, 6, 3, ".", "<=", "÷", "×", "-", "+", "="]

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.title("Calculator")
        # self.maxsize(300,420)
        self.minsize(300,420)

        self.value = tk.StringVar()
        self.value2 = tk.StringVar()
        self.iconbitmap('calculator_icon.ico')
        
        self.cols = 4
        self.rows = int(math.ceil(len(self.button_names)/self.cols))
        i = 0
        for col in range(self.cols):
            for row in range(self.rows):
                self._create_button(name=self.button_names[i], column=col, row=row+1)
                self.rowconfigure(row, weight=1)
                self.columnconfigure(col, weight=1)
                i += 1
        self._create_label()
        
    def main(self):
        self.mainloop()
    
    def _frame_create(self):
        self.frame = ttk.Frame(self)
        self.frame.grid(sticky="nsew", row=0, column=0)

    def _create_entry(self):
        entry = ttk.Entry(textvariable=self.value)
        entry.grid(row=0, column=0)
    
    def _create_label(self):
        font = ttk.Style()
        font.configure('TLabel',font=('Helvetica', 24))
        label = ttk.Label(style='TLabel',textvariable=self.value)
        label.grid(row=0, column=0)
    
    def _create_button(self,name,row=None,column=None):
        buttonFont = ttk.Style()
        buttonFont.configure('TButton',font=('Helvetica', 24))
        button = ttk.Button(text=name, style='TButton', command=lambda button=name: self.controller.onClick(button))
        button.grid(row=row, column=column, sticky="nsew")
