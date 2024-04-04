from mcdreforged.api.all import *

class datapack_music_config(Serializable):
    datapack_path: str = "./server/world/datapacks/"
    ignore_datapacks: set = []
    


