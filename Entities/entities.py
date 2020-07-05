import sys
sys.path.append('../Image/ProcessImg/')

from Process import ProcesarImagen

class GameOfLife():
    def __init__(self, name = str,  filepath, width, height):
        self.name = name
        self.life_dict = GetLife_Dict(filepath, width, height)
    
    def GetLife_Dict(filepath, width, height):
        tiles = ProcesarImagen(filepath, '../Image/CutImg/' + self.name, width, height)

    def RunStep():
        pass

class Celula():
    def __init__(self, alive, sliceImg):
        self.alive = alive
        self.slice = sliceImg 