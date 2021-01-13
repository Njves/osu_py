import cfg
from game.Map import Map


class MapStorage:
    hibikase_path = "songs/hibikase"
    modoki_path = "songs/modoki"
    dora_path = "songs/dora"

    def __init__(self):
        self.maps = []
        self.maps.append(
            Map(f"{self.hibikase_path}/bg.png", f"{self.hibikase_path}/miku.mp3",
                f"{self.hibikase_path}/normal-hitclap.wav", 140, (174, 124, 64), [] )
        )
        self.maps.append(
            Map(f"{self.modoki_path}/ss.jpg", f"{self.modoki_path}/Harumodoki.mp3",
                f"{self.modoki_path}/soft-hitclap.wav", 174, (174, 124, 64), [(0, 4), (6, 2), (15, 4) , (50, 2)])
        )
        self.maps.append(
            Map(f"{self.dora_path}/doradura.jpg", f"{self.dora_path}/audio.mp3",
                f"{self.dora_path}/drum-hitclap.wav", 120, (174, 124, 64), [])
        )

    def get_map_by_id(self, id):
        if id > 3:
            return None
        # Костыль))
        id -= 1
        return self.maps[id]
