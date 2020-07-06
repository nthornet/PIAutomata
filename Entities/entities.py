import sys
sys.path.append('../Image/ProcessImg/')

from Process import ProcesarImagen

class ImageTop:
    # Automatas(GameOfLife) con Pygame


class GameOfLife():
    def __init__(self, name,  filepath, width, height, cellsize):
        self.name = name
        self.life_dict = self.GetLife_Dict(filepath, width, height, cellsize)
    
    def GetLife_Dict(self, filepath, width, height, cellsize):
        tiles = ProcesarImagen(filepath, '../Image/CutImg/', width, height, cellsize)
        life_dict = {}
        for x in range( int(height/cellsize) ):
            for y in range( int(width/cellsize) ):
                life_dict[x,y] = Celula(False, tiles[x*width+y])


        return tiles

    def RunStep():
        pass

class Celula():
    def __init__(self, alive, sliceImg):
        self.alive = alive
        self.slice = sliceImg 

if __name__ == '__main__':
    Automata_1 = GameOfLife("Turismo", "../Image/TestImg/test.jpg",  600,600,100)