import sys
sys.path.append('../Image/ProcessImg/')

from Process import ProcesarImagen

class ImageTop:
    # Automatas(GameOfLife) con Pygame
    pass


class GameOfLife():
    def __init__(self, name,  filepath, width, height, cellsize):
        self.name = name
        self.life_dict = self.GetLife_Dict(filepath, width, height, cellsize)
    
    def GetLife_Dict(self, filepath, width, height, cellsize):
        tiles = ProcesarImagen(filepath, '../Image/CutImg/', width, height, cellsize)
        
        life_dict = {}

        cell_width = int(width/cellsize)
        cell_height = int(height/cellsize)
        
        for y in range(0, cell_height):
            for x in range(0, cell_width):
                life_dict[x,y] = Celula(False, tiles[y*cell_width+x])
        
        return life_dict

    def GetCell(x,y):
        return life_dict[x,y]

    def runStep(self):
        pass

class Celula():
    def __init__(self, alive, sliceImg):
        self.alive = alive
        self.slice = sliceImg 

if __name__ == '__main__':
    Automata_1 = GameOfLife("Turismo", "../Image/TestImg/test.jpg", 800, 600, 100)