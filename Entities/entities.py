import sys,pygame
from pygame.locals import *
sys.path.append('../Image/ProcessImg/')
sys.path.append('../Functions')
from Process import ProcesarImagen

WHITE = (255, 255, 255)

class Display():
    def __init__(self, width, height, cellsize):
        self.WIDTH = width
        self.HEIGHT = height
        self.CELL = cellsize
        self.Automatas = []
        self.screen = None
        self.CLOCK = None

    def AddAutomata(self, Automata):
        self.Automatas.append(Automata)

    def PlayGame(self): 
        pygame.init()
        pygame.display.set_caption('Swarm Intelligence Game of Life')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.CLOCK = pygame.time.Clock()
        
        while True:  # main loop that runs the game
            pygame.display.update()
            self.screen.fill(WHITE)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                #self.RunStep()
            #self.COUNT += 1
        #for item in self.Automatas[0].life_dict:
        #    Colorize(item)
        #drawGrid()
        #self.clock.tick(40)
    def RunStep(self):
        for automata in self.Automatas:
            automata.RunStep()

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

class GameOfLife():
    def __init__(self, name,  filepath, width, height, cellsize):
        self.name = name
        self.WIDTH = width
        self.HEIGHT = height
        self.life_dict = self.GetLife_Dict(filepath, width, height, cellsize)
    
    def GetLife_Dict(self, filepath, width, height, cellsize):
        tiles = ProcesarImagen(filepath, '../Image/CutImg/', width, height, cellsize)
        
        life_dict = {}

        cell_width = int(width/cellsize)
        cell_height = int(height/cellsize)
        
        for y in range(0, cell_height):
            for x in range(0, cell_width):
                life_dict[x,y] = Celula(0, tiles[y*cell_width+x])
        
        return life_dict

    def GetCell(x,y):
        return life_dict[x,y]

    def RunStep(self):
        new_life = {}
        for item in self.life_dict:
            neighbour_count = self.GetNeighbours(item)
            if self.life_dict[item].alive == 1:  # cell is alive and we need to check if it will stay alive
                if neighbour_count < 2:
                    # dies due to underpopulation
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
                elif neighbour_count > 3:
                    # dies due to overcrowding
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
                else:
                    # cell stays alive
                    new_life[item] = Celula(1, self.life_dict[item].slice) #1
            
            elif self.life_dict[item].alive == 0:
                if neighbour_count == 3:
                    new_life[item] = Celula(1, self.life_dict[item].slice) #1
                else:
                    new_life[item] = Celula(0, self.life_dict[item].slice) #0
        #   print('Run Step')
        self.life_dict = new_life

    def GetNeighbours(self, item):
        neighbour_count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                neighbour = (item[0] + x, item[1] + y)
                if neighbour[0] < self.WIDTH and neighbour[0] >= 0:
                    if neighbour[1] < self.HEIGHT and neighbour[1] >= 0:
                        try:
                            if self.life_dict[neighbour].alive == 1 and (x, y) != (0, 0):
                                neighbour_count += 1
                        except KeyError:
                            t = 1
                            # catch key errors
                            # print "error"
        return neighbour_count

class Celula():
    def __init__(self, alive, sliceImg):
        self.alive = alive
        self.slice = sliceImg 

if __name__ == '__main__':
    Go = Display(800,600,100)
    Automata_1 = GameOfLife("Turismo", "../Image/TestImg/test.jpg", \
                             Go.WIDTH, Go.HEIGHT, Go.CELL)
    Go.AddAutomata(Automata_1)
    Go.PlayGame()