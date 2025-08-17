import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana con Pestañas Ocultas")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Frame superior para el entry y el botón
        top_frame = tk.Frame(self)
        top_frame.pack(side="top", pady=10)

        # Entry
        self.entry = tk.Entry(top_frame)
        self.entry.pack(side="left", padx=5)

        # Botón
        self.toggle_button = tk.Button(top_frame, text="Cambiar Pestaña", command=self.toggle_tabs)
        self.toggle_button.pack(side="left", padx=5)

        # Notebook (el widget con pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # Crear las dos pestañas (frames)
        self.tab1 = tk.Frame(self.notebook)
        self.tab2 = tk.Frame(self.notebook)

        # Agregar contenido a las pestañas
        tk.Label(self.tab1, text="¡Estás en la Pestaña 1!").pack(padx=20, pady=20)
        tk.Label(self.tab2, text="¡Estás en la Pestaña 2!").pack(padx=20, pady=20)

        # Agregar las pestañas al notebook
        self.notebook.add(self.tab1, text="Pestaña 1")
        self.notebook.add(self.tab2, text="Pestaña 2")

        # Ocultar las pestañas
        style = ttk.Style()
        style.layout("TNotebook.Tab", [])
        style.configure("TNotebook", borderwidth=0)

    def toggle_tabs(self):
        # Obtener el índice de la pestaña actual
        current_tab_index = self.notebook.index(self.notebook.select())

        # Determinar el siguiente índice de la pestaña
        if current_tab_index == 0:
            next_tab_index = 1
        else:
            next_tab_index = 0

        # Seleccionar la siguiente pestaña
        self.notebook.select(next_tab_index)

if __name__ == "__main__":
    app = App()
    app.mainloop()