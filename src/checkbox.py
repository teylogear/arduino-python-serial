import tkinter as tk
from tkinter import ttk


class Checkbox(ttk.Checkbutton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.BooleanVar(self)        
        self.configure(variable=self.variable)
    
    def get_text(self):
      return self.cget('text')

    def checked(self):
      return self.variable.get()