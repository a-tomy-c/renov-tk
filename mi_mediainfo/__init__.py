import logging
import json
from typing import Literal
from pymediainfo import MediaInfo


class Tracks:
    def __init__(self, file:str):
        self.file = file
        self.logger = logging.getLogger(__name__)

    def get_info_track(
        self, track:Literal['general', 'video', 'audio', 'text']
    ) -> dict:
        mi = MediaInfo.parse(filename=self.file)
        output = {'tipo':track}
        match track:
            case 'general':
                list_tracks = mi.general_tracks
            case 'video':
                list_tracks = mi.video_tracks
            case 'audio':
                list_tracks = mi.audio_tracks
            case 'text':
                list_tracks = mi.text_tracks
            case _:
                list_tracks = []
        for track in list_tracks:
            output.update(track.to_data())
        return output
    
    def dict_to_json(self, dc:dict, name:str):
        with open(f'{name}.json', 'w', encoding='utf-8') as file:
            json.dump(dc, file, indent=4, ensure_ascii=False)


class InfoVideo(Tracks):
    def __init__(self, file:str):
        super().__init__(file=file)
        self.data = self.get_info_track(track='video')

    def get(self, key:str) -> str|None:
        return self.data.get(key, None)

    @property
    def codec(self) -> str:
        return self.get('codec_id')
    
    @property
    def format(self) -> str:
        return self.get('internet_media_type')
    
    @property
    def duration(self) -> str:
        return self.get('other_duration')[3]
    
    @property
    def duration_ms(self) -> str:
        return self.get('duration')
    
    @property
    def bitrate(self) -> int:
        return self.get('bit_rate')
    
    @property
    def bitrate_u(self) -> str:
        bt = self.get('other_bit_rate')[0]
        return bt.replace(' ', '').replace('/', '')
    
    @property
    def width(self) -> int:
        return self.get('width')
    
    @property
    def height(self) -> int:
        return self.get('height')
    
    @property
    def aspect_ratio(self) -> str:
        return self.get('display_aspect_ratio')
    
    # @property
    def get_time(self, ts:str) -> str:
        text = ts.split('.')[0]
        while text.startswith('00:'):
            text = text[3:]
        return text.replace(':', '')
    
    def get_info_text(self) -> str:
        return f'bitrate (u): {self.bitrate_u}\n'\
            f'codec: {self.codec}\n'\
            f'format: {self.format}\n'\
            f'duration: {self.duration}\n'\
            f'height: {self.height}\n'\
            f'width: {self.width}\n'\
            f'duration (ms): {self.duration_ms}\n'\
            f'aspect ratio: {self.aspect_ratio}'
    
    def get_info(self) -> dict:
        return {
            'bitrate':self.bitrate,
            'bitrateu':self.bitrate_u,
            'codec':self.codec,
            'format':self.format,
            'duration':self.duration,
            'durationms':self.duration_ms,
            'time':self.get_time(self.duration),
            'height':self.height,
            'width':self.width,
            'aspectratio':self.aspect_ratio
        }
    

class MiMediainfo:
    def __init__(self, filepath:str):
        self.videopath = filepath
        self.genProperties()

    def genProperties(self):
        self.video = InfoVideo(self.videopath)

    def get_translate(self, template:str) -> str:
        keywords = [p for p in template.split('$') if len(p)>3]
        data = self.video.get_info()
        for key in keywords:
            word = f'${key}$'
            if key in data.keys():
                template = template.replace(word, str(data.get(key)))
        return template


    
if __name__=="__main__":
    from pprint import pprint
    import platform

    system = platform.system()
    if system == 'Windows':
        v1 = ''
    elif system == 'Linux':
        v1 = '/run/media/tomy/sis/beta/renom/celmont.mp4'
    # mime = MiMediainfo(v1)
    # gen = mime.get_info_track('video')
    # # pprint(mime.get_info_track('general'))
    # mime.dict_to_json(dc=gen, name='salida-gen')

    # iv = InfoVideo(file=v1)
    # pprint(iv.get_info())


    # test templates
    # templa = "[$time$ $bitrateu$ $tags$]-$height$p"
    # mi = MiMediainfo(v1)
    # res = mi.get_translate(template=templa)
    # print(res)
