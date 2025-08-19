import platform
import tkinter as tk
from tkinter import ttk
from funciones import MiCarpeta, FileConfig


class MakeList:
    def __init__(self):
        file_config = FileConfig()
        self.cf = file_config.read_yaml(filepath='configs_renov.yaml')

    def get(self, key:str) -> str:
        return self.cf.get(key)
    
    def get_tags_from_path(self) -> list[str]:
        system = platform.system()
        if system == "Windows":
            path = self.get('path tags win')
        elif system == "Linux":
            path = self.get('path tags lnx')
        micarpeta = MiCarpeta(path=path)
        images = micarpeta.imagenes(ext=self.get('format images'))
        tags = micarpeta.nombresDe(images)
        return tags

    def make_txt(self, name:str='tags.txt'):
        tags = self.get_tags_from_path()
        with open(name, 'w', encoding='utf-8') as file:
            file.write('\n'.join(tags))


class VentanaMakeList(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.btn_create = ttk.Button(
            self, text='CREATE TAGS\ntags.txt',
            command=self.create_file_txt
        )
        self.btn_create.pack(fill=tk.BOTH, expand=1, padx=6, pady=6)
        s = ttk.Style()
        s.configure(
            'TButton',
            background='gray20',
            foreground='white',
            borderwidth=0,
            justify='center'
        )
        s.map(
            'TButton',
            background=[('pressed', 'gray10')],
            foreground=[('active', 'orange')],
            relief=[('pressed', 'sunken'), ('!pressed', 'flat')]
        )
        self.config(bg='black')

    def create_file_txt(self):
        mk_list = MakeList()
        mk_list.make_txt()

        self.btn_create.config(text='el archivo\nfue creado')
        self.after(2500, self.change_label_button)

    def change_label_button(self):
        self.btn_create.config(text='CREATE TAGS\ntags.txt')


if __name__ == "__main__":
    vn = VentanaMakeList()
    vn.geometry('220x100')
    vn.mainloop()
