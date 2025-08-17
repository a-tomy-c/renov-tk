import tkinter as tk
from tkinter import ttk
import os
from pathlib import Path

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TreeView con Íconos")
        self.geometry("400x400")

        # Cargar los íconos
        # Asegúrate de que las rutas a las imágenes son correctas.
        # Si no las tienes, puedes usar otras imágenes PNG pequeñas.
        self.folder_icon = tk.PhotoImage(file="folder.png")  # Reemplaza con tu icono de carpeta
        self.item_icon = tk.PhotoImage(file="item.png")      # Reemplaza con tu icono de archivo

        self.create_widgets()

    def create_widgets(self):
        # Frame superior para los controles de prueba
        top_frame = tk.Frame(self)
        top_frame.pack(side="top", pady=10)

        self.entry = tk.Entry(top_frame, width=30)
        self.entry.pack(side="left", padx=5)
        self.entry.insert(0, "/home/tomy/Descargas")  # Ejemplo de ruta

        test_button = tk.Button(top_frame, text="Cargar Ruta", command=self.load_path_from_entry)
        test_button.pack(side="left", padx=5)

        # Treeview (sin headers)
        self.tree = ttk.Treeview(self)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        # Ocultar los encabezados del Treeview
        self.tree.configure(show="tree")

    def load_path_from_entry(self):
        """Método de prueba para cargar la ruta desde el Entry."""
        path_str = self.entry.get()
        if path_str:
            self.add_items(path_str)

    def add_items(self, paths):
        """
        Limpia el Treeview y agrega los ítems de las rutas proporcionadas.
        :param paths: Una cadena de texto (ruta) o una lista de cadenas de texto (rutas).
        """
        # Limpiar el Treeview primero
        for item in self.tree.get_children():
            self.tree.delete(item)

        if isinstance(paths, str):
            paths = [paths]

        for path_str in paths:
            self._process_path(path_str)

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
        for item_id in self.tree.get_children():
            item_text = self.tree.item(item_id, "text")
            if item_text == parent_folder_name:
                parent_item_id = item_id
                break

        if not parent_item_id:
            parent_item_id = self.tree.insert("", "end", text=parent_folder_name, image=self.folder_icon)
            # --- NUEVA LÍNEA DE CÓDIGO ---
            # Expande el ítem padre inmediatamente después de crearlo
            self.tree.item(parent_item_id, open=True)
            # ---------------------------
        
        # Insertar el item hijo (el archivo)
        self.tree.insert(parent_item_id, "end", text=file_name, image=self.item_icon)

if __name__ == "__main__":
    app = App()
    app.mainloop()