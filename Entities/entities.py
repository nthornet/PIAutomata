import sys,pygame
from pygame.locals import *
sys.path.append('../Image/ProcessImg/')
from Process import ProcesarImagen

WHITE = (255, 255, 255)

class Display():
    def __init__(self,WIDTH,HEIGHT, GameT, GameB):
        pygame.init() 
        pygame.display.set_caption('Swarm Intelligence Game of Life')
        self.screen = pygame.pygame.set_mode(WIDTH,HEIGHT)
        self.clock = pygame.time.Clock()
        self.Automatas = []
        Automatas.append(GameT,GameB) 
   
    def PlayGame(self): 
        pygame.display.update()
        while True:  # main loop that runs the game
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                self.Automatas[0].RunStep()
            self.COUNT += 1
        self.screen.fill(WHITE)
        for item in self.Automatas[0].life_dict:
            Colorize(item)
        #drawGrid()
        pygame.display.update()
        self.clock.tick(40)

    def Colorize(self,item):
        x = item[0]
        y = item[1]
        
        cel = self.Automatas[0].getCel(x,y)
        image = cel.slice
        
        coordinates = cel.slice.coords
        coordinates = (coordinates[1], coordinates[0])
        
        if self.Automatas[0].life_dict[item] == 0:
            image.set_alpha(0)
        elif self.Automatas[0].life_dict[item] == 1:
            image.set_alpha(255)
        self.screen.blit(image, coordinates)
        return None


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