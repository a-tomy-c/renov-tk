from tkinter import ttk
import tkinter as tk


class ComboboxBase(ttk.Combobox):
    def __init__(self, master=None, fg='blue', bg='white', **kw):
        super().__init__(master=master, **kw)
        self.master = master
        self._config_comboboxbase()

    def _config_comboboxbase(self):
        self.var_item = tk.StringVar()
        self.config(textvariable=self.var_item)

    def items(self) -> list:
        return self['values']
    
    def set_items(self, values:list):
        self.config(values=values)

    def current_item(self) -> str:
        return self.get()
    
    def set_current_item(self, item:str):
        self.set(item)

    def index(self) -> int:
        return self.current()
    
    def set_index(self, index:int):
        self.current(index)

    def set_item(self, value:str):
        values = list(self.items())
        values.append(str(value))
        self.set_items(values=values)

    def set_command(self, method):
        self.bind('<<ComboboxSelected>>', method)
        