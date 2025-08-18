from skin_renovtk import SkinRenovTk
from funciones import MiCarpeta, FileConfig, Info
from funciones_renov import FuncionesRenov
import os
from pathlib import Path


class Principal(SkinRenovTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._config_principal()
    
    def _config_principal(self):
        self.fun = FuncionesRenov()
        self.reload_config()
        self.cmb_tags.bind("<<ComboboxSelected>>", self.select_tag)
        self.bt_reload.config(command=self.reload_tags)
        self.bt_rt.config(command=self.reload_template)
        self.bt_preview.config(command=self.preview_name)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def reload_config(self):
        self.PATH_OLD = None
        self.PATH_NEW = None
        self.reload_tags()
        self.reload_template()

    # combo funciones
    def setItems(self, items:list):
        self.cmb_tags.config(values=items)

    def reload_tags(self):
        """recarga tags, ruta yaml"""
        tags = self.fun.get_tags()
        self.setItems(items=tags)
        self.tex_log.msg(texto=f'{len(tags)} tags cargados.\n',fg='gray')
    # combo funciones

    def reload_template(self):
        self.var_template.set(self.fun.get_template())

    def select_tag(self, event=None):
        tag = self.cmb_tags.get()
        self.var_tags.set(self.fun.select_tag(tag))

    def preview_name(self):
        path = self.tree.path
        if path:
            file = Path(path)
            if file.is_file():
                stem = file.stem
                template = self.var_template.get()
                iv = Info(file.as_posix(), template=template)
                template_info = iv.get_data()

                tgs = self.var_tags.get()
                tags = f' {tgs}' if tgs else ''
                template_info = template_info.replace('$tags$', tags)


                stem_new = f'{stem} {template_info}'
                self.var_new_name.set(stem_new)
                new_path = file.with_stem(stem_new).as_posix()
                self.bt_rename.config(state='normal')


                self.PATH_OLD = file.as_posix()
                self.PATH_NEW = new_path
                self.show_info()
                self.tex_log.msg('\n')
                self.tex_log.msg(f'{self.PATH_OLD}\n', fg='gray')
                self.tex_log.msg(f'{self.PATH_NEW}\n', fg='white')

    
    def show_info(self):
        try:
            filepath = self.tree.path
            if filepath:
                iv = Info(filepath, "")
                res = iv.get_info_text()
                self.tex_log.msg('\n')
                for line in res.split('\n'):
                    self.tex_log.msg(f'{line}\n', fg='azure')
        except Exception as e:
            self.tex_log.msg(f'{e}')

    def rename_file(self):
        old = Path(self.PATH_OLD)
        if old.is_file():
            path_new = Path(self.PATH_NEW)
            stem = path_new.stem
            stem_mod = self.var_new_name.get()
            if stem != stem_mod and stem_mod:
                self.PATH_NEW = path_new.with_stem(stem_mod)
                self.tex_log.msg(f'el "stem" esta modificado\n', fg='orange')

            if Path(self.PATH_NEW).is_file():
                self.tex_log.msg('el archivo ya existe.\n', fg='orange')
            else:
                os.rename(self.PATH_OLD, self.PATH_NEW)
                self.tex_log.msg(f'Archivo Renombrado exitosamente', fg='lightgreen')
        else:
            self.tex_log.msg('no es un archivo\n')
            self.tex_log.msg(f'{self.PATH_OLD}')


if __name__ == "__main__":
    from tkinterdnd2 import DND_FILES, TkinterDnD


    def on_drop(event):
        files = root.tk.splitlist(event.data)
        file_path = files[0]
        if os.path.isfile(file_path):
            # print(f"File dropped: {file_path}")
            app.tree.load_path(file_path)


    root = TkinterDnD.Tk()
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", on_drop)

    root.geometry("750x350")
    root.title("vn Principal")
    app = Principal(master=root)
    # app.pack(fill='both', expand=True)
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.grid(row=0, column=0, sticky='wens')
    root.mainloop()