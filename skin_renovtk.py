from tkinter import ttk
import tkinter as tk
import os
from pathlib import Path
# import sv_ttk
# from dark import EstiloDark
from ktexto import KText
from tkinterdnd2 import DND_FILES, TkinterDnD


class TreePath(ttk.Treeview):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.configure(show='tree')
        self.folder_icon = tk.PhotoImage(file="folder.png")
        self.item_icon = tk.PhotoImage(file="item.png")
        # sv_ttk.set_theme("dark")
        # sv_ttk.set_theme("light")
        # s = ttk.Style()
        # s = EstiloDark(self)
        # s.theme_use('alt')
        # print(s.theme_names())
        # s.configs_widgets()

    def load_path(self, path_str:str):
        self.clear()
        if isinstance(path_str, str):
            paths = [path_str]

        for path_str in paths:
            self._process_path(path_str)

    def clear(self):
        for item in self.get_children():
            self.delete(item)

    def _process_path(self, path_str):
        """Procesa una sola ruta para agregarla al Treeview."""
        if not os.path.exists(path_str):
            print(f"La ruta no existe: {path_str}")
            return

        path = Path(path_str)
        parent_folder_name = path.parent.name
        file_name = path.name

        # Insertar o encontrar el item padre (el folder)
        parent_item_id = None
        for item_id in self.get_children():
            item_text = self.item(item_id, "text")
            if item_text == parent_folder_name:
                parent_item_id = item_id
                break

        if not parent_item_id:
            parent_item_id = self.insert(
                '', 'end', text=parent_folder_name,
                image=self.folder_icon
            )
            self.item(parent_item_id, open=True)

        # Insertar el archivo como hijo del folder
        self.insert(
            parent_item_id, 'end', text=file_name,
            image=self.item_icon
        )



class SkinRenovTk(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.init_ui()

    def init_ui(self):
        fm_top = tk.Frame(self)
        fm_top.grid(row=0, column=0, sticky='wens')
        fm0 = tk.Frame(fm_top)
        fm1 = tk.Frame(fm_top)
        fm0.grid(row=0, column=0, sticky='wens')
        fm1.grid(row=1, column=0, sticky='wens')
        self.columnconfigure(0, weight=1)
        fm_top.columnconfigure(0, weight=1)
        fm0.columnconfigure(2, weight=1)
        fm1.columnconfigure(0, weight=1)
        self.fm_top = fm_top
        self.fm0 = fm0
        self.fm1 = fm1
        # self.config(pady=2, bg='#141414')
        # fm_top.config(pady=2, bg="#313131")
        
        self.bt_info = ttk.Button(
            fm0,
            text='INFO',
            # padding=0,
            takefocus=False,
            width=6,
            command=self.toggle_tabs
        )
        self.bt_rt = ttk.Button(
            fm0,
            text='RT',
            # padding=0,
            takefocus=False,
            width=3
        )
        self.var_template = tk.StringVar()
        self.en_template = ttk.Entry(
            fm0,
            textvariable=self.var_template,
            takefocus=False,
        )
        self.var_tags = tk.StringVar()
        self.en_tags = ttk.Entry(
            fm1,
            textvariable=self.var_tags,
            takefocus=False,
        )
        self.bt_reload = ttk.Button(
            fm1,
            text='RELOAD',
            # padding=0,
            takefocus=False,
            width=8
        )
        self.var_current_tag = tk.StringVar()
        self.cmb_tags = ttk.Combobox(
            fm1,
            textvariable=self.var_current_tag,
            state='readonly',
            takefocus=False,
            width=16
        )
        self.bt_info.grid(
            row=0, column=0, sticky='wens',
            padx=1, pady=0
        )
        self.bt_rt.grid(
            row=0, column=1, sticky='wens',
            padx=1, pady=0,
        )
        self.en_template.grid(
            row=0, column=2, sticky='wens',
            padx=1, pady=0,
        )
        self.en_tags.grid(
            row=1, column=0, sticky='wens',
            padx=1, pady=0,
        )
        self.bt_reload.grid(
            row=1, column=1, sticky='wens',
            padx=1, pady=0,
        )
        self.cmb_tags.grid(
            row=1, column=2, sticky='wens',
            padx=1, pady=0,
        )

        self.wg_tabs = ttk.Notebook(self)
        self.wg_tabs.grid(row=1, column=0, sticky='wens')
        self.rowconfigure(1, weight=1)
        self.wg_tabs.columnconfigure(0, weight=1)
        self.wg_tabs.rowconfigure(0, weight=1)

        self.tab1 = tk.Frame(self.wg_tabs)
        self.tab2 = tk.Frame(self.wg_tabs)
        self.wg_tabs.add(self.tab1, text='Tab 1')
        self.wg_tabs.add(self.tab2, text='Tab 2')

        # Ocultar las pestañas
        style = ttk.Style()
        style.layout("TNotebook.Tab", [])
        style.configure("TNotebook", borderwidth=0)

        # TAB 1
        self.tree = TreePath(self.tab1, height=3)
        self.tree.grid(row=0, column=0, sticky='wens')
        self.tab1.rowconfigure(0, weight=0, minsize=70)
        self.tab1.columnconfigure(0, weight=1)
        # TAB 1
        self.tree.load_path('/home/tomy/Descargas/soft_para_tags_v1/renombrar_mi_tk_v0.3/ren3.py')
        # self.tex_log = tk.Text(self.tab1, wrap='word')
        self.tex_log = KText(self.tab1)
        self.tex_log.tex.config(bg="#17181B")
        self.tex_log.grid(row=1, column=0, sticky='wens')
        self.tab1.rowconfigure(1, weight=1)
        self.tab1.columnconfigure(0, weight=1)


        # TAB 2
        # self.text_info = tk.Text(self.tab2, wrap='word')
        self.text_info = KText(self.tab2)
        self.text_info.grid(row=0, column=0, sticky='wens')
        self.tab2.rowconfigure(0, weight=1)
        self.tab2.columnconfigure(0, weight=1)
        # TAB 2


        # self.bt_rename = ttk.Button(
        #     fm_top,
        #     text='RENAME',
        #     padding=-2,
        #     takefocus=False,
        # )
        # self.bt_rename.grid(
        #     row=0, column=0, sticky='wens',
        #     padx=0, pady=0,
        # )
        self._set_style()

        bg="#141414"        
        self.fm_top.configure(bg=bg)
        self.fm0.configure(bg=bg)
        self.fm1.configure(bg=bg)
        # self.tex_log.configure(
        #     bg=bg, fg='#ffffff',
        #     insertbackground='white',
        #     selectbackground="#3e2870",
        #     selectforeground='#ffffff',
        #     borderwidth=0,
        #     highlightthickness=0,
        #     font=('Consolas', 10, 'normal')
        # )
        

    def toggle_tabs(self):
        # Obtener el índice de la pestaña actual
        current_tab_index = self.wg_tabs.index(self.wg_tabs.select())
        index = 1 if current_tab_index == 0 else 0
        self.wg_tabs.select(index)

    def _set_style(self):
        s = ttk.Style()
        s.theme_use('default')
        # print(s.theme_names())

        bgt = "#2a3ca3"
        bg = "#191C20"
        bgb = "#303030"
        bgbh = "#1F294B"
        bge = "#0F180F"
        fg = "#FFFFFF"
        bd = "#2B334B"
        bgh = '#3e3e3e'
        
        self.fm_top.configure(bg=bg)
        self.fm0.configure(bg=bg)
        self.fm1.configure(bg=bg)

        s.configure(
            'TButton', padding=0,
            background=bgb,
            foreground='#ffffff',
            borderwidth=0,
            focusthickness=3,
            focuscolor=bgh,
        )
        s.map('TButton',
            background=[('active', bgbh)],
            foreground=[('active', '#ffffff')],
            bordercolor=[('focus', "#1e091f")],
            relief=[('pressed', 'sunken'), ('!pressed', 'flat')]
        )
        s.configure(
            'TEntry',
            padding=2,
            fieldbackground=bg,
            foreground='#ffffff',
            bordercolor=bd,
            lightcolor=bd,
            darkcolor=bd,
            borderwidth=0,
            insertcolor="#242323",
            selectbackground='#4e4e4e',
            selectforeground='#ffffff',
            relief='flat',
            highlightthickness=0,
            highlightbackground=bg,
            highlightcolor=bd,
            focuscolor=bd,
            takefocus=False,
            bd=0
        )
        s.map('TEntry',
            bordercolor=[('focus', bd), ('!focus', '#3e3e3e')],
            lightcolor=[('focus', bd), ('!focus', '#3e3e3e')],
            darkcolor=[('focus', bd), ('!focus', '#3e3e3e')],
        )
        s.configure(
            'TCombobox',
            padding=2,
            fieldbackground='#1e1e1e',
            foreground=fg,
            background=bg,
            focuscolor=bgh,
            focusbordercolor=bd,
            bordercolor=bd,
            lightcolor=bd,
            darkcolor=bd,
            borderwidth=1,
            arrowcolor=bgh,
            selectbackground=bg,
            selectforeground=fg,
            readonlybackground='#1e1e1e',
            state='readonly',
            takefocus=False,
        )
        s.map('TCombobox',
            bordercolor=[('focus', bd), ('!focus', bd)],
            lightcolor=[('focus', bd), ('!focus', bd)],
            darkcolor=[('focus', bd), ('!focus', bd)],
            arrowcolor=[('active', "#13e713"), ('!active', fg)],
            selectbackground=[('active', "#b1ff34"), ('!active', bg)],
            selectforeground=[('active', fg), ('!active', fg)],
            fieldbackground=[('readonly', bg)],
        )
        self.option_add('*TCombobox*Listbox.selectBackground', bgt)
        self.option_add('*TCombobox*Listbox.selectForeground', fg)
        s.configure(
            'Treeview',
            background=bg,
            foreground='#ffffff',
            fieldbackground=bg,
            bordercolor=bd,
            lightcolor=bd,
            darkcolor=bd,
            borderwidth=0,
            rowheight=24,
            selectbackground=bd,
            selectforeground='#ffffff',
            relief='flat',
            highlightthickness=0,
            highlightbackground=bg,
            highlightcolor=bd,
            bd=0,
        )
        s.map('Treeview',
            background=[('selected', bgt)],
            foreground=[('selected', '#ffffff')],
            bordercolor=[('focus', '#000000'), ('!focus', bd)],
            lightcolor=[('focus', bd), ('!focus', bd)],
            darkcolor=[('focus', bd), ('!focus', bd)],
        )
        s.configure(
            'TNotebook',
            background='#2e2e2e',
            foreground='#ffffff',
            bordercolor='#3e3e3e',
            lightcolor='#3e3e3e',
            darkcolor='#3e3e3e',
            borderwidth=1,
        )
        s.map('TNotebook',
            background=[('selected', '#3e3e3e'), ('!selected', '#2e2e2e')],
            foreground=[('selected', '#ffffff'), ('!selected', '#aaaaaa')],
            bordercolor=[('focus', bd), ('!focus', '#3e3e3e')],
            lightcolor=[('focus', bd), ('!focus', '#3e3e3e')],
            darkcolor=[('focus', bd), ('!focus', '#3e3e3e')],
        )
        # Ocultar las pestañas
        style = ttk.Style()
        style.layout("TNotebook.Tab", [])
        style.configure("TNotebook", borderwidth=0) # Evitar borde doble

        self.items = ["uno", "dos", "tres", "cuatro"]
        self.var_current_tag.set(self.items[0])
        self.cmb_tags['values'] = self.items

        self.fm_top.config(pady=2, bg="#313131")
        self.fm0.config(pady=2, bg="#313131")
        self.config(padx=6, bg='#141414')


if __name__ == "__main__":
    # from ttkthemes import ThemedTk

    # root = ThemedTk(theme="equilux")
    # root = ThemedTk(theme="yaru")
    
    # def on_drop(event):
    #     """Handle the drop event."""
    #     file_path = event.data
    #     if os.path.isfile(file_path):
    #         print(f"File dropped: {file_path}")
    #         app.tree.load_path(file_path)
    #     else:
    #         print(f"Not a valid file: {file_path}")

    def on_drop(event):
        files = root.tk.splitlist(event.data)
        # for file_path in files:
        #     if os.path.isfile(file_path):
        #         print(f"File dropped: {file_path}")
        #         app.tree.load_path(file_path)
        #     else:
        #         print(f"Not a valid file: {file_path}")

        file_path = files[0]
        if os.path.isfile(file_path):
            print(f"File dropped: {file_path}")
            app.tree.load_path(file_path)


    # root = tk.Tk()
    root = TkinterDnD.Tk()
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", on_drop)

    root.geometry("650x350")
    root.title("Skin RenovTk Example")
    app = SkinRenovTk(master=root)
    app.pack(fill='both', expand=True)
    root.mainloop()