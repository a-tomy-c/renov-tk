from pathlib import Path
from funciones import MiCarpeta, FileConfig, Info
import platform
# import logging


class FuncionesRenov:
    def __init__(self):
        file_config = FileConfig()
        self.cf = file_config.read_yaml(filepath='configs_renov.yaml')
        self.tags = []

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

    def get_template(self) -> str:
        return self.get('template')
    
    def get_sep(self) -> str:
        return self.get('sep tags')
    
    def select_tag(self, tag:str):
        sep = self.get_sep()
        if not tag in self.tags:
            self.tags.append(tag)
        return sep.join(self.tags)
    
    def get_tags_txt(self) -> list[str]:
        path = "tags.txt"
        tags = None
        if Path(path).is_file():
            with open(path, 'r') as file:
                lines = file.readlines()
                tags = [line.strip('\n') for line in lines]
        return tags
            
    def get_tags(self) -> list[str]:
        tags = []
        try:
            tags = self.get_tags_from_path()
        except Exception as err:
            tags = self.get_tags_txt()
        return tags