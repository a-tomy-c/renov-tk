import os
from os import DirEntry
from pathlib import Path
from typing import Generator, Iterator
import locale
from datetime import datetime
import yaml
from mi_mediainfo import MiMediainfo


class MiCarpeta:
    def __init__(self, path=str):
        self.path = Path(path)

    def _content(self) -> list[Path]:
        with os.scandir(self.path.as_posix()) as fs:
            return [Path(r) for r in fs]
        
    def archivos(self) -> Generator[str]:
        return (f.as_posix() for f in self._content() if f.is_file())
    
    def carpetas(self) -> Generator[str]:
        return (f.as_posix() for f in self._content() if f.is_dir())
    
    def nombresDe(self, files:Iterator, stem:bool=True) -> Generator[str]:
        if isinstance(files, (Iterator, list, tuple)):
            return [Path(f).stem if stem else Path(f).name for f in files]
        
    def porExtension(self, ext:Iterator=['.txt']) -> Generator[str]:
        return [Path(f).as_posix() for f in self.archivos() if Path(f).suffix in ext]
    
    def imagenes(self, ext=['.jpg', '.png', '.gif']) -> Generator[str]:
        return self.porExtension(ext=ext)
    

class FileConfig:
    def __init__(self):
        ...

    def write_yaml(self, filepath:str, data:dict):
        with open(filepath, 'w', encoding='utf-8') as file:
            yaml.dump(
            data, file,
            default_flow_style=False,
            allow_unicode=True
        )
    
    def read_yaml(self, filepath:str) -> dict:
        with open(filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
        

class Info:
    def __init__(self, videopath:str, template:str):
        self.videopath = videopath
        self.template = template

    def get_data(self) -> dict:
        mediainfo = MiMediainfo(filepath=self.videopath)
        return mediainfo.get_translate(template=self.template)
    
    def properties(self):
        mediainfo = MiMediainfo(filepath=self.videopath)
        return mediainfo.video

    def get_info_text(self):
        info_video = self.properties()
        return info_video.get_info_text()


    

if __name__=="__main__":
    from pprint import pprint
    import platform
    # r1 = '/run/media/tomy/DD1/TAG/RECURSOS/personajes2/dragon ball'
    # r1 = '/run/media/tomy/DD1/TAG/RECURSOS/personajes2/dragon ball/'
    # obten = MiCarpeta(r1)
    # # print(obten._content())
    # print([e for e in obten.imagenes()])

    # fc = FileConfig()
    # res = fc.read_yaml('configs_renov.yaml')
    # pprint(res)

    # test read templates
    # system = platform.system()
    # if system == 'Windows':
    #     v1 = ''
    # elif system == 'Linux':
    #     v1 = '/run/media/tomy/sis/beta/renom/celmont.mp4'

    # temp = "[$time$ $bitrateu$ $tags$]-$height$p"
    # info = Info(videopath=v1, template=temp)
    # res = info.get_data()
    # print(res)


    # test mi_carpeta
    path = "/run/media/tomy/DD1/TAG/RECURSOS/personajes2/modelos"
    mic = MiCarpeta(path=path)
        
