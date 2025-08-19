import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from skin_renovtk import SkinRenoTk
from tkinterdnd2 import DND_FILES, TkinterDnD
from funciones import Info
from funciones_renov import FuncionesRenov


class VentanaRenovTk(TkinterDnD.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.__cnf_ventana_reno_tk()

    def __cnf_ventana_reno_tk(self):
        self.sk = SkinRenoTk(self)
        self.sk.grid(row=0, column=0, sticky='wens')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.fun = FuncionesRenov()
        self.reload_config()
        self.sk.cmb_tags.bind('<<ComboboxSelected>>', self.select_tag)
        self.sk.bt_reload.config(command=self.reload_tags)
        self.sk.bt_rt.config(command=self.reload_template)
        self.sk.bt_rename.config(state='disabled')
        self.sk.bt_preview.config(command=self.preview_name)
        self.sk.bt_rename.config(command=self.rename_file)
        self.sk.bt_info.config(command=self.toggle_tabs)

        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self._drop_file)

        self.sk.tex_info.msg(
            texto='renovtk version 1.0 - tomy\n18 agosto 2025'
        )

    def reload_config(self):
        self.PATH_OLD = None
        self.PATH_NEW = None
        self.reload_tags()
        self.reload_template()

    def reload_tags(self):
        """recarga tags de yaml"""
        _ = ''
        try:
            tags = self.fun.get_tags()
        except Exception as err:
            tags = self.read_tags_from_txt()
            _ = '[file]'
        self.sk.cmb_tags.set_items(values=tags)
        self.msg_n(f'{_}{len(tags)} tags cargados.\n', 0)

    def read_tags_from_txt(self):
        file = 'tags.txt'
        tags = []
        if Path(file).is_file():
            with open(file, 'r') as txt:
                lines = txt.readlines()
            tags = [line.strip('\n') for line in lines]
        return tags
    
    def msg(self, text:str, **kw):
        self.sk.tex_log.msg(texto=text)

    def msg_n(self, text:str, i:int=0, **kw):
        self.sk.tex_log.msgNum(texto=text, i=i, **kw)

    def reload_template(self):
        self.sk.var_template.set(self.fun.get_template())

    def select_tag(self, event=None):
        tag = self.sk.cmb_tags.current_item()
        self.sk.var_tags.set(self.fun.select_tag(tag))

    def preview_name(self):
        path = self.sk.tree.get_path()
        if path:
            file = Path(path)
            if file.is_file():
                stem = file.stem
                template = self.sk.var_template.get()
                iv = Info(file.as_posix(), template)
                template_info = iv.get_data()

                tgs = self.sk.var_tags.get()
                tags = f' {tgs}' if tgs else ''
                template_info = template_info.replace('$tags$', tags)

                stem_new = f'{stem} {template_info}'
                self.sk.var_new_name.set(stem_new)
                new_path = file.with_stem(stem_new).as_posix()
                self.sk.bt_rename.config(state='normal')

                self.PATH_OLD = file.as_posix()
                self.PATH_NEW = new_path
                self.show_info()
                self.msg('\n')
                self.msg_n(f'{self.PATH_OLD}\n', 2)
                self.msg_n(f'{self.PATH_NEW}\n', 3)

    def show_info(self):
        try:
            filepath = self.sk.tree.get_path()
            if filepath:
                iv = Info(filepath, '')
                res = iv.get_info_text()
                self.msg_n('\n')
                for line in res.split('\n'):
                    self.msg_n(f'{line}\n', 1)
        except Exception as err:
            self.msg(f'{err}\n', fg='red')

    def _drop_file(self, event):
        files = self.tk.splitlist(event.data)
        file_path = files[0]
        if os.path.isfile(file_path):
            self.sk.tree.load_path(file_path)

    def rename_file(self):
        old = Path(self.PATH_OLD)
        if old.is_file():
            path_new = Path(self.PATH_NEW)
            stem = path_new.stem
            stem_mod = self.sk.var_new_name.get()
            if stem != stem_mod and stem_mod:
                self.PATH_NEW = path_new.with_stem(stem_mod)
                self.msg_n(f'[MOD] stem', 2)
            if Path(self.PATH_NEW).is_file():
                self.msg_n(f'el archivo ya existe.\n', 4)
            else:
                os.rename(self.PATH_OLD, self.PATH_NEW)
                self.msg_n(f'Archivo renombrado exitosamente.\n', 4)
        else:
            self.msg_n('no es un archivo\n', 5)
            folder = Path(self.PATH_OLD).parent.name
            name = Path(self.PATH_OLD).name
            self.msg_n(f'{folder}\n', 0)
            self.msg_n(f'{name}\n', 4)

    def toggle_tabs(self):
        self.sk.toggle_tabs()


if __name__ == '__main__':
    app = VentanaRenovTk()
    app.geometry('800x430')
    app.title('RENOV-Tk')
    app.mainloop()