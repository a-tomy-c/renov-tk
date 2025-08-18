import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from skin_widgets.combobox_base import ComboboxBase
from skin_widgets.ktexto import KText
from skin_widgets.treepath import TreePath
from skin_widgets.style_dark import StyleDark


class SkinRenoTk(tk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.__cnf_skinrenotk()

    def __cnf_skinrenotk(self):
        bg_frame = '#222020'

        fm_top = tk.Frame(self, bg=bg_frame)
        fm0 = tk.Frame(fm_top, bg=bg_frame)
        fm1 = tk.Frame(fm_top, bg=bg_frame)
        fm0.grid(row=0, column=0, sticky='we')
        fm1.grid(row=1, column=0, sticky='we')
        fm_top.grid(row=0, column=0, sticky='we')

        self.columnconfigure(0, weight=1)
        fm_top.columnconfigure(0, weight=1)
        # fm_top.rowconfigure((0,1), weight=0)

        self.bt_info = ttk.Button(
            fm0, text='INFO', takefocus=False,
            width=6,
        )
        self.bt_rt = ttk.Button(
            fm0, text='RT', takefocus=False,
            width=3
        )
        self.var_template = tk.StringVar()
        self.en_template = ttk.Entry(
            fm0, textvariable=self.var_template, takefocus=False,
        )
        self.var_tags = tk.StringVar()
        self.en_tags = ttk.Entry(
            fm1, textvariable=self.var_tags, takefocus=False
        )
        self.bt_reload = ttk.Button(
            fm1, text='RELOAD', takefocus=False, width=8
        )
        self.cmb_tags = ComboboxBase(
            fm1, takefocus=False, state='readonly', width=16
        )

        self.bt_info.grid(row=0, column=0, sticky='wens')
        self.bt_rt.grid(row=0, column=1, sticky='wens', padx=4)
        self.en_template.grid(row=0, column=2, sticky='wens')
        fm0.columnconfigure(2, weight=1)
        self.en_tags.grid(row=0, column=0, sticky='wens')
        self.bt_reload.grid(row=0, column=1, sticky='wens', padx=4)
        self.cmb_tags.grid(row=0, column=2, sticky='wens')
        fm1.columnconfigure(0, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        self.wg_tabs = ttk.Notebook(self)
        self.wg_tabs.grid(row=1, column=0, sticky='wens')
        self.wg_tabs.columnconfigure(0, weight=1)
        self.wg_tabs.rowconfigure(0, weight=1)
        self.tab1 = tk.Frame(self.wg_tabs, bg='blue')
        # self.tab2 = tk.Frame(self.wg_tabs)
        self.wg_tabs.add(self.tab1, text='Tab 1', sticky='wens')
        # self.wg_tabs.add(self.tab2, text='Tab 2')
        s_tab = ttk.Style()
        s_tab.layout('TNotebook.Tab', [])
        s_tab.configure('TNotebook', borderwidth=0)
        self.tab1.columnconfigure(0, weight=1)
        self.tab1.rowconfigure(0, weight=0, minsize=60)
        self.tab1.rowconfigure(1, weight=1)

        self.tree = TreePath(self.tab1, height=3)
        self.tree.grid(row=0, column=0, sticky='we')
        self.tex_log = KText(self.tab1)
        self.tex_log.grid(row=1, column=0, sticky='wens')
        self.rowconfigure(0, weight=0, minsize=58)
        self.rowconfigure(1, weight=1, minsize=58)
        self.rowconfigure(2, weight=1, minsize=30)

        fm_bot = tk.Frame(self, bg=bg_frame)
        fm_bot.grid(row=2, column=0, sticky='wens', pady=2)
        self.bt_rename = ttk.Button(
            fm_bot, text='RENAME', takefocus=False, width=8
        )
        self.var_new_name = tk.StringVar()
        self.en_new_name = ttk.Entry(
            fm_bot, textvariable=self.var_new_name, takefocus=False
        )
        self.bt_preview = ttk.Button(
            fm_bot, text='PREVIEW', width=8
        )
        self.bt_rename.grid(row=0, column=0, sticky='wens')
        self.en_new_name.grid(row=0, column=1, sticky='wens', padx=4)
        self.bt_preview.grid(row=0, column=2, sticky='wens')
        fm_bot.columnconfigure(1, weight=1)
        fm_bot.rowconfigure(0, weight=1)

        self.config(padx=4, pady=4, bg=bg_frame)
        fm1.config(pady=2)
        # fm_bot.config(pady=2)
        # aplica estilo
        s = StyleDark()
        self.tex_log.set_bg(color='gray18')
        self.tex_log.setScroll(s)


if __name__ == '__main__':
    rz = tk.Tk()
    rz.geometry('700x300')
    rz.title('test skin')
    app = SkinRenoTk(rz)
    app.grid(row=0, column=0, sticky='wens')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)

    rz.mainloop()