import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk


class TreePath(ttk.Treeview):
    def __init__(self, master=None, folder:str='folder.png', item:str='item.png', **kw):
        super().__init__(master, **kw)
        self.master = master
        self.set_icons(folder=folder, item=item)
        self.init_ui()

    def init_ui(self):
        self.config(show='tree')
        self.PATH = None

    def set_icons(self, folder:str, item:str):
        """asigna iconos"""
        self._icon_folder = tk.PhotoImage(file=folder)
        self._icon_item = tk.PhotoImage(file=item)

    def clear_items(self):
        for item in self.get_children():
            self.delete(item)

    def _process_path(self, path_str:str):
        path = Path(path_str)
        self.PATH = path.as_posix()

        if not os.path.exists(path_str):
            return
        
        parent_folder_name = path.parent.name
        file_name = path.name

        parent_item_id = 0
        for item_id in self.get_children():
            item_text = self.item(item_id, 'text')
            if item_text == parent_folder_name:
                parent_item_id = item_id
                break
        
        if not parent_item_id:
            parent_item_id = self.insert(
                '', tk.END, text=parent_folder_name,
                image=self._icon_folder
            )
            self.item(parent_item_id, open=True)

        self.insert(
            parent_item_id, tk.END, text=file_name,
            image=self._icon_item
        )

    def get_path(self) -> str:
        return self.PATH
    
    def load_path(self,paths:str):
        self.clear_items()
        if isinstance(paths, str):
            paths = [paths]
        
        for _path_str in paths:
            self._process_path(_path_str)
        