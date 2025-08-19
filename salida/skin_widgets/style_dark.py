from tkinter import ttk


class StyleDark(ttk.Style):
    def __init__(self):
        super().__init__()
        self.__cnf_styledark()

    def __cnf_styledark(self):
        self.theme_use('default')

        bg_button = '#303030'
        bgh_button = '#202030'
        fg_button = '#ffffff'
        bg_entry = "#373838"
        fg_entry = '#f0f0f0'
        bd_entry = "#21232B"
        bgs_entry = "#0e0d0d"
        fg_tree = '#ffffff'
        bg_tree = "#232325"
        bgs_tree = '#100010'
        fgs_tree = "#85E0FC"


        self.configure(
            'TButton', padding=0,
            background=bg_button,
            foreground=fg_button,
            borderwidth=0,
            focusthickness=3,
        )
        self.map(
            'TButton',
            background=[('active', bgh_button)],
            foreground=[('active', fg_button)],
            relief=[('pressed', 'sunken'), ('!pressed', 'flat')]
        )
        self.configure(
            'TEntry',
            padding=2,
            fieldbackground=bg_entry,
            foreground=fg_entry,
            bordercolor=bd_entry,
            lightcolor=bd_entry,
            darkcolor=bd_entry,
            borderwidth=0,
            insertcolor=fg_entry,
            selectbackground=bgs_entry,
            selectforeground=fg_entry,
            relief='flat',
            highlightthickness=0,
            highlightbackground=bg_entry,
            highlightcolor=bd_entry,
            focuscolor=bd_entry,
            takefocus=False,
            bd=0
        )
        self.map('TEntry',
            bordercolor=[('focus', bd_entry), ('!focus', '#3e3e3e')],
            lightcolor=[('focus', bd_entry), ('!focus', '#3e3e3e')],
            darkcolor=[('focus', bd_entry), ('!focus', '#3e3e3e')],
        )
        self.configure(
            'TCombobox',
            padding=2,
            fieldbackground='#1e1e1e',
            foreground=fg_entry,
            background=bg_entry,
            focuscolor=bgh_button,
            focusbordercolor=bd_entry,
            bordercolor=bd_entry,
            lightcolor=bd_entry,
            darkcolor=bd_entry,
            borderwidth=1,
            arrowcolor=bgh_button,
            selectbackground=bgh_button,
            selectforeground=fg_entry,
            readonlybackground=bg_button,
            state='readonly',
            takefocus=False,
        )
        self.map('TCombobox',
            bordercolor=[('focus', bd_entry), ('!focus', bd_entry)],
            lightcolor=[('focus', bd_entry), ('!focus', bd_entry)],
            darkcolor=[('focus', bd_entry), ('!focus', bd_entry)],
            arrowcolor=[('active', "#13e713"), ('!active', fg_entry)],
            selectbackground=[('active', "#b1ff34"), ('!active', bg_entry)],
            selectforeground=[('active', fg_entry), ('!active', fg_entry)],
            fieldbackground=[('readonly', bg_entry)],
        )

        self.configure(
            'Treeview',
            background=bg_tree,
            foreground='#ffffff',
            fieldbackground=bg_tree,
            bordercolor=bd_entry,
            lightcolor=bd_entry,
            darkcolor=bd_entry,
            borderwidth=0,
            rowheight=24,
            selectbackground=bd_entry,
            selectforeground=fg_tree,
            relief='flat',
            highlightthickness=0,
            highlightbackground=bgs_tree,
            highlightcolor=bd_entry,
            bd=0,
        )
        self.map('Treeview',
            background=[('selected', bg_tree)],
            foreground=[('selected', fgs_tree)],
            bordercolor=[('focus', '#000000'), ('!focus', bd_entry)],
            lightcolor=[('focus', bd_entry), ('!focus', bd_entry)],
            darkcolor=[('focus', bd_entry), ('!focus', bd_entry)],
        )
        # self.configure(
        #     'Text',
        #     foreground='gray'
        # )